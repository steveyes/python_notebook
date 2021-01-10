from .utils import FPS
import numpy as np
import argparse
import dlib
import cv2

# args
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-v", "--video", required=True, help="path to input video file")
ap.add_argument("-o", "--output", type=str, help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter week detections")
args = vars(ap.parse_args())

# SSD label
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# read model of net
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize
print("[INFO] starting video stream...")
vs = cv2.VideoCapture(args["video"])
writer = None

# multi tracking
trackers = []
labels = []

# computing FPS
fps = FPS().start()

while True:
    # read a frame
    (grabbed, frame) = vs.read()

    # if EOF
    if frame is None:
        break

    # pre execution
    (h, w) = frame.shape[:2]
    width = 600
    r = width / float(w)
    dim = (width, int(h * r))
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # if need to save the result
    if args["output"] is not None and writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJGP")
        writer = cv2.VideoWriter(args["output"], fourcc, 30, (frame.shape[1], frame.shape[0]), True)

    # detect, track
    if len(trackers) == 0:
        # get the blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (w, h), 127.5)

        # get the result of detect
        net.setInput(blob)
        detections = net.forward()

        # traverse the results
        for i in np.arange(0, detections.shape[2]):
            # multi return, keep the high probability ones
            confidence = detections[0, 0, i, 2]

            # filter
            if confidence > args["confidence"]:
                # extract the index of the class label from the detections list
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]

                # keep person
                if CLASSES[idx] != "person":
                    continue

                # get the BBOX
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # tracking using dlib
                t = dlib.correlation_tracker()
                rect = dlib.rectangle(int(startX), int(startY), int(endX), int(endY))
                t.start_track(rgb, rect)

                # save
                labels.append(label)
                trackers.append(t)

                # plot
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(frame, label, (startY, startY - 15), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 255, 0), 2)

    # just track it if already has frame
    else:
        # update every track
        for (t, l) in zip(trackers, labels):
            t.update(rgb)
            pos = t.get_position()

            # get position
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())

            # plot
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, 1, (startX, startY - 15), cv2.FONT_HERSHEY_COMPLEX, 0.25, (0, 255, 0), 2)

    # save
    if writer is not None:
        writer.write(frame)

    # display
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # exit
    if key == 27:
        break

    # compute FPS
    fps.update()

fps.stop()

print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

if writer is not None:
    writer.release()

cv2.destroyAllWindows()
vs.release()

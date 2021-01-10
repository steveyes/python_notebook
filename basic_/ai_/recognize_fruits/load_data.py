import os
import random
from os.path import join as pathjoin
import skimage
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, transform
from sklearn.utils import shuffle
import keras
from keras.utils import np_utils
from example_.isinstance_ import iscastable
import tensorflow as tf

BASE_PATH = 'C://var//images//Fruit-Images-Dataset-master'


def format_path(img):
    yes_int = []
    for s in range(len(img)):
        img[s] = img[s].split('_')
        if iscastable.IsCastableNumber(img[s][0])():
            img[s][0] = int(img[s][0])
            yes_int.append(img[s])
    yes_int.sort()
    for yi in range(len(yes_int)):
        yes_int[yi][0] = str(yes_int[yi][0])
        yes_int[yi] = yes_int[yi][0] + '_' + yes_int[yi][1]
    no5_img = yes_int[4]
    return no5_img


def load_data(dir_path):
    image_list = []
    label_list = []

    # 每个文件夹下的第5张图片实例
    no5_image_list = []

    # 每个文件夹下的第5张图片路径名
    no5_label_list = []

    n = 0
    for lab in os.listdir(pathjoin(dir_path)):
        _images = os.listdir(pathjoin(dir_path, lab))
        for img in _images:
            label_list.append(n)
            image_list.append(skimage.data.imread(pathjoin(dir_path, lab, img)))

        n += 1
        no5_label_list.append(lab)
        no5_image_list.append(skimage.data.imread(pathjoin(dir_path, lab, format_path(_images))))

    return image_list, label_list, no5_image_list, no5_label_list


def print_data_len():
    # os.chdir('C://var//images//Fruit-Images-Dataset-master')
    base_path = 'C://var//images//Fruit-Images-Dataset-master'
    pathTraining = pathjoin(base_path, 'Training')

    images, labels, no5_images, no5_labels = load_data(pathTraining)
    print(len(images), len(labels), len(no5_images), len(no5_labels))


def display_data(no5_images, no5_labels):
    plt.figure()
    for i in range(len(no5_images)):
        plt.subplot(12, 10, i + 1)
        plt.rcParams.update({'font.size': 6})
        plt.title(no5_labels[i], )
        plt.imshow(no5_images[i])
        plt.axis('off')

    plt.subplots_adjust(
        top=0.975,
        bottom=0.025,
        left=0.010,
        right=0.990,
        hspace=0.3,
        wspace=0.000,
    )

    plt.show()


def load_small_set(dir_path, times):
    image_list = []
    label_list = []
    n = 0
    for lab in os.listdir(dir_path):
        if n >= times: break
        for image in os.listdir(pathjoin(dir_path, lab)):
            label_list.append(int(n))
            image_list.append(skimage.data.imread(pathjoin(dir_path, lab, image)))
        n += 1
    return image_list, label_list,


def run_display_data():
    images, labels, no5_images, no5_labels = load_data(pathjoin(BASE_PATH, 'Training'))
    display_data(no5_images, no5_labels)


def cut_image(images, w, h):
    return [skimage.transform.resize(I, (w, h)) for I in images]


# def prepare_data(images, labels, n_classes):
#     train_x = np.array(images)
#     train_y = np.array(labels)
#     idx = np.arange(0, train_y.shape[0])
#     idx = shuffle(idx)
#     train_x = train_x[idx]
#     train_y = train_y[idx]
#     train_y = keras.utils.to_categorical(train_y, n_classes)
#     return train_x, train_y

def prepare_data(images, labels, n_classes):
    train_x = np.array(images)
    train_y = np.array(labels)
    nrand = random.randint(0, 100)

    random.seed(nrand)
    random.shuffle(train_x)
    random.seed(nrand)
    random.shuffle(train_y)

    return train_x, keras.utils.to_categorical(train_y, n_classes)  # one-hot 独热编码


def run_prepare_data():
    images_training, labels_training = load_small_set(pathjoin(BASE_PATH, 'Training'), 20)
    images_test, labels_test = load_small_set(pathjoin(BASE_PATH, 'Test'), 20)


def run_tf(train_x, test_x: np.ndarray):
    # 数据的类别
    n_classes = 20

    # 训练块的大小
    batch_size = 128

    # 卷积核尺寸
    kernel_h = kernel_w = 5

    # dropout 概率
    dropout = 0.8

    # 图片的通道数
    depth_in = 3

    # 第一层卷积的卷积核个数
    depth_out_l1 = 64

    # 第二层卷积的卷积核个数
    depth_out_l2 = 128

    # 图片尺寸
    image_size = train_x.shape[1]

    # 训练样本个数
    n_train_sample = train_x.shape[0]

    # 测试样本个数
    n_test_sample = test_x.shape[0]

    # feed给神经网络的图像数据类型与shape，shape四维，第一维训练的数据量，第二、三维图片尺寸，第四维图像通道数
    x = tf.placeholder(tf.float32, [None, 100, 100, 3])

    # feed给神经网络的标签数据的类型和shape
    y = tf.placeholder(tf.float32, [None, n_classes])

    # dropout的placeholder，解决过拟合
    keep_prob = tf.placeholder(tf.float32)

    # 用于扁平化处理的参数经过两层卷积池化后的图像大小*第二层的卷积核个数
    fla = int((image_size * image_size / 16) * depth_out_l2)

    # 定义各卷积层和全连接层的权重变量
    weights = {
        'con1_w': tf.Variable(tf.random_normal([kernel_h, kernel_w, depth_in, depth_out_l1])),
        'con2_w': tf.Variable(tf.random_normal([kernel_h, kernel_w, depth_out_l1, depth_out_l2])),
        'fc_w1': tf.Variable(tf.random_normal([int((image_size * image_size / 16) * depth_out_l2), 1024])),
        'fc_w2': tf.Variable(tf.random_normal([1024, 512])),
        'out': tf.Variable(tf.random_normal([512, n_classes])),
    }

    # 定义各卷积层和全连接层的偏置变量
    bias = {
        'conv1_b': tf.Variable(tf.random_normal([depth_out_l1])),
        'conv2_b': tf.Variable(tf.random_normal([depth_out_l2])),
        'fc_b1': tf.Variable(tf.random_normal([1024])),
        'fc_b2': tf.Variable(tf.random_normal([512])),
        'out': tf.Variable(tf.random_normal([n_classes])),
    }


if __name__ == '__main__':
    # test_display_data()
    run_prepare_data()

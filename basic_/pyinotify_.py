import pyinotify
import textwrap


class EventProcessor(pyinotify.ProcessEvent):
    _methods = [
        "IN_CREATE",
        "IN_OPEN",
        "IN_ACCESS",
        "IN_ATTRIB",
        "IN_CLOSE_NOWRITE",
        "IN_CLOSE_WRITE",
        "IN_DELETE",
        "IN_DELETE_SELF",
        "IN_IGNORED",
        "IN_MODIFY",
        "IN_MOVE_SELF",
        "IN_MOVED_FROM",
        "IN_MOVED_TO",
        "IN_Q_OVERFLOW",
        "IN_UNMOUNT",
        "default",
    ]


def process_generator(cls, method):
    def _method_name(self, event):
        print(textwrap.dedent('''\
        Method name: process_{}()
        Path name: {}
        Event name: {}
        '''.format(method, event.pathname, event.maskname)))

    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)


for method in EventProcessor._methods:
    process_generator(EventProcessor, method)

watch_manager = pyinotify.WatchManager()
watch_manager.add_watch("/tmp", pyinotify.ALL_EVENTS)
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())
event_notifier.loop()

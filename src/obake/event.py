from zope.interface import implements
from obake.interfaces import IBasicEvent, IEventTarget

class BasicEvent(object):
    implements(IBasicEvent)

    @property
    def type(self):
        return self._type

    @property
    def target(self):
        return self._target

    def __init__(self, type, target):
        self._type = type
        self._target = target

class EventTargetMixin(object):
    implements(IEventTarget)

    def __init__(self):
        self.event_listeners_map = {}

    def addEventListener(self, type, listener, use_capture=False):
        event_listeners = self.event_listeners_map.get(type)
        if event_listeners is None:
            event_listeners = self.event_listeners_map[type] = [set(), set()]
        event_listeners[int(use_capture)].add(listener)

    def removeEventListener(self, type, listener, use_capture=False):
        event_listeners = self.event_listeners_map.get(type)
        if event_listeners is None:
            return
        s = event_listeners[int(use_capture)]
        try:
            s.remove(listener)
        except KeyError:
            pass

    def _fire_event(self, event):
        event_listeners = self.event_listeners_map.get(event.type)
        if event_listeners is not None:
            for s in event_listeners:
                for listener in s:
                    listener(event)

    def dispatchEvent(self, event):
        self._fire_event(event)


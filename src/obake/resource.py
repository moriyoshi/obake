from zope.interface import implements
from obake.interfaces import IResourceCollection, IResource, IEventTarget
from obake.event import EventTargetMixin, BasicEvent

class ResourceEvent(BasicEvent):
    pass

class ResourceCollectionEvent(BasicEvent):
    def __init__(self, type, target, resource):
        super(ResourceCollectionEvent, self).__init__(type, target)
        self.resource = resource

class Resource(object):
    implements(IResource)

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._url

    def _notify_resource_loaded(self):
        self._fire_event(ResourceEvent('load', self))

    def _notify_response_received(self):
        self._fire_event(ResourceEvent('response_receive', self))

    def __init__(self, id, url):
        self._id = id
        self._url = url

class ObservableResource(Resource, EventTargetMixin):
    implements(IEventTarget)

    def __init__(self, id, url):
        super(ObservableResource, self).__init__(id, url)
        EventTargetMixin.__init__(self)

class MutableResourceCollection(object):
    implements(IResourceCollection)

    def __getitem__(self, resource_id):
        return self.items[resource_id]

    def __setitem__(self, resource_id, value):
        assert IResource.providedBy(value) 
        self.items[resource_id] = value

    def items():
        """Iterate all the resources"""
        return self.items.items()

    def __iter__():
        """Iterate all the resource identifiers"""
        return self.items.keys()

    def __init__(self):
        self.items = {}

class ObservableMutableResourceCollection(MutableResourceCollection, EventTargetMixin):
    def __setitem__(self, resource_id, value):
        super(ObservableMutableResourceCollection, self).__setitem__(resource_id, value)
        self._fire_event(ResourceCollectionEvent('add', self, value))

    def __init__(self):
        super(ObservableMutableResourceCollection, self).__init__()
        EventTargetMixin.__init__(self)

import os
from Cocoa import *
from Foundation import *
from WebKit import *
from ApplicationServices import *
from obake.interfaces import *
from zope.interface import implements
from obake.resource import ObservableMutableResourceCollection, ResourceEvent, ObservableResource
from obake.dom.interfaces import EventTarget
from obake.dom import interfaces as I
from obake.event import BasicEvent, EventTargetMixin
import thread

ui_thread_id = None

class UserAgentEvent(BasicEvent):
    implements(I.Event)

    @property
    def currentTarget(self):
        return self._currentTarget
 
    @property
    def eventPhase(self):
        return self._eventPhase

    @property
    def bubbles(self):
        return self._bubbles

    @property
    def cancelable(self):
        return self._cancelable

    @property
    def timeStamp(self):
        return self._timeStamp
 
    def stopPropagation(self):
        pass

    def preventDefault(self):
        pass

    def stopImmediatePropagation(self):
        pass

    @property
    def defaultPrevented(self):
        return self._defaultPrevented

    @property
    def isTrusted(self):
        return self._isTrusted

    def __init__(self, type, target, currentTarget=None, eventPhase=None, bubbles=True, cancelable=False, timeStamp=False, defaultPrevented=False, isTrusted=False, **kwargs):
        super(UserAgentEvent, self).__init__(type, target)
        self._currentTarget = currentTarget or target
        self._eventPhase = eventPhase
        self._bubbles = bubbles
        self._cancelable = cancelable
        self._timeStamp = timeStamp
        self._defaultPrevented = defaultPrevented
        self._isTrusted = isTrusted
        for k, v in kwargs.items():
            setattr(self, k, v) 

class Invoker(NSObject):
    def init__(self, bound_sel, args):
        self = super(Invoker, self).init()
        self.bound_sel = bound_sel
        self.args = args
        self.result = None
        return self

    def invoke(self):
        self.result = self.bound_sel(*self.args)

def invoke_later_sync(bound_sel, args=()):
    if ui_thread_id == thread.get_ident():
        return bound_sel(*args)
    else:
        invoker = Invoker.alloc().init__(bound_sel, args)
        invoker.performSelectorOnMainThread_withObject_waitUntilDone_(Invoker.invoke, None, True)
        return invoker.result

def become_foreground():
    psn = ProcessSerialNumber(0, kCurrentProcess)
    TransformProcessType(psn, kProcessTransformToForegroundApplication)
    SetFrontProcess(psn)

def init():
    global ui_thread_id
    ui_thread_id = thread.get_ident()
    become_foreground()
    NSApplication.sharedApplication()

class WebViewDelegate(NSObject):
    def init_(self, user_agent):
        self = super(WebViewDelegate, self).init()
        self.user_agent = user_agent
        return self

    def webView_didCommitLoadForFrame_(self, webView, frame):
        self.user_agent._fire_web_frame_event('load_committed', frame)

    def webView_didFailLoadWithError_forFrame_(self, webView, error, frame):
        self.user_agent._fire_web_frame_event('load_error', frame, error=error)

    def webView_didFailProvisionalLoadWithError_forFrame_(self, webView, error, frame):
        self.user_agent._fire_web_frame_event('provisional_load_error', frame, error=error)

    def webView_didFinishLoadForFrame_(self, webView, frame):
        self.user_agent._fire_web_frame_event('load', frame)

    def webView_didReceiveIcon_forFrame_(self, webView, icon, frame):
        self.user_agent._fire_web_frame_event('receive_icon', frame, icon=icon)

    def webView_didReceiveServerRedirectForProvisionalLoadForFrame(self, webView, frame):
        self.user_agent._fire_web_frame_event('redirect', frame)

    def webView_didReceiveTitle_forFrame_(self, webView, title, frame):
        self.user_agent._fire_web_frame_event('receive_title', frame, title=title)

    def webView_didStartProvisionalLoadForFrame_(self, webView, frame):
        self.user_agent._fire_web_frame_event('provisional_load_started', frame)

    def webView_willCloseFrame_(self, webView, frame):
        self.user_agent._fire_web_frame_event('close', frame)

    def webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_(self, webView, url, delay, fireDate, frame):
        self.user_agent._fire_web_frame_event('client_redirect', frame, url=url, delay=delay, fireDate=fireDate)

    def webView_didClearWindowObject_forFrame_(self, webView, windowObject, frame):
        self.user_agent._fire_web_frame_event('clear_window_object', frame, windowObject=windowOjbect)

    def webView_identifierForInitialRequest_fromDataSource_(self, webView, request, dataSource):
        retval = NSObject.new()
        url = request.URL()
        self.user_agent._register_resource(dataSource, retval, url)
        return retval

    def webView_plugInFailedWithError_dataSource_(self, webView, error, dataSource):
        print 'pluginFailedWithError: %s' % error

    def webView_resource_didCancelAuthenticationChallenge_fromDataSource_(self, webView, resource, challenge, dataSource):
        print 'cancelAuthenticationChallenge: %s' % challenge

    def webView_resource_didReceiveAuthenticationChallenge_fromDataSource_(self, webView, resource, challenge, dataSource):
        print 'cancelAuthenticationChallenge: %s' % challenge

    def webView_resource_didFailLoadingWithError_fromDataSource_(self, webView, resource, error, dataSource):
        print 'failLoadingWithError: %s' % error

    def webView_resource_didFinishLoadingFromDataSource_(self, webView, resource, dataSource):
        self.user_agent._notify_resource_loaded(dataSource, resource)

    def webView_resource_didReceiveResponse_fromDataSource_(self, webView, resource, response, dataSource):
        self.user_agent._notify_response_received(dataSource, resource)

    # def webView_resource_didReceiveContentLength_fromDataSource_(self, webView, resource, length, dataSource):
    #     print 'receiveContentLength: %s' % resource

    # def webView_resource_willSendRequest_redirectResponse_fromDataSource_(self, webView, resource, request, redirectResponse, dataSource):
    #     print 'willSendRequest: %s' % request

    def webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_(self, webView, message, frame):
        print 'alert: %s' % message

    def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_(self, webView, message, frame):
        print 'confirm: %s' % message

    def webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_(self, webView, prompt, defaultText, frame):
        print 'prompt: %s %s' % (prompt, defaultText)

    def webView_runOpenPanelForFileButtonWithResultListener_(self, webView, webOpenPanelResultListener):
        webOpenPanelResultListener.chooseFilename_("/tmp/blah")

class ApplicationDelegate(NSObject):
    def init_driver_entrypoint(self, driver, entrypoint):
        self = super(ApplicationDelegate, self).init()
        self.driver = driver
        self.entrypoint = entrypoint
        self.user_thread_id = None
        return self

    def applicationWillFinishLaunching_(self, sender):
        def user_thread():
            pool = NSAutoreleasePool.alloc().init()
            try:
                self.entrypoint(self.driver)
            finally:
                NSApp.performSelectorOnMainThread_withObject_waitUntilDone_(NSApplication.stop_, NSApp, None)
        user_thread_id = thread.start_new_thread(user_thread, ())

    def applicationDidFinishLaunching_(self, sender):
        pass

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return True

class WebFrameWrapper(EventTargetMixin):
    implements(IWebFrame, EventTarget)

    def __init__(self, owner, impl):
        super(WebFrameWrapper, self).__init__()
        self.owner = owner
        self.impl = impl

    @property
    def document(self):
        return domimpl.Document(invoke_later_sync(self.impl.DOMDocument))

    def load(self, url):
        invoke_later_sync(self.impl.loadRequest_, (NSURLRequest.alloc().initWithURL_(NSURL.URLWithString_(url)), ))

    def reload(self, invalidate_cache=False):
        if invalidate_cache:
            invoke_later_sync(self.impl.reloadFromOrigin)
        else:
            invoke_later_sync(self.impl.reload)

class UserAgent(object):
    implements(IUserAgent)

    @property
    def main_frame(self):
        return self._main_frame

    @property
    def resource_collection(self):
        return self._resource_collection

    def _get_web_frame_wrapper(self, web_frame):
        wrapper = self._web_frame_wrappers.get(web_frame)
        if wrapper is None:
            self._web_frame_wrappers[web_frame] = wrapper = WebFrameWrapper(self, web_frame)
        return wrapper

    def _fire_web_frame_event(self, type, web_frame, **kwargs):
        wrapper = self._web_frame_wrappers.get(web_frame)
        if wrapper is None:
            return
        wrapper._fire_event(UserAgentEvent(type=type, target=wrapper, **kwargs))

    def _register_resource(self, data_source, id, url):
        self._resource_collection[id] = ObservableResource(id, url)

    def _notify_resource_loaded(self, data_source, id):
        self._resource_collection[id]._notify_resource_loaded()

    def _notify_response_received(self, data_source, id):
        self._resource_collection[id]._notify_response_received()

    def __init__(self, configuration, window, web_view):
        self.configuration = configuration
        self.window = window
        self.web_view = web_view
        self._web_frame_wrappers = {}

        web_view_delegate = WebViewDelegate.alloc().init_(self)
        web_view.setFrameLoadDelegate_(web_view_delegate)
        web_view.setResourceLoadDelegate_(web_view_delegate)
        web_view.setUIDelegate_(web_view_delegate)

        self._web_view_delegate = web_view_delegate
        self._main_frame = self._get_web_frame_wrapper(self.web_view.mainFrame())
        self._resource_collection = ObservableMutableResourceCollection()

class Driver(object):
    implements(IUserAgentDriver)

    def __init__(self):
        self.windows = []
        self.delegate = None

    def init(self, entrypoint):
        from PyObjCTools import AppHelper
        init()
        self.delegate = ApplicationDelegate.alloc().init_driver_entrypoint(self, entrypoint)
        NSApp.setDelegate_(self.delegate)
        AppHelper.runEventLoop()

    def _create_window(self, configuration):
        window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(NSMakeRect(300, 300, 400, 400), NSTitledWindowMask | NSClosableWindowMask | NSResizableWindowMask, NSBackingStoreBuffered, False)
        window.setTitle_(u"test")
        window.makeKeyAndOrderFront_(NSApp)
        # window.makeMainWindow()
        self.windows.append(window)
        return window

    def _create_web_view(self, configuration):
        web_view = WebView.alloc().initWithFrame_frameName_groupName_(
            NSMakeRect(0, 0, 300, 300), None, None)
        web_view.setPreferences_(WebPreferences.standardPreferences())
        return web_view

    def create_user_agent(self, configuration):
        invoker = Invoker.alloc().init__(self._create_user_agent, [configuration])
        invoker.performSelectorOnMainThread_withObject_waitUntilDone_(Invoker.invoke, None, True)
        return invoker.result

    def _create_user_agent(self, configuration):
        web_view = self._create_web_view(configuration)

        window = self._create_window(configuration)
        window.setContentView_(web_view)

        return UserAgent(configuration, window, web_view)

from obake.driver.macosx.webkit import dom as domimpl

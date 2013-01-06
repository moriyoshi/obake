from zope.interface import Interface, Attribute

class IBasicEvent(Interface):
    type = Attribute('''[readonly] DOMString''')
    target = Attribute('''[readonly] EventTarget''')

class IEventListener(Interface):
    def __call__(event):
        pass

class IEventTarget(Interface):
    def addEventListener(type, listener, useCapture=False):
        pass
    
    def removeEventListener(type, listener, useCapture=False):
        pass
    
    def dispatchEvent(event):
        pass

class IResource(Interface):
    id = Attribute("Identifier that uniquely specifies the resource within a single page load")
    url = Attribute("URL for the resource")

class IResourceCollection(Interface):
    def __getitem__(resource_id):
        """Get the resource object of the specified identifier"""

    def items():
        """Iterate all the resources"""

    def __iter__():
        """Iterate all the resource identifiers"""

class IWebFrame(Interface):
    document = Attribute("""A DOMDocument object that represents the contents rendered in this frame""")

    def addEventListener(type, listener):
        """Add the listener of the specified type"""

    def load(url):
        """Make a request to the specified URL"""

    def reload(invalidate_cache=False):
        """Reload the entire content"""

class IUserAgentInteractionHandler(Interface):
    def handle_alert(message):
        """Handles the alert dialog"""

    def handle_confirm(message):
        """Handles the confirm dialog"""

    def handle_prompt(message, default_value):
        """Handles the prompt dialog"""

    def handle_file_dialog():
        """Handles the file dialog. Expected to return the list of file(s) to send"""

    def handle_console(message):
        """Handles the console output"""

class IUserAgent(Interface):
    configuration = Attribute("""Browser configuration.""")
    main_frame = Attribute("""IWebFrame object for the main frame.""")
    resource_collection = Attribute("""Resources for the current page load""")

    def load(url):
        """Load the specified page"""

class IUserAgentDriver(Interface):
    def init(entrypoint):
        """Init the driver. User can continue operation from the specified entry point"""

    def create_user_agent(configuration):
        """create a new IUserAgent object"""

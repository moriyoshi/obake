import zope.interface
from obake.interfaces import IBasicEvent, IEventTarget as EventTarget, IEventListener as EventListener

class DOMStringList(zope.interface.Interface):
    def item(index):
        pass
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def contains(str):
        pass
    
class NameList(zope.interface.Interface):
    def getName(index):
        pass
    
    def getNamespaceURI(index):
        pass
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def contains(str):
        pass
    
    def containsNS(namespaceURI, name):
        pass
    
class DOMImplementationList(zope.interface.Interface):
    def item(index):
        pass
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
class DOMImplementationSource(zope.interface.Interface):
    def getDOMImplementation(features):
        pass
    
    def getDOMImplementationList(features):
        pass
    
class DOMImplementation(zope.interface.Interface):
    def hasFeature(feature, version):
        pass
    
    def createDocumentType(qualifiedName, publicId, systemId):
        pass
    
    def createDocument(namespaceURI, qualifiedName, doctype):
        pass
    
    def getFeature(feature, version):
        pass
    
class Node(zope.interface.Interface):
    nodeName = zope.interface.Attribute('''[readonly] DOMString''')
    
    nodeValue = zope.interface.Attribute('''DOMString''')
    
    nodeType = zope.interface.Attribute('''[readonly] unsigned short''')
    
    parentNode = zope.interface.Attribute('''[readonly] Node''')
    
    childNodes = zope.interface.Attribute('''[readonly] NodeList''')
    
    firstChild = zope.interface.Attribute('''[readonly] Node''')
    
    lastChild = zope.interface.Attribute('''[readonly] Node''')
    
    previousSibling = zope.interface.Attribute('''[readonly] Node''')
    
    nextSibling = zope.interface.Attribute('''[readonly] Node''')
    
    attributes = zope.interface.Attribute('''[readonly] NamedNodeMap''')
    
    ownerDocument = zope.interface.Attribute('''[readonly] Document''')
    
    def insertBefore(newChild, refChild):
        pass
    
    def replaceChild(newChild, oldChild):
        pass
    
    def removeChild(oldChild):
        pass
    
    def appendChild(newChild):
        pass
    
    def hasChildNodes():
        pass
    
    def cloneNode(deep):
        pass
    
    def normalize():
        pass
    
    def isSupported(feature, version):
        pass
    
    namespaceURI = zope.interface.Attribute('''[readonly] DOMString''')
    
    prefix = zope.interface.Attribute('''DOMString''')
    
    localName = zope.interface.Attribute('''[readonly] DOMString''')
    
    def hasAttributes():
        pass
    
    baseURI = zope.interface.Attribute('''[readonly] DOMString''')
    
    def compareDocumentPosition(other):
        pass
    
    textContent = zope.interface.Attribute('''DOMString''')
    
    def isSameNode(other):
        pass
    
    def lookupPrefix(namespaceURI):
        pass
    
    def isDefaultNamespace(namespaceURI):
        pass
    
    def lookupNamespaceURI(prefix):
        pass
    
    def isEqualNode(arg):
        pass
    
    def getFeature(feature, version):
        pass
    
    def setUserData(key, data, handler):
        pass
    
    def getUserData(key):
        pass
    
class NodeList(zope.interface.Interface):
    def item(index):
        pass
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')

    def __iter__():
        pass

class NamedNodeMap(zope.interface.Interface):
    def getNamedItem(name):
        pass
    
    def setNamedItem(arg):
        pass
    
    def removeNamedItem(name):
        pass
    
    def item(index):
        pass
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def getNamedItemNS(namespaceURI, localName):
        pass
    
    def setNamedItemNS(arg):
        pass
    
    def removeNamedItemNS(namespaceURI, localName):
        pass
    
class CharacterData(Node):
    data = zope.interface.Attribute('''DOMString''')
    
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def substringData(offset, count):
        pass
    
    def appendData(arg):
        pass
    
    def insertData(offset, arg):
        pass
    
    def deleteData(offset, count):
        pass
    
    def replaceData(offset, count, arg):
        pass
    
class Attr(Node):
    name = zope.interface.Attribute('''[readonly] DOMString''')
    
    specified = zope.interface.Attribute('''[readonly] boolean''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    ownerElement = zope.interface.Attribute('''[readonly] Element''')
    
    schemaTypeInfo = zope.interface.Attribute('''[readonly] TypeInfo''')
    
    isId = zope.interface.Attribute('''[readonly] boolean''')
    
class Element(Node, EventTarget):
    tagName = zope.interface.Attribute('''[readonly] DOMString''')
    
    def getAttribute(name):
        pass
    
    def setAttribute(name, value):
        pass
    
    def removeAttribute(name):
        pass
    
    def getAttributeNode(name):
        pass
    
    def setAttributeNode(newAttr):
        pass
    
    def removeAttributeNode(oldAttr):
        pass
    
    def getElementsByTagName(name):
        pass
    
    def getAttributeNS(namespaceURI, localName):
        pass
    
    def setAttributeNS(namespaceURI, qualifiedName, value):
        pass
    
    def removeAttributeNS(namespaceURI, localName):
        pass
    
    def getAttributeNodeNS(namespaceURI, localName):
        pass
    
    def setAttributeNodeNS(newAttr):
        pass
    
    def getElementsByTagNameNS(namespaceURI, localName):
        pass
    
    def hasAttribute(name):
        pass
    
    def hasAttributeNS(namespaceURI, localName):
        pass
    
    schemaTypeInfo = zope.interface.Attribute('''[readonly] TypeInfo''')
    
    def setIdAttribute(name, isId):
        pass
    
    def setIdAttributeNS(namespaceURI, localName, isId):
        pass
    
    def setIdAttributeNode(idAttr, isId):
        pass
    
class Text(CharacterData):
    def splitText(offset):
        pass
    
    isElementContentWhitespace = zope.interface.Attribute('''[readonly] boolean''')
    
    wholeText = zope.interface.Attribute('''[readonly] DOMString''')
    
    def replaceWholeText(content):
        pass
    
class TypeInfo(zope.interface.Interface):
    typeName = zope.interface.Attribute('''[readonly] DOMString''')
    
    typeNamespace = zope.interface.Attribute('''[readonly] DOMString''')
    
    def isDerivedFrom(typeNamespaceArg, typeNameArg, derivationMethod):
        pass
    
class UserDataHandler(zope.interface.Interface):
    def handle(operation, key, data, src, dst):
        pass
    
class DOMError(zope.interface.Interface):
    severity = zope.interface.Attribute('''[readonly] unsigned short''')
    
    message = zope.interface.Attribute('''[readonly] DOMString''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    relatedException = zope.interface.Attribute('''[readonly] DOMObject''')
    
    relatedData = zope.interface.Attribute('''[readonly] DOMObject''')
    
    location = zope.interface.Attribute('''[readonly] DOMLocator''')
    
class DOMErrorHandler(zope.interface.Interface):
    def handleError(error):
        pass
    
class DOMLocator(zope.interface.Interface):
    lineNumber = zope.interface.Attribute('''[readonly] long''')
    
    columnNumber = zope.interface.Attribute('''[readonly] long''')
    
    byteOffset = zope.interface.Attribute('''[readonly] long''')
    
    utf16Offset = zope.interface.Attribute('''[readonly] long''')
    
    relatedNode = zope.interface.Attribute('''[readonly] Node''')
    
    uri = zope.interface.Attribute('''[readonly] DOMString''')
    
class DOMConfiguration(zope.interface.Interface):
    def setParameter(name, value):
        pass
    
    def getParameter(name):
        pass
    
    def canSetParameter(name, value):
        pass
    
    parameterNames = zope.interface.Attribute('''[readonly] DOMStringList''')
    
class DocumentType(Node):
    name = zope.interface.Attribute('''[readonly] DOMString''')
    
    entities = zope.interface.Attribute('''[readonly] NamedNodeMap''')
    
    notations = zope.interface.Attribute('''[readonly] NamedNodeMap''')
    
    publicId = zope.interface.Attribute('''[readonly] DOMString''')
    
    systemId = zope.interface.Attribute('''[readonly] DOMString''')
    
    internalSubset = zope.interface.Attribute('''[readonly] DOMString''')
    
class Notation(Node):
    publicId = zope.interface.Attribute('''[readonly] DOMString''')
    
    systemId = zope.interface.Attribute('''[readonly] DOMString''')
    
class Entity(Node):
    publicId = zope.interface.Attribute('''[readonly] DOMString''')
    
    systemId = zope.interface.Attribute('''[readonly] DOMString''')
    
    notationName = zope.interface.Attribute('''[readonly] DOMString''')
    
    inputEncoding = zope.interface.Attribute('''[readonly] DOMString''')
    
    xmlEncoding = zope.interface.Attribute('''[readonly] DOMString''')
    
    xmlVersion = zope.interface.Attribute('''[readonly] DOMString''')
    
class ProcessingInstruction(Node):
    target = zope.interface.Attribute('''[readonly] DOMString''')
    
    data = zope.interface.Attribute('''DOMString''')
    
class Document(Node, EventTarget):
    doctype = zope.interface.Attribute('''[readonly] DocumentType''')
    
    implementation = zope.interface.Attribute('''[readonly] DOMImplementation''')
    
    documentElement = zope.interface.Attribute('''[readonly] Element''')
    
    def createElement(tagName):
        pass
    
    def createDocumentFragment():
        pass
    
    def createTextNode(data):
        pass
    
    def createComment(data):
        pass
    
    def createCDATASection(data):
        pass
    
    def createProcessingInstruction(target, data):
        pass
    
    def createAttribute(name):
        pass
    
    def createEntityReference(name):
        pass
    
    def getElementsByTagName(tagname):
        pass
    
    def importNode(importedNode, deep):
        pass
    
    def createElementNS(namespaceURI, qualifiedName):
        pass
    
    def createAttributeNS(namespaceURI, qualifiedName):
        pass
    
    def getElementsByTagNameNS(namespaceURI, localName):
        pass
    
    def getElementById(elementId):
        pass
    
    inputEncoding = zope.interface.Attribute('''[readonly] DOMString''')
    
    xmlEncoding = zope.interface.Attribute('''[readonly] DOMString''')
    
    xmlStandalone = zope.interface.Attribute('''boolean''')
    
    xmlVersion = zope.interface.Attribute('''DOMString''')
    
    strictErrorChecking = zope.interface.Attribute('''boolean''')
    
    documentURI = zope.interface.Attribute('''DOMString''')
    
    def adoptNode(source):
        pass
    
    domConfig = zope.interface.Attribute('''[readonly] DOMConfiguration''')
    
    def normalizeDocument():
        pass
    
    def renameNode(n, namespaceURI, qualifiedName):
        pass
    
class Event(IBasicEvent):
    currentTarget = zope.interface.Attribute('''[readonly] EventTarget''')
    eventPhase = zope.interface.Attribute('''[readonly] unsigned short''')
    bubbles = zope.interface.Attribute('''[readonly] boolean''')
    cancelable = zope.interface.Attribute('''[readonly] boolean''')
    timeStamp = zope.interface.Attribute('''[readonly] DOMTimeStamp''')
    
    def stopPropagation():
        pass
    
    def preventDefault():
        pass
    
    def initEvent(eventTypeArg, canBubbleArg, cancelableArg):
        pass
    
    def stopImmediatePropagation():
        pass
    
    defaultPrevented = zope.interface.Attribute('''[readonly] boolean''')
    isTrusted = zope.interface.Attribute('''[readonly] boolean''')

class DocumentEvent(zope.interface.Interface):
    def createEvent(eventInterface):
        pass
    
class UIEvent(Event):
    view = zope.interface.Attribute('''[readonly] AbstractView''')
    
    detail = zope.interface.Attribute('''[readonly] long''')
    
class FocusEvent(UIEvent):
    relatedTarget = zope.interface.Attribute('''[readonly] EventTarget''')
    
class MouseEvent(UIEvent):
    screenX = zope.interface.Attribute('''[readonly] long''')
    
    screenY = zope.interface.Attribute('''[readonly] long''')
    
    clientX = zope.interface.Attribute('''[readonly] long''')
    
    clientY = zope.interface.Attribute('''[readonly] long''')
    
    ctrlKey = zope.interface.Attribute('''[readonly] boolean''')
    
    shiftKey = zope.interface.Attribute('''[readonly] boolean''')
    
    altKey = zope.interface.Attribute('''[readonly] boolean''')
    
    metaKey = zope.interface.Attribute('''[readonly] boolean''')
    
    button = zope.interface.Attribute('''[readonly] unsigned short''')
    
    buttons = zope.interface.Attribute('''[readonly] unsigned short''')
    
    relatedTarget = zope.interface.Attribute('''[readonly] EventTarget''')
    
    def getModifierState(keyArg):
        pass
    
class WheelEvent(MouseEvent):
    deltaX = zope.interface.Attribute('''[readonly] double''')
    
    deltaY = zope.interface.Attribute('''[readonly] double''')
    
    deltaZ = zope.interface.Attribute('''[readonly] double''')
    
    deltaMode = zope.interface.Attribute('''[readonly] unsigned long''')
    
class KeyboardEvent(UIEvent):
    char = zope.interface.Attribute('''[readonly] DOMString''')
    
    key = zope.interface.Attribute('''[readonly] DOMString''')
    
    location = zope.interface.Attribute('''[readonly] unsigned long''')
    
    ctrlKey = zope.interface.Attribute('''[readonly] boolean''')
    
    shiftKey = zope.interface.Attribute('''[readonly] boolean''')
    
    altKey = zope.interface.Attribute('''[readonly] boolean''')
    
    metaKey = zope.interface.Attribute('''[readonly] boolean''')
    
    repeat = zope.interface.Attribute('''[readonly] boolean''')
    
    locale = zope.interface.Attribute('''[readonly] DOMString''')
    
    def getModifierState(keyArg):
        pass
    
class CompositionEvent(UIEvent):
    data = zope.interface.Attribute('''[readonly] DOMString''')
    
    locale = zope.interface.Attribute('''[readonly] DOMString''')

class DOMFormData(zope.interface.Interface):
    def append(name, value, filename):
        pass
    
class DOMTokenList(zope.interface.Interface):
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def item(index):
        pass
    
    def contains(token):
        pass
    
    def add():
        pass
    
    def remove():
        pass
    
    def toggle(token, force):
        pass

class DOMSettableTokenList(DOMTokenList):
    value = zope.interface.Attribute('''DOMString''')
    
class DOMURL(zope.interface.Interface):
    def createObjectURL(blob):
        pass
    
    def revokeObjectURL(url):
        pass
    
class HTMLAllCollection(zope.interface.Interface):
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def item(index):
        pass
    
    def namedItem(name):
        pass
    
    def tags(name):
        pass
    
class HTMLElement(Element):
    id = zope.interface.Attribute('''DOMString''')
    
    title = zope.interface.Attribute('''DOMString''')
    
    lang = zope.interface.Attribute('''DOMString''')
    
    translate = zope.interface.Attribute('''boolean''')
    
    dir = zope.interface.Attribute('''DOMString''')
    
    tabIndex = zope.interface.Attribute('''long''')
    
    draggable = zope.interface.Attribute('''boolean''')
    
    webkitdropzone = zope.interface.Attribute('''DOMString''')
    
    hidden = zope.interface.Attribute('''boolean''')
    
    accessKey = zope.interface.Attribute('''DOMString''')
    
    innerHTML = zope.interface.Attribute('''DOMString''')
    
    innerText = zope.interface.Attribute('''DOMString''')
    
    outerHTML = zope.interface.Attribute('''DOMString''')
    
    outerText = zope.interface.Attribute('''DOMString''')
    
    def insertAdjacentElement(where, element):
        pass
    
    def insertAdjacentHTML(where, html):
        pass
    
    def insertAdjacentText(where, text):
        pass
    
    children = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    contentEditable = zope.interface.Attribute('''DOMString''')
    
    isContentEditable = zope.interface.Attribute('''[readonly] boolean''')
    
    spellcheck = zope.interface.Attribute('''boolean''')
    
    itemScope = zope.interface.Attribute('''boolean''')
    
    itemType = zope.interface.Attribute('''[readonly] DOMSettableTokenList''')
    
    itemId = zope.interface.Attribute('''DOMString''')
    
    itemRef = zope.interface.Attribute('''[readonly] DOMSettableTokenList''')
    
    itemProp = zope.interface.Attribute('''[readonly] DOMSettableTokenList''')
    
    itemValue = zope.interface.Attribute('''DOMObject''')
    
    def click():
        pass
    
class HTMLAnchorElement(HTMLElement):
    charset = zope.interface.Attribute('''DOMString''')
    
    coords = zope.interface.Attribute('''DOMString''')
    
    download = zope.interface.Attribute('''DOMString''')
    
    href = zope.interface.Attribute('''DOMString''')
    
    hreflang = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    ping = zope.interface.Attribute('''DOMString''')
    
    rel = zope.interface.Attribute('''DOMString''')
    
    rev = zope.interface.Attribute('''DOMString''')
    
    shape = zope.interface.Attribute('''DOMString''')
    
    target = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    hash = zope.interface.Attribute('''DOMString''')
    
    host = zope.interface.Attribute('''DOMString''')
    
    hostname = zope.interface.Attribute('''DOMString''')
    
    pathname = zope.interface.Attribute('''DOMString''')
    
    port = zope.interface.Attribute('''DOMString''')
    
    protocol = zope.interface.Attribute('''DOMString''')
    
    search = zope.interface.Attribute('''DOMString''')
    
    origin = zope.interface.Attribute('''[readonly] DOMString''')
    
    text = zope.interface.Attribute('''[readonly] DOMString''')
    
class HTMLAppletElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    alt = zope.interface.Attribute('''DOMString''')
    
    archive = zope.interface.Attribute('''DOMString''')
    
    code = zope.interface.Attribute('''DOMString''')
    
    codeBase = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''DOMString''')
    
    hspace = zope.interface.Attribute('''long''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    object = zope.interface.Attribute('''DOMString''')
    
    vspace = zope.interface.Attribute('''long''')
    
    width = zope.interface.Attribute('''DOMString''')
    
class HTMLAreaElement(HTMLElement):
    alt = zope.interface.Attribute('''DOMString''')
    
    coords = zope.interface.Attribute('''DOMString''')
    
    href = zope.interface.Attribute('''DOMString''')
    
    noHref = zope.interface.Attribute('''boolean''')
    
    ping = zope.interface.Attribute('''DOMString''')
    
    shape = zope.interface.Attribute('''DOMString''')
    
    target = zope.interface.Attribute('''DOMString''')
    
    hash = zope.interface.Attribute('''[readonly] DOMString''')
    
    host = zope.interface.Attribute('''[readonly] DOMString''')
    
    hostname = zope.interface.Attribute('''[readonly] DOMString''')
    
    pathname = zope.interface.Attribute('''[readonly] DOMString''')
    
    port = zope.interface.Attribute('''[readonly] DOMString''')
    
    protocol = zope.interface.Attribute('''[readonly] DOMString''')
    
    search = zope.interface.Attribute('''[readonly] DOMString''')
    
class HTMLBRElement(HTMLElement):
    clear = zope.interface.Attribute('''DOMString''')
    
class HTMLBaseElement(HTMLElement):
    href = zope.interface.Attribute('''DOMString''')
    
    target = zope.interface.Attribute('''DOMString''')
    
class HTMLBaseFontElement(HTMLElement):
    color = zope.interface.Attribute('''DOMString''')
    
    face = zope.interface.Attribute('''DOMString''')
    
    size = zope.interface.Attribute('''long''')
    
class HTMLBodyElement(HTMLElement):
    aLink = zope.interface.Attribute('''DOMString''')
    
    background = zope.interface.Attribute('''DOMString''')
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    link = zope.interface.Attribute('''DOMString''')
    
    text = zope.interface.Attribute('''DOMString''')
    
    vLink = zope.interface.Attribute('''DOMString''')
    
    onbeforeunload = zope.interface.Attribute('''EventListener''')
    
    onhashchange = zope.interface.Attribute('''EventListener''')
    
    onmessage = zope.interface.Attribute('''EventListener''')
    
    onoffline = zope.interface.Attribute('''EventListener''')
    
    ononline = zope.interface.Attribute('''EventListener''')
    
    onpopstate = zope.interface.Attribute('''EventListener''')
    
    onresize = zope.interface.Attribute('''EventListener''')
    
    onstorage = zope.interface.Attribute('''EventListener''')
    
    onunload = zope.interface.Attribute('''EventListener''')
    
    onorientationchange = zope.interface.Attribute('''EventListener''')
    
    onblur = zope.interface.Attribute('''EventListener''')
    
    onerror = zope.interface.Attribute('''EventListener''')
    
    onfocus = zope.interface.Attribute('''EventListener''')
    
    onload = zope.interface.Attribute('''EventListener''')
    
class HTMLButtonElement(HTMLElement):
    autofocus = zope.interface.Attribute('''boolean''')
    
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    formAction = zope.interface.Attribute('''DOMString''')
    
    formEnctype = zope.interface.Attribute('''DOMString''')
    
    formMethod = zope.interface.Attribute('''DOMString''')
    
    formNoValidate = zope.interface.Attribute('''boolean''')
    
    formTarget = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLCanvasElement(HTMLElement):
    width = zope.interface.Attribute('''long''')
    
    height = zope.interface.Attribute('''long''')
    
    def toDataURL(type):
        pass
    
    def getContext(contextId):
        pass
    
class HTMLCollection(zope.interface.Interface):
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def item(index):
        pass
    
    def namedItem(name):
        pass
    
class HTMLDListElement(HTMLElement):
    compact = zope.interface.Attribute('''boolean''')
    
class HTMLDataListElement(HTMLElement):
    options = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
class HTMLDetailsElement(HTMLElement):
    open = zope.interface.Attribute('''boolean''')
    
class HTMLDialogElement(HTMLElement):
    open = zope.interface.Attribute('''boolean''')
    
    def close():
        pass
    
    def show():
        pass
    
    def showModal():
        pass
    
class HTMLDirectoryElement(HTMLElement):
    compact = zope.interface.Attribute('''boolean''')
    
class HTMLDivElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
class HTMLDocument(Document):
    def open():
        pass
    
    def close():
        pass
    
    def write(text):
        pass
    
    def writeln(text):
        pass
    
    embeds = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    plugins = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    scripts = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    def clear():
        pass
    
    def captureEvents():
        pass
    
    def releaseEvents():
        pass
    
    width = zope.interface.Attribute('''[readonly] long''')
    
    height = zope.interface.Attribute('''[readonly] long''')
    
    dir = zope.interface.Attribute('''DOMString''')
    
    designMode = zope.interface.Attribute('''DOMString''')
    
    compatMode = zope.interface.Attribute('''[readonly] DOMString''')
    
    activeElement = zope.interface.Attribute('''[readonly] Element''')
    
    def hasFocus():
        pass
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    fgColor = zope.interface.Attribute('''DOMString''')
    
    alinkColor = zope.interface.Attribute('''DOMString''')
    
    linkColor = zope.interface.Attribute('''DOMString''')
    
    vlinkColor = zope.interface.Attribute('''DOMString''')
    
class HTMLEmbedElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''long''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''long''')
    
class HTMLFieldSetElement(HTMLElement):
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    elements = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
class HTMLFontElement(HTMLElement):
    color = zope.interface.Attribute('''DOMString''')
    
    face = zope.interface.Attribute('''DOMString''')
    
    size = zope.interface.Attribute('''DOMString''')
    
class HTMLFormControlsCollection(HTMLCollection):
    def namedItem(name):
        pass
    
class HTMLFormElement(HTMLElement):
    acceptCharset = zope.interface.Attribute('''DOMString''')
    
    action = zope.interface.Attribute('''DOMString''')
    
    autocomplete = zope.interface.Attribute('''DOMString''')
    
    enctype = zope.interface.Attribute('''DOMString''')
    
    encoding = zope.interface.Attribute('''DOMString''')
    
    method = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    noValidate = zope.interface.Attribute('''boolean''')
    
    target = zope.interface.Attribute('''DOMString''')
    
    elements = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    length = zope.interface.Attribute('''[readonly] long''')
    
    def submit():
        pass
    
    def reset():
        pass
    
    def checkValidity():
        pass
    
class HTMLFrameElement(HTMLElement):
    frameBorder = zope.interface.Attribute('''DOMString''')
    
    longDesc = zope.interface.Attribute('''DOMString''')
    
    marginHeight = zope.interface.Attribute('''DOMString''')
    
    marginWidth = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    noResize = zope.interface.Attribute('''boolean''')
    
    scrolling = zope.interface.Attribute('''DOMString''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    contentDocument = zope.interface.Attribute('''[readonly] Document''')
    
    contentWindow = zope.interface.Attribute('''[readonly] DOMWindow''')
    
    location = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''[readonly] long''')
    
    height = zope.interface.Attribute('''[readonly] long''')
    
class HTMLFrameSetElement(HTMLElement):
    cols = zope.interface.Attribute('''DOMString''')
    
    rows = zope.interface.Attribute('''DOMString''')
    
    onbeforeunload = zope.interface.Attribute('''EventListener''')
    
    onhashchange = zope.interface.Attribute('''EventListener''')
    
    onmessage = zope.interface.Attribute('''EventListener''')
    
    onoffline = zope.interface.Attribute('''EventListener''')
    
    ononline = zope.interface.Attribute('''EventListener''')
    
    onpopstate = zope.interface.Attribute('''EventListener''')
    
    onresize = zope.interface.Attribute('''EventListener''')
    
    onstorage = zope.interface.Attribute('''EventListener''')
    
    onunload = zope.interface.Attribute('''EventListener''')
    
    onorientationchange = zope.interface.Attribute('''EventListener''')
    
    onblur = zope.interface.Attribute('''EventListener''')
    
    onerror = zope.interface.Attribute('''EventListener''')
    
    onfocus = zope.interface.Attribute('''EventListener''')
    
    onload = zope.interface.Attribute('''EventListener''')
    
class HTMLHRElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    noShade = zope.interface.Attribute('''boolean''')
    
    size = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''DOMString''')
    
class HTMLHeadElement(HTMLElement):
    profile = zope.interface.Attribute('''DOMString''')
    
class HTMLHeadingElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
class HTMLHtmlElement(HTMLElement):
    version = zope.interface.Attribute('''DOMString''')
    
    manifest = zope.interface.Attribute('''DOMString''')
    
class HTMLIFrameElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    frameBorder = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''DOMString''')
    
    longDesc = zope.interface.Attribute('''DOMString''')
    
    marginHeight = zope.interface.Attribute('''DOMString''')
    
    marginWidth = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    sandbox = zope.interface.Attribute('''DOMString''')
    
    seamless = zope.interface.Attribute('''boolean''')
    
    scrolling = zope.interface.Attribute('''DOMString''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    srcdoc = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''DOMString''')
    
    contentDocument = zope.interface.Attribute('''[readonly] Document''')
    
    contentWindow = zope.interface.Attribute('''[readonly] DOMWindow''')
    
class HTMLImageElement(HTMLElement):
    name = zope.interface.Attribute('''DOMString''')
    
    align = zope.interface.Attribute('''DOMString''')
    
    alt = zope.interface.Attribute('''DOMString''')
    
    border = zope.interface.Attribute('''DOMString''')
    
    crossOrigin = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''long''')
    
    hspace = zope.interface.Attribute('''long''')
    
    isMap = zope.interface.Attribute('''boolean''')
    
    longDesc = zope.interface.Attribute('''DOMString''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    useMap = zope.interface.Attribute('''DOMString''')
    
    vspace = zope.interface.Attribute('''long''')
    
    width = zope.interface.Attribute('''long''')
    
    complete = zope.interface.Attribute('''[readonly] boolean''')
    
    lowsrc = zope.interface.Attribute('''DOMString''')
    
    naturalHeight = zope.interface.Attribute('''[readonly] long''')
    
    naturalWidth = zope.interface.Attribute('''[readonly] long''')
    
    x = zope.interface.Attribute('''[readonly] long''')
    
    y = zope.interface.Attribute('''[readonly] long''')
    
class HTMLInputElement(HTMLElement):
    accept = zope.interface.Attribute('''DOMString''')
    
    alt = zope.interface.Attribute('''DOMString''')
    
    autocomplete = zope.interface.Attribute('''DOMString''')
    
    autofocus = zope.interface.Attribute('''boolean''')
    
    defaultChecked = zope.interface.Attribute('''boolean''')
    
    checked = zope.interface.Attribute('''boolean''')
    
    dirName = zope.interface.Attribute('''DOMString''')
    
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    files = zope.interface.Attribute('''FileList''')
    
    formAction = zope.interface.Attribute('''DOMString''')
    
    formEnctype = zope.interface.Attribute('''DOMString''')
    
    formMethod = zope.interface.Attribute('''DOMString''')
    
    formNoValidate = zope.interface.Attribute('''boolean''')
    
    formTarget = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''unsigned long''')
    
    indeterminate = zope.interface.Attribute('''boolean''')
    
    list = zope.interface.Attribute('''[readonly] HTMLElement''')
    
    max = zope.interface.Attribute('''DOMString''')
    
    maxLength = zope.interface.Attribute('''long''')
    
    min = zope.interface.Attribute('''DOMString''')
    
    multiple = zope.interface.Attribute('''boolean''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    pattern = zope.interface.Attribute('''DOMString''')
    
    placeholder = zope.interface.Attribute('''DOMString''')
    
    readOnly = zope.interface.Attribute('''boolean''')
    
    required = zope.interface.Attribute('''boolean''')
    
    size = zope.interface.Attribute('''unsigned long''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    step = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    defaultValue = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    valueAsDate = zope.interface.Attribute('''Date''')
    
    valueAsNumber = zope.interface.Attribute('''double''')
    
    def stepUp(n):
        pass
    
    def stepDown(n):
        pass
    
    width = zope.interface.Attribute('''unsigned long''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
    def select():
        pass
    
    selectionStart = zope.interface.Attribute('''long''')
    
    selectionEnd = zope.interface.Attribute('''long''')
    
    selectionDirection = zope.interface.Attribute('''DOMString''')
    
    def setRangeText(replacement):
        pass
    
    def setRangeText(replacement, start, end, selectionMode):
        pass
    
    def setSelectionRange(start, end, direction):
        pass
    
    align = zope.interface.Attribute('''DOMString''')
    
    webkitdirectory = zope.interface.Attribute('''boolean''')
    
    useMap = zope.interface.Attribute('''DOMString''')
    
    incremental = zope.interface.Attribute('''boolean''')
    
    webkitSpeech = zope.interface.Attribute('''boolean''')
    
    webkitGrammar = zope.interface.Attribute('''boolean''')
    
    onwebkitspeechchange = zope.interface.Attribute('''EventListener''')
    
    def setValueForUser(value):
        pass
    
    capture = zope.interface.Attribute('''DOMString''')
    
class HTMLIntentElement(HTMLElement):
    action = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    href = zope.interface.Attribute('''DOMString''')
    
    title = zope.interface.Attribute('''DOMString''')
    
    disposition = zope.interface.Attribute('''DOMString''')
    
class HTMLKeygenElement(HTMLElement):
    autofocus = zope.interface.Attribute('''boolean''')
    
    challenge = zope.interface.Attribute('''DOMString''')
    
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    keytype = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLLIElement(HTMLElement):
    type = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''long''')
    
class HTMLLabelElement(HTMLElement):
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    htmlFor = zope.interface.Attribute('''DOMString''')
    
    control = zope.interface.Attribute('''[readonly] HTMLElement''')
    
class HTMLLegendElement(HTMLElement):
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    align = zope.interface.Attribute('''DOMString''')
    
class HTMLLinkElement(HTMLElement):
    disabled = zope.interface.Attribute('''boolean''')
    
    charset = zope.interface.Attribute('''DOMString''')
    
    href = zope.interface.Attribute('''DOMString''')
    
    hreflang = zope.interface.Attribute('''DOMString''')
    
    media = zope.interface.Attribute('''DOMString''')
    
    rel = zope.interface.Attribute('''DOMString''')
    
    rev = zope.interface.Attribute('''DOMString''')
    
    target = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    sheet = zope.interface.Attribute('''[readonly] StyleSheet''')
    
class HTMLMapElement(HTMLElement):
    areas = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    name = zope.interface.Attribute('''DOMString''')
    
class HTMLMarqueeElement(HTMLElement):
    def start():
        pass
    
    def stop():
        pass
    
    behavior = zope.interface.Attribute('''DOMString''')
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    direction = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''DOMString''')
    
    hspace = zope.interface.Attribute('''unsigned long''')
    
    loop = zope.interface.Attribute('''long''')
    
    scrollAmount = zope.interface.Attribute('''long''')
    
    scrollDelay = zope.interface.Attribute('''long''')
    
    trueSpeed = zope.interface.Attribute('''boolean''')
    
    vspace = zope.interface.Attribute('''unsigned long''')
    
    width = zope.interface.Attribute('''DOMString''')
    
class HTMLMediaElement(HTMLElement):
    error = zope.interface.Attribute('''[readonly] MediaError''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    currentSrc = zope.interface.Attribute('''[readonly] DOMString''')
    
    networkState = zope.interface.Attribute('''[readonly] unsigned short''')
    
    preload = zope.interface.Attribute('''DOMString''')
    
    buffered = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    def load():
        pass
    
    def canPlayType(type):
        pass
    
    readyState = zope.interface.Attribute('''[readonly] unsigned short''')
    
    seeking = zope.interface.Attribute('''[readonly] boolean''')
    
    currentTime = zope.interface.Attribute('''float''')
    
    initialTime = zope.interface.Attribute('''[readonly] double''')
    
    startTime = zope.interface.Attribute('''[readonly] float''')
    
    duration = zope.interface.Attribute('''[readonly] float''')
    
    paused = zope.interface.Attribute('''[readonly] boolean''')
    
    defaultPlaybackRate = zope.interface.Attribute('''float''')
    
    playbackRate = zope.interface.Attribute('''float''')
    
    played = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    seekable = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    ended = zope.interface.Attribute('''[readonly] boolean''')
    
    autoplay = zope.interface.Attribute('''boolean''')
    
    loop = zope.interface.Attribute('''boolean''')
    
    def play():
        pass
    
    def pause():
        pass
    
    controls = zope.interface.Attribute('''boolean''')
    
    volume = zope.interface.Attribute('''float''')
    
    muted = zope.interface.Attribute('''boolean''')
    
    defaultMuted = zope.interface.Attribute('''boolean''')
    
    webkitPreservesPitch = zope.interface.Attribute('''boolean''')
    
    webkitHasClosedCaptions = zope.interface.Attribute('''[readonly] boolean''')
    
    webkitClosedCaptionsVisible = zope.interface.Attribute('''boolean''')
    
    webkitAudioDecodedByteCount = zope.interface.Attribute('''[readonly] unsigned long''')
    
    webkitVideoDecodedByteCount = zope.interface.Attribute('''[readonly] unsigned long''')
    
    mediaGroup = zope.interface.Attribute('''DOMString''')
    
    controller = zope.interface.Attribute('''MediaController''')
    
class HTMLMenuElement(HTMLElement):
    compact = zope.interface.Attribute('''boolean''')
    
class HTMLMetaElement(HTMLElement):
    content = zope.interface.Attribute('''DOMString''')
    
    httpEquiv = zope.interface.Attribute('''DOMString''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    scheme = zope.interface.Attribute('''DOMString''')
    
class HTMLMeterElement(HTMLElement):
    value = zope.interface.Attribute('''double''')
    
    min = zope.interface.Attribute('''double''')
    
    max = zope.interface.Attribute('''double''')
    
    low = zope.interface.Attribute('''double''')
    
    high = zope.interface.Attribute('''double''')
    
    optimum = zope.interface.Attribute('''double''')
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLModElement(HTMLElement):
    cite = zope.interface.Attribute('''DOMString''')
    
    dateTime = zope.interface.Attribute('''DOMString''')
    
class HTMLOListElement(HTMLElement):
    compact = zope.interface.Attribute('''boolean''')
    
    start = zope.interface.Attribute('''long''')
    
    reversed = zope.interface.Attribute('''boolean''')
    
    type = zope.interface.Attribute('''DOMString''')
    
class HTMLObjectElement(HTMLElement):
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    code = zope.interface.Attribute('''DOMString''')
    
    align = zope.interface.Attribute('''DOMString''')
    
    archive = zope.interface.Attribute('''DOMString''')
    
    border = zope.interface.Attribute('''DOMString''')
    
    codeBase = zope.interface.Attribute('''DOMString''')
    
    codeType = zope.interface.Attribute('''DOMString''')
    
    data = zope.interface.Attribute('''DOMString''')
    
    declare = zope.interface.Attribute('''boolean''')
    
    height = zope.interface.Attribute('''DOMString''')
    
    hspace = zope.interface.Attribute('''long''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    standby = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    useMap = zope.interface.Attribute('''DOMString''')
    
    vspace = zope.interface.Attribute('''long''')
    
    width = zope.interface.Attribute('''DOMString''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    contentDocument = zope.interface.Attribute('''[readonly] Document''')
    
class HTMLOptGroupElement(HTMLElement):
    disabled = zope.interface.Attribute('''boolean''')
    
    label = zope.interface.Attribute('''DOMString''')
    
class HTMLOptionElement(HTMLElement):
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    label = zope.interface.Attribute('''DOMString''')
    
    defaultSelected = zope.interface.Attribute('''boolean''')
    
    selected = zope.interface.Attribute('''boolean''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    text = zope.interface.Attribute('''[readonly] DOMString''')
    
    index = zope.interface.Attribute('''[readonly] long''')
    
class HTMLOptionsCollection(HTMLCollection):
    selectedIndex = zope.interface.Attribute('''long''')
    
    length = zope.interface.Attribute('''unsigned long''')
    
    def namedItem(name):
        pass
    
    def add(option, index):
        pass
    
    def remove(index):
        pass
    
class HTMLOutputElement(HTMLElement):
    htmlFor = zope.interface.Attribute('''DOMSettableTokenList''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    defaultValue = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLParagraphElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
class HTMLParamElement(HTMLElement):
    name = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    valueType = zope.interface.Attribute('''DOMString''')
    
class HTMLPreElement(HTMLElement):
    width = zope.interface.Attribute('''long''')
    
    wrap = zope.interface.Attribute('''boolean''')
    
class HTMLProgressElement(HTMLElement):
    value = zope.interface.Attribute('''double''')
    
    max = zope.interface.Attribute('''double''')
    
    position = zope.interface.Attribute('''[readonly] double''')
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLPropertiesCollection(HTMLCollection):
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def item(index):
        pass
    
    names = zope.interface.Attribute('''[readonly] DOMStringList''')
    
    def namedItem(name):
        pass
    
class HTMLQuoteElement(HTMLElement):
    cite = zope.interface.Attribute('''DOMString''')
    
class HTMLScriptElement(HTMLElement):
    text = zope.interface.Attribute('''DOMString''')
    
    htmlFor = zope.interface.Attribute('''DOMString''')
    
    event = zope.interface.Attribute('''DOMString''')
    
    charset = zope.interface.Attribute('''DOMString''')
    
    async = zope.interface.Attribute('''boolean''')
    
    defer = zope.interface.Attribute('''boolean''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    crossOrigin = zope.interface.Attribute('''DOMString''')
    
    nonce = zope.interface.Attribute('''DOMString''')
    
class HTMLSelectElement(HTMLElement):
    autofocus = zope.interface.Attribute('''boolean''')
    
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    multiple = zope.interface.Attribute('''boolean''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    required = zope.interface.Attribute('''boolean''')
    
    size = zope.interface.Attribute('''long''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    options = zope.interface.Attribute('''[readonly] HTMLOptionsCollection''')
    
    length = zope.interface.Attribute('''unsigned long''')
    
    def item(index):
        pass
    
    def namedItem(name):
        pass
    
    def add(element, before):
        pass
    
    def remove(index):
        pass
    
    selectedOptions = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    selectedIndex = zope.interface.Attribute('''long''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
class HTMLSourceElement(HTMLElement):
    src = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    media = zope.interface.Attribute('''DOMString''')
    
class HTMLStyleElement(HTMLElement):
    disabled = zope.interface.Attribute('''boolean''')
    
    scoped = zope.interface.Attribute('''boolean''')
    
    media = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''DOMString''')
    
    sheet = zope.interface.Attribute('''[readonly] StyleSheet''')
    
class HTMLTableCaptionElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
class HTMLTableCellElement(HTMLElement):
    cellIndex = zope.interface.Attribute('''[readonly] long''')
    
    abbr = zope.interface.Attribute('''DOMString''')
    
    align = zope.interface.Attribute('''DOMString''')
    
    axis = zope.interface.Attribute('''DOMString''')
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    ch = zope.interface.Attribute('''DOMString''')
    
    chOff = zope.interface.Attribute('''DOMString''')
    
    colSpan = zope.interface.Attribute('''long''')
    
    headers = zope.interface.Attribute('''DOMString''')
    
    height = zope.interface.Attribute('''DOMString''')
    
    noWrap = zope.interface.Attribute('''boolean''')
    
    rowSpan = zope.interface.Attribute('''long''')
    
    scope = zope.interface.Attribute('''DOMString''')
    
    vAlign = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''DOMString''')
    
class HTMLTableColElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    ch = zope.interface.Attribute('''DOMString''')
    
    chOff = zope.interface.Attribute('''DOMString''')
    
    span = zope.interface.Attribute('''long''')
    
    vAlign = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''DOMString''')
    
class HTMLTableElement(HTMLElement):
    caption = zope.interface.Attribute('''HTMLTableCaptionElement''')
    
    tHead = zope.interface.Attribute('''HTMLTableSectionElement''')
    
    tFoot = zope.interface.Attribute('''HTMLTableSectionElement''')
    
    rows = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    tBodies = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    align = zope.interface.Attribute('''DOMString''')
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    border = zope.interface.Attribute('''DOMString''')
    
    cellPadding = zope.interface.Attribute('''DOMString''')
    
    cellSpacing = zope.interface.Attribute('''DOMString''')
    
    frame = zope.interface.Attribute('''DOMString''')
    
    rules = zope.interface.Attribute('''DOMString''')
    
    summary = zope.interface.Attribute('''DOMString''')
    
    width = zope.interface.Attribute('''DOMString''')
    
    def createTHead():
        pass
    
    def deleteTHead():
        pass
    
    def createTFoot():
        pass
    
    def deleteTFoot():
        pass
    
    def createTBody():
        pass
    
    def createCaption():
        pass
    
    def deleteCaption():
        pass
    
    def insertRow(index):
        pass
    
    def deleteRow(index):
        pass
    
class HTMLTableRowElement(HTMLElement):
    rowIndex = zope.interface.Attribute('''[readonly] long''')
    
    sectionRowIndex = zope.interface.Attribute('''[readonly] long''')
    
    cells = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    align = zope.interface.Attribute('''DOMString''')
    
    bgColor = zope.interface.Attribute('''DOMString''')
    
    ch = zope.interface.Attribute('''DOMString''')
    
    chOff = zope.interface.Attribute('''DOMString''')
    
    vAlign = zope.interface.Attribute('''DOMString''')
    
    def insertCell(index):
        pass
    
    def deleteCell(index):
        pass
    
class HTMLTableSectionElement(HTMLElement):
    align = zope.interface.Attribute('''DOMString''')
    
    ch = zope.interface.Attribute('''DOMString''')
    
    chOff = zope.interface.Attribute('''DOMString''')
    
    vAlign = zope.interface.Attribute('''DOMString''')
    
    rows = zope.interface.Attribute('''[readonly] HTMLCollection''')
    
    def insertRow(index):
        pass
    
    def deleteRow(index):
        pass
    
class HTMLTemplateElement(HTMLElement):
    content = zope.interface.Attribute('''[readonly] DocumentFragment''')
    
class HTMLTextAreaElement(HTMLElement):
    autofocus = zope.interface.Attribute('''boolean''')
    
    cols = zope.interface.Attribute('''long''')
    
    dirName = zope.interface.Attribute('''DOMString''')
    
    disabled = zope.interface.Attribute('''boolean''')
    
    form = zope.interface.Attribute('''[readonly] HTMLFormElement''')
    
    maxLength = zope.interface.Attribute('''long''')
    
    name = zope.interface.Attribute('''DOMString''')
    
    placeholder = zope.interface.Attribute('''DOMString''')
    
    readOnly = zope.interface.Attribute('''boolean''')
    
    required = zope.interface.Attribute('''boolean''')
    
    rows = zope.interface.Attribute('''long''')
    
    wrap = zope.interface.Attribute('''DOMString''')
    
    type = zope.interface.Attribute('''[readonly] DOMString''')
    
    defaultValue = zope.interface.Attribute('''DOMString''')
    
    value = zope.interface.Attribute('''DOMString''')
    
    textLength = zope.interface.Attribute('''[readonly] unsigned long''')
    
    willValidate = zope.interface.Attribute('''[readonly] boolean''')
    
    validity = zope.interface.Attribute('''[readonly] ValidityState''')
    
    validationMessage = zope.interface.Attribute('''[readonly] DOMString''')
    
    def checkValidity():
        pass
    
    def setCustomValidity(error):
        pass
    
    labels = zope.interface.Attribute('''[readonly] NodeList''')
    
    def select():
        pass
    
    selectionStart = zope.interface.Attribute('''long''')
    
    selectionEnd = zope.interface.Attribute('''long''')
    
    selectionDirection = zope.interface.Attribute('''DOMString''')
    
    def setRangeText(replacement):
        pass
    
    def setRangeText(replacement, start, end, selectionMode):
        pass
    
    def setSelectionRange(start, end, direction):
        pass
    
class HTMLTitleElement(HTMLElement):
    text = zope.interface.Attribute('''DOMString''')
    
class HTMLTrackElement(HTMLElement):
    kind = zope.interface.Attribute('''DOMString''')
    
    src = zope.interface.Attribute('''DOMString''')
    
    srclang = zope.interface.Attribute('''DOMString''')
    
    label = zope.interface.Attribute('''DOMString''')
    
    default = zope.interface.Attribute('''boolean''')
    
    readyState = zope.interface.Attribute('''[readonly] unsigned short''')
    
    track = zope.interface.Attribute('''[readonly] TextTrack''')
    
class HTMLUListElement(HTMLElement):
    compact = zope.interface.Attribute('''boolean''')
    
    type = zope.interface.Attribute('''DOMString''')
    
class HTMLVideoElement(HTMLMediaElement):
    width = zope.interface.Attribute('''unsigned long''')
    
    height = zope.interface.Attribute('''unsigned long''')
    
    videoWidth = zope.interface.Attribute('''[readonly] unsigned long''')
    
    videoHeight = zope.interface.Attribute('''[readonly] unsigned long''')
    
    poster = zope.interface.Attribute('''DOMString''')
    
    webkitSupportsFullscreen = zope.interface.Attribute('''[readonly] boolean''')
    
    webkitDisplayingFullscreen = zope.interface.Attribute('''[readonly] boolean''')
    
    def webkitEnterFullscreen():
        pass
    
    def webkitExitFullscreen():
        pass
    
    def webkitEnterFullScreen():
        pass
    
    def webkitExitFullScreen():
        pass
    
    webkitDecodedFrameCount = zope.interface.Attribute('''[readonly] unsigned long''')
    
    webkitDroppedFrameCount = zope.interface.Attribute('''[readonly] unsigned long''')
    
class ImageData(zope.interface.Interface):
    width = zope.interface.Attribute('''[readonly] long''')
    
    height = zope.interface.Attribute('''[readonly] long''')
    
    data = zope.interface.Attribute('''[readonly] Uint8ClampedArray''')
    
class MediaController(zope.interface.Interface):
    buffered = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    seekable = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    duration = zope.interface.Attribute('''[readonly] double''')
    
    currentTime = zope.interface.Attribute('''double''')
    
    paused = zope.interface.Attribute('''[readonly] boolean''')
    
    played = zope.interface.Attribute('''[readonly] TimeRanges''')
    
    playbackState = zope.interface.Attribute('''[readonly] DOMString''')
    
    def play():
        pass
    
    def pause():
        pass
    
    def unpause():
        pass
    
    defaultPlaybackRate = zope.interface.Attribute('''double''')
    
    playbackRate = zope.interface.Attribute('''double''')
    
    volume = zope.interface.Attribute('''double''')
    
    muted = zope.interface.Attribute('''boolean''')
    
    def addEventListener(type, listener, useCapture):
        pass
    
    def removeEventListener(type, listener, useCapture):
        pass
    
    def dispatchEvent(evt):
        pass
    
class MediaError(zope.interface.Interface):
    code = zope.interface.Attribute('''[readonly] unsigned short''')
    
class MediaKeyError(zope.interface.Interface):
    code = zope.interface.Attribute('''[readonly] unsigned short''')
    
class MediaKeyEvent(Event):
    keySystem = zope.interface.Attribute('''[readonly] DOMString''')
    
    sessionId = zope.interface.Attribute('''[readonly] DOMString''')
    
    initData = zope.interface.Attribute('''[readonly] Uint8Array''')
    
    message = zope.interface.Attribute('''[readonly] Uint8Array''')
    
    defaultURL = zope.interface.Attribute('''[readonly] DOMString''')
    
    errorCode = zope.interface.Attribute('''[readonly] MediaKeyError''')
    
    systemCode = zope.interface.Attribute('''[readonly] unsigned short''')
    
class RadioNodeList(NodeList):
    value = zope.interface.Attribute('''DOMString''')
    
class TextMetrics(zope.interface.Interface):
    width = zope.interface.Attribute('''[readonly] float''')
    
class TimeRanges(zope.interface.Interface):
    length = zope.interface.Attribute('''[readonly] unsigned long''')
    
    def start(index):
        pass
    
    def end(index):
        pass
    
class ValidityState(zope.interface.Interface):
    valueMissing = zope.interface.Attribute('''[readonly] boolean''')
    
    typeMismatch = zope.interface.Attribute('''[readonly] boolean''')
    
    patternMismatch = zope.interface.Attribute('''[readonly] boolean''')
    
    tooLong = zope.interface.Attribute('''[readonly] boolean''')
    
    rangeUnderflow = zope.interface.Attribute('''[readonly] boolean''')
    
    rangeOverflow = zope.interface.Attribute('''[readonly] boolean''')
    
    stepMismatch = zope.interface.Attribute('''[readonly] boolean''')
    
    badInput = zope.interface.Attribute('''[readonly] boolean''')
    
    customError = zope.interface.Attribute('''[readonly] boolean''')
    
    valid = zope.interface.Attribute('''[readonly] boolean''')

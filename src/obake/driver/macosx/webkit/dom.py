from weakref import WeakValueDictionary
from zope.interface import implements
from obake.dom import interfaces as I
from obake.driver.macosx.webkit.impl import invoke_later_sync

INDEX_SIZE_ERR = 1

DOMSTRING_SIZE_ERR = 2

HIERARCHY_REQUEST_ERR = 3

WRONG_DOCUMENT_ERR = 4

INVALID_CHARACTER_ERR = 5

NO_DATA_ALLOWED_ERR = 6

NO_MODIFICATION_ALLOWED_ERR = 7

NOT_FOUND_ERR = 8

NOT_SUPPORTED_ERR = 9

INUSE_ATTRIBUTE_ERR = 10

INVALID_STATE_ERR = 11

SYNTAX_ERR = 12

INVALID_MODIFICATION_ERR = 13

NAMESPACE_ERR = 14

INVALID_ACCESS_ERR = 15

VALIDATION_ERR = 16

TYPE_MISMATCH_ERR = 17

class DOMStringList(object):
    implements(I.DOMStringList)
    
    _instances = WeakValueDictionary()
    
    
    def item(self, index):
        return invoke_later_sync(self.impl.item_, [index])
    
    @property
    def length(self):
        return self.impl.length()
    
    def contains(self, str):
        return invoke_later_sync(self.impl.contains_, [str])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class NameList(object):
    implements(I.NameList)
    
    _instances = WeakValueDictionary()
    
    
    def getName(self, index):
        return invoke_later_sync(self.impl.getName_, [index])
    
    def getNamespaceURI(self, index):
        return invoke_later_sync(self.impl.getNamespaceURI_, [index])
    
    @property
    def length(self):
        return self.impl.length()
    
    def contains(self, str):
        return invoke_later_sync(self.impl.contains_, [str])
    
    def containsNS(self, namespaceURI, name):
        return invoke_later_sync(self.impl.containsNS__, [namespaceURI, name])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMImplementationList(object):
    implements(I.DOMImplementationList)
    
    _instances = WeakValueDictionary()
    
    
    def item(self, index):
        return DOMImplementation(invoke_later_sync(self.impl.item_, [index]))
    
    @property
    def length(self):
        return self.impl.length()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMImplementationSource(object):
    implements(I.DOMImplementationSource)
    
    _instances = WeakValueDictionary()
    
    
    def getDOMImplementation(self, features):
        return DOMImplementation(invoke_later_sync(self.impl.getDOMImplementation_, [features]))
    
    def getDOMImplementationList(self, features):
        return DOMImplementationList(invoke_later_sync(self.impl.getDOMImplementationList_, [features]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMImplementation(object):
    implements(I.DOMImplementation)
    
    _instances = WeakValueDictionary()
    
    
    def hasFeature(self, feature, version):
        return invoke_later_sync(self.impl.hasFeature__, [feature, version])
    
    def createDocumentType(self, qualifiedName, publicId, systemId):
        return DocumentType(invoke_later_sync(self.impl.createDocumentType___, [qualifiedName, publicId, systemId]))
    
    def createDocument(self, namespaceURI, qualifiedName, doctype):
        return Document(invoke_later_sync(self.impl.createDocument___, [namespaceURI, qualifiedName, doctype.impl]))
    
    def getFeature(self, feature, version):
        return DOMObject(invoke_later_sync(self.impl.getFeature__, [feature, version]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Node(object):
    implements(I.Node)
    
    _instances = WeakValueDictionary()
    
    
    ELEMENT_NODE = 1
    
    ATTRIBUTE_NODE = 2
    
    TEXT_NODE = 3
    
    CDATA_SECTION_NODE = 4
    
    ENTITY_REFERENCE_NODE = 5
    
    ENTITY_NODE = 6
    
    PROCESSING_INSTRUCTION_NODE = 7
    
    COMMENT_NODE = 8
    
    DOCUMENT_NODE = 9
    
    DOCUMENT_TYPE_NODE = 10
    
    DOCUMENT_FRAGMENT_NODE = 11
    
    NOTATION_NODE = 12
    
    @property
    def nodeName(self):
        return self.impl.nodeName()
    
    @property
    def nodeValue(self):
        return self.impl.nodeValue()
    
    @property
    def nodeType(self):
        return self.impl.nodeType()
    
    @property
    def parentNode(self):
        return Node(self.impl.parentNode())
    
    @property
    def childNodes(self):
        return NodeList(self.impl.childNodes())
    
    @property
    def firstChild(self):
        return Node(self.impl.firstChild())
    
    @property
    def lastChild(self):
        return Node(self.impl.lastChild())
    
    @property
    def previousSibling(self):
        return Node(self.impl.previousSibling())
    
    @property
    def nextSibling(self):
        return Node(self.impl.nextSibling())
    
    @property
    def attributes(self):
        return NodeList(invoke_later_sync(self.impl.attributes))
    
    @property
    def ownerDocument(self):
        return Document(self.impl.ownerDocument())
    
    def insertBefore(self, newChild, refChild):
        return Node(invoke_later_sync(self.impl.insertBefore__, [newChild.impl, refChild.impl]))
    
    def replaceChild(self, newChild, oldChild):
        return Node(invoke_later_sync(self.impl.replaceChild__, [newChild.impl, oldChild.impl]))
    
    def removeChild(self, oldChild):
        return Node(invoke_later_sync(self.impl.removeChild_, [oldChild.impl]))
    
    def appendChild(self, newChild):
        return Node(invoke_later_sync(self.impl.appendChild_, [newChild.impl]))
    
    def hasChildNodes(self, ):
        return invoke_later_sync(self.impl.hasChildNodes, [])
    
    def cloneNode(self, deep):
        return Node(invoke_later_sync(self.impl.cloneNode_, [deep]))
    
    def normalize(self, ):
        return invoke_later_sync(self.impl.normalize, [])
    
    def isSupported(self, feature, version):
        return invoke_later_sync(self.impl.isSupported__, [feature, version])
    
    @property
    def namespaceURI(self):
        return self.impl.namespaceURI()
    
    @property
    def prefix(self):
        return self.impl.prefix()
    
    @property
    def localName(self):
        return self.impl.localName()
    
    def hasAttributes(self, ):
        return invoke_later_sync(self.impl.hasAttributes, [])
    
    @property
    def baseURI(self):
        return self.impl.baseURI()
    
    DOCUMENT_POSITION_DISCONNECTED = 0x01
    
    DOCUMENT_POSITION_PRECEDING = 0x02
    
    DOCUMENT_POSITION_FOLLOWING = 0x04
    
    DOCUMENT_POSITION_CONTAINS = 0x08
    
    DOCUMENT_POSITION_CONTAINED_BY = 0x10
    
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 0x20
    
    def compareDocumentPosition(self, other):
        return invoke_later_sync(self.impl.compareDocumentPosition_, [other.impl])
    
    @property
    def textContent(self):
        return self.impl.textContent()
    
    def isSameNode(self, other):
        return invoke_later_sync(self.impl.isSameNode_, [other.impl])
    
    def lookupPrefix(self, namespaceURI):
        return invoke_later_sync(self.impl.lookupPrefix_, [namespaceURI])
    
    def isDefaultNamespace(self, namespaceURI):
        return invoke_later_sync(self.impl.isDefaultNamespace_, [namespaceURI])
    
    def lookupNamespaceURI(self, prefix):
        return invoke_later_sync(self.impl.lookupNamespaceURI_, [prefix])
    
    def isEqualNode(self, arg):
        return invoke_later_sync(self.impl.isEqualNode_, [arg.impl])
    
    def getFeature(self, feature, version):
        return DOMObject(invoke_later_sync(self.impl.getFeature__, [feature, version]))
    
    def setUserData(self, key, data, handler):
        return DOMUserData(invoke_later_sync(self.impl.setUserData___, [key, data.impl, handler.impl]))
    
    def getUserData(self, key):
        return DOMUserData(invoke_later_sync(self.impl.getUserData_, [key]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        assert impl.__class__.__name__.startswith('DOM')
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(globals()[impl.__class__.__name__[3:]])
        return instance


class NodeList(list):
    implements(I.NodeList)
    
    _instances = WeakValueDictionary()
    
    
    def item(self, index):
        return Node(self.impl.item_(index))
    
    @property
    def length(self):
        return self.impl.length()

    def __setitem__(self, index, value):
        raise NotImplementedError

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def pop(self, index):
        raise NotImplementedError

    def extend(self, value):
        raise NotImplementedError

    def remove(self, value):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError
        
    def sort(self):
        raise NotImplementedError

    def __delitem__(self, index):
        raise NotImplementedError

    def __getitem__(self, index):
        return self.item(index)

    def __len__(self):
        return self.length

    def __iter__(self):
        for i in range(0, self.length):
            yield self.item(i)

    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = list.__new__(cls)
        return instance


class NamedNodeMap(object):
    implements(I.NamedNodeMap)
    
    _instances = WeakValueDictionary()
    
    
    def getNamedItem(self, name):
        return Node(invoke_later_sync(self.impl.getNamedItem_, [name]))
    
    def setNamedItem(self, arg):
        return Node(invoke_later_sync(self.impl.setNamedItem_, [arg.impl]))
    
    def removeNamedItem(self, name):
        return Node(invoke_later_sync(self.impl.removeNamedItem_, [name]))
    
    def item(self, index):
        return Node(invoke_later_sync(self.impl.item_, [index]))
    
    @property
    def length(self):
        return self.impl.length()
    
    def getNamedItemNS(self, namespaceURI, localName):
        return Node(invoke_later_sync(self.impl.getNamedItemNS__, [namespaceURI, localName]))
    
    def setNamedItemNS(self, arg):
        return Node(invoke_later_sync(self.impl.setNamedItemNS_, [arg.impl]))
    
    def removeNamedItemNS(self, namespaceURI, localName):
        return Node(invoke_later_sync(self.impl.removeNamedItemNS__, [namespaceURI, localName]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class CharacterData(Node):
    implements(I.CharacterData)
    
    @property
    def data(self):
        return self.impl.data()
    
    @property
    def length(self):
        return self.impl.length()
    
    def substringData(self, offset, count):
        return invoke_later_sync(self.impl.substringData__, [offset, count])
    
    def appendData(self, arg):
        return invoke_later_sync(self.impl.appendData_, [arg])
    
    def insertData(self, offset, arg):
        return invoke_later_sync(self.impl.insertData__, [offset, arg])
    
    def deleteData(self, offset, count):
        return invoke_later_sync(self.impl.deleteData__, [offset, count])
    
    def replaceData(self, offset, count, arg):
        return invoke_later_sync(self.impl.replaceData___, [offset, count, arg])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Attr(Node):
    implements(I.Attr)
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def specified(self):
        return self.impl.specified()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def ownerElement(self):
        return self.impl.ownerElement()
    
    @property
    def schemaTypeInfo(self):
        return self.impl.schemaTypeInfo()
    
    @property
    def isId(self):
        return self.impl.isId()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Element(Node):
    implements(I.Element)

    @property
    def tagName(self):
        return self.impl.tagName()
    
    def getAttribute(self, name):
        return invoke_later_sync(self.impl.getAttribute_, [name])
    
    def setAttribute(self, name, value):
        return invoke_later_sync(self.impl.setAttribute__, [name, value])
    
    def removeAttribute(self, name):
        return invoke_later_sync(self.impl.removeAttribute_, [name])
    
    def getAttributeNode(self, name):
        return Attr(invoke_later_sync(self.impl.getAttributeNode_, [name]))
    
    def setAttributeNode(self, newAttr):
        return Attr(invoke_later_sync(self.impl.setAttributeNode_, [newAttr.impl]))
    
    def removeAttributeNode(self, oldAttr):
        return Attr(invoke_later_sync(self.impl.removeAttributeNode_, [oldAttr.impl]))
    
    def getElementsByTagName(self, name):
        return NodeList(invoke_later_sync(self.impl.getElementsByTagName_, [name]))
    
    def getAttributeNS(self, namespaceURI, localName):
        return invoke_later_sync(self.impl.getAttributeNS__, [namespaceURI, localName])
    
    def setAttributeNS(self, namespaceURI, qualifiedName, value):
        return invoke_later_sync(self.impl.setAttributeNS___, [namespaceURI, qualifiedName, value])
    
    def removeAttributeNS(self, namespaceURI, localName):
        return invoke_later_sync(self.impl.removeAttributeNS__, [namespaceURI, localName])
    
    def getAttributeNodeNS(self, namespaceURI, localName):
        return Attr(invoke_later_sync(self.impl.getAttributeNodeNS__, [namespaceURI, localName]))
    
    def setAttributeNodeNS(self, newAttr):
        return Attr(invoke_later_sync(self.impl.setAttributeNodeNS_, [newAttr.impl]))
    
    def getElementsByTagNameNS(self, namespaceURI, localName):
        return NodeList(invoke_later_sync(self.impl.getElementsByTagNameNS__, [namespaceURI, localName]))
    
    def hasAttribute(self, name):
        return invoke_later_sync(self.impl.hasAttribute_, [name])
    
    def hasAttributeNS(self, namespaceURI, localName):
        return invoke_later_sync(self.impl.hasAttributeNS__, [namespaceURI, localName])
    
    @property
    def schemaTypeInfo(self):
        return self.impl.schemaTypeInfo()
    
    def setIdAttribute(self, name, isId):
        return invoke_later_sync(self.impl.setIdAttribute__, [name, isId])
    
    def setIdAttributeNS(self, namespaceURI, localName, isId):
        return invoke_later_sync(self.impl.setIdAttributeNS___, [namespaceURI, localName, isId])
    
    def setIdAttributeNode(self, idAttr, isId):
        return invoke_later_sync(self.impl.setIdAttributeNode__, [idAttr.impl, isId])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Text(CharacterData):
    implements(I.Text)

    def splitText(self, offset):
        return Text(invoke_later_sync(self.impl.splitText_, [offset]))
    
    @property
    def isElementContentWhitespace(self):
        return self.impl.isElementContentWhitespace()
    
    @property
    def wholeText(self):
        return self.impl.wholeText()
    
    def replaceWholeText(self, content):
        return Text(invoke_later_sync(self.impl.replaceWholeText_, [content]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class TypeInfo(object):
    implements(I.TypeInfo)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def typeName(self):
        return self.impl.typeName()
    
    @property
    def typeNamespace(self):
        return self.impl.typeNamespace()
    
    DERIVATION_RESTRICTION = 0x00000001
    
    DERIVATION_EXTENSION = 0x00000002
    
    DERIVATION_UNION = 0x00000004
    
    DERIVATION_LIST = 0x00000008
    
    def isDerivedFrom(self, typeNamespaceArg, typeNameArg, derivationMethod):
        return invoke_later_sync(self.impl.isDerivedFrom___, [typeNamespaceArg, typeNameArg, derivationMethod])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class UserDataHandler(object):
    implements(I.UserDataHandler)
    
    _instances = WeakValueDictionary()
    
    
    NODE_CLONED = 1
    
    NODE_IMPORTED = 2
    
    NODE_DELETED = 3
    
    NODE_RENAMED = 4
    
    NODE_ADOPTED = 5
    
    def handle(self, operation, key, data, src, dst):
        return invoke_later_sync(self.impl.handle_____, [operation, key, data.impl, src.impl, dst.impl])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMError(object):
    implements(I.DOMError)
    
    _instances = WeakValueDictionary()
    
    
    SEVERITY_WARNING = 1
    
    SEVERITY_ERROR = 2
    
    SEVERITY_FATAL_ERROR = 3
    
    @property
    def severity(self):
        return self.impl.severity()
    
    @property
    def message(self):
        return self.impl.message()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def relatedException(self):
        return self.impl.relatedException()
    
    @property
    def relatedData(self):
        return self.impl.relatedData()
    
    @property
    def location(self):
        return self.impl.location()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMErrorHandler(object):
    implements(I.DOMErrorHandler)
    
    _instances = WeakValueDictionary()
    
    
    def handleError(self, error):
        return invoke_later_sync(self.impl.handleError_, [error.impl])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMLocator(object):
    implements(I.DOMLocator)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def lineNumber(self):
        return self.impl.lineNumber()
    
    @property
    def columnNumber(self):
        return self.impl.columnNumber()
    
    @property
    def byteOffset(self):
        return self.impl.byteOffset()
    
    @property
    def utf16Offset(self):
        return self.impl.utf16Offset()
    
    @property
    def relatedNode(self):
        return self.impl.relatedNode()
    
    @property
    def uri(self):
        return self.impl.uri()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMConfiguration(object):
    implements(I.DOMConfiguration)
    
    _instances = WeakValueDictionary()
    
    
    def setParameter(self, name, value):
        return invoke_later_sync(self.impl.setParameter__, [name, value.impl])
    
    def getParameter(self, name):
        return DOMUserData(invoke_later_sync(self.impl.getParameter_, [name]))
    
    def canSetParameter(self, name, value):
        return invoke_later_sync(self.impl.canSetParameter__, [name, value.impl])
    
    @property
    def parameterNames(self):
        return self.impl.parameterNames()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DocumentType(Node):
    implements(I.DocumentType)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def entities(self):
        return self.impl.entities()
    
    @property
    def notations(self):
        return self.impl.notations()
    
    @property
    def publicId(self):
        return self.impl.publicId()
    
    @property
    def systemId(self):
        return self.impl.systemId()
    
    @property
    def internalSubset(self):
        return self.impl.internalSubset()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Notation(Node):
    implements(I.Notation)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def publicId(self):
        return self.impl.publicId()
    
    @property
    def systemId(self):
        return self.impl.systemId()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Entity(Node):
    implements(I.Entity)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def publicId(self):
        return self.impl.publicId()
    
    @property
    def systemId(self):
        return self.impl.systemId()
    
    @property
    def notationName(self):
        return self.impl.notationName()
    
    @property
    def inputEncoding(self):
        return self.impl.inputEncoding()
    
    @property
    def xmlEncoding(self):
        return self.impl.xmlEncoding()
    
    @property
    def xmlVersion(self):
        return self.impl.xmlVersion()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class ProcessingInstruction(Node):
    implements(I.ProcessingInstruction)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def target(self):
        return self.impl.target()
    
    @property
    def data(self):
        return self.impl.data()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Document(Node):
    implements(I.Document)
    
    _instances = WeakValueDictionary()
    
    
    @property
    def doctype(self):
        return self.impl.doctype()
    
    @property
    def implementation(self):
        return self.impl.implementation()
    
    @property
    def documentElement(self):
        return Element(self.impl.documentElement())
    
    def createElement(self, tagName):
        return Element(invoke_later_sync(self.impl.createElement_, [tagName]))
    
    def createDocumentFragment(self, ):
        return DocumentFragment(invoke_later_sync(self.impl.createDocumentFragment, []))
    
    def createTextNode(self, data):
        return Text(invoke_later_sync(self.impl.createTextNode_, [data]))
    
    def createComment(self, data):
        return Comment(invoke_later_sync(self.impl.createComment_, [data]))
    
    def createCDATASection(self, data):
        return CDATASection(invoke_later_sync(self.impl.createCDATASection_, [data]))
    
    def createProcessingInstruction(self, target, data):
        return ProcessingInstruction(invoke_later_sync(self.impl.createProcessingInstruction__, [target, data]))
    
    def createAttribute(self, name):
        return Attr(invoke_later_sync(self.impl.createAttribute_, [name]))
    
    def createEntityReference(self, name):
        return EntityReference(invoke_later_sync(self.impl.createEntityReference_, [name]))
    
    def getElementsByTagName(self, tagname):
        return NodeList(invoke_later_sync(self.impl.getElementsByTagName_, [tagname]))
    
    def importNode(self, importedNode, deep):
        return Node(invoke_later_sync(self.impl.importNode__, [importedNode.impl, deep]))
    
    def createElementNS(self, namespaceURI, qualifiedName):
        return Element(invoke_later_sync(self.impl.createElementNS__, [namespaceURI, qualifiedName]))
    
    def createAttributeNS(self, namespaceURI, qualifiedName):
        return Attr(invoke_later_sync(self.impl.createAttributeNS__, [namespaceURI, qualifiedName]))
    
    def getElementsByTagNameNS(self, namespaceURI, localName):
        return NodeList(invoke_later_sync(self.impl.getElementsByTagNameNS__, [namespaceURI, localName]))
    
    def getElementById(self, elementId):
        return Element(invoke_later_sync(self.impl.getElementById_, [elementId]))
    
    @property
    def inputEncoding(self):
        return self.impl.inputEncoding()
    
    @property
    def xmlEncoding(self):
        return self.impl.xmlEncoding()
    
    @property
    def xmlStandalone(self):
        return self.impl.xmlStandalone()
    
    @property
    def xmlVersion(self):
        return self.impl.xmlVersion()
    
    @property
    def strictErrorChecking(self):
        return self.impl.strictErrorChecking()
    
    @property
    def documentURI(self):
        return self.impl.documentURI()
    
    def adoptNode(self, source):
        return Node(invoke_later_sync(self.impl.adoptNode_, [source.impl]))
    
    @property
    def domConfig(self):
        return self.impl.domConfig()
    
    def normalizeDocument(self, ):
        return invoke_later_sync(self.impl.normalizeDocument, [])
    
    def renameNode(self, n, namespaceURI, qualifiedName):
        return Node(invoke_later_sync(self.impl.renameNode___, [n.impl, namespaceURI, qualifiedName]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class Event(object):
    implements(I.Event)

    @property
    def type(self):
        return self.impl.type()
   
    @property
    def target(self):
        return self.impl.target()

    @property
    def currentTarget(self):
        return self.impl.currentTarget()
    
    @property
    def eventPhase(self):
        return self.impl.eventPhase()

    @property
    def bubbles(self):
        return self.impl.bubbles()

    @property
    def cancelable(self):
        return self.impl.cancelable()

    @property
    def timeStamp(self):
        return self.impl.timeStamp()
    
    def stopPropagation(self):
        return invoke_later_sync(self.impl.stopPropagation, [])

    def preventDefault(self):
        return invoke_later_sync(self.impl.preventDefault, [])
    
    def initEvent(self, eventTypeArg, canBubbleArg, cancelableArg):
        return invoke_later_sync(self.impl.initEvent___, [eventTypeArg, canBubbleArg, cancelableArg])

    def stopImmediatePropagation(self):
        return invoke_later_sync(self.impl.stopImmediatePropagation, [])

    @property
    def defaultPrevented(self):
        return self.impl.defaultPrevented()

    @property
    def isTrusted(self):
        return self.impl.isTrusted()


class DocumentEvent(object):
    implements(I.DocumentEvent)


class UIEvent(Event):
    @property
    def view(self):
        return self.impl.view()

    @property
    def detail(self):
        return self.impl.detail()


class FocusEvent(UIEvent):
    @property
    def relatedTarget(self):
        return self.impl.relatedTarget()


class MouseEvent(UIEvent):
    @property
    def screenX(self):
        return self.impl.screenX()

    @property
    def screenY(self):
        return self.impl.screenY()

    @property
    def clientX(self):
        return self.impl.clientX()

    @property
    def clientY(self):
        return self.impl.clientY()

    @property
    def ctrlKey(self):
        return self.impl.ctrlKey()

    @property
    def shiftKey(self):
        return self.impl.shiftKey()

    @property
    def altKey(self):
        return self.impl.altKey()

    @property
    def metaKey(self):
        return self.impl.metaKey()

    @property
    def button(self):
        return self.impl.button()

    @property
    def buttons(self):
        return self.impl.buttons()

    @property
    def relatedTarget(self):
        return self.impl.relatedTarget()

    def getModifierState(self, keyArg):
        return self.impl.getModifierState_(keyArg)


class WheelEvent(MouseEvent):
    @property
    def deltaX(self):
        return self.impl.deltaX()

    @property
    def deltaY(self):
        return self.impl.deltaY()
    
    @property
    def deltaZ(self):
        return self.impl.deltaZ()

    @property
    def deltaMode(self):
        return self.impl.deltaMode()


class KeyboardEvent(UIEvent):
    @property
    def char(self):
        return self.impl.char()
    
    @property
    def key(self):
        return self.impl.key()

    @property
    def location(self):
        return self.impl.location()

    @property
    def ctrlKey(self):
        return self.impl.ctrlKey()
    
    @property
    def shiftKey(self):
        return self.impl.shiftKey()

    @property
    def altKey(self):
        return self.impl.altKey()
    
    @property
    def metaKey(self):
        return self.impl.metaKey()

    @property
    def repeat(self):
        return self.impl.repeat()
    
    @property
    def locale(self):
        return self.impl.locale()

    def getModifierState(self, keyArg):
        return self.impl.getModifierState_(keyArg)


class CompositionEvent(UIEvent):
    @property
    def data(self):
        return self.impl.data()

    @property
    def locale(self):
        return self.impl.locale()


class DOMFormData(object):
    implements(I.DOMFormData)
    
    _instances = WeakValueDictionary()
    
    def append(self, name, value, filename):
        return invoke_later_sync(self.impl.append___, [name.impl, value.impl, filename.impl])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMTokenList(object):
    implements(I.DOMTokenList)
    
    _instances = WeakValueDictionary()
    
    @property
    def length(self):
        return self.impl.length()
    
    def item(self, index):
        return DOMString(invoke_later_sync(self.impl.item_, [index]))
    
    def contains(self, token):
        return invoke_later_sync(self.impl.contains_, [token.impl])
    
    def add(self):
        return invoke_later_sync(self.impl.add, [])
    
    def remove(self):
        return invoke_later_sync(self.impl.remove, [])
    
    def toggle(self, token, force):
        return invoke_later_sync(self.impl.toggle__, [token.impl, force])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMSettableTokenList(DOMTokenList):
    implements(I.DOMSettableTokenList)
    
    @property
    def value(self):
        return self.impl.value()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class DOMURL(object):
    implements(I.DOMURL)
    
    _instances = WeakValueDictionary()
    
    def createObjectURL(self, blob):
        return DOMString(invoke_later_sync(self.impl.createObjectURL_, [blob.impl]))
    
    def revokeObjectURL(self, url):
        return invoke_later_sync(self.impl.revokeObjectURL_, [url.impl])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class HTMLAllCollection(object):
    implements(I.HTMLAllCollection)
    
    _instances = WeakValueDictionary()
    
    @property
    def length(self):
        return self.impl.length()
    
    def item(self, index):
        return Node(invoke_later_sync(self.impl.item_, [index]))
    
    def namedItem(self, name):
        return Node(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def tags(self, name):
        return NodeList(invoke_later_sync(self.impl.tags_, [name.impl]))
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        if impl is None:
            return None
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class HTMLElement(Element):
    implements(I.HTMLElement)
    
    @property
    def id(self):
        return self.impl.id()
    
    @property
    def title(self):
        return self.impl.title()
    
    @property
    def lang(self):
        return self.impl.lang()
    
    @property
    def translate(self):
        return self.impl.translate()
    
    @property
    def dir(self):
        return self.impl.dir()
    
    @property
    def tabIndex(self):
        return self.impl.tabIndex()
    
    @property
    def draggable(self):
        return self.impl.draggable()
    
    @property
    def webkitdropzone(self):
        return self.impl.webkitdropzone()
    
    @property
    def hidden(self):
        return self.impl.hidden()
    
    @property
    def accessKey(self):
        return self.impl.accessKey()
    
    @property
    def innerHTML(self):
        return self.impl.innerHTML()
    
    @property
    def innerText(self):
        return self.impl.innerText()
    
    @property
    def outerHTML(self):
        return self.impl.outerHTML()
    
    @property
    def outerText(self):
        return self.impl.outerText()
    
    def insertAdjacentElement(self, where, element):
        return Element(invoke_later_sync(self.impl.insertAdjacentElement__, [where.impl, element.impl]))
    
    def insertAdjacentHTML(self, where, html):
        return invoke_later_sync(self.impl.insertAdjacentHTML__, [where.impl, html.impl])
    
    def insertAdjacentText(self, where, text):
        return invoke_later_sync(self.impl.insertAdjacentText__, [where.impl, text.impl])
    
    @property
    def children(self):
        return self.impl.children()
    
    @property
    def contentEditable(self):
        return self.impl.contentEditable()
    
    @property
    def isContentEditable(self):
        return self.impl.isContentEditable()
    
    @property
    def spellcheck(self):
        return self.impl.spellcheck()
    
    @property
    def itemScope(self):
        return self.impl.itemScope()
    
    @property
    def itemType(self):
        return self.impl.itemType()
    
    @property
    def itemId(self):
        return self.impl.itemId()
    
    @property
    def itemRef(self):
        return self.impl.itemRef()
    
    @property
    def itemProp(self):
        return self.impl.itemProp()
    
    @property
    def itemValue(self):
        return self.impl.itemValue()
    
    def click(self):
        return invoke_later_sync(self.impl.click, [])
    
    def __init__(self, impl):
        self.impl = impl


class HTMLAnchorElement(HTMLElement):
    implements(I.HTMLAnchorElement)
    
    @property
    def charset(self):
        return self.impl.charset()
    
    @property
    def coords(self):
        return self.impl.coords()
    
    @property
    def download(self):
        return self.impl.download()
    
    @property
    def href(self):
        return self.impl.href()
    
    @property
    def hreflang(self):
        return self.impl.hreflang()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def ping(self):
        return self.impl.ping()
    
    @property
    def rel(self):
        return self.impl.rel()
    
    @property
    def rev(self):
        return self.impl.rev()
    
    @property
    def shape(self):
        return self.impl.shape()
    
    @property
    def target(self):
        return self.impl.target()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def hash(self):
        return self.impl.hash()
    
    @property
    def host(self):
        return self.impl.host()
    
    @property
    def hostname(self):
        return self.impl.hostname()
    
    @property
    def pathname(self):
        return self.impl.pathname()
    
    @property
    def port(self):
        return self.impl.port()
    
    @property
    def protocol(self):
        return self.impl.protocol()
    
    @property
    def search(self):
        return self.impl.search()
    
    @property
    def origin(self):
        return self.impl.origin()
    
    @property
    def text(self):
        return self.impl.text()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLAppletElement(HTMLElement):
    implements(I.HTMLAppletElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def alt(self):
        return self.impl.alt()
    
    @property
    def archive(self):
        return self.impl.archive()
    
    @property
    def code(self):
        return self.impl.code()
    
    @property
    def codeBase(self):
        return self.impl.codeBase()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def hspace(self):
        return self.impl.hspace()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def object(self):
        return self.impl.object()
    
    @property
    def vspace(self):
        return self.impl.vspace()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLAreaElement(HTMLElement):
    implements(I.HTMLAreaElement)
    
    @property
    def alt(self):
        return self.impl.alt()
    
    @property
    def coords(self):
        return self.impl.coords()
    
    @property
    def href(self):
        return self.impl.href()
    
    @property
    def noHref(self):
        return self.impl.noHref()
    
    @property
    def ping(self):
        return self.impl.ping()
    
    @property
    def shape(self):
        return self.impl.shape()
    
    @property
    def target(self):
        return self.impl.target()
    
    @property
    def hash(self):
        return self.impl.hash()
    
    @property
    def host(self):
        return self.impl.host()
    
    @property
    def hostname(self):
        return self.impl.hostname()
    
    @property
    def pathname(self):
        return self.impl.pathname()
    
    @property
    def port(self):
        return self.impl.port()
    
    @property
    def protocol(self):
        return self.impl.protocol()
    
    @property
    def search(self):
        return self.impl.search()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLBRElement(HTMLElement):
    implements(I.HTMLBRElement)
    
    @property
    def clear(self):
        return self.impl.clear()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLBaseElement(HTMLElement):
    implements(I.HTMLBaseElement)
    
    @property
    def href(self):
        return self.impl.href()
    
    @property
    def target(self):
        return self.impl.target()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLBaseFontElement(HTMLElement):
    implements(I.HTMLBaseFontElement)
    
    @property
    def color(self):
        return self.impl.color()
    
    @property
    def face(self):
        return self.impl.face()
    
    @property
    def size(self):
        return self.impl.size()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLBodyElement(HTMLElement):
    implements(I.HTMLBodyElement)
    
    @property
    def aLink(self):
        return self.impl.aLink()
    
    @property
    def background(self):
        return self.impl.background()
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def link(self):
        return self.impl.link()
    
    @property
    def text(self):
        return self.impl.text()
    
    @property
    def vLink(self):
        return self.impl.vLink()
    
    @property
    def onbeforeunload(self):
        return self.impl.onbeforeunload()
    
    @property
    def onhashchange(self):
        return self.impl.onhashchange()
    
    @property
    def onmessage(self):
        return self.impl.onmessage()
    
    @property
    def onoffline(self):
        return self.impl.onoffline()
    
    @property
    def ononline(self):
        return self.impl.ononline()
    
    @property
    def onpopstate(self):
        return self.impl.onpopstate()
    
    @property
    def onresize(self):
        return self.impl.onresize()
    
    @property
    def onstorage(self):
        return self.impl.onstorage()
    
    @property
    def onunload(self):
        return self.impl.onunload()
    
    @property
    def onorientationchange(self):
        return self.impl.onorientationchange()
    
    @property
    def onblur(self):
        return self.impl.onblur()
    
    @property
    def onerror(self):
        return self.impl.onerror()
    
    @property
    def onfocus(self):
        return self.impl.onfocus()
    
    @property
    def onload(self):
        return self.impl.onload()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLButtonElement(HTMLElement):
    implements(I.HTMLButtonElement)
    
    @property
    def autofocus(self):
        return self.impl.autofocus()
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def formAction(self):
        return self.impl.formAction()
    
    @property
    def formEnctype(self):
        return self.impl.formEnctype()
    
    @property
    def formMethod(self):
        return self.impl.formMethod()
    
    @property
    def formNoValidate(self):
        return self.impl.formNoValidate()
    
    @property
    def formTarget(self):
        return self.impl.formTarget()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLCanvasElement(HTMLElement):
    implements(I.HTMLCanvasElement)
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def height(self):
        return self.impl.height()
    
    def toDataURL(self, type):
        return DOMString(invoke_later_sync(self.impl.toDataURL_, [type.impl]))
    
    def getContext(self, contextId):
        return DOMObject(invoke_later_sync(self.impl.getContext_, [contextId.impl]))
    
    def __init__(self, impl):
        self.impl = impl


class HTMLCollection(object):
    implements(I.HTMLCollection)
    
    _instances = WeakValueDictionary()
    
    @property
    def length(self):
        return self.impl.length()
    
    def item(self, index):
        return Node(invoke_later_sync(self.impl.item_, [index]))
    
    def namedItem(self, name):
        return Node(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def __init__(self, impl):
        self.impl = impl


class HTMLDListElement(HTMLElement):
    implements(I.HTMLDListElement)
    
    @property
    def compact(self):
        return self.impl.compact()
    
    def __init__(self, impl):
        self.impl = impl


class HTMLDataListElement(HTMLElement):
    implements(I.HTMLDataListElement)
    
    @property
    def options(self):
        return self.impl.options()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLDetailsElement(HTMLElement):
    implements(I.HTMLDetailsElement)
    
    @property
    def open(self):
        return self.impl.open()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLDialogElement(HTMLElement):
    implements(I.HTMLDialogElement)
    
    @property
    def open(self):
        return self.impl.open()
    
    def close(self):
        return invoke_later_sync(self.impl.close, [])
    
    def show(self):
        return invoke_later_sync(self.impl.show, [])
    
    def showModal(self):
        return invoke_later_sync(self.impl.showModal, [])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLDirectoryElement(HTMLElement):
    implements(I.HTMLDirectoryElement)
    
    @property
    def compact(self):
        return self.impl.compact()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLDivElement(HTMLElement):
    implements(I.HTMLDivElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLDocument(Document):
    implements(I.HTMLDocument)
    
    def open(self):
        return invoke_later_sync(self.impl.open, [])
    
    def close(self):
        return invoke_later_sync(self.impl.close, [])
    
    def write(self, text):
        return invoke_later_sync(self.impl.write_, [text.impl])
    
    def writeln(self, text):
        return invoke_later_sync(self.impl.writeln_, [text.impl])
    
    @property
    def embeds(self):
        return self.impl.embeds()
    
    @property
    def plugins(self):
        return self.impl.plugins()
    
    @property
    def scripts(self):
        return self.impl.scripts()
    
    def clear(self):
        return invoke_later_sync(self.impl.clear, [])
    
    def captureEvents(self):
        return invoke_later_sync(self.impl.captureEvents, [])
    
    def releaseEvents(self):
        return invoke_later_sync(self.impl.releaseEvents, [])
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def dir(self):
        return self.impl.dir()
    
    @property
    def designMode(self):
        return self.impl.designMode()
    
    @property
    def compatMode(self):
        return self.impl.compatMode()
    
    @property
    def activeElement(self):
        return self.impl.activeElement()
    
    def hasFocus(self):
        return invoke_later_sync(self.impl.hasFocus, [])
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def fgColor(self):
        return self.impl.fgColor()
    
    @property
    def alinkColor(self):
        return self.impl.alinkColor()
    
    @property
    def linkColor(self):
        return self.impl.linkColor()
    
    @property
    def vlinkColor(self):
        return self.impl.vlinkColor()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLEmbedElement(HTMLElement):
    implements(I.HTMLEmbedElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFieldSetElement(HTMLElement):
    implements(I.HTMLFieldSetElement)
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def elements(self):
        return self.impl.elements()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFontElement(HTMLElement):
    implements(I.HTMLFontElement)
    
    @property
    def color(self):
        return self.impl.color()
    
    @property
    def face(self):
        return self.impl.face()
    
    @property
    def size(self):
        return self.impl.size()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFormControlsCollection(HTMLCollection):
    implements(I.HTMLFormControlsCollection)
    
    def namedItem(self, name):
        return Node(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFormElement(HTMLElement):
    implements(I.HTMLFormElement)
    
    @property
    def acceptCharset(self):
        return self.impl.acceptCharset()
    
    @property
    def action(self):
        return self.impl.action()
    
    @property
    def autocomplete(self):
        return self.impl.autocomplete()
    
    @property
    def enctype(self):
        return self.impl.enctype()
    
    @property
    def encoding(self):
        return self.impl.encoding()
    
    @property
    def method(self):
        return self.impl.method()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def noValidate(self):
        return self.impl.noValidate()
    
    @property
    def target(self):
        return self.impl.target()
    
    @property
    def elements(self):
        return self.impl.elements()
    
    @property
    def length(self):
        return self.impl.length()
    
    def submit(self):
        return invoke_later_sync(self.impl.submit, [])
    
    def reset(self):
        return invoke_later_sync(self.impl.reset, [])
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFrameElement(HTMLElement):
    implements(I.HTMLFrameElement)
    
    @property
    def frameBorder(self):
        return self.impl.frameBorder()
    
    @property
    def longDesc(self):
        return self.impl.longDesc()
    
    @property
    def marginHeight(self):
        return self.impl.marginHeight()
    
    @property
    def marginWidth(self):
        return self.impl.marginWidth()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def noResize(self):
        return self.impl.noResize()
    
    @property
    def scrolling(self):
        return self.impl.scrolling()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def contentDocument(self):
        return self.impl.contentDocument()
    
    @property
    def contentWindow(self):
        return self.impl.contentWindow()
    
    @property
    def location(self):
        return self.impl.location()
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def height(self):
        return self.impl.height()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLFrameSetElement(HTMLElement):
    implements(I.HTMLFrameSetElement)
    
    @property
    def cols(self):
        return self.impl.cols()
    
    @property
    def rows(self):
        return self.impl.rows()
    
    @property
    def onbeforeunload(self):
        return self.impl.onbeforeunload()
    
    @property
    def onhashchange(self):
        return self.impl.onhashchange()
    
    @property
    def onmessage(self):
        return self.impl.onmessage()
    
    @property
    def onoffline(self):
        return self.impl.onoffline()
    
    @property
    def ononline(self):
        return self.impl.ononline()
    
    @property
    def onpopstate(self):
        return self.impl.onpopstate()
    
    @property
    def onresize(self):
        return self.impl.onresize()
    
    @property
    def onstorage(self):
        return self.impl.onstorage()
    
    @property
    def onunload(self):
        return self.impl.onunload()
    
    @property
    def onorientationchange(self):
        return self.impl.onorientationchange()
    
    @property
    def onblur(self):
        return self.impl.onblur()
    
    @property
    def onerror(self):
        return self.impl.onerror()
    
    @property
    def onfocus(self):
        return self.impl.onfocus()
    
    @property
    def onload(self):
        return self.impl.onload()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLHRElement(HTMLElement):
    implements(I.HTMLHRElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def noShade(self):
        return self.impl.noShade()
    
    @property
    def size(self):
        return self.impl.size()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLHeadElement(HTMLElement):
    implements(I.HTMLHeadElement)
    
    @property
    def profile(self):
        return self.impl.profile()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLHeadingElement(HTMLElement):
    implements(I.HTMLHeadingElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLHtmlElement(HTMLElement):
    implements(I.HTMLHtmlElement)
    
    @property
    def version(self):
        return self.impl.version()
    
    @property
    def manifest(self):
        return self.impl.manifest()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLIFrameElement(HTMLElement):
    implements(I.HTMLIFrameElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def frameBorder(self):
        return self.impl.frameBorder()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def longDesc(self):
        return self.impl.longDesc()
    
    @property
    def marginHeight(self):
        return self.impl.marginHeight()
    
    @property
    def marginWidth(self):
        return self.impl.marginWidth()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def sandbox(self):
        return self.impl.sandbox()
    
    @property
    def seamless(self):
        return self.impl.seamless()
    
    @property
    def scrolling(self):
        return self.impl.scrolling()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def srcdoc(self):
        return self.impl.srcdoc()
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def contentDocument(self):
        return self.impl.contentDocument()
    
    @property
    def contentWindow(self):
        return self.impl.contentWindow()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLImageElement(HTMLElement):
    implements(I.HTMLImageElement)
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def alt(self):
        return self.impl.alt()
    
    @property
    def border(self):
        return self.impl.border()
    
    @property
    def crossOrigin(self):
        return self.impl.crossOrigin()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def hspace(self):
        return self.impl.hspace()
    
    @property
    def isMap(self):
        return self.impl.isMap()
    
    @property
    def longDesc(self):
        return self.impl.longDesc()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def useMap(self):
        return self.impl.useMap()
    
    @property
    def vspace(self):
        return self.impl.vspace()
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def complete(self):
        return self.impl.complete()
    
    @property
    def lowsrc(self):
        return self.impl.lowsrc()
    
    @property
    def naturalHeight(self):
        return self.impl.naturalHeight()
    
    @property
    def naturalWidth(self):
        return self.impl.naturalWidth()
    
    @property
    def x(self):
        return self.impl.x()
    
    @property
    def y(self):
        return self.impl.y()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLInputElement(HTMLElement):
    implements(I.HTMLInputElement)
    
    @property
    def accept(self):
        return self.impl.accept()
    
    @property
    def alt(self):
        return self.impl.alt()
    
    @property
    def autocomplete(self):
        return self.impl.autocomplete()
    
    @property
    def autofocus(self):
        return self.impl.autofocus()
    
    @property
    def defaultChecked(self):
        return self.impl.defaultChecked()
    
    @property
    def checked(self):
        return self.impl.checked()
    
    @property
    def dirName(self):
        return self.impl.dirName()
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def files(self):
        return self.impl.files()
    
    @property
    def formAction(self):
        return self.impl.formAction()
    
    @property
    def formEnctype(self):
        return self.impl.formEnctype()
    
    @property
    def formMethod(self):
        return self.impl.formMethod()
    
    @property
    def formNoValidate(self):
        return self.impl.formNoValidate()
    
    @property
    def formTarget(self):
        return self.impl.formTarget()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def indeterminate(self):
        return self.impl.indeterminate()
    
    @property
    def list(self):
        return self.impl.list()
    
    @property
    def max(self):
        return self.impl.max()
    
    @property
    def maxLength(self):
        return self.impl.maxLength()
    
    @property
    def min(self):
        return self.impl.min()
    
    @property
    def multiple(self):
        return self.impl.multiple()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def pattern(self):
        return self.impl.pattern()
    
    @property
    def placeholder(self):
        return self.impl.placeholder()
    
    @property
    def readOnly(self):
        return self.impl.readOnly()
    
    @property
    def required(self):
        return self.impl.required()
    
    @property
    def size(self):
        return self.impl.size()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def step(self):
        return self.impl.step()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def defaultValue(self):
        return self.impl.defaultValue()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def valueAsDate(self):
        return self.impl.valueAsDate()
    
    @property
    def valueAsNumber(self):
        return self.impl.valueAsNumber()
    
    def stepUp(self, n):
        return invoke_later_sync(self.impl.stepUp_, [n])
    
    def stepDown(self, n):
        return invoke_later_sync(self.impl.stepDown_, [n])
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def select(self):
        return invoke_later_sync(self.impl.select, [])
    
    @property
    def selectionStart(self):
        return self.impl.selectionStart()
    
    @property
    def selectionEnd(self):
        return self.impl.selectionEnd()
    
    @property
    def selectionDirection(self):
        return self.impl.selectionDirection()
    
    def setRangeText(self, replacement):
        return invoke_later_sync(self.impl.setRangeText_, [replacement.impl])
    
    def setRangeText(self, replacement, start, end, selectionMode):
        return invoke_later_sync(self.impl.setRangeText____, [replacement.impl, start, end, selectionMode.impl])
    
    def setSelectionRange(self, start, end, direction):
        return invoke_later_sync(self.impl.setSelectionRange___, [start, end, direction.impl])
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def webkitdirectory(self):
        return self.impl.webkitdirectory()
    
    @property
    def useMap(self):
        return self.impl.useMap()
    
    @property
    def incremental(self):
        return self.impl.incremental()
    
    @property
    def webkitSpeech(self):
        return self.impl.webkitSpeech()
    
    @property
    def webkitGrammar(self):
        return self.impl.webkitGrammar()
    
    @property
    def onwebkitspeechchange(self):
        return self.impl.onwebkitspeechchange()
    
    def setValueForUser(self, value):
        return invoke_later_sync(self.impl.setValueForUser_, [value.impl])
    
    @property
    def capture(self):
        return self.impl.capture()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLIntentElement(HTMLElement):
    implements(I.HTMLIntentElement)
    
    @property
    def action(self):
        return self.impl.action()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def href(self):
        return self.impl.href()
    
    @property
    def title(self):
        return self.impl.title()
    
    @property
    def disposition(self):
        return self.impl.disposition()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLKeygenElement(HTMLElement):
    implements(I.HTMLKeygenElement)
    
    @property
    def autofocus(self):
        return self.impl.autofocus()
    
    @property
    def challenge(self):
        return self.impl.challenge()
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def keytype(self):
        return self.impl.keytype()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLLIElement(HTMLElement):
    implements(I.HTMLLIElement)
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def value(self):
        return self.impl.value()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLLabelElement(HTMLElement):
    implements(I.HTMLLabelElement)
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def htmlFor(self):
        return self.impl.htmlFor()
    
    @property
    def control(self):
        return self.impl.control()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLLegendElement(HTMLElement):
    implements(I.HTMLLegendElement)
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def align(self):
        return self.impl.align()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLLinkElement(HTMLElement):
    implements(I.HTMLLinkElement)
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def charset(self):
        return self.impl.charset()
    
    @property
    def href(self):
        return self.impl.href()
    
    @property
    def hreflang(self):
        return self.impl.hreflang()
    
    @property
    def media(self):
        return self.impl.media()
    
    @property
    def rel(self):
        return self.impl.rel()
    
    @property
    def rev(self):
        return self.impl.rev()
    
    @property
    def target(self):
        return self.impl.target()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def sheet(self):
        return self.impl.sheet()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMapElement(HTMLElement):
    implements(I.HTMLMapElement)
    
    @property
    def areas(self):
        return self.impl.areas()
    
    @property
    def name(self):
        return self.impl.name()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMarqueeElement(HTMLElement):
    implements(I.HTMLMarqueeElement)
    
    def start(self):
        return invoke_later_sync(self.impl.start, [])
    
    def stop(self):
        return invoke_later_sync(self.impl.stop, [])
    
    @property
    def behavior(self):
        return self.impl.behavior()
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def direction(self):
        return self.impl.direction()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def hspace(self):
        return self.impl.hspace()
    
    @property
    def loop(self):
        return self.impl.loop()
    
    @property
    def scrollAmount(self):
        return self.impl.scrollAmount()
    
    @property
    def scrollDelay(self):
        return self.impl.scrollDelay()
    
    @property
    def trueSpeed(self):
        return self.impl.trueSpeed()
    
    @property
    def vspace(self):
        return self.impl.vspace()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMediaElement(HTMLElement):
    implements(I.HTMLMediaElement)
    
    @property
    def error(self):
        return self.impl.error()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def currentSrc(self):
        return self.impl.currentSrc()
    
    NETWORK_EMPTY = 0
    
    NETWORK_IDLE = 1
    
    NETWORK_LOADING = 2
    
    NETWORK_NO_SOURCE = 3
    
    @property
    def networkState(self):
        return self.impl.networkState()
    
    @property
    def preload(self):
        return self.impl.preload()
    
    @property
    def buffered(self):
        return self.impl.buffered()
    
    def load(self):
        return invoke_later_sync(self.impl.load, [])
    
    def canPlayType(self, type):
        return DOMString(invoke_later_sync(self.impl.canPlayType_, [type.impl]))
    
    HAVE_NOTHING = 0
    
    HAVE_METADATA = 1
    
    HAVE_CURRENT_DATA = 2
    
    HAVE_FUTURE_DATA = 3
    
    HAVE_ENOUGH_DATA = 4
    
    @property
    def readyState(self):
        return self.impl.readyState()
    
    @property
    def seeking(self):
        return self.impl.seeking()
    
    @property
    def currentTime(self):
        return self.impl.currentTime()
    
    @property
    def initialTime(self):
        return self.impl.initialTime()
    
    @property
    def startTime(self):
        return self.impl.startTime()
    
    @property
    def duration(self):
        return self.impl.duration()
    
    @property
    def paused(self):
        return self.impl.paused()
    
    @property
    def defaultPlaybackRate(self):
        return self.impl.defaultPlaybackRate()
    
    @property
    def playbackRate(self):
        return self.impl.playbackRate()
    
    @property
    def played(self):
        return self.impl.played()
    
    @property
    def seekable(self):
        return self.impl.seekable()
    
    @property
    def ended(self):
        return self.impl.ended()
    
    @property
    def autoplay(self):
        return self.impl.autoplay()
    
    @property
    def loop(self):
        return self.impl.loop()
    
    def play(self):
        return invoke_later_sync(self.impl.play, [])
    
    def pause(self):
        return invoke_later_sync(self.impl.pause, [])
    
    @property
    def controls(self):
        return self.impl.controls()
    
    @property
    def volume(self):
        return self.impl.volume()
    
    @property
    def muted(self):
        return self.impl.muted()
    
    @property
    def defaultMuted(self):
        return self.impl.defaultMuted()
    
    @property
    def webkitPreservesPitch(self):
        return self.impl.webkitPreservesPitch()
    
    @property
    def webkitHasClosedCaptions(self):
        return self.impl.webkitHasClosedCaptions()
    
    @property
    def webkitClosedCaptionsVisible(self):
        return self.impl.webkitClosedCaptionsVisible()
    
    @property
    def webkitAudioDecodedByteCount(self):
        return self.impl.webkitAudioDecodedByteCount()
    
    @property
    def webkitVideoDecodedByteCount(self):
        return self.impl.webkitVideoDecodedByteCount()
    
    @property
    def mediaGroup(self):
        return self.impl.mediaGroup()
    
    @property
    def controller(self):
        return self.impl.controller()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMenuElement(HTMLElement):
    implements(I.HTMLMenuElement)
    
    @property
    def compact(self):
        return self.impl.compact()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMetaElement(HTMLElement):
    implements(I.HTMLMetaElement)
    
    @property
    def content(self):
        return self.impl.content()
    
    @property
    def httpEquiv(self):
        return self.impl.httpEquiv()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def scheme(self):
        return self.impl.scheme()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLMeterElement(HTMLElement):
    implements(I.HTMLMeterElement)
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def min(self):
        return self.impl.min()
    
    @property
    def max(self):
        return self.impl.max()
    
    @property
    def low(self):
        return self.impl.low()
    
    @property
    def high(self):
        return self.impl.high()
    
    @property
    def optimum(self):
        return self.impl.optimum()
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLModElement(HTMLElement):
    implements(I.HTMLModElement)
    
    @property
    def cite(self):
        return self.impl.cite()
    
    @property
    def dateTime(self):
        return self.impl.dateTime()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLOListElement(HTMLElement):
    implements(I.HTMLOListElement)
    
    @property
    def compact(self):
        return self.impl.compact()
    
    @property
    def start(self):
        return self.impl.start()
    
    @property
    def reversed(self):
        return self.impl.reversed()
    
    @property
    def type(self):
        return self.impl.type()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLObjectElement(HTMLElement):
    implements(I.HTMLObjectElement)
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def code(self):
        return self.impl.code()
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def archive(self):
        return self.impl.archive()
    
    @property
    def border(self):
        return self.impl.border()
    
    @property
    def codeBase(self):
        return self.impl.codeBase()
    
    @property
    def codeType(self):
        return self.impl.codeType()
    
    @property
    def data(self):
        return self.impl.data()
    
    @property
    def declare(self):
        return self.impl.declare()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def hspace(self):
        return self.impl.hspace()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def standby(self):
        return self.impl.standby()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def useMap(self):
        return self.impl.useMap()
    
    @property
    def vspace(self):
        return self.impl.vspace()
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def contentDocument(self):
        return self.impl.contentDocument()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLOptGroupElement(HTMLElement):
    implements(I.HTMLOptGroupElement)
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def label(self):
        return self.impl.label()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLOptionElement(HTMLElement):
    implements(I.HTMLOptionElement)
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def label(self):
        return self.impl.label()
    
    @property
    def defaultSelected(self):
        return self.impl.defaultSelected()
    
    @property
    def selected(self):
        return self.impl.selected()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def text(self):
        return self.impl.text()
    
    @property
    def index(self):
        return self.impl.index()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLOptionsCollection(HTMLCollection):
    implements(I.HTMLOptionsCollection)
    
    @property
    def selectedIndex(self):
        return self.impl.selectedIndex()
    
    @property
    def length(self):
        return self.impl.length()
    
    def namedItem(self, name):
        return Node(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def add(self, option, index):
        return invoke_later_sync(self.impl.add__, [option.impl, index])
    
    def remove(self, index):
        return invoke_later_sync(self.impl.remove_, [index])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLOutputElement(HTMLElement):
    implements(I.HTMLOutputElement)
    
    @property
    def htmlFor(self):
        return self.impl.htmlFor()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def defaultValue(self):
        return self.impl.defaultValue()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLParagraphElement(HTMLElement):
    implements(I.HTMLParagraphElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLParamElement(HTMLElement):
    implements(I.HTMLParamElement)
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def valueType(self):
        return self.impl.valueType()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLPreElement(HTMLElement):
    implements(I.HTMLPreElement)
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def wrap(self):
        return self.impl.wrap()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLProgressElement(HTMLElement):
    implements(I.HTMLProgressElement)
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def max(self):
        return self.impl.max()
    
    @property
    def position(self):
        return self.impl.position()
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLPropertiesCollection(HTMLCollection):
    implements(I.HTMLPropertiesCollection)
    
    @property
    def length(self):
        return self.impl.length()
    
    def item(self, index):
        return Node(invoke_later_sync(self.impl.item_, [index]))
    
    @property
    def names(self):
        return self.impl.names()
    
    def namedItem(self, name):
        return PropertyNodeList(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLQuoteElement(HTMLElement):
    implements(I.HTMLQuoteElement)
    
    @property
    def cite(self):
        return self.impl.cite()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLScriptElement(HTMLElement):
    implements(I.HTMLScriptElement)
    
    @property
    def text(self):
        return self.impl.text()
    
    @property
    def htmlFor(self):
        return self.impl.htmlFor()
    
    @property
    def event(self):
        return self.impl.event()
    
    @property
    def charset(self):
        return self.impl.charset()
    
    @property
    def async(self):
        return self.impl.async()
    
    @property
    def defer(self):
        return self.impl.defer()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def crossOrigin(self):
        return self.impl.crossOrigin()
    
    @property
    def nonce(self):
        return self.impl.nonce()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLSelectElement(HTMLElement):
    implements(I.HTMLSelectElement)
    
    @property
    def autofocus(self):
        return self.impl.autofocus()
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def multiple(self):
        return self.impl.multiple()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def required(self):
        return self.impl.required()
    
    @property
    def size(self):
        return self.impl.size()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def options(self):
        return self.impl.options()
    
    @property
    def length(self):
        return self.impl.length()
    
    def item(self, index):
        return Node(invoke_later_sync(self.impl.item_, [index]))
    
    def namedItem(self, name):
        return Node(invoke_later_sync(self.impl.namedItem_, [name.impl]))
    
    def add(self, element, before):
        return invoke_later_sync(self.impl.add__, [element.impl, before.impl])
    
    def remove(self, index):
        return invoke_later_sync(self.impl.remove_, [index])
    
    @property
    def selectedOptions(self):
        return self.impl.selectedOptions()
    
    @property
    def selectedIndex(self):
        return self.impl.selectedIndex()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLSourceElement(HTMLElement):
    implements(I.HTMLSourceElement)
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def media(self):
        return self.impl.media()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLStyleElement(HTMLElement):
    implements(I.HTMLStyleElement)
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def scoped(self):
        return self.impl.scoped()
    
    @property
    def media(self):
        return self.impl.media()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def sheet(self):
        return self.impl.sheet()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableCaptionElement(HTMLElement):
    implements(I.HTMLTableCaptionElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableCellElement(HTMLElement):
    implements(I.HTMLTableCellElement)
    
    @property
    def cellIndex(self):
        return self.impl.cellIndex()
    
    @property
    def abbr(self):
        return self.impl.abbr()
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def axis(self):
        return self.impl.axis()
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def ch(self):
        return self.impl.ch()
    
    @property
    def chOff(self):
        return self.impl.chOff()
    
    @property
    def colSpan(self):
        return self.impl.colSpan()
    
    @property
    def headers(self):
        return self.impl.headers()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def noWrap(self):
        return self.impl.noWrap()
    
    @property
    def rowSpan(self):
        return self.impl.rowSpan()
    
    @property
    def scope(self):
        return self.impl.scope()
    
    @property
    def vAlign(self):
        return self.impl.vAlign()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableColElement(HTMLElement):
    implements(I.HTMLTableColElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def ch(self):
        return self.impl.ch()
    
    @property
    def chOff(self):
        return self.impl.chOff()
    
    @property
    def span(self):
        return self.impl.span()
    
    @property
    def vAlign(self):
        return self.impl.vAlign()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableElement(HTMLElement):
    implements(I.HTMLTableElement)
    
    @property
    def caption(self):
        return self.impl.caption()
    
    @property
    def tHead(self):
        return self.impl.tHead()
    
    @property
    def tFoot(self):
        return self.impl.tFoot()
    
    @property
    def rows(self):
        return self.impl.rows()
    
    @property
    def tBodies(self):
        return self.impl.tBodies()
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def border(self):
        return self.impl.border()
    
    @property
    def cellPadding(self):
        return self.impl.cellPadding()
    
    @property
    def cellSpacing(self):
        return self.impl.cellSpacing()
    
    @property
    def frame(self):
        return self.impl.frame()
    
    @property
    def rules(self):
        return self.impl.rules()
    
    @property
    def summary(self):
        return self.impl.summary()
    
    @property
    def width(self):
        return self.impl.width()
    
    def createTHead(self):
        return HTMLElement(invoke_later_sync(self.impl.createTHead, []))
    
    def deleteTHead(self):
        return invoke_later_sync(self.impl.deleteTHead, [])
    
    def createTFoot(self):
        return HTMLElement(invoke_later_sync(self.impl.createTFoot, []))
    
    def deleteTFoot(self):
        return invoke_later_sync(self.impl.deleteTFoot, [])
    
    def createTBody(self):
        return HTMLElement(invoke_later_sync(self.impl.createTBody, []))
    
    def createCaption(self):
        return HTMLElement(invoke_later_sync(self.impl.createCaption, []))
    
    def deleteCaption(self):
        return invoke_later_sync(self.impl.deleteCaption, [])
    
    def insertRow(self, index):
        return HTMLElement(invoke_later_sync(self.impl.insertRow_, [index]))
    
    def deleteRow(self, index):
        return invoke_later_sync(self.impl.deleteRow_, [index])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableRowElement(HTMLElement):
    implements(I.HTMLTableRowElement)
    
    @property
    def rowIndex(self):
        return self.impl.rowIndex()
    
    @property
    def sectionRowIndex(self):
        return self.impl.sectionRowIndex()
    
    @property
    def cells(self):
        return self.impl.cells()
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def bgColor(self):
        return self.impl.bgColor()
    
    @property
    def ch(self):
        return self.impl.ch()
    
    @property
    def chOff(self):
        return self.impl.chOff()
    
    @property
    def vAlign(self):
        return self.impl.vAlign()
    
    def insertCell(self, index):
        return HTMLElement(invoke_later_sync(self.impl.insertCell_, [index]))
    
    def deleteCell(self, index):
        return invoke_later_sync(self.impl.deleteCell_, [index])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTableSectionElement(HTMLElement):
    implements(I.HTMLTableSectionElement)
    
    @property
    def align(self):
        return self.impl.align()
    
    @property
    def ch(self):
        return self.impl.ch()
    
    @property
    def chOff(self):
        return self.impl.chOff()
    
    @property
    def vAlign(self):
        return self.impl.vAlign()
    
    @property
    def rows(self):
        return self.impl.rows()
    
    def insertRow(self, index):
        return HTMLElement(invoke_later_sync(self.impl.insertRow_, [index]))
    
    def deleteRow(self, index):
        return invoke_later_sync(self.impl.deleteRow_, [index])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTemplateElement(HTMLElement):
    implements(I.HTMLTemplateElement)
    
    @property
    def content(self):
        return self.impl.content()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTextAreaElement(HTMLElement):
    implements(I.HTMLTextAreaElement)
    
    @property
    def autofocus(self):
        return self.impl.autofocus()
    
    @property
    def cols(self):
        return self.impl.cols()
    
    @property
    def dirName(self):
        return self.impl.dirName()
    
    @property
    def disabled(self):
        return self.impl.disabled()
    
    @property
    def form(self):
        return self.impl.form()
    
    @property
    def maxLength(self):
        return self.impl.maxLength()
    
    @property
    def name(self):
        return self.impl.name()
    
    @property
    def placeholder(self):
        return self.impl.placeholder()
    
    @property
    def readOnly(self):
        return self.impl.readOnly()
    
    @property
    def required(self):
        return self.impl.required()
    
    @property
    def rows(self):
        return self.impl.rows()
    
    @property
    def wrap(self):
        return self.impl.wrap()
    
    @property
    def type(self):
        return self.impl.type()
    
    @property
    def defaultValue(self):
        return self.impl.defaultValue()
    
    @property
    def value(self):
        return self.impl.value()
    
    @property
    def textLength(self):
        return self.impl.textLength()
    
    @property
    def willValidate(self):
        return self.impl.willValidate()
    
    @property
    def validity(self):
        return self.impl.validity()
    
    @property
    def validationMessage(self):
        return self.impl.validationMessage()
    
    def checkValidity(self):
        return invoke_later_sync(self.impl.checkValidity, [])
    
    def setCustomValidity(self, error):
        return invoke_later_sync(self.impl.setCustomValidity_, [error.impl])
    
    @property
    def labels(self):
        return self.impl.labels()
    
    def select(self):
        return invoke_later_sync(self.impl.select, [])
    
    @property
    def selectionStart(self):
        return self.impl.selectionStart()
    
    @property
    def selectionEnd(self):
        return self.impl.selectionEnd()
    
    @property
    def selectionDirection(self):
        return self.impl.selectionDirection()
    
    def setRangeText(self, replacement):
        return invoke_later_sync(self.impl.setRangeText_, [replacement.impl])
    
    def setRangeText(self, replacement, start, end, selectionMode):
        return invoke_later_sync(self.impl.setRangeText____, [replacement.impl, start, end, selectionMode.impl])
    
    def setSelectionRange(self, start, end, direction):
        return invoke_later_sync(self.impl.setSelectionRange___, [start, end, direction.impl])
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTitleElement(HTMLElement):
    implements(I.HTMLTitleElement)
    
    @property
    def text(self):
        return self.impl.text()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLTrackElement(HTMLElement):
    implements(I.HTMLTrackElement)
    
    @property
    def kind(self):
        return self.impl.kind()
    
    @property
    def src(self):
        return self.impl.src()
    
    @property
    def srclang(self):
        return self.impl.srclang()
    
    @property
    def label(self):
        return self.impl.label()
    
    @property
    def default(self):
        return self.impl.default()
    
    NONE = 0
    
    LOADING = 1
    
    LOADED = 2
    
    ERROR = 3
    
    @property
    def readyState(self):
        return self.impl.readyState()
    
    @property
    def track(self):
        return self.impl.track()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLUListElement(HTMLElement):
    implements(I.HTMLUListElement)
    
    @property
    def compact(self):
        return self.impl.compact()
    
    @property
    def type(self):
        return self.impl.type()
    
    def __init__(self, impl):
        self.impl = impl
    

class HTMLVideoElement(HTMLMediaElement):
    implements(I.HTMLVideoElement)
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def videoWidth(self):
        return self.impl.videoWidth()
    
    @property
    def videoHeight(self):
        return self.impl.videoHeight()
    
    @property
    def poster(self):
        return self.impl.poster()
    
    @property
    def webkitSupportsFullscreen(self):
        return self.impl.webkitSupportsFullscreen()
    
    @property
    def webkitDisplayingFullscreen(self):
        return self.impl.webkitDisplayingFullscreen()
    
    def webkitEnterFullscreen(self):
        return invoke_later_sync(self.impl.webkitEnterFullscreen, [])
    
    def webkitExitFullscreen(self):
        return invoke_later_sync(self.impl.webkitExitFullscreen, [])
    
    def webkitEnterFullScreen(self):
        return invoke_later_sync(self.impl.webkitEnterFullScreen, [])
    
    def webkitExitFullScreen(self):
        return invoke_later_sync(self.impl.webkitExitFullScreen, [])
    
    @property
    def webkitDecodedFrameCount(self):
        return self.impl.webkitDecodedFrameCount()
    
    @property
    def webkitDroppedFrameCount(self):
        return self.impl.webkitDroppedFrameCount()
    
    def __init__(self, impl):
        self.impl = impl
    

class ImageData(object):
    implements(I.ImageData)
    
    _instances = WeakValueDictionary()
    
    @property
    def width(self):
        return self.impl.width()
    
    @property
    def height(self):
        return self.impl.height()
    
    @property
    def data(self):
        return self.impl.data()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class MediaController(object):
    implements(I.MediaController)
    
    _instances = WeakValueDictionary()
    
    @property
    def buffered(self):
        return self.impl.buffered()
    
    @property
    def seekable(self):
        return self.impl.seekable()
    
    @property
    def duration(self):
        return self.impl.duration()
    
    @property
    def currentTime(self):
        return self.impl.currentTime()
    
    @property
    def paused(self):
        return self.impl.paused()
    
    @property
    def played(self):
        return self.impl.played()
    
    @property
    def playbackState(self):
        return self.impl.playbackState()
    
    def play(self):
        return invoke_later_sync(self.impl.play, [])
    
    def pause(self):
        return invoke_later_sync(self.impl.pause, [])
    
    def unpause(self):
        return invoke_later_sync(self.impl.unpause, [])
    
    @property
    def defaultPlaybackRate(self):
        return self.impl.defaultPlaybackRate()
    
    @property
    def playbackRate(self):
        return self.impl.playbackRate()
    
    @property
    def volume(self):
        return self.impl.volume()
    
    @property
    def muted(self):
        return self.impl.muted()
    
    def addEventListener(self, type, listener, useCapture):
        return invoke_later_sync(self.impl.addEventListener___, [type.impl, listener.impl, useCapture])
    
    def removeEventListener(self, type, listener, useCapture):
        return invoke_later_sync(self.impl.removeEventListener___, [type.impl, listener.impl, useCapture])
    
    def dispatchEvent(self, evt):
        return invoke_later_sync(self.impl.dispatchEvent_, [evt.impl])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class MediaError(object):
    implements(I.MediaError)
    
    _instances = WeakValueDictionary()
    
    MEDIA_ERR_ABORTED = 1
    
    MEDIA_ERR_NETWORK = 2
    
    MEDIA_ERR_DECODE = 3
    
    MEDIA_ERR_SRC_NOT_SUPPORTED = 4
    
    @property
    def code(self):
        return self.impl.code()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class MediaKeyError(object):
    implements(I.MediaKeyError)
    
    _instances = WeakValueDictionary()
    
    MEDIA_KEYERR_UNKNOWN = 1
    
    MEDIA_KEYERR_CLIENT = 2
    
    MEDIA_KEYERR_SERVICE = 3
    
    MEDIA_KEYERR_OUTPUT = 4
    
    MEDIA_KEYERR_HARDWARECHANGE = 5
    
    MEDIA_KEYERR_DOMAIN = 6
    
    @property
    def code(self):
        return self.impl.code()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class MediaKeyEvent(Event):
    implements(I.MediaKeyEvent)
    
    @property
    def keySystem(self):
        return self.impl.keySystem()
    
    @property
    def sessionId(self):
        return self.impl.sessionId()
    
    @property
    def initData(self):
        return self.impl.initData()
    
    @property
    def message(self):
        return self.impl.message()
    
    @property
    def defaultURL(self):
        return self.impl.defaultURL()
    
    @property
    def errorCode(self):
        return self.impl.errorCode()
    
    @property
    def systemCode(self):
        return self.impl.systemCode()
    
    def __init__(self, impl):
        self.impl = impl
    

class RadioNodeList(NodeList):
    implements(I.RadioNodeList)
    
    @property
    def value(self):
        return self.impl.value()
    
    def __init__(self, impl):
        self.impl = impl
    

class TextMetrics(object):
    implements(I.TextMetrics)
    
    _instances = WeakValueDictionary()
    
    @property
    def width(self):
        return self.impl.width()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class TimeRanges(object):
    implements(I.TimeRanges)
    
    _instances = WeakValueDictionary()
    
    @property
    def length(self):
        return self.impl.length()
    
    def start(self, index):
        return invoke_later_sync(self.impl.start_, [index])
    
    def end(self, index):
        return invoke_later_sync(self.impl.end_, [index])
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance


class ValidityState(object):
    implements(I.ValidityState)
    
    _instances = WeakValueDictionary()
    
    @property
    def valueMissing(self):
        return self.impl.valueMissing()
    
    @property
    def typeMismatch(self):
        return self.impl.typeMismatch()
    
    @property
    def patternMismatch(self):
        return self.impl.patternMismatch()
    
    @property
    def tooLong(self):
        return self.impl.tooLong()
    
    @property
    def rangeUnderflow(self):
        return self.impl.rangeUnderflow()
    
    @property
    def rangeOverflow(self):
        return self.impl.rangeOverflow()
    
    @property
    def stepMismatch(self):
        return self.impl.stepMismatch()
    
    @property
    def badInput(self):
        return self.impl.badInput()
    
    @property
    def customError(self):
        return self.impl.customError()
    
    @property
    def valid(self):
        return self.impl.valid()
    
    def __init__(self, impl):
        self.impl = impl
    
    def __new__(cls, impl):
        instance = cls._instances.get(impl)
        if instance is None:
            instance = cls._instances[impl] = object.__new__(cls)
        return instance

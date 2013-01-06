import ctypes

__all__ = (
    'ProcessSerialNumber',
    'TransformProcessType',
    'SetFrontProcess',
    'kProcessTransformToForegroundApplication',
    'kProcessTransformToBackgroundApplication',
    'kProcessTransformToUIElementAppication',
    'kNoProcess',
    'kSystemProcess',
    'kCurrentProcess',
    )

class ProcessSerialNumber(ctypes.Structure):
    _fields_ = [
        ('highLongOfPSN', ctypes.c_uint32),
        ('lowLongOfPSN', ctypes.c_uint32),
        ]

kNoProcess = 0
kSystemProcess = 1
kCurrentProcess = 2

kProcessTransformToForegroundApplication = 1
kProcessTransformToBackgroundApplication = 2
kProcessTransformToUIElementAppication = 4

_ = ctypes.CDLL('/System/Library/Frameworks/ApplicationServices.framework/ApplicationServices')
_.TransformProcessType.argtypes = [ctypes.POINTER(ProcessSerialNumber), ctypes.c_uint32]
_.SetFrontProcess.argtypes = [ctypes.POINTER(ProcessSerialNumber)]

for name in __all__:
    _locals = locals()
    f = getattr(_, name, None)
    if f is not None:
        _locals[name] = f

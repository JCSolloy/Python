from pysnmp.hlapi import *

iterator = nextCmd(
    SnmpEngine(),
    UsmUserData('admin', 'Administrator'),
    UdpTransportTarget(('10.232.3.39', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('system'))
)

clase = dir(iterator)
print(clase)
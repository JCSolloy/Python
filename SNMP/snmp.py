"""
from pysnmp.hlapi import *

iterator = nextCmd(
    SnmpEngine(),
    UsmUserData('usr-md5-none', 'authkey1'),
    UdpTransportTarget(('demo.snmplabs.com', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('IF-MIB'))
)

for errorIndication, errorStatus, errorIndex, varBinds in iterator:

    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
"""

from pysnmp.hlapi import *

iterator = nextCmd(
    SnmpEngine(),
    UsmUserData('admin', 'Administrator'),
    UdpTransportTarget(('10.232.3.39', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('IF-MIB'))
)

for errorIndication, errorStatus, errorIndex, varBinds in iterator:

    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


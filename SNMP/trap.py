from pysnmp.hlapi import *
g = sendNotification(SnmpEngine(),
                    CommunityData('public'),
                    UdpTransportTarget(('10.232.3.39', 162)),
                    ContextData(),
                    'trap',
                    NotificationType(ObjectIdentity('IF-MIB', 'linkDown')))

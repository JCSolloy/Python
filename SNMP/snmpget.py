from pysnmp.hlapi.asyncore import *

def cbFun(snmpEngine, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    print(errorIndication, errorStatus, errorIndex, varBinds)

snmpEngine = SnmpEngine()
getCmd(snmpEngine,
        UsmUserData('admin', 'Administrator'),
        UdpTransportTarget(('10.232.3.39', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')),
        cbFun=cbFun)

try:
    snmpEngine.transportDispatcher.runDispatcher()

except:
    print('Error de comunicación del Router')

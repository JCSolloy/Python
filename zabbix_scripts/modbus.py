from pyModbusTCP.client import ModbusClient
import sys 

def Modbus(IP, Puerto, Registro, Cantidad_de_registros, ID_Dispositivo):
    Regs = list()
    try:
        c = ModbusClient(host=IP,
                         port=Puerto,
                         unit_id=ID_Dispositivo,
                         debug=False,
                         auto_open=True,
                         auto_close=True)
        Regs = c.read_holding_registers(Registro, Cantidad_de_registros)
        Message = "Comunicación Modbus Correcta"
    except:
        Message = "Error de comunicación"
    return Regs, Message

IP = str(sys.argv[1])
Puerto = int(sys.argv[2])
Registro = int(sys.argv[3])
Cantidad_de_registros = int(sys.argv[4])
ID_Dispositivo = int(sys.argv[5])

print(IP,Puerto,Registro,Cantidad_de_registros,ID_Dispositivo)

#test = Modbus("10.232.2.170", 502, 4419,10,0)
test = Modbus(IP, Puerto, Registro, Cantidad_de_registros, ID_Dispositivo)
print(test)

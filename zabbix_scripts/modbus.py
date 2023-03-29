from pyModbusTCP.client import ModbusClient
import sys 

#funcion para realizar las interrogaciones modbus 
#para ejecutar el script se hace de la siguiente manera "python modbus.py "172.0.0.1" 502 4419 10 0" 
def Modbus(IP, Puerto, Registro, Cantidad_de_registros, ID_Dispositivo):
    Regs = list()
    try:
         connection = ModbusClient(host=IP, port=Puerto, unit_id=ID_Dispositivo, debug=False)
         Regs = connection.read_holding_registers(Registro, Cantidad_de_registros)
    except:
        prin("Error de interrogación")
    return Regs

if __name__ == '__main__':

    IP = str(sys.argv[1])
    Puerto = int(sys.argv[2])
    Registro = int(sys.argv[3])
    Cantidad_de_registros = int(sys.argv[4])
    ID_Dispositivo = int(sys.argv[5])

    test = Modbus(IP, Puerto, Registro, Cantidad_de_registros, ID_Dispositivo)

    if test == None:
        print("Error de comunicación Modbus 🛑🔴")
    else:
        print(f"""
            Comunicación Modbus OK✅🟢
            {test}
            """)

    print(f"""
            IP = {IP} 
            Puerto = {Puerto} 
            Registro = {Registro} 
            Cantidad de registros = {Cantidad_de_registros} 
            ID Dispositivo = {ID_Dispositivo}""")

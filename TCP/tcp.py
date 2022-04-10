from pymodbus.client.sync import ModbusTcpClient
"""
10.98.59.193
id = 1
puerto = 502
45001
"""
client = ModbusTcpClient('127.0.0.1')
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()



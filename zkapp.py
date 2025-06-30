from zk import ZK, const

zk = ZK('192.168.14.203', port=4370, timeout=5, password=123456, force_udp=False)
conn = zk.connect()
conn.disable_device()

users = conn.get_users()
print(users)
for user in users:
    print('Usuario:', user.name)

print("Conectado. Obteniendo logs de asistencia...")
attendance = conn.get_attendance()

print(attendance)

for record in attendance:
    print(f"ID: {record.user_id}, Fecha: {record.timestamp}, Tipo: {record.status}")

conn.enable_device()
conn.disconnect()

import socket

# Buat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))  # Hubungkan ke server

# Kirim pesan ke server
client_socket.sendall(b"Hello Arif Cahyo W_50421200 dari client TCP!")

# Terima balasan dari server
data = client_socket.recv(1024)
print("Balasan dari server:", data.decode())

client_socket.close()  # Tutup koneksi

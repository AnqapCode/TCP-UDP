import socket

# Buat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim pesan ke server
client_socket.sendto(
    b"Hello dari Arif Cahyo W_50421200 client UDP!", ("localhost", 54321)
)

# Terima balasan dari server
data, _ = client_socket.recvfrom(1024)
print("Balasan dari server:", data.decode())

client_socket.close()  # Tutup socket

import socket

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 54321))  # Bind ke port 54321

print("UDP Server menunggu pesan...")
while True:
    data, client_address = server_socket.recvfrom(1024)  # Terima data
    print("Pesan dari client:", data.decode())

    # Kirim balasan ke client
    server_socket.sendto(b"Pesan diterima oleh server UDP!", client_address)

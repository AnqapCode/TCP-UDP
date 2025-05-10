import socket

# Buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))  # Bind ke port 12345
server_socket.listen(1)  # Listen hingga 1 koneksi

print("TCP Server menunggu koneksi...")
connection, client_address = server_socket.accept()  # Terima koneksi

try:
    print("Terhubung dengan:", client_address)
    data = connection.recv(1024)  # Terima data dari client
    print("Pesan dari client:", data.decode())

    # Kirim balasan ke client
    connection.sendall(b"Pesan diterima oleh server TCP!")
finally:
    connection.close()  # Tutup koneksi

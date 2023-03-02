import socket

HOST = "190.166.14.96" # IP address of your Raspberry PI
PORT = 8081          # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(text.encode())     # send the encoded message (send in binary format)

        data = s.recv(1024)
        print("from server: ", data)
from shutil import move
from gpiozero import CPUTemperature
import picar_4wd
import socket
import binascii

HOST = "190.166.14.96" # IP address of your Raspberry PI
PORT = 8081          # Port to listen on (non-privileged ports are > 1023)

def remote_control(s):
    speed = 0
    if("w" in s):
        picar_4wd. forward(10)
        speed = 10
    elif ("s" in s):
        picar_4wd.backward(10)
        speed = -10
    elif("a" in s):
        picar_4wd. turn_left(10)
        speed = 0
    elif("d" in s):
        picar_4wd.turn_right(10)
        speed = 0
    else:
        picar_4wd.stop()
        speed = 0
    return speed

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                # print(data) 
                speed = 0
                temp = 0
                distance_ = 0
                data_ = []
                decode_ = data_.decode('ascii')
                speed = str(remote_control(decode_))
                distance_ = str(picar_4wd.get_distance_at(0))
                temp = str(CPUTemperature().temperature)
                data_.append(speed)
                data_.append(distance_)
                data_.append(temp)
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    
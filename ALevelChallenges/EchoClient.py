import socket

LOCAL_HOST = "127.0.0.1"
PORT = 9000

def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((LOCAL_HOST, PORT))
        s.sendall(b"Hello world")
        return s.recv(1024)

def main():
    a = send()
    print(f"Received data: {a!r}")

if __name__ == "__main__":
    main()
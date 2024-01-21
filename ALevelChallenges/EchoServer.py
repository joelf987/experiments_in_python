import socket

LOCAL_HOST = "127.0.0.1"
PORT = 9000

def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LOCAL_HOST, PORT))
        s.listen()
        print(f"Listening on {LOCAL_HOST}:{PORT}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def main():
    a = listen()

if __name__ == "__main__":
    main()

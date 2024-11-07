import socket
import threading
import sys

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.settimeout(0.5)
            if conn.connect_ex((host, port)) == 0:
                try:
                    service_name = socket.getservbyport(port, "tcp")
                except OSError:
                    service_name = "Unknown service"
                print("%d open %s" % (port, service_name))
                return True
            return False
    except socket.error as error:
        print(error)
        return None

def scan_ports_range(host, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()
    for thread in threads:
        thread.join()
    print("Scanning completed.")

def main():
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <host> <start_port> <end_port>")
        sys.exit(1)
    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    print("Starting scan %s from port %d to %d" % (host, start_port, end_port))
    scan_ports_range(host, start_port, end_port)

if __name__ == "__main__":
    main()

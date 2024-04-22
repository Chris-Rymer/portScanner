
import nmap

def portScanner(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ','.join(map(str, ports)))
    for host in nm.all_hosts():
        print(f"Scanning ports for {host}:")
        for port in nm[host]['tcp'].keys():
            state = nm[host]['tcp'][port]['state']
            print(f"Port {port} is {state}")
    

def main():
    while True: 
        try:
            print("Welcome to IPv4 Port Scanner by Chris Rymer!")
            target = input("Enter IPv4 Address to scan:")
            startPort = int(input("Input starting port:"))
            endPort = int(input("Input ending port:"))
            ports = range(startPort, endPort + 1)
            portScanner(target, ports)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
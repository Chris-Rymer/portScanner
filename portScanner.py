#Import nmap library
import nmap

#Function that will scan target IP with nmap through range of ports specified by user and print results. 
def portScanner(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ','.join(map(str, ports)))
    for host in nm.all_hosts():
        print(f"Scanning ports for {host}:")
        for port in nm[host]['tcp'].keys():
            state = nm[host]['tcp'][port]['state']
            print(f"Port {port} is {state}")
    
#Main function that will ask user for IP and port range to scan. 
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

#Does not run "main" function if imported into another program. 
if __name__ == "__main__":
    main()

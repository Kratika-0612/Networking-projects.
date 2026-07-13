import socket

def main():
    host=input("enter the host or domain name: ") 
    port=int(input("enter the port: "))
    scan_port(host,port)

def get_protocol(port):
    protocols = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate"

 }

    return protocols.get(port, "Unknown")



def scan_port(host,port):
    scanner=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        result=scanner.connect_ex((host,port))
        protocol = get_protocol(port)
        if result ==  0:
            print(
                {"host":host,"port":port,"status":"OPEN","protocol": protocol}
                )
        else:
            print(
                {"host":host,"port":port,"status":"CLOSED","protocol": protocol})
    
    except Exception as e:
        print(e)
    finally:
        scanner.close()

if __name__ == "__main__":
    main()


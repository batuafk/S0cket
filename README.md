# S0cket

https://github.com/batuafk/S0cket/blob/main/S0cket.py

![image](https://github.com/user-attachments/assets/28241f95-de9f-452f-98c5-b8fe2ca157a3)

### Network Socket: A network socket is an endpoint for sending or receiving data across a computer network. It allows software applications to communicate with each other over a network, whether it's a local network or the internet.

## Components of a Network Socket
	IP Address: Identifies the networked device.
		IPv4: Consists of four octets separated by dots, e.g., 192.168.1.1.
		IPv6: Uses a longer format with hexadecimal digits separated by colons, e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
	Port Number: Identifies the specific application or service on the device.
		Well-Known Ports: 0 to 1023 (e.g., HTTP uses port 80, HTTPS uses port 443).
		Registered Ports: 1024 to 49151 (e.g., MySQL uses port 3306).
		Dynamic/Private Ports: 49152 to 65535 (used for ephemeral ports assigned temporarily for client-side connections).
	Protocol: Defines the rules for data transmission, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).

## Layers and protocols:
	Layer 1 (Physical):
	Ethernet (Wired network technology using frames to transmit data)
	Fiber Optic (Uses light to transmit data over long distances)
	DSL (Digital Subscriber Line, uses phone lines for internet)
	Wi-Fi (Wireless technology for local area networking)
	Coaxial Cable (Cable used for internet and TV signals)
	Bluetooth (Short-range wireless communication for devices)
	Infrared (Wireless communication using infrared light)
	Serial (RS-232) (Standard for serial communication between devices)
	ISDN (Integrated Services Digital Network, digital phone lines)
	Powerline Communication (Uses electrical wiring to transmit data)
	
	Layer 2 (Data Link):
	Ethernet (Wired LAN technology, handles data frames)
	Wi-Fi (Wireless LAN technology, handles data frames)
	PPP (Point-to-Point Protocol, used for direct connections)
	ARP (Address Resolution Protocol, maps IP addresses to MAC addresses)
	VLAN (Virtual LAN, segments network into different logical networks)
	Frame Relay (Wide area network technology for data transmission)
	HDLC (High-Level Data Link Control, encapsulates data frames)
	MPLS (Multiprotocol Label Switching, directs data based on labels)
	ATM (Asynchronous Transfer Mode, cell-based data transmission)
	L2TP (Layer 2 Tunneling Protocol, tunnels data for VPNs)
	
	Layer 3 (Network):
	IP (Internet Protocol) (Primary protocol for routing data across networks)
	ICMP (Internet Control Message Protocol, handles errors and network diagnostics)
	IPv6 (Next-generation IP protocol with a larger address space)
	OSPF (Open Shortest Path First, internal network routing protocol)
	BGP (Border Gateway Protocol, external network routing protocol)
	RIP (Routing Information Protocol, simpler internal network routing)
	EIGRP (Enhanced Interior Gateway Routing Protocol, advanced routing protocol)
	IS-IS (Intermediate System to Intermediate System, routing protocol for large networks)
	NAT (Network Address Translation, maps private IP addresses to public ones)
	IGMP (Internet Group Management Protocol, manages multicast groups)
	
	Layer 4 (Transport):
	TCP (Transmission Control Protocol) (Reliable, connection-oriented protocol)
	UDP (User Datagram Protocol) (Fast, connectionless protocol)
	SCTP (Stream Control Transmission Protocol, handles multiple streams)
	DCCP (Datagram Congestion Control Protocol, manages congestion control)
	QUIC (Quick UDP Internet Connections, improves web performance)
	RUDP (Reliable User Datagram Protocol, adds reliability to UDP)
	MPTCP (Multipath TCP, allows multiple network paths for a connection)
	RSVP (Resource Reservation Protocol, reserves resources for data flows)
	SPX (Sequenced Packet Exchange, used in Novell NetWare)
	SCTP (Stream Control Transmission Protocol, provides multi-streaming and reliability)
	
	Layer 5 (Session):
	HTTP (Hypertext Transfer Protocol, used for web browsing)
	SMB (Server Message Block) (File sharing and network communication protocol)
	NetBIOS (Network Basic Input/Output System, provides network services)
	RPC (Remote Procedure Call) (Executes programs on remote servers)
	SIP (Session Initiation Protocol) (Manages multimedia communication sessions)
	PPTP (Point-to-Point Tunneling Protocol) (VPN protocol for secure connections)
	LDAP (Lightweight Directory Access Protocol) (Accesses directory services)
	NFS (Network File System) (File sharing across networks)
	H.323 (Protocol for multimedia communication over networks)
	RDP (Remote Desktop Protocol) (Allows remote desktop access)
	
	Layer 6 (Presentation):
	SSL/TLS (Secure Sockets Layer/Transport Layer Security) (Encrypts data for secure communication)
	JPEG (Image format with lossy compression)
	PNG (Image format with lossless compression)
	GIF (Image format supporting animations)
	MPEG (Video compression standard)
	ASN.1 (Abstract Syntax Notation One) (Data format for representing structured data)
	XML (eXtensible Markup Language) (Markup language for data representation)
	JSON (JavaScript Object Notation) (Lightweight data interchange format)
	Base64 (Encoding scheme for binary data in text format)
	XDR (External Data Representation) (Standard for data serialization)
	
	Layer 7 (Application):
	HTTP (Hypertext Transfer Protocol) (Foundation of web communication)
	DNS (Domain Name System) (Translates domain names to IP addresses)
	FTP (File Transfer Protocol) (Transfers files between systems)
	SMTP (Simple Mail Transfer Protocol) (Sends email)
	IMAP (Internet Message Access Protocol) (Retrieves and manages email)
	POP3 (Post Office Protocol 3) (Retrieves email from servers)
	SNMP (Simple Network Management Protocol) (Manages network devices)
	Telnet (Remote command-line interface)
	LDAP (Lightweight Directory Access Protocol) (Accesses and manages directory information)
	NTP (Network Time Protocol) (Synchronizes clocks over a network)
	SFTP (SSH File Transfer Protocol) (Securely transfers files over SSH)
	HTTPS (HTTP Secure) (Secure version of HTTP using SSL/TLS)
	DHCP (Dynamic Host Configuration Protocol) (Automatically assigns IP addresses)
	TFTP (Trivial File Transfer Protocol) (Simple file transfer protocol)
	RADIUS (Remote Authentication Dial-In User Service) (Manages network access authentication)

# Socket

Network Socket: In computing, this is an endpoint for sending or receiving data across a computer network. It’s often used in programming to enable communication between applications over a network.

Components of a Network Socket
	IP Address: Identifies the networked device.
		IPv4: Consists of four octets separated by dots, e.g., 192.168.1.1.
		IPv6: Uses a longer format with hexadecimal digits separated by colons, e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
	Port Number: Identifies the specific application or service on the device.
		Well-Known Ports: 0 to 1023 (e.g., HTTP uses port 80, HTTPS uses port 443).
		Registered Ports: 1024 to 49151 (e.g., MySQL uses port 3306).
		Dynamic/Private Ports: 49152 to 65535 (used for ephemeral ports assigned temporarily for client-side connections).
	Protocol: Defines the rules for data transmission, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).

Stream Sockets (TCP):
	Use the Transmission Control Protocol (TCP) to provide a reliable, connection-oriented communication channel.
	Ensure that data is delivered in the correct order and without errors.
	Suitable for applications requiring guaranteed delivery.
		Web browsers (HTTP/HTTPS)
		Email (SMTP, IMAP, POP3)
		File transfers (FTP)

Datagram Sockets (UDP):
	Use the User Datagram Protocol (UDP) for connectionless communication.
	Data is sent without establishing a connection, and there is no guarantee of delivery or order.
	Suitable for applications where speed is crucial and occasional data loss is acceptable.
		Streaming media (video/audio)
		Online games
		DNS queries
		
		
Network protocols categories:
Web and Internet Protocols
Email Protocols
File Transfer Protocols
Network Management and Routing
Remote Access and Management
Network Configuration and Discovery
Security and Encryption
Time and Synchronization
Streaming and Real-Time Communication
Database Protocols
Peer-to-Peer and File Sharing
Tunneling and VPN
Multicast and Broadcast
Miscellaneous
Application Protocols
Network File Systems
Directory Services
Authentication and Authorization
Voice over IP (VoIP)
Messaging Protocols
Streaming Media Protocols
Remote Procedure Call (RPC)
Network Time Protocols
Dynamic Host Configuration Protocol (DHCP)
Label Switching
Network Discovery Protocols
Network Diagnostics and Testing
Routing Protocols
Service Discovery Protocols
Real-Time Transport Protocols
Internet Control Protocols
Peer-to-Peer Protocols
Data Transfer Protocols
Secure Communication Protocols
Network Access Control
Wireless Protocols
Integrated Services Digital Network (ISDN)
Quality of Service (QoS) Protocols
Multimedia Protocols
Session Management Protocols
Data Encryption Protocols
Telecommunications Protocols
Network Address Translation (NAT)
Application Layer Protocols
Traffic Management Protocols
Content Delivery Network (CDN) Protocols
Virtual Private Network (VPN) Protocols
Streaming Protocols
Service Management Protocols
Emerging Protocols

Network protocols:
HTTP (HyperText Transfer Protocol) - Web browsing
HTTPS (HTTP Secure) - Secure web browsing
DNS (Domain Name System) - Domain name resolution
SMTP (Simple Mail Transfer Protocol) - Email sending
FTP (File Transfer Protocol) - File transfers
IMAP (Internet Message Access Protocol) - Email retrieval
POP3 (Post Office Protocol 3) - Email retrieval
SSH (Secure Shell) - Secure remote access
TCP (Transmission Control Protocol) - Connection-oriented communication
UDP (User Datagram Protocol) - Connectionless communication
RDP (Remote Desktop Protocol) - Remote desktop access
SNMP (Simple Network Management Protocol) - Network management
SFTP (SSH File Transfer Protocol) - Secure file transfers
Telnet - Remote command-line access
NTP (Network Time Protocol) - Time synchronization
HTTP/2 (HyperText Transfer Protocol version 2) - Improved web browsing
DHCP (Dynamic Host Configuration Protocol) - IP address allocation
LDAP (Lightweight Directory Access Protocol) - Directory services
RTP (Real-Time Transport Protocol) - Streaming media
RTCP (Real-Time Control Protocol) - Control protocol for RTP
SIP (Session Initiation Protocol) - VoIP signaling
BGP (Border Gateway Protocol) - Internet routing
ICMP (Internet Control Message Protocol) - Network diagnostics
NFS (Network File System) - File sharing
TFTP (Trivial File Transfer Protocol) - Simple file transfers
QUIC (Quick UDP Internet Connections) - Fast, secure connections
MSSQL (Microsoft SQL Server) - Database access
PostgreSQL - Database access
MySQL - Database access
FTPES (FTP Explicit TLS/SSL) - Secure file transfers
L2TP (Layer 2 Tunneling Protocol) - VPNs
PPPoE (Point-to-Point Protocol over Ethernet) - DSL connections
GTP (GPRS Tunneling Protocol) - Mobile data transport
IPSec (Internet Protocol Security) - Secure network communication
XMPP (Extensible Messaging and Presence Protocol) - Instant messaging
Wi-Fi (Wireless Fidelity) - Wireless networking
UPnP (Universal Plug and Play) - Device discovery
IGMP (Internet Group Management Protocol) - Multicast group management
SSDP (Simple Service Discovery Protocol) - Device discovery
MPLS (Multiprotocol Label Switching) - Data packet routing
RADIUS (Remote Authentication Dial-In User Service) - Network access control
Diameter - Advanced RADIUS replacement
SCTP (Stream Control Transmission Protocol) - Reliable, message-oriented communication
Kerberos - Network authentication
Z39.50 - Library search and retrieval
EIGRP (Enhanced Interior Gateway Routing Protocol) - Network routing
OSPF (Open Shortest Path First) - Network routing
VNC (Virtual Network Computing) - Remote desktop access
Bittorrent - Peer-to-peer file sharing
Gopher - Early text-based Internet browsing

### LINK Penjelasan Soal No.03 :https://www.youtube.com/watch?v=H2wKcrfqAH4

Question  below are based on the trace file tcp-ethereal-trace-1 in in http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip

Answer the following questions for the TCP segments:
1.	What is the IP address and TCP port number used by your client computer (source) to transfer the file to gaia.cs.umass.edu? (10%)

2.	What does gaia.cs.umass.edu use the IP address and port number to receive the file. (Attach the screenshot of your Wireshark's display) (10%)

3.	What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? What is it in the segment that identifies the segment as a SYN segment? (Attach the screenshot of your Wireshark's display) (10%)

4.	What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is the value of the ACKnowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment? (Attach the screenshot of your Wireshark's display) (10%)

5.	What is the sequence number of the TCP segment containing the HTTP POST command? Note that in order to find the POST command, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with a “POST” within its DATA field.(Attach the screenshot of your Wireshark's display) (15%)

6.	Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six TCP connection segments (including the HTTP POST segment)? At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments? What is the EstimatedRTT value (see page 237 in textbook) after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 237 for all subsequent segments. (30%)
Note: Wireshark has a nice feature that allows you to plot the RTT for each of the TCP segments sent. Select a TCP segment in the “listing of captured packets” window that is being sent from the client to the gaia.cs.umass.edu server. Then select: Statistics->TCP Stream Graph->Round Trip Time Graph.

7.	What is the length of each of the first six TCP segments?(Attach the screenshot of your Wireshark's display)  (15%).

	# ANSWER:
**No 1.** 

	Client Computer : 
	Used Ip Address : 192.168.1.102
	Tcp port Number : 1161
	
  Destination computer: gaia.cs.umass.edu(This is the domain name of a server. This domain name is translated into a numeric IP address by the Domain Name System     (DNS) so that computers can locate the destination server.)
  
	Ip Address : 128.119.245.12
	Tcp Port Number : 80

 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture%201.png?raw=true)
 
 **Picture 1 : IP addresses and TCP port numbers of the client computer (source) and gaia.cs.umass.edu**

 **No 2.** 

  ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture2.png?raw=true)

  **Picture 2 : IP addresses and TCP port numbers gaia.cs.umass.edu**


  	Destination computer: gaia.cs.umass.edu
	Ip Address : 128.119.245.12
	Tcp Port Number : 80

 **No 3.** 
 
 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture3.png?raw=true)
 
**Picture 3 : Sequence number of the TCP SYN segment**

Solution : Sequence number of the TCP SYN segment is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu. The value is 0 in this trace.

This is because the sequence number is used to synchronize the data stream between the sender and receiver and initiate a new connection. When a new connection is established, there's no prior sequence to reference, so the initial sequence number is set to 0

Here's a breakdown of why this is the case:

- **TCP Sequence Numbers: TCP uses sequence numbers to ensure reliable and in-order delivery of data packets. Each byte of data sent within a connection has a unique sequence number.**

- **Initiating a Connection: The SYN segment marks the beginning of a TCP connection establishment process. It includes the initial sequence number that the sender will use for the data portion of the connection.**

- **No Prior Sequence: Since this is the first segment to initiate the connection, there's no prior sequence number to reference. Therefore, the sender sets the sequence number in the SYN segment to 0.**

The SYN flag is set to 1 and it indicates that this segment is a SYN segment. which further confirms that this is a SYN segment used to initiate the connection handshake between the client and the server.

**No 4.** 

![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture4.png?raw=true)
 
**Picture 4 : Sequence number and Acknowledgement number of the SYNACK segment**

Solution: 
**Sequence number of the SYNACK segment**: Sequence number of the SYNACK segment from gaia.cs.umass.edu to the client computer in reply to the SYN has the value of 0 in this trace.
	
**ACKnowledgement field value in the SYNACK segment**: The value of the ACKnowledgement field in the SYNACK segment is 1.

**How gaia.cs.umass.edu determined the ACK value**: The server acknowledges the receipt of the SYN segment sent by the client by setting the ACK field in the SYNACK segment to 1. This value (1) signifies that the server has received all the data up to the sequence number of the client's SYN segment (0).

**Identifying the segment as a SYNACK segment**: Two flags in the TCP header identify the segment as a SYNACK segment: 
- **SYN flag set to 1**: This indicates that the segment is initiating a connection request from the server.
- **SYN ACK flag set to 1**: This acknowledges the receipt of the client's SYN segment.

  **No 5.**

  ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture5.png?raw=true)
 
**Picture 5 : Sequence number and Acknowledgement number of the SYNACK segment**

Solution:  Segment is the TCP segment containing the HTTP POST command. The sequence number of this segment has the value of 1. 

**No 6.**
Solution: The HTTP POST segment is considered as the first segment. Segments 1 – 6 are No. 4, 5, 7, 8, 10, and 11 in this trace respectively. The ACKs of segments 1 – 6 are No. 6, 9, 12, 14, 15, and 16 in this trace.

**Segment 1 sequence number: 1 
Segment 2 sequence number: 566 
Segment 3 sequence number: 2026 
Segment 4 sequence number: 3486 
Segment 5 sequence number: 4946 
Segment 6 sequence number: 6406**

The sending time and the received time of ACKs are tabulated in the following table.
![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Tabel%20RTT.png?raw=true)

How to get RTT Second segment 1? 
( Ack Received Time – Sent Time= Rtt (Second) )

How to get RTT Second segment 2-6 ? 
(EstimatedRTT = 0.875 * EstimatedRTT + 0.125 * SampleRTT)

EstimatedRTT after the receipt of the ACK of segment 1:
EstimatedRTT = RTT for Segment 1 = 0.02746 second

EstimatedRTT after the receipt of the ACK of segment 2: 
EstimatedRTT = 0.875 * 0.02746 + 0.125 * 0.035557 = 0.0285

EstimatedRTT after the receipt of the ACK of segment 3: 
EstimatedRTT = 0.875 * 0.0285 + 0.125 * 0.070059 = 0.0337

EstimatedRTT after the receipt of the ACK of segment 4: 
EstimatedRTT = 0.875 * 0.0337+ 0.125 * 0.11443 = 0.0438

EstimatedRTT after the receipt of the ACK of segment 5: 
EstimatedRTT = 0.875 * 0.0438 + 0.125 * 0.13989 = 0.0558

EstimatedRTT after the receipt of the ACK of segment 6: 
EstimatedRTT = 0.875 * 0.0558 + 0.125 * 0.18964 = 0.0725 Second

  ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture6.png?raw=true)

**Picture 6 : Segments 1 – 6**

  ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture7.png?raw=true)

**Picture 7 : ACKs of segments 1 - 6**

  ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture8.png?raw=true)

**Picture 8 : Round Trip Time Graph**

**No 7.**

Solution: Length of the first TCP segment (containing the HTTP POST): 565 bytes Length of each of the other five TCP segments: 1460 bytes (MSS) 

The first segment is smaller because it contains the HTTP POST request, while the following segments use the full MSS of 1460 bytes to transfer more application data.

 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture9.png?raw=true)

**Picture 9 : Lenghts of Segments 1 – 6**

 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture10.png?raw=true)

**Picture 10 : TCP Segments 1 565 Bytes**

 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/UAS/Picture/Picture11.png?raw=true)

**Picture 9 : TCP Segments 2 - etc 1460 Bytes**

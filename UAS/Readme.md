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


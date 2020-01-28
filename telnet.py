# telnet program example
import socket, select, string, sys
from Crypto import Random #use to generate a random byte string of a length we decide
from Crypto.Cipher import AES
import base64
import hashlib



#main function
if __name__ == "__main__":	
	if(len(sys.argv) < 5) :
		print('Usage : python telnet.py hostname port name encryption_password')
		sys.exit()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	name = sys.argv[3]
	cypher_pass = sys.argv[4]
	def prompt() :
		sys.stdout.write("<" + name + "> ")
		sys.stdout.flush()

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print('Unable to connect')
		sys.exit()
	
	print('Connected to remote host. Start sending messages')
	prompt()


	while 1:
		socket_list = [sys.stdin, s]

		
		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
		for sock in read_sockets:
			#incoming message from remote server
			if sock == s:
				data = sock.recv(4096)
				if not data:
					print('\nDisconnected from chat server')
					sys.exit()
				else :
					#print data
					data = data.decode(encoding =  'utf-8', errors='strict')		
					sys.stdout.write(data)
					prompt()
			
			#user entered a message
			else:
				msg = sys.stdin.readline()
				msg = msg.encode(encoding =  'utf-8', errors='strict')
				s.send(msg)
				prompt()
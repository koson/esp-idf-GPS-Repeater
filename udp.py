import select, socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('<broadcast>', 9000))
s.setblocking(0)

while True:
	result = select.select([s],[],[])
	msg = result[0][0].recv(1024)
	if (type(msg) is bytes):
		#print("bytes")
		msg=msg.decode('utf-8')
		print("type(msg)={}".format(type(msg)))
	print(msg.strip())

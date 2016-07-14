import rpyc

queue = []

class MyServer(rpyc.Service):

	def exposed_ask_request(self, myTime, myId):
		queue.append(myId)
		while True:
			if((len(queue) == 0) or (queue[0] == myId)):
				return 1 #GRANT

	def exposed_send_release(self, myTime, myId):
		del queue[0]
		return 1 #SLEEP
		    


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyServer, port = 18860)
    t.start()
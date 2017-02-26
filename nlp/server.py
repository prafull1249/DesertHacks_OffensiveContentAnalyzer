import zmq
import nlp

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

def get_scores(s):
    return nlp.start(s)

def get_api_scores(s):
    return nlp.get_api_result(s)

# Run a simple "Echo" server
while True:
    message = sock.recv()
    message = get_api_scores(message)
    sock.send("Echo: " + message )
    print "Echo: " + message
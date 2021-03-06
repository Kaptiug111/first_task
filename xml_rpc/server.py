from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from dict import selectAll, insert, selectByID, delete

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("127.0.0.1", 8000),
                            requestHandler=RequestHandler)


server.register_function(selectAll)
server.register_function(selectByID)
server.register_function(insert)
server.register_function(delete)

# Run the server's main loop
server.serve_forever()
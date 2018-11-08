from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#change 'user' to your user name and directory!
authorizer = DummyAuthorizer()
authorizer.add_user("user", "8231335704", "/home/user", perm="elradfmw")
authorizer.add_anonymous("/home/user", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler) #host goes here
server.serve_forever()
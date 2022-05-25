from config import server
from routes import Routes


routes = Routes()
if __name__ == "__main__":
    server.run()
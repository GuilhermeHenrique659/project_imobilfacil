from config import server
from routes import Routes

app = server

routes = Routes()
if __name__ == "__main__":
    app.run()
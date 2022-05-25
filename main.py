from config import server as app
from routes import Routes


routes = Routes()
if __name__ == "__main__":
    app.run()
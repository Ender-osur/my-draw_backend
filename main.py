from src.config.api.Server import Server
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv(".env")

host = str(os.environ.get("HOST", "0.0.0.0"))
port = int(os.environ.get("POST", 8000))
server = Server()
app = server.app

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)

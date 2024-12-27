from hypercorn.config import Config
from hypercorn.asyncio import serve
from src.config.api.Server import Server
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

class Main(Server):
    def __init__(self) -> None:
        super().__init__()
        self.config = Config()
        self._setup_routes()
        self.config.bind = ["localhost:8000"]

    async def start(self) -> None:
        try:
            logging.info("Starting server...")
            await serve(self.app, self.config)
        except Exception as e:
            logging.error(f"An error occurred: {e}")

server = Main()
app = server.app

if __name__ == "__main__":
    server.start()

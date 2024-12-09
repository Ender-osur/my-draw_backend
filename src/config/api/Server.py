from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import uvicorn
from dotenv import load_dotenv
import os
import asyncio

load_dotenv(".env")


class Server:
    def __init__(self, *args,) -> None:
        self.app = FastAPI()
        self.load_config()
        self.load_routes()

    def load_config(self) -> None:
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        import logging
        logging.basicConfig(level=logging.DEBUG)

    def load_routes(self) -> None:
        from src.routes import router
        self.app.include_router(router)
        


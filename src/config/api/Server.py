from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Server:
    def __init__(self) -> None:
        self.app = FastAPI()
        self._setup_cors()
        self._setup_routes()

    def _setup_cors(self) -> None:
        origins = [
            "http://localhost",
            "http://localhost:3000",
        ]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _setup_routes(self) -> None:
        from src.routes.routes import router
        self.app.include_router(router)
    

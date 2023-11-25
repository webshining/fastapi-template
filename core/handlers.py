from fastapi import FastAPI

from .logging import logger


def start_app_handler(app: FastAPI) -> callable:
    async def start_app() -> None:
        logger.info("Server started!")

    return start_app


def shutdown_app_handler(app: FastAPI) -> callable:
    async def stop_app() -> None:
        logger.info("Server shutting down!")

    return stop_app

import os
import sys
from datetime import datetime
from fastapi import FastAPI
from PyLog.log import Logger

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

server = FastAPI()

@server.get("/")
def handle_get_root():
    Logger.get_instance().log(
        level="INFO",
        module="Main",
        method_trace="handle_get_root",
        message="Entered server root",
        timestamp=datetime.now()
    )
    return {"message": "Server Up and Running"}

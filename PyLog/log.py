import os
from datetime import datetime
from pydantic import BaseModel

class Log(BaseModel):
    level: str
    message: str
    module: str
    method_trace: str
    timestamp: datetime


class Logger:
    class_instance = None

    def __init__(self, folder_path = "logs"):
        self.folder_path = folder_path
        self.filter_level = 0
        self.filters = {
            "INFO" : 0,
            "DEBUG" : 1,
            "WARNING" : 2,
            "ERROR" : 3,
            "CRITICAL" : 4
        }

        # create a folder if it does not exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def set_filter_level(self, level):
        self.filter_level = self.filters[level.upper()]

    @staticmethod
    def get_instance():
        if Logger.class_instance is None:
            Logger.class_instance = Logger()
        return Logger.class_instance
    
  
    def _write_log(self, log: Log):
        #create a file with current date
        current_date = log.timestamp.strftime("%d-%m-%Y")
        file_path = f"{self.folder_path}/{current_date}.log"
        with open(file_path, "a") as file:
            file.write(f"{log.timestamp} - {self.filters[log.level]} - Module: {log.module} - Method: {log.method_trace} - Message: {log.message}\n")
    
    def log(self, level, message, module, method_trace, timestamp):
        if self.filters[level.upper()] >= self.filter_level:
            log = Log(level=level, message=message, module=module, method_trace=method_trace, timestamp=timestamp)
            self._write_log(log)

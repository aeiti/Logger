# Imports
import os

from datetime import datetime

import constants as const

class Log:
    def __init__(self, filename, txt):
        self._FILENAME = filename
        self._PATH = f"{const._LOG_DIR}/{filename}"
        self._TXT = txt

        self.file = None
    # End __init__

    def open(self):
        dir_exists = os.path.isdir(const._LOG_DIR)
        if not dir_exists:
            os.mkdir(const._LOG_DIR)

        try:
            self.file = open(self._PATH, 'a+', encoding=const._UTF8)
        except FileNotFoundError:
            self.file = open(self._PATH, 'w+', encoding=const._UTF8)
        except OSError:
            self.file = None
            print(const._LOG_OPENED_UNSUCCESSFULLY.format(self._TXT))
        else:
            print(const._LOG_OPENED_SUCCESSFULLY.format(self._TXT))
    # End open

    def write(self, msg):
        if self.file is not None:
            now = datetime.now()
            date = now.strftime("%m/%d/%Y %H:%M:%S.%f")

            self.file.write(f"[{date}]: [{self._TXT}]\n")
            self.file.write(f"\t-- {msg}\n")

            self.file.flush()
        else:
            print(f"Unable to write to file {self._TXT}")
    # End write

    def close(self):
        if self.file is not None:
            self.file.close()
    # End close

    def __del__(self):
        self.close()
    # End __del__
# End Log

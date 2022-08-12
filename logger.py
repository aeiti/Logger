# logger.py
# (C) Adam Manning 2022

# Imports
import constants as const

from log import Log

class Logger:
    # pylint: disable=too-many-instance-attributes
    # All attributes are needed for logging

    def __init__(self):
        # Initialize logs
        self._LOG_FATAL = Log("fatal.txt", const._TXT_FATAL) # FATAL log
        self._LOG_ERROR = Log("error.txt", const._TXT_ERROR) # ERROR log
        self._LOG_WARNING = Log("warnings.txt", const._TXT_WARNING) # WARNING log
        self._LOG_INFO = Log("info.txt", const._TXT_INFO) # INFO log
        self._LOG_DEBUG = Log("debug.txt", const._TXT_DEBUG) # DEBUG log
        self._LOG_TRACE = Log("trace.txt", const._TXT_TRACE) # TRACE log
        self._LOG_ALL = Log("all.txt", const._TXT_ALL) # ALL log

        self.open_logs() # Open all log files
    # End __init__

    def open_logs(self):
        self._LOG_FATAL.open()
        self._LOG_ERROR.open()
        self._LOG_WARNING.open()
        self._LOG_INFO.open()
        self._LOG_DEBUG.open()
        self._LOG_TRACE.open()
        self._LOG_ALL.open()
    # End open_logs

    def close_logs(self):
        self._LOG_FATAL.close()
        self._LOG_ERROR.close()
        self._LOG_WARNING.close()
        self._LOG_INFO.close()
        self._LOG_DEBUG.close()
        self._LOG_TRACE.close()
        self._LOG_ALL.close()
    # End close_log

    def fatal(self, msg):
        self._LOG_FATAL.write(f"{msg}")
    # End fatal

    def error(self, msg):
        self._LOG_ERROR.write(f"{msg}")
    # End error

    def warning(self, msg):
        self._LOG_WARNING.write(f"{msg}")
    # End warning

    def info(self, msg):
        self._LOG_INFO.write(f"{msg}")
    # End info

    def debug(self, msg):
        self._LOG_DEBUG.write(f"{msg}")
    # End debug

    def trace(self, msg):
        self._LOG_TRACE.write(f"{msg}")
    # End trace

    def all(self, msg):
        self._LOG_ALL.write(f"{msg}")
    # End all

    def __del__(self):
        self.close_logs()
    # End __del__
# End Logger class

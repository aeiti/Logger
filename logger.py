# logger.py
# (C) Adam Manning 2022

# Imports
import os

# Encodings
_UTF8 = "utf-8"

# Log name strings
_TXT_FATAL = "FATAL"
_TXT_ERROR = "ERROR"
_TXT_WARNING = "WARNING"
_TXT_INFO = "INFO"
_TXT_DEBUG = "DEBUG"
_TXT_TRACE = "TRACE"
_TXT_ALL = "ALL"

# Message strings
_LOG_OPENED_SUCCESSFULLY = "{0} file opened successfully!"
_LOG_OPENED_UNSUCCESSFULLY = "Unable to open {0} log file"

class Logger:
    # pylint: disable=too-many-instance-attributes
    # All attributes are needed for logging

    def __init__(self):
        #  Filenames of all logs
        self._FILENAME_FATAL = "fatal.txt" # Filename of FATOR log
        self._FILENAME_ERROR = "error.txt" # Filename of ERROR log
        self._FILENAME_WARNING = "warnings.txt" # Filename of WARNINGS log
        self._FILENAME_INFO = "info.txt" # Filename of INFO log
        self._FILENAME_DEBUG = "debug.txt" # Filename of DEBUG log
        self._FILENAME_TRACE = "trace.txt" # Filename of TRACE log
        self._FILENAME_ALL = "all.txt" # Filename of ALL log

        self._PATH_LOGS = "logs" # Directory containing all log files
        self._PATH_FATAL = f"{self._PATH_LOGS}/{self._FILENAME_FATAL}" # Filename of ERROR log
        self._PATH_ERROR = f"{self._PATH_LOGS}/{self._FILENAME_ERROR}" # Filename of ERROR log
        self._PATH_WARNING = f"{self._PATH_LOGS}/{self._FILENAME_WARNING}" # Filename of WARNINGS log
        self._PATH_INFO = f"{self._PATH_LOGS}/{self._FILENAME_INFO}" # Filename of INFO log
        self._PATH_DEBUG = f"{self._PATH_LOGS}/{self._FILENAME_DEBUG}" # Filename of DEBUG log
        self._PATH_TRACE = f"{self._PATH_LOGS}/{self._FILENAME_TRACE}" # Filename of INFO log
        self._PATH_ALL = f"{self._PATH_LOGS}/{self._FILENAME_ALL}" # Filename of ERROR log

        self.fatal_log = None # Initalize FATAL log
        self.error_log = None # Initalize ERROR log
        self.warning_log = None # Initalize WARNING log
        self.info_log = None # Initalize INFO log
        self.debug_log = None # Initalize DEBUG log
        self.trace_log = None # Initalize TRACE log
        self.all_log = None # Initalize ALL log

        self.open_logs() # Open all log files
    # End __init__

    def open_logs(self):
        is_dir = os.path.isdir(self._PATH_LOGS)
        if not is_dir:
            os.mkdir(self._PATH_LOGS)

        self.open_fatal_log()
        self.open_error_log()
        self.open_warning_log()
        self.open_info_log()
        self.open_debug_log()
        self.open_trace_log()
        self.open_all_log()
    # End open_logs

    def open_fatal_log(self):
        try:
            self.fatal_log = open(self._PATH_FATAL, 'a+', encoding=_UTF8)
        except FileNotFoundError:
            self.fatal_log = open(self._PATH_FATAL, 'w+', encoding=_UTF8)
        except OSError:
            self.fatal_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_FATAL))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_FATAL))
    # End open_fatal_log

    def open_error_log(self):
        try:
            self.error_log = open(self._PATH_ERROR, 'a', encoding=_UTF8)
        except OSError:
            self.error_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_ERROR))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_ERROR))
    # End open_error_log

    def open_warning_log(self):
        try:
            self.warning_log = open(self._PATH_WARNING, 'a', encoding=_UTF8)
        except OSError:
            self.warning_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_WARNING))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_WARNING))
    # End open_warning_log

    def open_info_log(self):
        try:
            self.info_log = open(self._PATH_INFO, 'a', encoding=_UTF8)
        except OSError:
            self.info_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_INFO))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_INFO))
    # End info_log

    def open_debug_log(self):
        try:
            self.debug_log = open(self._PATH_DEBUG, 'a', encoding=_UTF8)
        except OSError:
            self.debug_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_DEBUG))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_DEBUG))
    # End open_debug_log

    def open_trace_log(self):
        try:
            self.trace_log = open(self._PATH_TRACE, 'a', encoding=_UTF8)
        except OSError:
            self.trace_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_TRACE))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_TRACE))
    # End open_trace_log

    def open_all_log(self):
        try:
            self.all_log = open(self._PATH_ALL, 'a', encoding=_UTF8)
        except OSError:
            self.all_log = None
            print(_LOG_OPENED_UNSUCCESSFULLY.format(_TXT_ALL))
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_ALL))
    # End open_all_log

    def __del__(self):
        pass
    # End __del__
# End Logger class

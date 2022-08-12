_TXT_FATAL = "FATAL"
_TXT_ERROR = "ERROR"
_TXT_WARNING = "WARNING"
_TXT_INFO = "INFO"
_TXT_DEBUG = "DEBUG"
_TXT_TRACE = "TRACE"
_TXT_ALL = "ALL"

_UTF8 = "utf-8"
_LOG_OPENED_SUCCESSFULLY = "{0} file opened successfully!"

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

        self.fatal_log = None
        self.error_log = None
        self.warning_log = None
        self.info_log = None
        self.debug_log = None
        self.trace_log = None
        self.all_log = None

        self.open_fatal_log()
        self.open_error_log()
        self.open_warning_log()
        self.open_info_log()
        self.open_debug_log()
        self.open_trace_log()
        self.open_all_log()

    def open_fatal_log(self):
        try:
            self.fatal_log = open(self._PATH_FATAL, 'a', encoding=_UTF8)
        except OSError:
            self.fatal_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_FATAL))
    # End open_fatal_log

    def open_error_log(self):
        try:
            self.error_log = open(self._PATH_ERROR, 'a', encoding=_UTF8)
        except OSError:
            self.error_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_ERROR))
    # End open_error_log

    def open_warning_log(self):
        try:
            self.warning_log = open(self._PATH_WARNING, 'a', encoding=_UTF8)
        except OSError:
            self.warning_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_WARNING))
    # End open_warning_log

    def open_info_log(self):
        try:
            self.info_log = open(self._PATH_INFO, 'a', encoding=_UTF8)
        except OSError:
            self.info_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_INFO))
    # End info_log

    def open_debug_log(self):
        try:
            self.debug_log = open(self._PATH_DEBUG, 'a', encoding=_UTF8)
        except OSError:
            self.debug_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_DEBUG))
    # End open_debug_log

    def open_trace_log(self):
        try:
            self.trace_log = open(self._PATH_TRACE, 'a', encoding=_UTF8)
        except OSError:
            self.trace_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_TRACE))
    # End open_trace_log

    def open_all_log(self):
        try:
            self.all_log = open(self._PATH_ALL, 'a', encoding=_UTF8)
        except OSError:
            self.all_log = None
        else:
            print(_LOG_OPENED_SUCCESSFULLY.format(_TXT_ALL))
    # End open_all_log
# End Logger class

# logger.py
# (C) Adam Manning 2022

# Imports
import constants as const
import log as log

# Initialize logs
log._LOG_FATAL = log.Log("fatal.txt", const._TXT_FATAL) # FATAL log
log._LOG_ERROR = log.Log("error.txt", const._TXT_ERROR) # ERROR log
log._LOG_WARNING = log.Log("warnings.txt", const._TXT_WARNING) # WARNING log
log._LOG_INFO = log.Log("info.txt", const._TXT_INFO) # INFO log
log._LOG_DEBUG = log.Log("debug.txt", const._TXT_DEBUG) # DEBUG log
log._LOG_TRACE = log.Log("trace.txt", const._TXT_TRACE) # TRACE log
log._LOG_ALL = log.Log("all.txt", const._TXT_ALL) # ALL log

_logs_enabled = True
def disable_logs():
    global _logs_enabled
    _logs_enabled = False
# End disable_logs

def enable_logs():
    global _logs_enabled
    _logs_enabled = True
# End enable_logs

def log_fatal(msg):
    if _logs_enabled:
        log._LOG_FATAL.write(msg)
        log._LOG_ERROR.write(msg, const._TXT_FATAL)
        log._LOG_WARNING.write(msg, const._TXT_FATAL)
        log._LOG_INFO.write(msg, const._TXT_FATAL)
        log._LOG_DEBUG.write(msg, const._TXT_FATAL)
        log._LOG_TRACE.write(msg, const._TXT_FATAL)
        log._LOG_ALL.write(msg, const._TXT_FATAL)
# End log_fatal

def log_error(msg):
    if _logs_enabled:
        log._LOG_ERROR.write(msg)
        log._LOG_WARNING.write(msg, const._TXT_ERROR)
        log._LOG_INFO.write(msg, const._TXT_ERROR)
        log._LOG_DEBUG.write(msg, const._TXT_ERROR)
        log._LOG_TRACE.write(msg, const._TXT_ERROR)
        log._LOG_ALL.write(msg, const._TXT_ERROR)
# End log_error

def log_warning(msg):
    if _logs_enabled:
        log._LOG_WARNING.write(msg)
        log._LOG_INFO.write(msg, const._TXT_WARNING)
        log._LOG_DEBUG.write(msg, const._TXT_WARNING)
        log._LOG_TRACE.write(msg, const._TXT_WARNING)
        log._LOG_ALL.write(msg, const._TXT_WARNING)
# End log_warning

def log_info(msg):
    if _logs_enabled:
        log._LOG_INFO.write(msg)
        log._LOG_DEBUG.write(msg, const._TXT_INFO)
        log._LOG_TRACE.write(msg, const._TXT_INFO)
        log._LOG_ALL.write(msg, const._TXT_INFO)
# End log_info

def log_debug(msg):
    if _logs_enabled:
        log._LOG_DEBUG.write(msg)
        log._LOG_TRACE.write(msg, const._TXT_DEBUG)
        log._LOG_ALL.write(msg, const._TXT_DEBUG)
# End log_debug

def log_trace(msg):
    if _logs_enabled:
        log._LOG_TRACE.write(msg)
        log._LOG_ALL.write(msg, const._TXT_TRACE)
# End log_trace

def log_all(msg):
    if _logs_enabled:
        log._LOG_ALL.write(msg)
# End log_all

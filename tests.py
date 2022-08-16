import constants as const

import logger as log

def main():
    log.open_logs()

    log.log_all("Logging started")

    log.log_fatal(f"{const._TXT_FATAL} log test")
    log.log_error(f"{const._TXT_ERROR} log test")
    log.log_warning(f"{const._TXT_WARNING} log test")
    log.log_info(f"{const._TXT_INFO} log test")
    log.log_debug(f"{const._TXT_DEBUG} log test")
    log.log_trace(f"{const._TXT_TRACE} log test")
    log.log_all(f"{const._TXT_ALL} log test")

    for i in range(0, 5):
        log.log_fatal(f"The count is ({i})")
        log.log_error(f"The count is ({i})")
        log.log_warning(f"The count is ({i})")
        log.log_info(f"The count is ({i})")
        log.log_debug(f"The count is ({i})")
        log.log_trace(f"The count is ({i})")
        log.log_all(f"The count is ({i})")

    log.close_logs()
    
if __name__ == '__main__':
    main()

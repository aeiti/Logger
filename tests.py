import constants as const

from logger import Logger

log = Logger()

log.all("Logging started")

log.fatal(f"{const._TXT_FATAL} log test")
log.error(f"{const._TXT_ERROR} log test")
log.warning(f"{const._TXT_WARNING} log test")
log.info(f"{const._TXT_INFO} log test")
log.debug(f"{const._TXT_DEBUG} log test")
log.trace(f"{const._TXT_TRACE} log test")
log.all(f"{const._TXT_ALL} log test")

for i in range(0, 5):
    log.fatal(f"The count is ({i})")
    log.error(f"The count is ({i})")
    log.warning(f"The count is ({i})")
    log.info(f"The count is ({i})")
    log.debug(f"The count is ({i})")
    log.trace(f"The count is ({i})")
    log.all(f"The count is ({i})")

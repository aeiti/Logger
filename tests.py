import constants as const

from logger import Logger

log = Logger()

log.fatal(f"{const._TXT_FATAL} log successful")
log.error(f"{const._TXT_ERROR} log successful")
log.warning(f"{const._TXT_WARNING} log successful")
log.info(f"{const._TXT_INFO} log successful")
log.debug(f"{const._TXT_DEBUG} log successful")
log.trace(f"{const._TXT_TRACE} log successful")
log.all(f"{const._TXT_ALL} log successful")

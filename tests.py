import constants as const

import logger as log

def single_tests():
    test_fatal()
    test_error()
    test_warning()
    test_info()
    test_debug()
    test_trace()
    test_all()

def test_fatal():
    log.log_fatal(f"{const._TXT_FATAL} log test")

def test_error():
    log.log_error(f"{const._TXT_ERROR} log test")

def test_warning():
    log.log_warning(f"{const._TXT_WARNING} log test")

def test_info():
    log.log_info(f"{const._TXT_INFO} log test")

def test_debug():
    log.log_debug(f"{const._TXT_DEBUG} log test")

def test_trace():
    log.log_trace(f"{const._TXT_TRACE} log test")

def test_all():
    log.log_all(f"{const._TXT_ALL} log test")

loop_max = 2
def loop_tests():
    loop_fatal()
    loop_error()
    loop_warning()
    loop_info()
    loop_debug()
    loop_trace()
    loop_all()

def loop_fatal():
    for i in range(0, loop_max):
        log.log_fatal(f"The count is ({i})")

def loop_error():
    for i in range(0, loop_max):
        log.log_error(f"The count is ({i})")

def loop_warning():
    for i in range(0, loop_max):
        log.log_warning(f"The count is ({i})")

def loop_info():
    for i in range(0, loop_max):
        log.log_info(f"The count is ({i})")

def loop_debug():
    for i in range(0, loop_max):
        log.log_debug(f"The count is ({i})")

def loop_trace():
    for i in range(0, loop_max):
        log.log_trace(f"The count is ({i})")

def loop_all():
    for i in range(0, loop_max):
        log.log_all(f"The count is ({i})")

def force_log(msg):
    log.enable_logs()

    log.log_fatal(f"{msg}")
    log.log_error(f"{msg}")
    log.log_warning(f"{msg}")
    log.log_info(f"{msg}")
    log.log_debug(f"{msg}")
    log.log_trace(f"{msg}")
    log.log_all(f"{msg}")

    log.disable_logs()

def main():
    print("Enabling logging")
    log.enable_logs()
    print("Logging enabled")

    print("Running tests")

    single_tests()
    loop_tests()

    print("Logging enabled complete")

    print("Disabling logging")
    log.disable_logs()
    print("Logging diabled")

    force_log("LOGGING HAS BEEN DISABLED FOR FLAG TESTING")

    print("Running tests")
    single_tests()
    loop_tests()

    print("Logging disabled complete")

    log.enable_logs()
    force_log("LOGGING HAS BEEN REENABLED")

    print("Tests complete!")

if __name__ == '__main__':
    main()

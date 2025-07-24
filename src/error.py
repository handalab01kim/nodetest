import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import threading # 멀티스레드 에러 로거 설정 필요

# error + info
def error_log(path):
    # 로거
    logger = logging.getLogger("error_logger")
    logger.setLevel(logging.DEBUG)

    log_path = os.path.join(path, "log.log")
    handler = RotatingFileHandler(
        log_path,
        maxBytes=1024 * 1024 * 10,  # 최대 10MB
        backupCount=10          # rotate -> 파일 최대 10개
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 예외 전역 핸들링
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logger.error("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_exception

    # 멀티스레드 에러 핸들링
    def thread_exception_handler(args):
        handle_exception(args.exc_type, args.exc_value, args.exc_traceback)

    threading.excepthook = thread_exception_handler  # Python 3.8+

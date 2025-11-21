import logging
import types
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Add custom log level for successful operations (between INFO and WARNING)
SUCCESS = logging.INFO + 5
logging.SUCCESS = SUCCESS   # Attach to logging module for detection and reuse
logging.addLevelName(SUCCESS, 'SUCCESS')

class CustomLogger(logging.Logger):
    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(SUCCESS):
            # Use .log() so it respects handlers & levels
            self.log(SUCCESS, msg, *args, **kwargs)

# Register the custom logger class BEFORE any getLogger() calls occur
logging.setLoggerClass(CustomLogger)


def _ensure_success_method(logger: logging.Logger):
    """
    Attach a `.success()` method to *this logger instance* if it doesn't exist.
    This makes the call robust even if the logger was created before setLoggerClass.
    """
    if not hasattr(logger, "success"):
        def _success(self, msg, *args, **kwargs):
            if self.isEnabledFor(SUCCESS):
                self.log(SUCCESS, msg, *args, **kwargs)
        # Bind as a real instance method
        logger.success = types.MethodType(_success, logger)


def setup_logger(name=__name__, log_level=logging.INFO):
    """
    Returns a logger with RotatingFileHandlers and a StatusCode filter.
    Robust against Streamlit reruns & early-created loggers.
    """
    # Create logs directory in project root if it doesn't exist
    project_root = Path(__file__).parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    
    
    # If a non-CustomLogger already exists for this name, force re-create:
    mgr = logging.Logger.manager
    existing = mgr.loggerDict.get(name)
    # Avoid nuking PlaceHolder (safe to recreate) but if a Logger exists and
    # it's not our CustomLogger, delete and get a fresh one of the new class.
    if isinstance(existing, logging.Logger) and not isinstance(existing, CustomLogger):
        del mgr.loggerDict[name]

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # capture everything; handlers decide

    # Ensure success method exists regardless of class
    _ensure_success_method(logger)

    # Prevent adding multiple handlers if logger already configured
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)-8s - Status: %(status_code)s - %(message)s"
    )
    
    # Add a filter to include status_code in log records
    class StatusCodeFilter(logging.Filter):
        def filter(self, record):
            if not hasattr(record, 'status_code'):
                record.status_code = 'N/A'
            return True
    
    status_filter = StatusCodeFilter()
    
    # Create a file handler for error and above logs
    error_log = log_dir / 'error.log'
    error_handler = RotatingFileHandler(
        error_log,
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    error_handler.addFilter(status_filter)
    
    # Create a file handler for all logs
    info_log = log_dir / 'app.log'
    file_handler = RotatingFileHandler(
        info_log,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(status_filter)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(status_filter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create a default logger instance
logger = setup_logger('TEAMS_Summarizer_FAQgen')

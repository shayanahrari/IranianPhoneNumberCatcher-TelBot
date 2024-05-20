import logging

logger = logging.getLogger(__name__)

file_h = logging.FileHandler("logsfile.log")
stream_h = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s"
)

file_h.setFormatter(formatter)
stream_h.setFormatter(formatter)

file_h.setLevel(logging.ERROR)
stream_h.setLevel(logging.INFO)

logger.addHandler(file_h)
logger.addHandler(stream_h)

logger.setLevel(logging.INFO)

# Selenium WebDriver Python coding
import logging as L
def log(level, message, file):
    # Configure logging to start with the INFO level, the log file and the filemode as append to log file.
    L.basicConfig(level=L.INFO, filename=file, filemode="a",
                  format="%(asctime)-12s %(levelname)s %(message)s", # log entry format
                  datefmt="%d-%m-%Y %H:%M:%S") # date time format
    if level == "INFO": L.info(message)
    if level == "WARNING": L.warning(message)
    if level == "ERROR": L.error(message)
    if level == "CRITICAL": L.critical(message)

from pathlib import Path
import logging
from datetime import datetime

def get_script_folder() -> Path: 
    try: 
        return Path(__file__).resolve().parent
    except NameError: 
        return Path.cwd().resolve()
    
def create_logger(script_folder: str | Path) -> logging.Logger: 
    script_folder = Path(script_folder)

    timestamp = datetime.now().strftime("%m%d%Y_%H%M%S") # file system safe and readable
    logger_output = (
        script_folder
        / "output"
        / "temp"
        / f"geo_logger_output_{timestamp}.txt"
    )
    logger_output.parent.mkdir(parents=True, exist_ok=True) # generate dynamic logger file output

    file_handler = logging.FileHandler(logger_output, 
                                       mode="w", 
                                       encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger
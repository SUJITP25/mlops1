import logging.config
import pandas as pd 
import os 
from sklearn.model_selection import train_test_split 
import logging 

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)



# What is Logging? 
# In Python is a built-in Logging Function. 
# We will make object of the logging module 
# logger = logging()
# We have to define the handler in the logger object 



# logging configuration
logger = logging.getLogger("data_ingestion")
logger.setLevel("DEBUG")


console_handler = logging.StreamHandler()
console_handler("DEBUG")


log_file_path = os.path.join(log_dir, "data_ingestion.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

formatter =formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def load_data(url): 
    try: 
        df = pd.read_csv(url)
        logger.debug("Data loaded from url", url)
    except pd.errors.ParserError as e: 
        logger.error("Failed to Parse the CSV file")
        raise
    except Exception as e: 
        logger.error("Unexpected Error Happened While loading the data",e)
        raise


def pereprocess_data(df): 
    try: 
        df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace = True)
        df.rename(columns = {'v1': 'target', 'v2': 'text'}, inplace = True)
    except Exception as e: 
        logger.error("error in preprocessing the data")
        raise
    except Exception as e: 
        logger.error("Unexpected Error Happened While Preprocessing the data",e)
        raise 




def save_data(train_data,test_data,data_path): 
    try: 
        raw_data_path =os.path.join(data_path,"raw")
        os.makedirs(raw_data_path,exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_path,'train.csv'), index=False)
        test_data.to_csv(os.path.join(raw_data_path,'test.csv'), index=False)
        logger.debug("Data saved at location", raw_data_path)
    except Exception as e: 
        logger.error("Unexpected Error Happened While Preprocessing the data",e)
        raise 


def main(): 
    try: 
        pass 
    except Exception as e:
        logger.error("Unexpected Error Happened While Preprocessing the data",e)
        raise 

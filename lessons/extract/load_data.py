import requests
import logging
import pandas as pd

class Loader:
    """
    Class to handle loading operations
    """

    def __init__(self, url: str, save_path: str) -> None:
        """
        Args:
            url: URL to download data
            save_path: Path to store the data
        """
        self.url = url
        self.save_path = save_path

    
    def download_file(self) -> requests.Response:
        """
        Downloads a CSV file from specified URL to specified path

        Returns:
            requests.Response: The HTTP response object containing the CSV file data
        """
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
            logging.info("Successfully downloaded data")
            return response
        except requests.exceptions.RequestException as e:
            logging.error("Failed to download file: %s", e)
            return None

    def save_file(self, response: requests.Response) -> None:
        """
        Saves downloaded file into specified path

        Args:
            requests.Response: The HTTP response object containing the CSV file data
        """
        try:
            if response.status_code == 200:
                with open(self.save_path, 'wb') as file:
                    file.write(response.content)
                logging.info("File successfully saved data into: %s", self.save_path)
        except FileNotFoundError as e:
            logging.error("File path does not exist: %s", e)

    def ingest_data(self) -> pd.DataFrame:
        """
        Ingests data as DataFrame from defined path

        Return:
            pd.DataFrame: Data in DataFrame
        """
        try:
            df = pd.read_csv(self.save_path)
            return df
        except FileNotFoundError as e:
            logging.error("The specified file path does not exist: %s. Error message: %s", self.save_path, e)
            raise e



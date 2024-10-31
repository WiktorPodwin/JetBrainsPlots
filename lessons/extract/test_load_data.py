from unittest import mock, TestCase
from load_data import Loader
import requests
import pandas as pd

class TestLoader(TestCase):
    """
    Unit tests for the Loader class, focusing on downloading, saving, and ingesting data
    """
    def setUp(self):
        """
        Sets up the test environment by defining default test URL and file path
        """
        self.save_path = "dummy_path"
        self.url = "http://test.com"
        
    @mock.patch('requests.get')
    def test_download_file_success(self, mock_get: mock.Mock):
        """
        Tests successful file download by mocking `requests.get`
        """
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = b"Test data"
        mock_get.return_value = mock_response

        loader = Loader(self.url, self.save_path)
        response = loader.download_file()

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Test data")
    
    @mock.patch('requests.get')
    def test_download_file_failure(self, mock_get: mock.Mock):
        """
        Tests failed file download by simulating a connection error by mocking `requests.get` 
        """
        mock_get.side_effect = requests.exceptions.RequestException("Connection failed")
        loader = Loader(self.url, self.save_path)
        
        with self.assertLogs(level='ERROR') as log:
            response = loader.download_file()

            self.assertIsNone(response)
            self.assertIn("Failed to download file", log.output[0])

    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_save_file_success(self, mock_open: mock.Mock):
        """
        Tests successful file saving by mocking `builtins.open` 
        """
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.content = b"Test data"

        loader = Loader(self.url, self.save_path)
        loader.save_file(mock_response)

        mock_open.assert_called_once_with(self.save_path, 'wb')
        mock_open().write.assert_called_once_with(b"Test data")

    @mock.patch('builtins.open')
    def test_save_file_failure(self, mock_open: mock.Mock):
        """
        Test that save_file logs an error when a FileNotFoundError is raised
        due to an invalid or inaccessible path by mocking `builtins.open` 
        """        
        mock_response = mock.Mock(spec=requests.Response)
        mock_response.status_code = 200
        mock_response.content = b"Test data"

        mock_open.side_effect = FileNotFoundError()

        with self.assertLogs(level='ERROR') as log:
            loader = Loader(self.url, self.save_path)
            loader.save_file(mock_response)

            mock_open.assert_called_once_with(self.save_path, 'wb')
            
            self.assertIn("File path does not exist", log.output[0])

    @mock.patch('pandas.read_csv')
    def test_ingest_data(self, mock_read_csv: mock.Mock):
        """
        Tests successful data ingestion from a CSV file by mocking 'pandas.read_csv'
        """
        mock_df = pd.DataFrame({'col1': [1, 2],
                                'col2': [3, 4]})
        mock_read_csv.return_value = mock_df

        loader = Loader(self.url, self.save_path)
        result = loader.ingest_data()

        mock_read_csv.assert_called_once_with(self.save_path)
        pd.testing.assert_frame_equal(result, mock_df)

    @mock.patch('pandas.read_csv')
    def test_ingest_data_wrong_path(self, mock_read_csv: mock.Mock):
        """
        Tests error handling when ingesting data from a non-existent file path by mocking 'pandas.read_csv'
        """
        mock_read_csv.side_effect = FileNotFoundError()
        loader = Loader(self.url, self.save_path)

        with self.assertLogs(level='ERROR') as log:
            with self.assertRaises(FileNotFoundError):
                loader.ingest_data()
            self.assertIn("The specified file path does not exist", log.output[0])

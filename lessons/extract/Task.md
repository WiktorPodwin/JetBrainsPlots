# Step: Extract
## Theory
In this step, we will focus on the extraction of data from a remote source and its preparation for analysis. This involves three main processes:

1 - `Downloading the Data`: We will use the requests library to download a CSV file from a given URL. This library allows us to send HTTP requests and handle responses conveniently.

Key points to remember:

* Ensure the URL is valid and points directly to a CSV file.
Handle exceptions properly to manage errors, such as connection issues or invalid URLs.

2 - `Saving the Data Locally`: After successfully downloading the file, we will save it to a specified path on our local machine. This allows us to work with the dataset offline.

Important considerations:

* Verify that the directory path where you want to save the file exists.
* Handle potential file writing errors gracefully, such as file permission issues or incorrect paths.

3 - `Loading the Data into a DataFrame`: Once the CSV file is saved, we will use the pandas library to load the data into a DataFrame. This is crucial for data manipulation and visualization, as Pandas provides powerful data structures to work with.

Key functions in Pandas:

* pd.read_csv() is used to read CSV files into a DataFrame.
* It’s important to handle exceptions while loading data, such as file not found errors.

This entire process is encapsulated in the Loader class, which has three primary methods:
* `download_file()`: Handles the downloading of the file, returns response.
* `save_file(response)`: Saves the file locally.
* `ingest_data()`: Loads the CSV data into a DataFrame.

## Task
Your task is to implement a script that utilizes the Loader class defined in the reference solution. Follow these steps to complete the task:

1. Instantiate the Loader Class:
* Create an instance of the Loader class, providing a valid URL for the dataset and a desired local file path to save the CSV file.

2. Download the File:
* Call the download_file() method to download the CSV file from the specified URL.

3. Save the File:
* After successfully downloading, use the save_file() method to save the file to your local machine.

4. Ingest the Data:
* Finally, use the ingest_data() method to load the data into a Pandas DataFrame.
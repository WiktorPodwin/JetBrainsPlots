# Step: Transform

## Theory
In this step, we will focus on transforming the data to prepare it for analysis and visualization. This involves three main processes:

1 - `Cleaning the Data`: We will remove any samples with missing values and select only the necessary features and specified feature classes from the dataset. This ensures that our analysis is based on complete and relevant data.

Key points to remember:

* Use dropna() to remove rows with empty fields.
* Select features using DataFrame indexing.
* Filter the dataset based on specified classes to retain only relevant entries.

2 - `Grouping and Counting`: Once the data is cleaned, we will group the DataFrame by all unique pairs of samples and count the occurrences of each combination. This step is crucial for understanding the distribution of the data across different features.

Important considerations:

* Use groupby() combined with size() to create a summary table that counts the frequency of each unique combination.
* This helps in visualizing the data in a meaningful way by simplifying the dataset.

3 - `Sorting the Data`: After grouping and counting, we will sort the DataFrame based on specified features in ascending order. This will facilitate better visualization in the final bar chart.

Key functions in Pandas:
* pd.Categorical() is used to set an ordered categorical type for the specified features, allowing for logical sorting.
* Use sort_values() to arrange the DataFrame based on selected columns.

This entire transformation process is encapsulated in the Transform class, which includes three primary methods:

* `clean_data()`: Cleans the dataset and selects relevant features.
* `group_and_count()`: Groups the DataFrame and counts occurrences of unique combinations.
* `sort_data()`: Sorts the DataFrame based on specified features.

## Task
Your task is to implement a script that utilizes the Transform class defined in the reference solution. Follow these steps to complete the task:

1. Instantiate the Transform Class:
* Create an instance of the Transform class, providing the DataFrame obtained from the previous extraction step, a list of features to retain, and a dictionary specifying the classes to select for each feature.

2. Clean the Data:
* Call the clean_data() method to clean the DataFrame by removing samples with missing values and filtering based on the specified features and classes.

3. Group and Count:
* Use the group_and_count() method to group the DataFrame and count occurrences of each unique combination of samples.

4. Sort the Data:
* Finally, call the sort_data() method to sort the DataFrame based on the specified features in ascending order.
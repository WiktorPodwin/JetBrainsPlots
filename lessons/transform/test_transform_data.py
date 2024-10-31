from unittest import TestCase
from transform_data import Transform
import pandas as pd


class TestTransform(TestCase):
    """
    Unit tests for the Transform class, focusing on data cleaning, grouping, and sorting operations
    """
    def test_clean_data_success(self):
        """
        Tests successful data cleaning with specified features and filter conditions
        """
        df = pd.DataFrame({'feature1': [1, 2, 3, None],
                           'feature2': ['A', 'B', 'A', 'B'],
                           'feature3': [1.4, 2.9, 3.1, 1.73]})
        
        features = ['feature1', 'feature2']
        classes = {'feature2': ['B']}

        expected_df = pd.DataFrame({'feature1': [2.],
                                    'feature2': ['B']})

        transform = Transform(df, features, classes)
        result_df = transform.clean_data()

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_clean_data_key_error(self):
        """
        Tests data cleaning when a specified feature is missing from the DataFrame
        """
        df = pd.DataFrame({'feature1': [1, 2, 3, None],
                           'feature3': [1.4, 2.9, 3.1, 1.73]})
        
        features = ['feature1', 'feature2']
        classes = {'feature2': ['B']}

        transform = Transform(df, features, classes)

        with self.assertLogs(level='ERROR') as log:
            result_df = transform.clean_data()
            self.assertIsNone(result_df)
            self.assertIn("Error while cleaning the data", log.output[0])

    def test_group_and_count_success(self):
        """
        Tests successful grouping and counting of DataFrame rows by specified features
        """
        df = pd.DataFrame({'feature1': [1, 1, 2, 1],
                           'feature2': ['A', 'B', 'A', 'B']})
        
        expected_df = pd.DataFrame({'feature1': [1, 1, 2],
                                    'feature2': ['A', 'B', 'A'],
                                    'count': [1, 2, 1]})
        
        features = ['feature1', 'feature2']
        classes = {'feature2': ['B']}
        
        transform = Transform(df, features, classes)
        result_df = transform.group_and_count()
        
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_group_and_count_failure(self):
        """
        Tests handling of invalid DataFrame input when grouping and counting
        """
        df = None        
        features = ['feature1', 'feature2']
        classes = {'feature2': ['B']}

        transform = Transform(df, features, classes)
        with self.assertLogs(level='ERROR') as log:
            result_df = transform.group_and_count()
            self.assertIsNone(result_df)
            self.assertIn("Data need to be in pandas.DataFrame format", log.output[0])

    def test_sort_data_success(self):
        """
        Tests successful sorting of DataFrame rows based on class order for specified features
        """
        df = pd.DataFrame({'feature1': [1, 1, 2],
                           'feature2': ['A', 'B', 'A'],
                           'count': [1, 2, 1]})
        
        features = ['feature1', 'feature2']
        classes = {'feature2': ['B', 'A']}

        expected_df = pd.DataFrame({'feature1': [1, 1, 2],
                                    'feature2': pd.Categorical(['B', 'A', 'A'], categories=['B', 'A'], ordered=True),
                                    'count': [2, 1, 1]})

        transform = Transform(df, features, classes)
        result_df = transform.sort_data()
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_sort_data_key_error(self):
        """
        Tests handling of missing features in DataFrame when sorting data
        """
        df = pd.DataFrame({'feature1': [1, 1, 2],
                           'feature2': ['A', 'B', 'A'],
                           'count': [1, 2, 1]})
               
        features = ['feature1', 'feature3']
        classes = {'feature2': ['B', 'A']}

        transform = Transform(df, features, classes)
        with self.assertLogs(level='ERROR') as log:
            result_df = transform.sort_data()
            self.assertIsNone(result_df)
            self.assertIn("Provided features are not found in the DataFrame", log.output[0])
   


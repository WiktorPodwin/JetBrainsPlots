import pandas as pd
import logging
from typing import List, Dict

class Transform:
    """
    Class to handle transform operations
    """

    def __init__(self, 
                 df: pd.DataFrame, 
                 features: List[str], 
                 classes: Dict[str, List[str]]
                 ) -> None:
        """       
        Args:
            df: Data before transformation
            features: Features to select
            classes: A dictionary storing feature and their classes to select
        """
        self.df = df
        self.features = features
        self.classes = classes
        
    def clean_data(self) -> pd.DataFrame:
        """
        Cleans the data: deletes samples with empty fields and selects 
        only necessary features and specified feature classes from the data

        Returns: 
            pd.DataFrame: Data after transformation
        """
        try:
            self.df = self.df.dropna()
            self.df = self.df[self.features]
            for feature, class_list in self.classes.items():
                self.df = self.df[self.df[feature].isin(class_list)]
            self.df = self.df.reset_index(drop=True)
            logging.info("Data has been cleaned")
            return self.df
        except KeyError as e:
            logging.error("Error while cleaning the data: %s", e)
            return None
    
    def group_and_count(self) -> pd.DataFrame:
        """
        Groups and counts each unique pair of samples

        Returns: 
            pd.DataFrame: Data after transformation
        """
        try:
            self.df = self.df.groupby(self.df.columns.tolist()).size().reset_index(name='count')
            logging.info("Data has been grouped and counted")
            return self.df
        except AttributeError as e:
            logging.error("Data need to be in pandas.DataFrame format: %s", e)
            return None
            
    def sort_data(self) -> pd.DataFrame:
        """
        Sorts the data ascended
        """
        try:
            for feature, class_list in self.classes.items():
                self.df[feature] = pd.Categorical(self.df[feature], categories=class_list, ordered=True)
    
            self.df = self.df.sort_values(by=self.features, ascending=[True, True])
            self.df = self.df.reset_index(drop=True)
            logging.info("Data has been sorted")
            return self.df
        except KeyError as e:
            logging.error("Provided features are not found in the DataFrame: %s", e)
            return None

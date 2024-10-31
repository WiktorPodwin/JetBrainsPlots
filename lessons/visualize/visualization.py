import matplotlib.pyplot as plt
import logging
import pandas as pd
import numpy as np

class EmptyDataFrameError(Exception):
    """Custom exception for handling empty DataFrame errors in BarPlot"""
    pass

class BarPlot:
    """
    Class to create and save bar plot to specified path
    """

    def __init__(self) -> None:
        self.ax = None
        self.fig = None

    def create_plot(self, df: pd.DataFrame) -> None:
        """
        Creates a bar plot
        
        Args:
            df: DataFrame storing data to visualize
        """
        if df.empty:
            error_message = "The provided DataFrame is empty and cannot be used to create a plot."
            logging.error(error_message)
            raise EmptyDataFrameError(error_message)
        try:
            platform = df.columns[0]
            columns = df.columns[1]
            values = df.columns[2]

            pivot_df = df.pivot(index=platform, columns=columns, values=values)
            genres = pivot_df.columns

            half_samples = int(len(genres)/2)
            genre_blues = plt.cm.Blues(np.linspace(0.2, 0.8, half_samples))
            genre_greens = plt.cm.Greens(np.linspace(0.2, 0.8, len(genres) - half_samples))
            genre_colors = np.concatenate((genre_blues, genre_greens), axis=0)

            genre_color_map = {genre: genre_colors[i] for i, genre in enumerate(genres)}

            x = np.arange(len(pivot_df.index))
            width = 0.05
            multiplier = 0

            self.fig, self.ax = plt.subplots(figsize=(12, 6))

            for genre in genres:
                offset = width * multiplier
                counts = pivot_df[genre]
                multiplier += 1
                
                self.ax.bar(x + offset,
                            counts, 
                            width=width, 
                            label=genre, 
                            color=genre_color_map[genre])
                
            self.ax.set_title('Game Genre Distribution Across Platforms')
            self.ax.set_xticks(x + width * (len(genres) - 1) / 2)
            self.ax.set_xticklabels(pivot_df.index)
            self.ax.set_xlabel('Platform')
            self.ax.set_ylabel('Count')
            self.ax.legend(title='Genre', bbox_to_anchor=(1.05, 1))
            plt.tight_layout()
            plt.grid()
            
        except EmptyDataFrameError as e:
            logging.error(str(e))
            raise
        except Exception as e:
            logging.error("Error in creating the bar plot: %s", e)
        
    def save_image(self, plot_path: str) -> None:
        """
        Saves an image to the specified file

        Args:
            plot_path: Path to save the image
        """
        try:
            plt.savefig(plot_path)
            plt.close(self.fig)
            logging.info(f"Plot saved to {plot_path}")
        except FileNotFoundError as e:
            logging.error("Path to save the image is incorrect: %s", e)  
            raise e      




from unittest import TestCase, mock
from visualization import BarPlot, EmptyDataFrameError
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.axes._axes import Axes

class TestBarPlot(TestCase):
    """
    Unit tests for the BarPlot class, focusing on plot creation and image saving functionality
    """
    def setUp(self):
        self.bar_plot = BarPlot()
        
    def test_create_plot_success(self):
        """
        Tests successful creation of a bar plot from a valid DataFrame
        """
        df = pd.DataFrame({
            'Platform': ['PC', 'PlayStation'],
            'Genre': ['Action', 'Adventure'],
            'Count': [10, 20]
            })
        
        self.bar_plot.create_plot(df)

        self.assertIsInstance(self.bar_plot.fig, Figure, "Figure was not created")
        self.assertIsInstance(self.bar_plot.ax, Axes, "Axis was not created")

        self.assertEqual(self.bar_plot.ax.get_title(), "Game Genre Distribution Across Platforms")
        self.assertEqual(self.bar_plot.ax.get_xlabel(), "Platform")
        self.assertEqual(self.bar_plot.ax.get_ylabel(), "Count")
    
    def test_create_plot_failure(self):
        """
        Tests handling of empty DataFrame input when creating a plot
        """
        df = pd.DataFrame({})

        with self.assertLogs(level='ERROR') as log:
            with self.assertRaises(EmptyDataFrameError):
                self.bar_plot.create_plot(df)
            self.assertIn("The provided DataFrame is empty and cannot be used to create a plot", log.output[0])


    @mock.patch('matplotlib.pyplot.savefig')
    def test_save_image(self, mock_savefig: mock.Mock):
        """
        Tests successful saving of a plot image by mocking 'matplotlib.pyplot.savefig'
        """
        df = pd.DataFrame({
            'Platform': ['PC', 'PlayStation'],
            'Genre': ['Action', 'Adventure'],
            'Count': [10, 20]
            })
        plot_path = "test/path.png"

        self.bar_plot.create_plot(df)
        self.bar_plot.save_image(plot_path)
        
        mock_savefig.assert_called_once_with(plot_path)

    @mock.patch('matplotlib.pyplot.savefig')
    def test_save_image_failure(self, mock_savefig: mock.Mock):
        """
        Tests handling of invalid file path when saving plot image by mocking 'matplotlib.pyplot.savefig'
        """
        df = pd.DataFrame({
            'Platform': ['PC', 'PlayStation'],
            'Genre': ['Action', 'Adventure'],
            'Count': [10, 20]
            })
        plot_path = "invalid/path.png"

        mock_savefig.side_effect = FileNotFoundError()
        self.bar_plot.create_plot(df)

        with self.assertLogs(level='ERROR') as log:
            with self.assertRaises(FileNotFoundError):
                self.bar_plot.save_image(plot_path)
            self.assertIn("Path to save the image is incorrect", log.output[0])

from configuration.config import BaseConfig as config
from lessons.extract.load_data import Loader
from lessons.transform.transform_data import Transform
from lessons.visualize.visualization import BarPlot
import logging

logging.basicConfig(level="INFO", format="%(message)s")

if __name__ == "__main__":
    """
    Executes whole process:
    1. Data Download
    2. Data Saving
    3. Data Ingesting
    4. Data Cleaning
    5. Data Visualization
    6. Image Saving
    """
    loader = Loader(config.DATA_URL, config.DATA_PATH)
    response = loader.download_file()
    loader.save_file(response)
    df = loader.ingest_data()

    transform = Transform(df, config.FEATURES, config.CLASSES)
    df = transform.clean_data()
    df = transform.group_and_count()
    df = transform.sort_data()
    
    bar_plot = BarPlot()
    bar_plot.create_plot(df)
    bar_plot.save_image(config.GRAPH_PATH)
import os
from attrs import define

@define
class BaseConfig:
    """
    Class storing base parameters
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data/dataset.csv")
    DATA_URL = "https://drive.usercontent.google.com/download?id=1Cw2wO3lHHJ13B1w4p-FgX1SHVtlUtfga&export=download&authuser=0&confirm=t&uuid=9a6e08b8-8a24-43b3-9713-02140da60817&at=AN_67v0A06kVxvTX977sTQolmtrD:1729850216110"
    FEATURES = ['platform', 'genre']
    CLASSES = {"platform": ["PS4", "XOne", "PC", "WiiU"]}
    GRAPH_PATH = os.path.join(BASE_DIR, "data/graphs/graph.png")
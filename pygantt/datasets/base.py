import os
import pandas as pd

def load_concert():
    """Loads concert data.
    """
    module_path = os.path.dirname(__file__)

    return pd.read_csv(os.path.join(module_path, 'data','concert.csv'))

import os
import pandas as pd

def load_concert():
    """Loads concert data.
    """
    module_path = os.path.dirname(__file__)

    return pd.read_csv(os.path.join(module_path, 'data','concert.csv'), parse_dates=['Start','Finish'])

def load_equities():
    """Loads equities positions data.
    """
    module_path = os.path.dirname(__file__)

    return pd.read_csv(os.path.join(module_path, 'data','equities.csv'), parse_dates=['Start','Finish'])

def load_equities_ptf():
    """Loads equities portfolio price series.
    """
    module_path = os.path.dirname(__file__)

    return pd.read_csv(os.path.join(module_path, 'data','equities_ptf.csv'), parse_dates=['Date'])

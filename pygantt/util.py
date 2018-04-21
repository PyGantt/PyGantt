# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from functools import reduce



def get_starts(arr):
    bounded = np.hstack(([0], arr, [0]))
    diffs = np.diff(bounded)
    starts, = np.where(diffs)
    return starts

def with_full_nans(arr):
    arr = arr.copy()
    arr[np.isnan(arr)] = 0
    return arr

def get_all_starts(arr):
    normal_starts = get_starts(with_full_nans(arr))
    nan_starts = get_starts(np.isnan(arr))
    return np.union1d(normal_starts, nan_starts)


def binary_encode_pd_series(series):
#     this is giving end exclusive, which seems fair
    all_starts = get_all_starts(series.values)
    starts = all_starts[:-1]
    #     the final value of end will not exist in the original series
    ends = all_starts[1:]
    return starts, ends

def series_to_gantt_format(series, index, starts_ends):
    categories = series.iloc[starts_ends[0]]
    starts = index.iloc[starts_ends[0]]
    ends = index.iloc[starts_ends[1]]
    #ends = pd.concat([index.iloc[starts_ends[1][:-1]], pd.Series([np.NaN])])
    name = series.name
    return pd.DataFrame({
       "Task": [name] * len(starts),
       "Type": categories.values,
       "Starts": starts.values,
       "Ends": ends.values})

 
def transform_df_to_start_end(df, index_col=None):
    '''
    Transform DataFrames to start end.
    '''
    index_col_name = index_col
    if index_col is None:
        index_col = df.index.to_series()
    elif isinstance(index_col, str):
        index_col = df[index_col]
    elif isinstance(index_col, pd.Series):
        index_col_name = index_col.name
    else:
        raise
    starts_ends = {}
    for col in df.columns.difference([index_col_name]):
        starts_ends[col] = binary_encode_pd_series(df[col])
    gantt_dfs = []
    for col in starts_ends:
        gantt_df = series_to_gantt_format(df[col], index_col, starts_ends[col])
        gantt_dfs.append(gantt_df)
    return pd.concat(gantt_dfs)

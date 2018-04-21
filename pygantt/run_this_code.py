import pandas as pd
from datetime import datetime

msft = np.array([0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0])
fb = np.array([0, 0, -1, -1, -1, 0, 0, 1, 1, 1, 0])
appl = np.array([1, 0, 0, -1, -1, 0, 0, 0, 1, 1, 0])
goog = np.array([1, 0, 0, -1, -1, 0, 0, 0, 1, 1, 0])
example_to_encode = pd.DataFrame({
   "MSFT": msft,
   "APPL": appl,
   "FB": fb,
   "GOOG": goog})


example_to_encode_idx = example_to_encode.set_index(pd.date_range(datetime(2017,1,1), periods=len(example_to_encode)))


df = transform_df_to_start_end(example_to_encode_idx)

gantt(df.Task, df.Starts, df.Ends, task_type=df.Type)

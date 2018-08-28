import pandas as pd
import numpy as np
import math
from fastparquet import write

def proc_radon(df_radon):
    data = df_radon[df_radon.state=='MN']

    data = data.loc[:,['county','activity','floor']]

    data['log_radon'] = data.activity.apply(lambda x: float(x.strip()))
    
    data['log_radon'] = data['log_radon'].apply(lambda x: math.log(x) if x>0. else np.nan)
    
    data = data.loc[:,['county','log_radon','floor']]
    
    repo_path='.'
    radon_path = repo_path+'/data/processed/radon_proc.parq'
    write(radon_path,data)
    
    print('Processed Radon data saved to parquet file')
    
    return data
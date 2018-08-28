import pandas as pd
import urllib
from fastparquet import write


def get_load_radon_dat(refresh_radon_data_flag):
    repo_path='.'
    radon_path = repo_path+'/data/raw/radon_raw.parq'
    if refresh_radon_data_flag==True:
        data_url = 'http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs2.dat'
        resp = urllib.request.urlopen(data_url).read()
        data = str(resp).split('\\n')
        data = [nstr.split(',') for nstr in data]
        df_data = pd.DataFrame(data[1:])
        df_data.columns=['idnum', 'state', 'state2', 'stfips', 'zip', 'region',
                            ' typebldg', 'floor', 'room', 'basement', 'windoor', 'rep',
                            'stratum', 'wave', 'starttm', 'stoptm', 'startdt', 'stopdt',
                            'activity', 'pcterr', 'adjwt', 'dupflag', 'zipflag', 'cntyfips','county']
        df_data.county = df_data.county.apply(lambda x: str(x).replace('\\r','').strip())
        
        write(radon_path,df_data)
        print('Raw Data saved to parquet file')
    
    df_radon = pd.read_parquet(radon_path,engine='fastparquet')
    
    return df_radon 
    
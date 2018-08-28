import pandas as pd
import urllib
from fastparquet import write
import os


def get_load_radon_dat():
    repo_path='.'
    radon_path = repo_path+'/data/radon.parq'
    data_url = 'http://www.stat.columbia.edu/~gelman/arm/examples/radon/srrs2.dat'
    resp = urllib.request.urlopen(data_url).read()
    data = str(resp).split('\\n')
    data = [nstr.split(',') for nstr in data]
    df_data = pd.DataFrame(data[1:])
    df_data.columns=['idnum', ' state', ' state2', ' stfips', ' zip', ' region',
						' typebldg', ' floor', ' room', ' basement', ' windoor', ' rep',
						' stratum', ' wave', ' starttm', ' stoptm', ' startdt', ' stopdt',
						' activity', ' pcterr', ' adjwt', ' dupflag', ' zipflag', ' cntyfips',' county']
    write(radon_path,df_data)
    print('Data saved to parquet file')
    
    
    
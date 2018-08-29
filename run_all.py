import warnings
warnings.filterwarnings("ignore")

### load cfg file
from src import cfg


### Refresh Radon data if flag==True, otherwise load from saved parquet file
from src.etl.get_load_radon_dat import get_load_radon_dat as glrd

df_radon = glrd(cfg.refresh_radon_data_flag)

### Process Radon data 
from src.etl.proc_radon import proc_radon

data =  proc_radon(df_radon)

### Run pymc3 hier regression
from src.models.models_pymc3 import hier_reg as hr

time_del = hr.run_hier_reg(data, cfg.sample_size, cfg.njobs)

print('Time Delta for Hierarchical Regression Using pymc3 is %s seconds' %(time_del))

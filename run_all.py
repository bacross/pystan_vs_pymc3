import warnings
warnings.filterwarnings("ignore")

### load cfg file
from src import cfg

### Refresh Radon data if flag==True, otherwise load from saved parquet file
from src.etl.get_load_radon_dat import get_load_radon_dat as glrd

df_radon = glrd(cfg.refresh_radon_data_flag, cfg.radon_data_url)

### Process Radon data 
from src.etl.proc_radon import proc_radon

data =  proc_radon(df_radon)

### Run pymc3 hier regression
from src.models.models_pymc3 import hier_reg_pymc3 as hr_pymc3

time_del_pm = hr_pymc3.run_hier_reg(data, cfg.sample_size, cfg.njobs)

### Run pystan hier regression 
from src.models.models_pystan import hier_reg_pystan as hr_stan

time_del_stan = hr_stan.run_hier_reg(data, cfg.sample_size, 4, cfg.hier_stan_code)

print('Time Delta for Hierarchical Regression Using pymc3 is %s seconds' %(time_del_pm))
print('Time Delta for Hierarchical Regression Using pystan is %s seconds' %(time_del_stan))


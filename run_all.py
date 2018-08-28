### load cfg file
from src import cfg

### Refresh Radon data if flag==True, otherwise load from saved parquet file
from etl.get_load_radon_dat import get_load_radon_dat as glrd

df_radon = glrd(cfg.refresh_radon_data_flag)

### Process Radon data 



import numpy as np
import pandas as pd
import pystan as ps
import timeit

def run_hier_reg(ndata, sample_size, chains, hier_stan_code):
	start_time = timeit.default_timer()
	county_names = ndata.county.unique()
	counties = len(county_names)
	county_idx=pd.factorize(ndata.county)[0]
	county_lookup = dict(zip(county_names, range(counties)))
	county = ndata['county_code']=ndata.county.replace(county_lookup).values
	hier_data = {'N': len(ndata.log_radon),
				 'J': counties,
				 'county': county+1, #stan counts start at 1
				 'x': ndata.floor,
				 'y': ndata.log_radon}
	hier_fit = ps.stan(model_code=hier_stan_code, data=hier_data,
						iter=sample_size, chains=chains,n_jobs=chains)
	time_del = timeit.default_timer() - start_time
	return time_del

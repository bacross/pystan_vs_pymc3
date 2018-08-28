import numpy as np
import pandas as pd
import pymc3 as pm
import timeit

def run_hier_reg(ndata, sample_size, njobs):
	start_time = timeit.default_timer()
	with pm.Model() as hier_mod:
		# Hyperpriors
		mu_a = pm.Normal('mu_alpha', mu=0., sd=1)
		sigma_a = pm.HalfCauchy('sigma_alpha', beta=1)
		mu_b = pm.Normal('mu_beta', mu=0., sd=1)
		sigma_b = pm.HalfCauchy('sigma_beta', beta=1)
    
		# Intercept for each county, distributed around group mean mu_a
		a = pm.Normal('alpha', mu=mu_a, sd=sigma_a, shape=len(ndata.county.unique()))
		# Intercept for each county, distributed around group mean mu_a
		b = pm.Normal('beta', mu=mu_b, sd=sigma_b, shape=len(ndata.county.unique()))
    
		# Model error
		eps = pm.HalfCauchy('eps', beta=1)
    
		# Expected value
		radon_est = a[county_idx] + b[county_idx] * ndata.floor.values
    
		# Data likelihood
		y_like = pm.Normal('y_like', mu=radon_est, sd=eps, observed=ndata.log_radon)
		
		hier_trace = pm.sample(draws=sample_size, n_jobs=njobs)
	time_del = timeit.default_timer() - start_time
	return time_del
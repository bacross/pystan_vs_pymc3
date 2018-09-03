# pystan_vs_pymc3

This github repo was meant to primarily be a performance comparison between MCMC sampling implementations between pymc3 and pystan.  Additionally, it served as a learning tool as I tried to replicate the "classic" examples found most commonly online. The plan is to implement three different models: 1) Hierarchical Regression; 2) Switchpoints; and 3) Time-Series Model.  As of 20180902 only Hierarchical Regression is implemented.

## Getting Started

After cloning this repo, navigate to the repo location and set up the conda virtual environment referencing the "bayesvs.txt" file by:

~~~bash
source setup_env.bash
~~~

## Configuration File

The configuration file is a .py file that holds key model information and configuration parameters.  For the radon model, there is a flag on whether you want to download an updated radon file from Gelman's website: http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs2.dat

The configuration file also controls the number of iterations used in the MCMC samplers, the number of parallel jobs where applicable, as well as the stan model code.





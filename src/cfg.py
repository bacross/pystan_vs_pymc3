refresh_radon_data_flag=True

radon_data_url = 'http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs2.dat'

sample_size=1000

njobs = 4

hier_stan_code = """
    data {
        int<lower=0> J;
        int<lower=0> N;
        int county[N];
        vector[N] x;
        vector[N] y;
    }
    parameters {
        vector[J] a;
        vector[J] b;
        real mu_a;
        real<lower=0> sigma_a;
        real mu_b;
        real<lower=0> sigma_b;
        real<lower=0> sigma_y;
    }

    model {
        mu_a ~ normal (0,1);
        sigma_a ~ cauchy(0,1);
        a ~ normal (mu_a, sigma_a);
        
        mu_b ~ normal(0,1);
        sigma_b ~ cauchy(0,1);
        b ~ normal (mu_b, sigma_b);
        
        sigma_y ~ cauchy(0,1);
        y ~ normal(a[county] + b[county].*x, sigma_y);
    }
    """

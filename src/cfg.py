refresh_radon_data_flag=True

sample_size=1000

njobs = 4

hier_stan_code = """
	data {
		int<lower=0> J;
		int<lower=1,upper=J> county[N];
		vector[N] x;
		vector[N] y;
	}
	parameters {
		vector[J] a;
		vector[J] b;
		real mu_a;
		real sigma_a;
		real mu_b;
		real sigma_b;
		real sigma_y;
	}
	transformed parameters {
		
		vector[N] y_hat;
		
		for (i in 1:N)
			y_hat[i] <- a[county[i]] + x[i]*b[county[i]];
	}
	model {
		mu_a ~ normal (0,1);
		sigma_a ~ cauchy(0,1);
		a ~ normal (mu_a, sigma_a);
		
		mu_b ~ normal(0,1);
		sigma_b ~ cauchy(0,1);
		b ~ normal (mu_b, sigma_b);
		
		sigma_y ~ cauchy(0,1);
		y ~ normal(y_hat, sigma_y);
	}
	"""
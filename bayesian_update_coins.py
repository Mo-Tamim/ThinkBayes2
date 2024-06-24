import numpy as np

# Define the prior probabilities
prior_fair = 0.6
prior_biased = 0.4

# Define the likelihoods
likelihood_fair = 0.5  # P(Heads | Fair) = 0.5
likelihood_biased = 0.9  # P(Heads | Biased) = 0.9

# Assume we observe 3 heads in a row
observations = [1, 1, 1]  # 1 represents heads, 0 represents tails

# Calculate the posterior probability for each hypothesis
for observation in observations:
    # Update the likelihood for the observation
    if observation == 1:  # Heads
        likelihood_fair *= 0.5
        likelihood_biased *= 0.9
    else:  # Tails (not used in this example)
        likelihood_fair *= 0.5
        likelihood_biased *= 0.1
    
    # Calculate the evidence (normalizing constant)
    evidence = (likelihood_fair * prior_fair) + (likelihood_biased * prior_biased)
    
    # Update the posteriors
    posterior_fair = (likelihood_fair * prior_fair) / evidence
    posterior_biased = (likelihood_biased * prior_biased) / evidence
    
    # Update priors for the next iteration
    prior_fair = posterior_fair
    prior_biased = posterior_biased

# Print the final posterior probabilities
print(f"Posterior probability of the coin being fair: {posterior_fair:.4f}")
print(f"Posterior probability of the coin being biased: {posterior_biased:.4f}")

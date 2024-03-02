import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t

st.title('Sampling Distribution Experiments')

# Experiment 1: Free Throw Shooting
st.header('Experiment 1: Free Throw Shooting')
population_size = 100000
p = 0.82  # Success probability
population_proportion = np.random.binomial(1, p, population_size)

sample_size = st.number_input('Enter sample size for free throws:', min_value=1, value=1000)
number_of_samples = st.number_input('Enter number of samples for free throws:', min_value=1, value=1000)

if st.button('Generate Sampling Distribution for Free Throws'):
    sample_proportions = [np.mean(np.random.choice(population_proportion, sample_size)) for _ in range(number_of_samples)]
    plt.hist(sample_proportions, bins=30, density=True, alpha=0.6, color='g')
    plt.title('Sampling Distribution of Sample Proportions for Free Throws')
    plt.xlabel('Sample Proportion')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# Confidence Interval for Free Throws
if number_of_samples == 1:
    confidence_level = st.slider('Confidence Level for Free Throws:', 0.0, 100.0, 95.0)
    z_score = norm.ppf(1 - (1 - (confidence_level / 100)) / 2)
    margin_of_error = z_score * np.sqrt((sample_proportions[0] * (1 - sample_proportions[0])) / sample_size)
    lower_bound = sample_proportions[0] - margin_of_error
    upper_bound = sample_proportions[0] + margin_of_error
    st.write(f'{confidence_level}% confidence interval for the proportion is ({lower_bound}, {upper_bound})')

# Experiment 2: Average Heights
st.header('Experiment 2: Average Heights')
mean_height = 1.72  # Average height
std_dev = 0.2  # Standard deviation
population_heights = np.random.normal(mean_height, std_dev, population_size)

sample_size_heights = st.number_input('Enter sample size for heights:', min_value=1, value=1000)
number_of_samples_heights = st.number_input('Enter number of samples for heights:', min_value=1, value=1000)

if st.button('Generate Sampling Distribution for Heights'):
    sample_means_heights = [np.mean(np.random.choice(population_heights, sample_size_heights)) for _ in range(number_of_samples_heights)]
    plt.hist(sample_means_heights, bins=30, density=True, alpha=0.6, color='b')
    plt.title('Sampling Distribution of Sample Means for Heights')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# Confidence Interval for Heights
if number_of_samples_heights == 1:
    confidence_level_heights = st.slider('Confidence Level for Heights:', 0.0, 100.0, 95.0)
    t_score = t.ppf(1 - (1 - (confidence_level_heights / 100)) / 2, df=sample_size_heights-1)
    margin_of_error_heights = t_score * (np.std(sample_means_heights, ddof=1) / np.sqrt(sample_size_heights))
    lower_bound_heights = np.mean(sample_means_heights) - margin_of_error_heights
    upper_bound_heights = np.mean(sample_means_heights) + margin_of_error_heights
    st.write(f'{confidence_level_heights}% confidence interval for the mean height is ({lower_bound_heights}, {upper_bound_heights})')

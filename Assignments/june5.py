#1

import numpy as np
from scipy import stats

# Generate sample dataset
np.random.seed(42)  # for reproducibility
sample_size = 30
mean = 50
std_dev = 5
sample_data = np.random.normal(mean, std_dev, sample_size)

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample_data, 50)

# Print results
print("Sample Mean:", np.mean(sample_data))
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Null hypothesis rejected. Sample mean is significantly different from 50.")
else:
    print("Null hypothesis cannot be rejected. Sample mean is not significantly different from 50.")


#2

import numpy as np
from scipy import stats

# Generate sample dataset
np.random.seed(42)  # for reproducibility
sample_size = 30
pop_mean = 60
pop_std_dev = 10
sample_data = np.random.normal(pop_mean, pop_std_dev, sample_size)

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample_data, 50)

# Print results
print("Sample Mean:", np.mean(sample_data))
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Null hypothesis rejected. Sample mean is significantly different from 50.")
else:
    print("Null hypothesis cannot be rejected. Sample mean is not significantly different from 50.")


#3

import numpy as np
from scipy import stats

# Generate sample datasets
np.random.seed(42)  # for reproducibility
sample_size = 25
mean1 = 55
mean2 = 60
std_dev = 8
sample_data1 = np.random.normal(mean1, std_dev, sample_size)
sample_data2 = np.random.normal(mean2, std_dev, sample_size)

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(sample_data1, sample_data2)

# Print results
print("Sample Mean 1:", np.mean(sample_data1))
print("Sample Mean 2:", np.mean(sample_data2))
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Null hypothesis rejected. Means of the two samples are significantly different.")
else:
    print("Null hypothesis cannot be rejected. Means of the two samples are not significantly different.")


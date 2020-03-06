import matplotlib as plt
import math

offset = 0
avg_sample_val = 0
mode = 0
median = 0

x = [17.1, 21.4, 15.9, 19.1, 22.4, 20.7, 17.9, 18.6, 21.8, 16.1, 19.1, 20.5, 14.2, 16.9, 17.8, 18.1, 19.1, 15.8, 18.8, 17.2, 16.2, 17.3, 22.5, 19.9, 21.1, 15.1, 17.7, 19.8, 14.9, 20.5, 17.5, 19.2, 18.5, 15.7, 14.0, 18.6, 21.2, 16.8, 19.3, 17.8, 18.8, 14.3,
     17.1, 19.5, 16.3, 20.3, 17.9, 23.0, 17.2, 15.2, 15.6, 17.4, 21.3, 22.1, 20.1, 14.5, 19.3, 18.4, 16.7, 18.2, 16.4, 18.7, 14.3, 18.2, 19.1, 15.3, 21.5, 17.2, 22.6, 20.4, 22.8, 17.5, 20.2, 15.5, 21.6, 18.1, 20.5, 14.0, 18.9, 16.5, 20.8, 16.6, 18.3, 21.7]

data_len = len(x)
x.sort()


def find_median(dataset):
    dataset_len = len(dataset)
    if len(dataset) % 2 == 0:
        mid = (dataset[dataset_len // 2] + dataset[dataset_len // 2 + 1]) / 2
    else:
        mid = dataset[dataset_len // 2]
    return mid


median = find_median(x)
first_q = len(x) // 4
third_q = 3 * len(x) // 4

if data_len % 2 == 0:
    lowerQ = find_median(x[:first_q])
    upperQ = find_median(x[third_q:])
else:
    lowerQ = find_median(x[:first_q])
    upperQ = find_median(x[third_q + 1:])

d = dict.fromkeys(x, 0)

for elem in x:
    avg_sample_val += elem
    d[elem] += 1

avg_sample_val /= data_len

for elem in d:
    if d[elem] > mode:
        mode = d[elem]
    offset += d[elem] / data_len
    d[elem] = round(offset, 3)

#plt.boxplot(x)
#plt.hist(x, bins=10)
#plt.show()
# https://habr.com/ru/post/267123/

square_diff = sum((elem - avg_sample_val) ** 2 for elem in x)
sample_variance = square_diff / data_len
standard_error = sample_variance ** (1 / 2)
standard_deviation = (square_diff / (data_len - 1)) ** (1 / 2)
kurtosis = (sum((elem - avg_sample_val)**4 for elem in x) /
            data_len) / (standard_deviation ** 4) - 3
skewness = (sum((elem - avg_sample_val)**3 for elem in x) /
            data_len) / (standard_deviation ** 3)

print('Average sample value = ', round(avg_sample_val, 3))
print('Sample variance = ', sample_variance)
print('Standard error = ', standard_error)
print('Mode = ', mode)
print('Median = ', median)
print('Quartiles: ', lowerQ, median, upperQ)
print('Standard Deviation = ', standard_deviation)
print('Kurtosis = ', kurtosis)
print('Skewness = ', skewness)
print('Min value = ', x[0])
print('Max value = ', x[len(x) - 1])

# Maxim B #



print(avg_sample_val); # выборочное среднее

sum_x_minus_x_delta = 0

for elem in x:
    sum_x_minus_x_delta += (elem - avg_sample_val) ** 2

dispersion = sum_x_minus_x_delta * (1/(len(x)-1)) 
dispersion = math.sqrt(dispersion)

print(dispersion) # выборочная исправленная дисперсия


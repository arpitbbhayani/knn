__author__ = 'arpit'

import math


def mean(values):
    total_sum = 0.0
    for i in values:
        total_sum += float(i)
    return round(total_sum/len(values), 5)


def variance(values):
    mu = mean(values)
    total_sum = 0.0
    for i in values:
        total_sum += math.pow(abs(i-mu), 2)
    return round(total_sum/len(values), 5)


def standard_deviation(values):
    return round(math.sqrt(variance(values)), 5)
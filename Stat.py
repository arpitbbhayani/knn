__author__ = 'arpit'

import math


def mean(values):
    total_sum = 0.0
    for i in values:
        total_sum += float(i)
    return total_sum/len(values)


def variance(values):
    mu = mean(values)
    total_sum = 0.0
    for i in values:
        total_sum += math.pow(abs(i-mu), 2)
    return total_sum/len(values)


def standard_deviation(values):
    return math.sqrt(variance(values))
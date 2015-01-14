__author__ = 'arpit'

import math


class Datatypes():
    DISCRETE = 'discrete'
    CONTINUOUS = 'continuous'


def euclidean(column_map, data1, data2):
    """
    Calculates the euclidean distance
    between data1 and data2 using metadata
    map pased from the CSV metadata file.

    For Iris Dataset:
    column_map : {
                    'sepal length in cm': 'continous',
                    'sepal width in cm': 'continous',
                    'petal length in cm': 'continous',
                    'petal width in cm': 'continous',
                    'class': 'discrete'
                }
    data1 :     {
                    'sepal length in cm': 5.1,
                    'sepal width in cm': 3.5,
                    'petal length in cm': 1.4,
                    'petal width in cm': 0.2,
                    'class': 'Iris-setosa'
                }
    similar will be data2
    """
    distance_sum = 0.0
    for key in data1.keys():
        xi = data1[key]
        yi = data2[key]

        if column_map[key] == Datatypes.CONTINUOUS:
            distance_sum += ((float(xi) - float(yi))**2)
        elif column_map[key] == Datatypes.DISCRETE:
            pass
        else:
            print 'Datatype missmatch'
    return round(math.sqrt(distance_sum), 5)
__author__ = 'arpit'

import csv

def knn(file_path, on_attributes, column_map, column_list, distance_function):
    distance_function
    print 'parse'

"""
    Accepts the CSV meta file
    <attribute_name>,<attribute_type>
    attribute_type can take values from
    Globals.Datatypes
        1. CONTINOUS
        2. DISCRETE
    The function returns a list containing meta information
"""
def parse_meta(file_path):
    column_list = []
    column_map = {}
    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            column_map[row[0]] = row[1]
            column_list.append(row[0])
    return column_list, column_map
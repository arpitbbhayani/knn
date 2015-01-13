__author__ = 'arpit'

import csv


def knn(file_path, on_attributes, column_map, column_list, distance_function):
    """
    The actual algorithmic implementation of KNN-Classification
    :param file_path:
    :param on_attributes:
    :param column_map:
    :param column_list:
    :param distance_function:
    :return:
    """
    column_name_to_number = {}
    csv_data = []

    index = 0
    for column_name in column_list:
        column_name_to_number[column_name] = index
        index += 1

    included_cols = list(value for key, value in column_name_to_number.iteritems() if key in on_attributes)

    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if len(row) > 0:
                temp_list = dict((column_list[i], row[i]) for i in included_cols)
                csv_data.append(temp_list)

    """print csv_data"""

    distance_function(column_map, csv_data[0], csv_data[1])


def parse_meta(file_path):
    """
    Accepts the CSV meta file
    <attribute_name>,<attribute_type>
    attribute_type can take values from
    Globals.Datatypes
        1. CONTINUOUS
        2. DISCRETE
    The function returns a list containing meta information
    """
    column_list = []
    column_map = {}
    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            column_map[row[0]] = row[1]
            column_list.append(row[0])
    return column_list, column_map
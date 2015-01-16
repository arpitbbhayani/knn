__author__ = 'arpit'

import csv
import random
import Queue


def knn_classify(file_path, meta_file_path, on_attributes, class_column_name, distance_function):
    """
    :param file_path: File path to the actual csv data that needs to be classified
    :param meta_file_path: File path to the meta data fle of the dataset
    :param on_attributes: List of attributes (column_names) using which classification is to be done
    :param class_column_name: The column that needs to be classified
    :param distance_function: The distance function that needs to be applied
    :return:
    """
    summary = {}
    column_list, column_map = parse_meta(meta_file_path)
    column_name_to_number = {}
    csv_data = []
    list_classes = set()

    index = 0
    for column_name in column_list:
        column_name_to_number[column_name] = index
        index += 1

    included_cols = list(value for key, value in column_name_to_number.iteritems() if key in on_attributes)
    class_column_number = column_name_to_number[class_column_name]

    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if len(row) > 0:
                temp_list = dict((column_list[i], row[i]) for i in included_cols)
                temp_list[class_column_name] = row[class_column_number]
                list_classes.add(row[class_column_number])
                csv_data.append(temp_list)

    n = len(csv_data)

    aggregated_confusion_matrix = {}
    for i in list_classes:
        aggregated_confusion_matrix[i] = {}
        for j in list_classes:
            aggregated_confusion_matrix[i][j] = 0

    for i in range(10):
        """ Shuffle the dataset """
        random.shuffle(csv_data)

        training_dataset = csv_data[0:n/2]
        test_dataset = csv_data[n/2:]
        confusion_matrix = knn(training_dataset, test_dataset, distance_function, list_classes, class_column_name,
                               column_map, 1)
        summary[i] = get_statistics_for_dataset(training_dataset, class_column_name, confusion_matrix)
        aggregate(aggregated_confusion_matrix, confusion_matrix)

    summary['aggregated_confusion_matrix'] = aggregated_confusion_matrix
    summary['training_dataset'] = training_dataset
    summary['test_dataset'] = test_dataset
    summary['class_column_name'] = class_column_name
    return summary


def get_statistics_for_dataset(dataset, class_column_name, confusion_matrix):
    stat_data = {}
    number_of_datapoints = len(dataset)
    class_stat = {}
    freq = {}
    for i in dataset:
        freq[i[class_column_name]] = freq.get(i[class_column_name], 0) + 1
    class_stat['freq'] = freq

    sum_data = 0.0
    for i in confusion_matrix.keys():
        sum_data += confusion_matrix[i][i]
    class_stat['accuracy'] = sum_data/number_of_datapoints
    stat_data['number_of_datapoints'] = number_of_datapoints
    stat_data['number_of_classes'] = len(freq.keys())
    stat_data['class_stat'] = class_stat
    return stat_data


def aggregate(aggregated_confusion_matrix, confusion_matrix):
    for i in aggregated_confusion_matrix.keys():
        for j in aggregated_confusion_matrix.keys():
            aggregated_confusion_matrix[i][j] += confusion_matrix[i][j]


def knn(training_dataset, test_dataset, distance_function, list_classes, class_column_name, column_map, K):
    confusion_matrix = {}

    for i in list_classes:
        confusion_matrix[i] = {}
        for j in list_classes:
            confusion_matrix[i][j] = 0

    for row_test in test_dataset:
        k = K
        actual_class = row_test[class_column_name]
        q = Queue.PriorityQueue()
        for row_training in training_dataset:
            d = distance_function(column_map, row_test, row_training)
            q.put((d, row_training))

        list_probables = []
        last_dist = None
        if not q.empty():
            t = q.get()
            list_probables.append(t)
            last_dist = t[0]

        while not q.empty():
            t = q.get()
            if t[0] != last_dist:
                last_dist = t[0]
                k -= 1
            if k <= 0:
                break
            list_probables.append(t)

        if len(list_probables) == 1:
            predicted_class = list_probables[0][1][class_column_name]
        else:
            """predicted_class = list_probables[0][1][class_column_name]"""
            freq = {}
            for i in list_probables:
                freq[i[1][class_column_name]] = freq.get(i[1][class_column_name], 0) + 1
            predicted_class = max(freq, key=freq.get)
        confusion_matrix[predicted_class][actual_class] += 1

    return confusion_matrix


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
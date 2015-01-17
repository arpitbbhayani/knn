__author__ = 'arpit'

import Stat
import utils
import Globals
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


""" Specific to Breast Cancer Dataset
column_list, column_map = utils.parse_meta("/home/arpit/Downloads/bc.meta")
result = utils.knn_classify(
    "/home/arpit/Downloads/bc.data",
    "/home/arpit/Downloads/bc.meta",
    ['Mitoses', 'Bare Nuclei', 'Uniformity of Cell Shape'],
    'class',
    Globals.euclidean
)
data = result['aggregated_confusion_matrix']
list_accuracy = list(result[i]['class_stat']['accuracy'] for i in range(10))


print 'Number of instances : ', result['number_instance']
print 'Number of Features : ', len(result['column_list']) - 1
print 'Classes : ', result['list_classes']
print 'Confusion Matrix for the dataset over 10 runs :'
for i in data.keys():
    print i, ' ',
    for j in data.keys():
        print data[i][j], ' ',
    print ''

print 'Accuracy for 10 runs: ', list_accuracy
print 'Mean Accuracy : ', Stat.mean(list_accuracy)
print 'Variance : ', Stat.variance(list_accuracy)
print 'Standard Deviation : ', Stat.standard_deviation(list_accuracy)
"""


""" Specific to Wine Dataset
column_list, column_map = utils.parse_meta("/home/arpit/Downloads/wine.meta")
result = utils.knn_classify(
    "/home/arpit/Downloads/wine.data",
    "/home/arpit/Downloads/wine.meta",
    ['Alcohol', 'Ash', 'Malic acid', 'Flavanoids'],
    'class',
    Globals.euclidean
)
data = result['aggregated_confusion_matrix']
list_accuracy = list(result[i]['class_stat']['accuracy'] for i in range(10))


print 'Number of instances : ', result['number_instance']
print 'Number of Features : ', len(result['column_list']) - 1
print 'Classes : ', result['list_classes']
print 'Confusion Matrix for the dataset over 10 runs :'
for i in data.keys():
    print i, ' ',
    for j in data.keys():
        print data[i][j], ' ',
    print ''

print 'Accuracy for 10 runs: ', list_accuracy
print 'Mean Accuracy : ', Stat.mean(list_accuracy)
print 'Variance : ', Stat.variance(list_accuracy)
print 'Standard Deviation : ', Stat.standard_deviation(list_accuracy)

"""








""" Specific to Iris Dataset """
column_list, column_map = utils.parse_meta("/home/arpit/Downloads/iris.meta")
result = utils.knn_classify(
    "/home/arpit/Downloads/iris.data",
    "/home/arpit/Downloads/iris.meta",
    ['sepal width in cm', 'petal width in cm'],
    'class',
    Globals.euclidean
)
data = result['aggregated_confusion_matrix']
list_accuracy = list(result[i]['class_stat']['accuracy'] for i in range(10))


print 'Number of instances : ', result['number_instance']
print 'Number of Features : ', len(result['column_list']) - 1
print 'Classes : ', result['list_classes']
print 'Confusion Matrix for the dataset over 10 runs :'
for i in data.keys():
    print i, ' ',
    for j in data.keys():
        print data[i][j], ' ',
    print ''

print 'Accuracy for 10 runs: ', list_accuracy
print 'Mean Accuracy : ', Stat.mean(list_accuracy)
print 'Variance : ', Stat.variance(list_accuracy)
print 'Standard Deviation : ', Stat.standard_deviation(list_accuracy)

plt.xlabel('sepal width in cm')
plt.ylabel('petal width in cm')

x, y, class_column_name = 'sepal width in cm', 'petal width in cm', result['class_column_name']
new_train_list = sorted(result['training_dataset'], key=lambda k: (float(k[y]), float(k[x])), reverse=True)
new_test_list = sorted(result['test_dataset'], key=lambda k: (float(k[y]), float(k[x])), reverse=True)

plt.axis([0, 5, 0, 3])

for i in new_train_list:
    if i[class_column_name] == 'Iris-setosa':
        ro, = plt.plot(i[x], i[y], 'ro')
    elif i[class_column_name] == 'Iris-virginica':
        bo, = plt.plot(i[x], i[y], 'bo')
    else:
        go, = plt.plot(i[x], i[y], 'go')

for i in new_test_list:
    if i[class_column_name] == 'Iris-setosa':
        rc, = plt.plot(i[x], i[y], 'r^')
    elif i[class_column_name] == 'Iris-virginica':
        bc, = plt.plot(i[x], i[y], 'b^')
    else:
        gc, = plt.plot(i[x], i[y], 'g^')


fontP = FontProperties()
fontP.set_size('small')

plt.legend([ro, bo, go, rc, bc, gc],
           [
               'Iris-setosa (training)', 'Iris-virginica(training)', 'Iris-versicolor(training)',
               'Iris-setosa (test)', 'Iris-virginica(test)', 'Iris-versicolor(test)'
           ], prop=fontP)

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

""" Decision Boundary """

print result['training_dataset'][0]

i,j = 0, 0
while i < 5:
    last_class = None
    j = 0
    while j < 3:
        c = utils.get_predicted_class(result['training_dataset'],
                                  {'sepal width in cm': round(i,2), 'class': 'Iris-versicolor', 'petal width in cm': round(j,2)},
                                  Globals.euclidean, class_column_name, column_map, 1)

        if last_class is None or c != last_class:
            last_class = c
            plt.plot(i, j, 'r.')
        j += 0.1
    i += 0.1

plt.show()

__author__ = 'arpit'

import Stat
import utils
import Globals
import matplotlib.pyplot as plt

""" Specific to Iris Dataset """
column_list, column_map = utils.parse_meta("/home/arpit/Downloads/iris.meta.txt")
result = utils.knn_classify(
    "/home/arpit/Downloads/iris.data.txt",
    "/home/arpit/Downloads/iris.meta.txt",
    ['sepal width in cm', 'petal width in cm'],
    'class',
    Globals.euclidean
)
data = result['aggregated_confusion_matrix']
list_accuracy = list(result[i]['class_stat']['accuracy'] for i in range(10))
print list_accuracy
print 'Mean Accuracy : ', Stat.mean(list_accuracy)
print 'Variance : ', Stat.variance(list_accuracy)
print 'Standard Deviation : ', Stat.standard_deviation(list_accuracy)

plt.xlabel('sepal width in cm')
plt.ylabel('petal width in cm')
""" To be used for decision boundary plt.plot([1,2,3,4], [1,4,9,16]) """

x, y, class_column_name = 'sepal width in cm', 'petal width in cm', result['class_column_name']
new_train_list = sorted(result['training_dataset'], key=lambda k: (float(k[y]), float(k[x])), reverse=True)
new_test_list = sorted(result['test_dataset'], key=lambda k: (float(k[y]), float(k[x])), reverse=True)

plt.axis([0, 5, 0, 3])

for i in new_train_list:
    if i[class_column_name] == 'Iris-setosa':
        plt.plot(i[x], i[y], 'ro')
    elif i[class_column_name] == 'Iris-virginica':
        plt.plot(i[x], i[y], 'bo')
    else:
        plt.plot(i[x], i[y], 'go')

for i in new_test_list:
    if i[class_column_name] == 'Iris-setosa':
        plt.plot(i[x], i[y], 'r^')
    elif i[class_column_name] == 'Iris-virginica':
        plt.plot(i[x], i[y], 'b^')
    else:
        plt.plot(i[x], i[y], 'g^')


plt.show()
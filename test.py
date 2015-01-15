__author__ = 'arpit'

import utils
import Globals

column_list, column_map = utils.parse_meta("/home/arpit/Downloads/iris.meta.txt")

result = utils.knn_classify(
    "/home/arpit/Downloads/iris.data.txt",
    "/home/arpit/Downloads/iris.meta.txt",
    ['sepal width in cm', 'petal width in cm'],
    'class',
    Globals.euclidean
)

print result

data = result['aggregated_confusion_matrix']

__author__ = 'arpit'

import utils
import Globals

column_list, column_map = utils.parse_meta("/home/arpit/Downloads/iris.meta.txt")

print utils.knn_classify(
    "/home/arpit/Downloads/iris.data.txt",
    "/home/arpit/Downloads/iris.meta.txt",
    ['sepal length in cm', 'petal length in cm'],
    'class',
    Globals.euclidean
)
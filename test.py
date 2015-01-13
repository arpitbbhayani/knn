__author__ = 'arpit'

import utils
import Globals

column_list, column_map = utils.parse_meta("/home/arpit/Downloads/iris.meta.txt")
print column_list
print column_map

utils.knn(" ", " ", " ", " ", Globals.euclidean())
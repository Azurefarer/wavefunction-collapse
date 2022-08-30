import numpy as np
import pygame as pg
import json
from PIL import Image

# min_entropy = 7


# a = [3, 2, 4, 5, 12, 2]
# b = [3, 2, 4, 5, 8, 7]
# c = [3, 2, 4]
# d = [3, 2, 4, 5, 12, 23, 2]
# e = [3, 2, 4, 5, 12, 6]
# f = [3, 2, 4]
# g = [3, 2, 4]
# h = [3, 2, 4, 5, 12]

# assets = (a, b, c, d, e, f, g, h)
# for i in range(len(assets)):

#     if len(assets[i]) < min_entropy:
#         min_entropy_coords = []
#         min_entropy = len(assets[i])
#         min_entropy_coords.append(i)
#     elif len(assets[i]) == min_entropy:
#         min_entropy_coords.append(i)


# print(min_entropy_coords)


# if not len(min_entropy_coords) == 1:
#     min_entropy_coords = [min_entropy_coords[np.random.randint(len(min_entropy_coords))]]


# print(min_entropy_coords[0])

a = ['tile_0_0', 'tile_0_1', ['tile_0_5', 'tile_0_3']]
b = ['tile_0_4', 'tile_0_3', 'tile_0_2', 'tile_0_1', 'tile_0_0']

a[0] = 3


print(len(a))

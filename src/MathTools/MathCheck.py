import numpy as np
import pygame as pg
import json


thisdict = {
  "car1": {
    "models": {
      "up": 0,
      "mpg": 27.5,
      "left": 0,
      "right": [9, 9]
    },
    "models2": {
      "up": 3,
      "mpg": 7.5,
      "left": 2,
      "right": [2, 5]
    }
  },
  "car2": {
    "models": {
      "up": 6,
      "mpg": 2.5,
      "left": 2,
      "right": [1, 4]
    },
    "models2": {
      "up": 3,
      "mpg": 7.5,
      "left": 2,
      "right": [2, 5]
    }
  },
  "car3": {
    "models": {
      "up": 0,
      "mpg": 27.5,
      "left": 0,
      "right": [9, 9]
    },
    "models2": {
      "up": 3,
      "mpg": 7.5,
      "left": 2,
      "right": [2, 5]
    }
  },
}

# print(json.dumps(thisdict, indent = 3, separators=(".", " = "),  sort_keys=True))

for car in thisdict:
  models = thisdict[car]
  for model in models:
    for qual in models[model]:
      print(models[model][qual])

print(thisdict['car1'])

import pygame as pg
import numpy as np
from PIL import Image


class spriteSheet:

    def  __init__(self, spritesheet):


        self.spritesheet = pg.image.load(spritesheet).convert()
        self.pillow = Image.open(spritesheet)
        
        self.size = self.pillow.size
        self.images = int(self.size[0]/16 * self.size[1]/16)
        self.cols = int(self.size[0]/16)
        self.rows = int(self.size[1]/16)

        self.assets = {}

    def parse(self):
        spritepos = []
        for i in range(self.rows):
            for j in range(self.cols):
                spritepos.append([16*j, 16*i, 16, 16])

        return spritepos

    def asset_pos(self):
        spritepos = self.parse()
        assetpos = {}
        for i in range(len(spritepos)):
            assetpos[f"tile{i}"] = spritepos[i]
        return assetpos

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def get_image(self):
        return self.pillow

    def get_SS(self):
        return self.spritesheet


class assetData:

    def __init__(self, spritesheet):

        self.ss = spritesheet

        self.assets = {}

    def init_dict(self):
        assetpos = self.ss.asset_pos()
        rows = self.ss.get_rows()
        cols = self.ss.get_cols()
        for i in range(rows):
            for j in range(cols):    
                self.assets[f"tile_{i}_{j}"] = {
                        "mesh": assetpos[f"tile{j}"],
                        "sockets": {
                            "up": 0,
                            "down": 0,
                            "left": 0,
                            "right": 0
                        },
                        "neighbor_list": {
                            "up": [],
                            "down": [],
                            "left": [],
                            "right": []
                        }
                    }
            
    def get_sockets(self):
        sprite = self.ss.get_image()
        rows = self.ss.get_rows()
        cols = self.ss.get_cols()
        for i in range(rows):
            topy = 16*i
            midy = 8 + 16*i
            bottomy = 15 + 16*i

            for j in range(cols):
                midx = 8 + 16*j
                leftx = 16*j
                rightx = 15 + 16*j
                
                if not sprite.getpixel((midx, topy))[:3] == (0, 0, 0):
                    self.assets[f"tile_{i}_{j}"]["sockets"]["up"] = 1
                if not sprite.getpixel((midx, bottomy))[:3] == (0, 0, 0):
                    self.assets[f"tile_{i}_{j}"]["sockets"]["down"] = 1
                if not sprite.getpixel((leftx, midy))[:3] == (0, 0, 0):
                    self.assets[f"tile_{i}_{j}"]["sockets"]["left"] = 1
                if not sprite.getpixel((rightx, midy))[:3] == (0, 0, 0):
                    self.assets[f"tile_{i}_{j}"]["sockets"]["right"] = 1
    
    def get_neighbors(self):
        for tiles in self.assets:
            tile = self.assets[tiles]
            sockets = self.assets[tiles]["sockets"]

            for tiles2 in self.assets:
                sockets2 = self.assets[tiles2]["sockets"]

                if sockets["up"] == sockets2["down"]:
                    tile["neighbor_list"]["up"].append(f"{tiles2}")
                if sockets["down"] == sockets2["up"]:
                    tile["neighbor_list"]["down"].append(f"{tiles2}")
                if sockets["left"] == sockets2["right"]:
                    tile["neighbor_list"]["left"].append(f"{tiles2}")
                if sockets["right"] == sockets2["left"]:
                    tile["neighbor_list"]["right"].append(f"{tiles2}")

    def init_data(self):
        self.init_dict()
        self.get_sockets()
        self.get_neighbors()

    def get_assets(self):
        return self.assets


class waveFunction:

    def __init__(self, spritesheet, assetdata, size):

        self.sS = spritesheet
        self.aD = assetdata
        self.scene = []
        self.size = size

    def init_scene(self):
        self.aD.init_data()
        tile_possibility = self.possibilities()

        while len(self.scene) < self.size[1]:
            x = []
            while len(x) < self.size[0]:
                x.append(tile_possibility)
            self.scene.append(x)
        # print(self.scene)
        # print(self.aD.get_assets())

    def possibilities(self):
        assets = self.aD.get_assets()
        all_tiles = []
        for tile in assets:
            all_tiles.append(f"{tile}")
        return all_tiles

    def start(self):
        self.init_scene()
        # print(self.scene)
        # while self.collapsing():
        #     self.iterate()

    def go(self):
        if self.collapsing():
            self.iterate()

    def collapsing(self):
        collapse_param = 0
        collapse_cond = self.size[0]*self.size[1]
        collapsed = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if len(self.scene[j][i]) == 1:
                     collapsed += 1
                collapse_param += len(self.scene[j][i])
        if collapse_param == collapse_cond:
            return False
        else:
            print(collapsed)
            return True

    def iterate(self):
        coords = self.min_entropy_coords()
        self.collapse(coords)
        self.consequence(coords)

    def min_entropy_coords(self):
        min_entropy = len(self.possibilities())
        min_entropy_coords = []
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if not len(self.scene[i][j]) == 1:
                    if len(self.scene[i][j]) < min_entropy:
                        min_entropy_coords = []
                        min_entropy = len(self.scene[i][j])
                        min_entropy_coords.append([i, j])
                    elif len(self.scene[i][j]) == min_entropy:
                        min_entropy_coords.append([i, j])
        if len(min_entropy_coords) > 1:
            min_entropy_coords = [min_entropy_coords[np.random.randint(len(min_entropy_coords))]]

        return min_entropy_coords[0]

    def collapse(self, coords):
        self.scene[coords[0]][coords[1]] = [self.scene[coords[0]][coords[1]][np.random.randint(len(self.scene[coords[0]][coords[1]]))]]
        print('cell', coords)

    def consequence(self, coords):
        cur_tile = self.scene[coords[0]][coords[1]]
        up = coords[0]-1
        down = coords[0]+1
        left = coords[1]-1
        right = coords[1]+1
        cur_tile_neighbor_data = self.aD.get_assets()[cur_tile[0]]['neighbor_list']
        for direction in cur_tile_neighbor_data:
            if direction == 'up':
                if up < 0:
                    continue
                elif not len(self.scene[up][coords[1]]) == 1:
                    new_cell = list(set(self.scene[up][coords[1]]).intersection(cur_tile_neighbor_data[direction]))
                    self.scene[up][coords[1]] = new_cell
                    if len(new_cell) == 1:
                        new_coords = [up, coords[1]]
                        self.consequence(new_coords)
            elif direction == 'down':
                if down >= self.size[1]:
                    continue
                elif not len(self.scene[down][coords[1]]) == 1:    
                    new_cell = list(set(self.scene[down][coords[1]]).intersection(cur_tile_neighbor_data[direction]))
                    self.scene[down][coords[1]] = new_cell
                    if len(new_cell) == 1:
                        new_coords = [down, coords[1]]
                        self.consequence(new_coords)
            elif direction == 'left':
                if left < 0:
                    continue
                elif not len(self.scene[coords[0]][left]) == 1:
                    new_cell = list(set(self.scene[coords[0]][left]).intersection(cur_tile_neighbor_data[direction]))
                    self.scene[coords[0]][left] = new_cell
                    if len(new_cell) == 1:
                        new_coords = [coords[0], left]
                        self.consequence(new_coords)
            elif direction == 'right':
                if right >= self.size[0]:
                    continue
                elif not len(self.scene[coords[0]][right]) == 1:
                    new_cell = list(set(self.scene[coords[0]][right]).intersection(cur_tile_neighbor_data[direction]))
                    self.scene[coords[0]][right] = new_cell
                    if len(new_cell) == 1:
                        new_coords = [coords[0], right]
                        self.consequence(new_coords)

                

    def get_scene(self):
        return self.scene

    def get_scene_size(self):
        return self.size

import pygame as pg
import numpy as np
from PIL import Image
from spriteSheet import *
from Game.Controls import UIcontroller

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Sprites")

def main():
    run = True
    a = spriteSheet('tileAssets.png')
    b = assetData(a)
    c = waveFunction(a, b, [110, 60])
    c.start()

    ctrl = UIcontroller(a)

    while run:

        ctrlr = ctrl.inputs()
        if ctrlr == 0:
            run = False

        c.go()
        size = c.get_scene_size()
        scene = c.get_scene()
        for i in range(size[0]):
            for j in range(size[1]):
                if len(scene[j][i]) == 1:
                    Win.blit(a.get_SS(), (16*i, 16*j), b.assets[scene[j][i][0]]['mesh'])

        pg.display.update()

    pg.quit()

main()

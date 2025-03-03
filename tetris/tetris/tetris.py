import pygame as pg

pg.init()

console = pg.display.set_mode((1000,600))
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.draw.rect(console,(255,255,0),[100,100,100,100],0)
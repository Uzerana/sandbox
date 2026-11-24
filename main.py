import pygame as pg

pg.init()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Catch The Target")


running = True
x = 285
y = 285
w = 40
h = 40

while running:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(mouse_x, mouse_y)

        if event.type == pg.QUIT:
            running = False


    screen.fill((255, 255, 255))
    pg.draw.rect(screen,(255,50,50),(x, y, w, h))

    pg.display.update()

pg.quit()

from pygame import *

window = display.set_mode((700, 500))
display.set_caption("catch")
background = transform.scale(image.load("download.jpg"), (700, 500))

x1 = 100
y1 = 300
x2 = 300
y2 = 300
x3 = 300
y3 = 300


sprite1 = transform.scale(image.load('F-removebg-preview.png'), (100, 200))
sprite2 = transform.scale(image.load('images-removebg-preview.png'), (100, 200))
speed = 10

run = True
clock = time.Clock()
FPS = 60000000

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(sprite3, (x3, y3))

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 595:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 595:
        y2 += speed

    if keys_pressed[K_f] and x3 > 5:
        x3 -= speed
    if keys_pressed[K_h] and x3 < 595:
        x3 += speed
    if keys_pressed[K_t] and y3 > 5:
        y3 -= speed
    if keys_pressed[K_g] and y3 < 595:
        y3 += speed


    display.update()
    clock.tick(FPS)
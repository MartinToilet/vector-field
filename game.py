import pygame
import random
import math
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


width = 1600
height = 1000

window = pygame.display.set_mode((width, height))


class Dot:
    image = pygame.image.load(resource_path('images/lolguy.png')).convert_alpha()
    image = pygame.transform.scale(image, (100, 100))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def tick(self):
        rx = self.x - width / 2
        ry = self.y - height / 2
        self.x += self.vx
        self.y += self.vy
        self.vx = 0.0001 * (10 + rx + -ry ** 2)
        self.vy = 0.0001 * (2 * ry - rx ** 2)
        if math.sqrt(rx ** 2 + ry ** 2) > width * 2:
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
            self.vx = 0
            self.vy = 0

        window.blit(Dot.image, (int(self.x), int(self.y)))


pygame.display.set_caption("Vector Field")

crashed = False

clock = pygame.time.Clock()

entities = []

for i in range(120):
    entities.append(Dot(random.randint(0, width), random.randint(0, height)))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    window.fill((150, 100, 150))

    for e in entities:
        e.tick()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

import pygame as pg
from random import randint
from settings import *

class Player:
  def __init__(self, game) -> None:
    self.game = game
    self.name = names[randint(0, len(names)-1)]
    self.color = colors[randint(0, len(colors)-1)]
    self.players_list = []
    self.x, self.y = randint(0, WIDTH-50), randint(0, HEIGHT-50)
    self.size = 20

  def check_screen_collision(self, dx, dy):
    # solved by chat gpt
    if self.x + dx >= 25 and self.x + dx <= WIDTH-25:
        self.x += dx
    if self.y + dy >= 25 and self.y + dy <= HEIGHT-25:
        self.y += dy

  def mouvement(self):
    dx, dy = 0, 0
    keys = pg.key.get_pressed()
    if keys[pg.K_z]:
      dy -= 1
    if keys[pg.K_s]:
      dy += 1
    if keys[pg.K_q]:
      dx -= 1
    if keys[pg.K_d]:
      dx += 1
    self.check_screen_collision(dx, dy)

  def update(self):
    self.mouvement()

  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)
import pygame as pg
from random import randint
from settings import *

class Player:
  def __init__(self, game) -> None:
    self.game = game
    self.name = names[randint(0, len(names)-1)]
    self.color = colors[randint(0, len(colors)-1)]
    self.players_list = []
    self.x, self.y = 25, 25
    self.size = 20

  def check_screen_collision(self, dx, dy):
    # solved by chat gpt
    if self.x + dx >= 25 and self.x + dx <= WIDTH-25:
        self.x += dx
    if self.y + dy >= 25 and self.y + dy <= HEIGHT-25:
        self.y += dy

  def mouvement(self, x, y):
    dx, dy = 0, 0
    # keys = pg.key.get_pressed()
    if x < 550 - 25 and y == 25:
      dx += 1
    if x == 550 - 25 and y <= 500 - 25:
      dy += 1
    if y == 500 - 25:
      dx -= 1
    if x == 25 and y <= 475:
      dy -= 1
    self.check_screen_collision(dx, dy)

  def move(self):
    print(self.x, self.y)
    self.mouvement(self.x, self.y)
    # n %= 40 

  def update(self):
    self.move()

  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)
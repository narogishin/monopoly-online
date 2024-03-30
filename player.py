import pygame as pg
from random import randint
from settings import *
import time

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

  def mouvement(self, x: int, y: int, setpoint: tuple):
    dx, dy = 0, 0
    # keys = pg.key.get_pressed()
    # if not setpoint:
    if x < setpoint[0] and y == setpoint[1]:
      dx += 1
    if x == setpoint[0] and y <= setpoint[1]:
      dy += 1
    if y == setpoint[1]:
      dx -= 1
    if x == setpoint[0] and y <= setpoint[1]:
      dy -= 1
    self.check_screen_collision(dx, dy)
    # else:
    #   dx += 0
    #   dy += 0

  def move(self, x, y):
    print(self.x, self.y)
    # if x != self.x and y != self.y:
    self.mouvement(self.x, self.y, (x, y))
    # else:
    # self.mouvement(self.x, self.y, x - self.x and y - self.y)
    # time.sleep(2)

  def update(self):
    self.move(525, 525)
    
  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)
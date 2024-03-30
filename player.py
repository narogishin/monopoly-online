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
    self.n, self.m = 0, 0
    self.size = 20

  def check_screen_collision(self, dx, dy):
    # solved by chat gpt
    if self.x + dx >= 25 and self.x + dx <= WIDTH-25:
        self.x += dx
    if self.y + dy >= 25 and self.y + dy <= HEIGHT-25:
        self.y += dy

  def mouvement(self, x: int, y: int, setpoint: tuple):
    dx, dy = 0, 0
    if (x, y) != setpoint:
      if x < 550 - 25 and y == 25:
        dx += 1
      if x == 550 - 25 and y <= 500 - 25:
        dy += 1
      if y == 500 - 25:
        dx -= 1
      if x == 25 and y <= 500 - 25:
        dy -= 1
      self.check_screen_collision(dx, dy)

  def move(self, x, y):
    self.mouvement(self.x, self.y, (x, y))

  def play(self):
    click = pg.mouse.get_pressed()[0]
    if click:
      n, m = randint(0, 10), randint(0, 10)
      if n == 0 or n == 10:
        m = randint(0, 10)
      elif m == 0 or m == 9:
        n = randint(0, 10)
      # time.sleep(1)
      print(n, m)
      self.move(25 + 50*n, 25 + 50*m)

  def update(self):
    self.play()
    
  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)
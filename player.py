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
    self.current_index = 0
    self.size = 20
    self.alpha = True

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
      if x == 550 - 25 and y <= 550 - 25:
        dy += 1
      if y == 550 - 25:
        dx -= 1
      if x == 25 and y <= 550 - 25:
        dy -= 1
      self.check_screen_collision(dx, dy)

  def move(self, x, y):
    self.mouvement(self.x, self.y, (x, y))

  def check_right_click(self, index: int):
    right_click_triggered = False
    for event in pg.event.get():
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 3 and not right_click_triggered:  # Check for right mouse button click
          self.current_index += index
          self.current_index %= 40
          n, m = positions[self.current_index]
          while (self.x != 25 + 50*n) and (self.y != 25 + 50*m):
            print("current index", self.current_index)
            # print("n and m : ", n, m)
            # print("x and y : ", self.x, self.y)
            self.move(25 + 50*n, 25 + 50*m)
          right_click_triggered = True
      elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 3:
          right_click_triggered = False

  def play(self):
    click = pg.mouse.get_pressed()[0]
    index = randint(1, 6)
    print("index : ", index)
    # self.check_right_click(index)
    if click:
      self.current_index += index
      self.current_index %= 40
      n, m = positions[self.current_index]
      # while (self.x != 25 + 50*n) and (self.y != 25 + 50*m):
      print("current index : ", self.current_index)
      print("n and m : ", n, m)
      # print("x and y : ", self.x, self.y)
      self.move(25 + 50*n, 25 + 50*m)
      self.alpha = not self.alpha

  def update(self):
    self.play()
    
  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)
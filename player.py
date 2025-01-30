import pygame as pg
from random import randint
from time import sleep

from cities import Cities
from settings import *
from rules import rules_list

class Player:
  def __init__(self, game) -> None:
    self.game = game
    self.players_list = []
    self.x, self.y = 25, 25
    self.current_index = 0
    self.last_index = 0
    self.size = 20
    self.owned_cities = []

  def __str__(self):
    return f"Player {self.name} is at {self.current_index}"

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

  def play(self):
    click = pg.key.get_pressed()[pg.K_SPACE]
    if click:
      first_index = randint(1, 6)
      second_index = randint(1, 6)
      index = first_index + second_index
      sleep(0.5)
      
    try:
      self.current_index += index
      self.current_index %= 40
      # self.cities.update()
      print(self.current_index, index)

    except UnboundLocalError:
      # now only God knows -why I did this
      self.current_index += 0

    n, m = positions[self.current_index]
    self.move(25 + 50*n, 25 + 50*m)
    
  def update(self):
    self.play()
    
  def draw(self):
    pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.size)


class GamePlayer(Player):
  def __init__(self, game) -> None:
    super().__init__(game)
    # self.cities = CityWrapper(self)
    self.name = names[randint(0, len(names)-1)]
    self.color = colors[randint(0, len(colors)-1)]
    self.current_money = PLAYER_BUDGET
    
  def update(self):
    super().update()
    rules_list[self.current_index](game_player = self)
    self.last_index = self.current_index
    print(f"Player {self.name} was at {self.last_index} and now in ${self.current_money}")
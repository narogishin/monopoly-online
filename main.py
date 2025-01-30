from settings import *
from player import GamePlayer
from screen import Screen
from client import Client
from threading import Thread
import pygame as pg
import sys

class Game:
  def __init__(self) -> None:
    self.screen = pg.display.set_mode(RESOLUTION)
    self.clock = pg.time.Clock()
    self.new_game()
    
  def new_game(self):
    self.player = GamePlayer(self)
    self.board = Screen(self)
    # self.global_thread = Thread(target=self.start_game)
    self.player_thread = Thread(target=self.player.update)
    self.player_thread.start()
    # self.client = Client(self)

  def update(self):
    self.player_thread.join()
    # self.player.update()
    # self.client.update()
    pg.display.set_caption(f'Moroccan Monopoly : {self.clock.get_fps() :.1f}')
    pg.display.flip()

  def draw(self):
    self.screen.fill('black')
    self.board.draw()
    self.player.draw()
    # self.client.draw()

  def check_event(self):
    keys = pg.key.get_pressed()
    for event in pg.event.get():
      if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
        # self.client.disconnect() # maybe we don't need to do it since sys.exit
        pg.quit()
        sys.exit()

  def run(self):
    while True:
      self.check_event()
      self.update()
      self.draw()


if __name__ == '__main__':
  game = Game()
  game.run()
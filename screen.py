import pygame as pg
from settings import *

board = [
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
  [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
  ]

class Screen:
  def __init__(self, game) -> None:
    self.game = game
    self.board = board

  def draw(self):

    [pg.draw.rect(self.game.screen, 'darkgray', 
                  (i*100*RATIO, 0*100*RATIO, 100*RATIO, 100*RATIO), 2)
                  for i in range(len(self.board[0]))]
    
    [pg.draw.rect(self.game.screen, 'darkgray', 
                  (10*100*RATIO, i*100*RATIO, 100*RATIO, 100*RATIO), 2)
                  for i in range(len(self.board[1]))]
    
    [pg.draw.rect(self.game.screen, 'darkgray', 
                  (i*100*RATIO, 10*100*RATIO, 100*RATIO, 100*RATIO), 2)
                  for i in range(len(self.board[2])+1)]
    
    [pg.draw.rect(self.game.screen, 'darkgray', 
                  (0*100*RATIO, i*100*RATIO, 100*RATIO, 100*RATIO), 2)
                  for i in range(len(self.board[3]))]
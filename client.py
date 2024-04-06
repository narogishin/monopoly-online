import socket, pickle
from settings import *
import pygame as pg

class Client:
  def __init__(self, game) -> None:
    self.game = game
    self.get_connected()

  def get_connected(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def update(self):
    # print('sending coordinates')
    self.send_coordinates()

  def draw(self):
    msg = self.recv_message()
    # print(msg)
    # for player, data in msg.items():
    #   if player != self.game.player.name:
    #     x, y, color = data.split(',')
    #     pg.draw.circle(self.game.screen, color, (int(x), int(y)), self.game.player.size)

    [pg.draw.circle(self.game.screen, f(data, 2), (int(f(data, 0)), int(f(data, 1))), self.game.player.size) 
     for player, data in msg.items() if player != self.game.player.name]

  def send_msg(self, msg: bytes):
    msg += b' ' * (HEADER - len(msg))
    self.client.sendto(msg, ADDR)

  def send_coordinates(self):
    self.data = f'{self.game.player.x},{self.game.player.y},{self.game.player.name},{self.game.player.color}'
    self.send_msg(pickle.dumps(self.data))

  def recv_message(self) -> dict:
    # print('receiving from server')
    msg = pickle.loads(self.client.recvfrom(HEADER)[0])
    if msg:
      return msg

  def disconnect(self):
    self.send_msg(pickle.dumps(f'{DM}:{self.game.player.name}'))
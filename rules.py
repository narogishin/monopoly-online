# ALL THESE RULES MUST BE CHANGED ACCORDING TO THE CITIES CLASS

from player import GamePlayer
from cities import City, Cities
import random

# AIRPORT HANDLER

class Airport:
  def __init__(self, airport_number: int) -> None:
    self.airport_number = airport_number
    self.price = 200
    self.rent = 50
    self.owners = [0 for _ in range(4)]

  def buy(self, player: GamePlayer):
    player.current_money -= self.price
    self.owners[self.airport_number] = player

  def rent_calcutalator(self, player: GamePlayer):
    self.rent = 50 * self.owners.count(player)
    print(f"Player {player.name} owns {self.owners.count(player)} airports")

  def pay_rent(self, player: GamePlayer):
    player.current_money -= self.rent
    print(f"Player {player.name} paid ${self.rent} as rent")


def airport(game_player: GamePlayer, idx: int):
  '''buy or pass, if not bought, pay rent'''
  airport = Airport(idx)
  say = get_input_from_user(f"Do you want to buy the airport? (y/n): ")
  if say == 'y':
    airport.buy(game_player)
  else:
    airport.rent_calcutalator(game_player)
    airport.pay_rent(game_player)

# GLOBAL FUNCTIONS

def get_input_from_user(prompt: str) -> str:
  say = input(prompt)
  while say not in ['y', 'n']:
    say = input('Please enter a valid input (y/n): ')
  return say

def pass_to_next_player(game_player: GamePlayer):
  '''pass to the next player'''
  print(f"{game_player.name} passed to the next player!")

# SURPRISE FUNCTIONS

def surprise_win_200(player: GamePlayer):
  '''win 200'''
  print(f"{player.name} wins a lottery of $200!")
  player.current_money += 200

def surprise_lose_100(player: GamePlayer):
  '''lose 100'''
  print(f"{player.name} loses $100 to a scam!")
  player.current_money -= 100

def surprise_pay_50(player: GamePlayer, all_players: list[GamePlayer]):
  '''pay 50 to each player'''
  print(f"{player.name} pays $50 to each player!")
  for p in all_players:
    if p != player:
      p.current_money += 50
  player.current_money -= 50 * (len(all_players) - 1)

# GAME RULES

def start(game_player: GamePlayer):
  '''collect as you pass'''
  # should check if last index was bigger than current index before granting the money,
  # but if was exactly in 0 then we granted 300.
  if game_player.current_index == 0:
    print(f"{game_player.name} passed the start!")
    game_player.current_money += 200

def fes_1(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  say = get_input_from_user('Do you want to buy the first land of Fes? (y/n): ')
  city = Cities(game_player).cities_objects['Fes']
  if city.owners[city.citys_indexes.index(game_player.current_index)] != game_player.name:
    city.offer() if say == 'y' else pass_to_next_player(game_player)
  if city.right_to_build:
    # instead of passing one should pay the rent based on the pay_rent method, but we should determine the owner who should be payed and the payer
    city.build_house_or_hotel(game_player) if city in game_player.owned_cities else pass_to_next_player(game_player)

    


def treasure(game_player: GamePlayer):
  '''indexes: 2, 17 and 33'''
  pass

def fes_2(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  say = input('Do you want to buy the second land of Fes? (y/n): ')

def tax(game_player: GamePlayer):
  '''pay taxes'''
  pass

def marrakech_1(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the first land of Marrakech? (y/n): ')

def surprise(game_player: GamePlayer, all_players=None):
  '''indexes: 7, 22 and 36'''
  outcome = random.choice([
    surprise_win_200,
    surprise_lose_100,
    # surprise_pay_50 can't be called yet until we get the list of all players which can be taken from the player instance itself
  ])
  outcome(game_player)
  print("Surprise!")

def marrakech_2(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the second land of Marrakech? (y/n): ')

def marrakech_3(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the third land of Marrakech? (y/n): ')

def prison(game_player: GamePlayer):
  '''stays, tries to escape'''
  pass

def chefchaouen_1(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the first land of Chefchaouen? (y/n): ')

def power_company(game_player: GamePlayer):
  '''owns 1 rent = 10, owns 2 rent = 100'''
  pass

def chefchaouen_2(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the second land of Chefchaouen? (y/n): ')

def chefchaouen_3(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the third land of Chefchaouen? (y/n): ')

def tetouan_1(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the first land of Tetouan? (y/n): ')

def tetouan_2(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the second land of Tetouan? (y/n): ')

def tetouan_3(game_player: GamePlayer):
  '''buy land, build house or pay rent'''
  get_input_from_user('Do you want to buy the third land of Tetouan? (y/n): ')

def vacation(game_player: GamePlayer):
  '''Sleep for a little while, you deserve it!'''
  print('You are on vacation!')

rules_list = [
  start,
  fes_1,
  treasure,
  fes_2,
  tax,
  airport(idx=0),
  marrakech_1,
  surprise,
  marrakech_2,
  marrakech_3,
  prison,
  chefchaouen_1,
  power_company,
  chefchaouen_2,
  chefchaouen_3,
  airport(idx=1),
  tetouan_1,
  treasure,
  tetouan_2,
  tetouan_3,
  vacation,
  # beni_mellal_1,
  treasure,
  # beni_mellal_2,
  # beni_mellal_3,
  airport(idx=2),
  # meknes_1,
  # meknes_2,
  power_company,
  # meknes_3,
  prison,
  # essaouira_1,
  # essaoura_2,
  treasure,
  # essaouira_3,
  airport(idx=3),
  surprise,
  # casablanca_1,
  tax,
  # casablanca_2
]
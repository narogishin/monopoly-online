from player import GamePlayer

class City:
  def __init__(self, player: GamePlayer, name: str, citys_indexes: list, price: int, house_price: int, rent_pay: int) -> None:
    self.player = player
    self.name = name
    self.citys_indexes = citys_indexes
    self.price = price
    self.house_price = house_price
    self.hotel_price = 2.5 * house_price
    self.rent_pay = rent_pay
    self.number_of_houses = 0
    self.number_of_hotels = 0
    self.owners = ['' for _ in range(len(self.citys_indexes))]
    self.right_to_build = False

  def __str__(self):
    return f"{self.name} : {self.owners}"

  def check_ownership(self, player: GamePlayer) -> bool:
    # check if the player owns all the cities to aquire the right to build
    condition = self.owners == [player for _ in range(len(self.citys_indexes))]
    if condition:
      self.right_to_build = True
      self.player.owned_cities.append(self)
    return condition
  
  def check_position(self, position: int) -> bool:
    return position in self.citys_indexes
  
  def offer(self):
    player_position = self.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice OR End turn'''
      self.owners[self.citys_indexes.index(player_position)] = self.player.name
      print(f"Choice Offering, in {self.name}")

  def calculate_rent(self):
    total_buildings = sum([1 for owner in self.owners if owner != self.player.name])
    if self.player.name not in self.owners:
      self.rent_pay += (total_buildings * self.house_price, 0)[self.right_to_build]

  def pay_rent(self, owner_player: GamePlayer, game_player: GamePlayer):
    # if self.player.name in self.owners:
    self.calculate_rent()
    game_player.current_money -= self.rent_pay
    owner_player.current_money += self.rent_pay

  def build_house_or_hotel(self, player: GamePlayer):
    done = False
    while not done:
      choice = input("Do you want to build a house or a hotel? (house/hotel), if you're done say (done): ")
      if choice == 'h':
        if self.check_ownership(player):
          self.number_of_houses += 1
          self.player.current_money -= self.house_price
        # print("You don't have the right to build a house")
      elif choice == 'h':
        if self.check_ownership(player):
          self.number_of_hotels += 1
          self.player.current_money -= self.hotel_price
        # print("You don't have the right to build a hotel")
      elif choice == 'done':
        done = True
    
  # def update(self, player_name: str):
  #   self.check_ownership(player_name)
  #   self.offer()


class Cities(City):
  def __init__(self, player: GamePlayer) -> None:
    self.player = player
    # self.cities_list = ['Fes', 'Marrakech', 'Chefchaouen', 'Tetouan', 'beni mellal', 'Meknes', 'essaouira', 'casablanca']
    self.cities_objects = {}
    add_city = self.add_city

    add_city(City(player, name='Fes', citys_indexes=[1, 3], price=100, house_price=50, rent_pay=10))
    add_city(City(player, name='Marrakech', citys_indexes=[6, 8, 9], price=150, house_price=75, rent_pay=15))
    add_city(City(player, name='Chefchaouen', citys_indexes=[11, 13, 14], price=200, house_price=100, rent_pay=20))
    add_city(City(player, name='Tetouan', citys_indexes=[16, 18, 19], price=250, house_price=125, rent_pay=25))
    add_city(City(player, name='Beni Mellal', citys_indexes=[21, 23, 24], price=300, house_price=150, rent_pay=30))
    add_city(City(player, name='Meknes', citys_indexes=[26, 27, 29], price=350, house_price=175, rent_pay=35))
    add_city(City(player, name='Essaouira', citys_indexes=[31, 32, 34], price=400, house_price=200, rent_pay=40))
    add_city(City(player, name='Casablanca', citys_indexes=[37, 39], price=450, house_price=225, rent_pay=45))

  def add_city(self, city: City) -> None:
    self.cities_objects[city.name] = city

  def update(self) -> None:
    player_name = self.player.name
    [city.update(player_name) for city in self.cities_list]
  
  def check_ownership(self, player):
    return super().check_ownership(player)
class City:
  def __init__(self, player, name: str, indexes: list) -> None:
    self.player = player
    self.name = name
    self.indexes = indexes
    self.owners = ['' for _ in range(len(self.indexes))]
    self.right_to_build = False

  def check_ownership(self, player: str):
    condition = self.owners == [player for _ in range(len(self.indexes))]
    if condition:
      self.right_to_build = True
    return condition
  
  def check_position(self, position: int) -> bool:
    return True if position in self.indexes else False
  
  def offer(self):
    player_position = self.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice/End turn'''
      self.owners[self.indexes.index(player_position)] = self.player.name
      print(f"Choice Offering, in {self.name}")

  def update(self, player_name: str):
    self.check_ownership(player_name)
    self.offer()


class Cities(City):
  def __init__(self, player) -> None:
    self.player = player
    self.cities_list = []
    add_city = self.add_city

    add_city(City(player, name='fes', indexes=[1, 3]))
    add_city(City(player, name='marrakech', indexes=[6, 8, 9]))
    add_city(City(player, name='chefchaouen', indexes=[11, 13, 14]))
    add_city(City(player, name='tetouan', indexes=[16, 18, 19]))

  def add_city(self, city):
    self.cities_list.append(city)

  def update(self):
    player_name = self.player.name
    [city.update(player_name) for city in self.cities_list]
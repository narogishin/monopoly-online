class City:
  def __init__(self, game, name: str, indexes: list) -> None:
    self.game = game
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

  def update(self):
    self.check_ownership(self.game.player.name)


class Cities(City):
  pass


class Chefchaouen(City):
  def __init__(self, game, name: str, indexes: list) -> None:
    super().__init__(game, name, indexes)
    self.name = 'chefchaouen'
    self.indexes = [11, 13, 14]


  def update(self):
    super().update()
    self.offer()

  def offer(self):
    player_position = self.game.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice/End turn'''
      print(f"Choice Offering, in {self.name}")
  
  
class Fes(City):
  def __init__(self, game, name: str, indexes: list) -> None:
    super().__init__(game, name, indexes)
    self.name = 'fes'
    self.indexes = [1, 3]

  def update(self):
    super().update()
    self.offer()

  def offer(self):
    player_position = self.game.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice/End turn'''
      print(f"Choice Offering, in {self.name}")
  

class Marrakech(City):
  def __init__(self, game, name: str, indexes: list) -> None:
    super().__init__(game, name, indexes)
    self.name = 'marrakech'
    self.indexes = [16, 18, 19]

  def update(self):
    super().update()
    self.offer()

  def offer(self):
    player_position = self.game.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice/End turn'''
      print(f"Choice Offering, in {self.name}")


class Tetouan(City):
  def __init__(self, game, name: str, indexes: list) -> None:
    super().__init__(game, name, indexes)
    self.name = 'marrakech'
    self.indexes = [16, 18, 19]

  def update(self):
    super().update()
    self.offer()

  def offer(self):
    player_position = self.game.player.current_index
    if self.check_position(player_position):
      '''Offer the player a choice between : buying the land OR rolling the dice/End turn'''
      print(f"Choice Offering, in {self.name}")


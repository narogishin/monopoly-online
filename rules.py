

class city:
  def __init__(self, game, name: str, indexes: list, rents: int) -> None:
    self.game = game
    self.name = name
    self.indexes = indexes
    self.rents = rents
    self.owners = ['' for _ in range(rents)]
    self.right_to_build = False

  def check_ownership(self, player):
    condition = self.owners == [player for _ in range(self.rents)]
    if condition:
      self.right_to_build = True
    return condition

  



def start():
  '''collect as you pass'''
  pass

def fes_1():
  '''buy land, build house or pay rent'''
  pass

def treasure():
  '''indexes: 2, 17 and 33'''
  pass

def fes_2():
  '''buy land, build house or pay rent'''
  pass

def tax():
  '''pay taxes'''
  pass

def airport_1():
  '''pay airport'''
  pass

def marrakech_1():
  '''buy land, build house or pay rent'''
  pass

def suprise():
  '''indexes: 7, 22 and 36'''
  pass

def marrakech_2():
  '''buy land, build house or pay rent'''
  pass

def marrakech_3():
  '''buy land, build house or pay rent'''
  pass

def prison():
  '''stays, tries to escape'''
  pass

def chefchaouen_1():
  '''buy land, build house or pay rent'''
  pass

def power_company():
  '''owns 1 rent = 10, owns 2 rent = 100'''
  pass

def chefchaouen_2():
  '''buy land, build house or pay rent'''
  pass

def chefchaouen_3():
  '''buy land, build house or pay rent'''
  pass

def airport_2():
  '''pay airport'''
  pass

def tetouan_1():
  '''buy land, build house or pay rent'''
  pass
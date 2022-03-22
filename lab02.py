from enum import Enum
class FoodCategory(Enum):
  VEGETABLE=0
  FRUIT=1
  GRAIN=2
  PROTEIN=3
  DAIRY=4
  OIL=5
  OTHER=6
class FoodItem(object):
  def __init__(self,name,category,cals):
    if FoodCategory(category):
      self.category = category
    self._calories = int(cals)
    self.name = name
  def name(self):
    return self.name
    
  def category(self):
    return self.category
    
  def calories_per_100g(self):
    return self._calories

  def __str__(self):
    return f'{self.name} ({self.category}) {self._calories}cal/100g'

class FoodServing(object): 
  
  def __init__(self, foodItem, amount):
    self._foodItem = foodItem
    self._amount = amount
    
  def food(self):
    return self._foodItem
    
  def amount(self):
    return self._amount
    
  def calories(self):
    return int((self._amount / 100) * self._foodItem.calories_per_100g())
    
  def __str__(self):
    return f'{self._amount}g of {self._foodItem}'
    
class Meal(object):
  def __init__(self):
    self.servingsList = []

  def addFood(self, FoodServing):
    self.servingsList.append(FoodServing)

  def calories(self):
    sum = 0
    if len(self.servingsList) == 0:
      return 0
    else:
      for serving in self.servingsList:
        sum += serving.calories()
    return sum

  def __str__(self):
    list = ""
    for serving in self.servingsList:
      list += str(serving)+ "\n"
    list = list[:len(list)-1]
    return list  
    

    
      
    
      
      
  
  

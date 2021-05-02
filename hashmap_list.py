import numpy as np
from get_hash import get_hash
from item import Item
from hashmap import HashMap, HashMapIterator

class HashMapList(HashMap):
  def __init__(self, *args):
    super().__init__()
    self.__array = [0]*self._size #create empty array

    for arg in args:
      if type(arg) is not dict:
        raise TypeError(f"HashMap must be initialized empty or with a dict, got {arg} of type {type(arg)}")

      for key, value in arg.items():
        self.__setitem__(key, value)

  def __resize(self):
    old_items = self.__items()
    self._size = 2 * self._size
    self._len = 0
    self.__array = [0]*self._size

    for item, value in old_items:
      self.__setitem__(item, value)  
      assert self.__contains__(item)  

class HashMapListIterator(HashMapIterator):
  def __init__(self, array):
    self.__values = []
    for val in array:
      if val != 0:
        self.__values.append(val)
    self.__curr = None
    self.__index = 0

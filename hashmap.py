from collections.abc import MutableMapping
import numpy as np
from get_hash import get_hash
from item import Item

class HashMap(MutableMapping):
  def __init__(self, *args):
    self.__size = 2**8 #initialize array length
    self.__array = np.zeros(self.__size, dtype=object) #create empty array

    for arg in args:
      if type(arg) is not dict:
        raise TypeError("HashMap must be initialized empty or with a dict")

      for key, value in arg.items():
        self.__setitem__(key, value)

  def __del__(self):
    pass

  def __len__(self):
    pass

  def __setitem__(self, key, value):
    h = get_hash(self.__size, key)

    if self.__array[h] == 0:
      self.__array[h] = Item(key, value)

    else:
      curr_item = self.__array[h]
      while curr_item.key != key and curr_item.chain is not None:
        curr_item = curr_item.chain
      curr_item.chain = Item(key, value)     

  def __getitem__(self, key):
    h = get_hash(self.__size, key)
    if self.__array[h] == 0:
      raise NameError(f"{key} does not exist!")
    else:
      curr_item = self.__array[h]
      while curr_item.key != key and curr_item.chain is not None:
        curr_item = curr_item.chain

      if curr_item.key is not key:
        raise NameError(f"{key} does not exist!")
      else:
        return curr_item.value

  def __delitem__(self, key):
    pass

  def __contains__(self, key):
    h = get_hash(self.__size, key)
    if self.__array[h] == 0:
      return False
    else:
      curr_item = self.__array[h]
      while curr_item.key != key and curr_item.chain is not None:
        curr_item = curr_item.chain

      if curr_item.key is not key:
        return False
      else:
        return True

  def __iter__(self):
    pass




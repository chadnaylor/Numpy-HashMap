from collections.abc import MutableMapping, Iterator
import numpy as np
from get_hash import get_hash
from item import Item

class HashMap(MutableMapping):
  def __init__(self, *args):
    self._size = 2**4 #initialize array length
    self.__array = np.zeros(self._size, dtype=object) #create empty array
    self._len = 0
    self._max_load = 0.2

    for arg in args:
      if type(arg) is not dict:
        raise TypeError(f"HashMap must be initialized empty or with a dict, got {arg} of type {type(arg)}")

      for key, value in arg.items():
        self.__setitem__(key, value)

  def __len__(self):
    return self._len

  def __resize(self):
    old_items = self.__items()
    self._size = 2 * self._size
    self._len = 0
    self.__array = np.zeros(self._size, dtype=object)

    for item, value in old_items:
      self.__setitem__(item, value)  

  def __setitem__(self, key, value):
    h = get_hash(self._size, key)

    curr_item = self.__array[h]
    while curr_item != 0 and curr_item.key != key and curr_item.chain is not None:
      curr_item = curr_item.chain

    if self.__array[h] == 0:
      self.__array[h] = Item(key, value)
      self._len += 1
    elif curr_item.key == key:
      curr_item.value = value
    else:
      curr_item.chain = Item(key, value)    
      self._len += 1 

    if self._len / self._size > self._max_load:
      self.__resize()

  def __getitem__(self, key):
    h = get_hash(self._size, key)
    if self.__array[h] == 0:
      raise NameError(f"{key} does not exist!")
    else:
      curr_item = self.__array[h]
      while curr_item.key != key and curr_item.chain is not None:
        curr_item = curr_item.chain

      if curr_item.key != key:
        raise NameError(f"{key} does not exist!")
      else:
        return curr_item.value

  def __delitem__(self, key):
    h = get_hash(self._size, key)
    if self.__array[h] == 0:
      raise NameError(f"{key} does not exist!")
    elif self.__array[h].key == key:
      if self.__array[h].chain is not None:
        self.__array[h] = self.__array[h].chain
      else: 
        self.__array[h] = 0
      self._len -= 1
      return
    else:
      curr_item = self.__array[h]
      while curr_item.key != key and curr_item.chain is not None:
        if curr_item.chain.key == key:
          if curr_item.chain.chain is not None:
            curr_item.chain = curr_item.chain.chain
          else:
            curr_item.chain = None
          self._len -= 1
          return
        curr_item = curr_item.chain

      raise NameError(f"{key} does not exist!")

  def __contains__(self, key):
    h = get_hash(self._size, key)
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
    return HashMapIterator(self.__array)

  def __items(self):
    items = []
    for item in HashMapIterator(self.__array):
      items.append((item, self.__getitem__(item)))
    return items

class HashMapIterator(Iterator):
  def __init__(self, array):
    self.__values = array[np.nonzero(array)]
    self.__curr = None
    self.__index = 0

  def __next__(self):
    if self.__curr is not None and self.__curr.chain is not None:
      self.__curr = self.__curr.chain  
    elif self.__index < len(self.__values):
      
      self.__curr = self.__values[self.__index]
      self.__index += 1
    else:
      raise StopIteration

    return self.__curr.key

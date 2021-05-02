from collections.abc import MutableMapping
import numpy as np

class HashMap(MutableMapping):
  def __init__(self, *args, **kwargs):
    self._size = 2**10 #initialize array length
    self._array = np.zeros(self._size, dtype=object) #create array

  def __del__(self):
    pass

  def __len__(self):
    pass

  def __setitem__(self, key, value):
    pass

  def __getitem__(self, key):
    pass

  def __delitem__(self, key):
    pass

  def __contains__(self, key):
    pass

  def __iter__(self):
    pass

  def _handle_collision(self):
    pass


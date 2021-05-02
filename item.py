class Item:
  def __init__(self, key, value):
    self.__key = key
    self.__value = value
    self.__chain = None

  @property
  def key(self):
    return self.__key

  @property
  def value(self):
    return self.__value

  @property
  def chain(self):
    return self.__chain

  @chain.setter
  def chain(self, chain):
    if type(chain) is not Item:
      raise TypeError("Chained value must be an Item")
    self.__chain = chain
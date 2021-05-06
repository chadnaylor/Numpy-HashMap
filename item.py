class Item:
  def __init__(self, key, value):
    self.__key = key
    self.value = value
    self.__chain = None

  @property
  def key(self):
    return self.__key

  @property
  def chain(self):
    return self.__chain

  @chain.setter
  def chain(self, chain):
    if type(chain) is not Item and chain is not None:
      raise TypeError("Chained value must be an Item, got ", chain)
    self.__chain = chain
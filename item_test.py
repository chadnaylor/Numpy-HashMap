from item import Item
import pytest
from hypothesis import given, find, settings, Verbosity, strategies as st
import test_helpers

### Uncomment this line to show test inputs
# settings(verbosity=Verbosity.verbose)

@given(key=test_helpers.RANDOM_KEYS, value=test_helpers.RANDOM_VALUES)
def test_immutable_key(key, value):
    i = Item(key=key, value=value)
    with pytest.raises(AttributeError):
      i.key = "Some key"

@given(key=test_helpers.RANDOM_KEYS, value=test_helpers.RANDOM_VALUES)
def test_immutable_value(key, value):
    i = Item(key=key, value=value)
    with pytest.raises(AttributeError):
      i.value = "Some value"

@given(key=test_helpers.RANDOM_KEYS, value=test_helpers.RANDOM_VALUES)
def test_get_key(key, value):
    i = Item(key=key, value=value)
    assert i.key == key

@given(key=test_helpers.RANDOM_KEYS, value=test_helpers.RANDOM_VALUES)
def test_get_value(key, value):
    i = Item(key=key, value=value)
    assert i.value == value

@given(key=test_helpers.RANDOM_KEYS, value=test_helpers.RANDOM_VALUES)
def test_set_chain_type(key, value):
    i = Item(key=key, value=value)
    with pytest.raises(TypeError):
      i.chain = "Not an Item object"

@given(
  key=test_helpers.RANDOM_KEYS, 
  value=test_helpers.RANDOM_VALUES,
  key2=test_helpers.RANDOM_KEYS, 
  value2=test_helpers.RANDOM_VALUES
)
def test_set_chain(key, value, key2, value2):
  i = Item(key=key, value=value)
  i2 = Item(key=key2, value=value2)

  i.chain = i2
  assert i.chain == i2

from hashmap import HashMap
import pytest
from hypothesis import given, strategies as st
import test_helpers

@given(test_helpers.RANDOM_DICTS)
def test_init_from_dict(d):
  HashMap(d)

@given(st.one_of(st.integers(), st.booleans(), st.text(), st.floats())) 
def test_init_other_types(args):
  with pytest.raises(TypeError):
    HashMap(args)

@given(test_helpers.RANDOM_KEYS)
def test_getitem_dne(i):
  hashmap = HashMap()
  with pytest.raises(NameError):
    hashmap[i]

@given(init=test_helpers.RANDOM_DICTS)
def test_getitem(init):
  hashmap = HashMap(init)
  for item in init:
    assert hashmap[item] == init[item]

@given(init=test_helpers.RANDOM_DICTS)
def test_contains(init):
  hashmap = HashMap(init)
  for item in init:
    assert item in hashmap

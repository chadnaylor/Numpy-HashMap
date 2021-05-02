from hashmap import HashMap
import pytest
from hypothesis import given, find, settings, Verbosity, strategies as st
import test_helpers

### Uncomment this line to show all test inputs
### Use this line as a decorator to see inputs for a given test
# settings(verbosity=Verbosity.verbose)

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
def test_iter(init):
  hashmap = HashMap(init)

  i = 0
  for item in hashmap:
    assert hashmap[item] == init[item]
    i +=1

  assert len(init) == i

@given(init=test_helpers.RANDOM_DICTS)
def test_contains(init):
  hashmap = HashMap(init)
  for item in init:
    assert item in hashmap

@given(init=test_helpers.RANDOM_DICTS)
def test_len(init):
  hashmap = HashMap(init)
  assert len(hashmap) == len(init)

@given(init=test_helpers.RANDOM_DICTS)
def test_delitem(init):
  hashmap = HashMap(init)

  for item in init:
    curr_len = len(hashmap)
    del hashmap[item]

    assert item not in hashmap
    assert len(hashmap) == curr_len - 1

@given(
  init=test_helpers.RANDOM_DICTS, 
  key = test_helpers.RANDOM_KEYS, 
  value = test_helpers.RANDOM_VALUES
)
def test_setitem(init, key, value):
  hashmap = HashMap(init)
  curr_len = len(hashmap)

  hashmap[key] = value
  assert hashmap[key] == value
  if key not in init:
    assert len(hashmap) == curr_len + 1

@given(
  init=test_helpers.RANDOM_DICTS, 
  newvalue = test_helpers.RANDOM_VALUES 
)
def test_setitem_existing(init, newvalue):
  hashmap = HashMap(init)
  for item in init:
    curr_len = len(hashmap)

    hashmap[item] = newvalue
    assert hashmap[item] == newvalue
    assert len(hashmap) == curr_len

@given(st.dictionaries(st.integers(), st.integers(), min_size=2**6, max_size=2**9))
def test_grow_array(init):
  hashmap = HashMap(init)
  for item in init:
    assert item in hashmap
    assert hashmap[item] == init[item]

  

from hashmap import HashMap
import pytest
from hypothesis import given, strategies as st
import test_helpers

@given(test_helpers.RANDOM_DICTS)
def test_fuzz_HashMap(d):
  HashMap(*d)
  HashMap(d)

@given(test_helpers.RANDOM_KEYS)
def test_getitem(i):
  hashmap = HashMap()

  with pytest.raises(NameError):
    hashmap[i]

  

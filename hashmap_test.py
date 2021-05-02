from hashmap import HashMap
import pytest
from hypothesis import given, strategies as st

random_dict = st.dictionaries(
  st.one_of(st.integers(), st.text()), 
  st.one_of(st.integers(), st.text(), st.lists(st.integers()))
)

@given(random_dict)
def test_fuzz_HashMap(d):
  HashMap(*d)
  HashMap(d)

@given(st.one_of(st.integers(), st.text()))
def test_getitem(i):
  hashmap = HashMap()

  with pytest.raises(NameError):
    hashmap[i]

  

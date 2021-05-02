from get_hash import get_hash
from hypothesis import given, find, settings, Verbosity,  strategies as st

### Uncomment this line to show test inputs
# settings(verbosity=Verbosity.verbose)

@given(size=st.integers(min_value=1), key=st.one_of(st.integers(), st.text()))
def test_correct_range(size, key):
    h = get_hash(size=size, key=key)
    assert type(h) is int
    assert h >= 0
    assert h <= size-1

@given(size=st.integers(min_value=1), key=st.one_of(st.integers(), st.text()))
def test_consistency(size, key):
    assert get_hash(size=size, key=key) == get_hash(size=size, key=key)

@given(l=st.lists(st.one_of(st.integers(), st.text()), unique=True, min_size=1, max_size=100))

def test_few_collisions(l):
    uniques = set()
    size = 2**10

    for h in l:
        uniques.add(get_hash(size, h))

    assert len(uniques) >= len(l)/2
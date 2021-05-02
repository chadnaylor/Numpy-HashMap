from hypothesis import strategies as st

RANDOM_KEYS = st.one_of(st.integers(), st.text())
RANDOM_VALUES = st.one_of(st.integers(), st.text())

RANDOM_DICTS = st.dictionaries(
  st.one_of(st.integers(), st.text()), 
  st.one_of(st.integers(), st.text(), st.lists(st.integers()))
)
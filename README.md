# Numpy HashMap

Numpy Hashmap explores several approaches for performant Hash Table behavior, without making use of python's built-in dict or other hashmap primitives. 

Structures:

**HashMap** class in hashmap.py uses a 1-D numpy array for storing key-value pairs, and resolves collisions by chaining
**HashMapList** class in hashmap_list.py is identical to hashmap.py, but uses python's list primitive 

## Installation

```bash
pip install -r requirements.txt
```

## Usage

HashMap implements the **MutableMapping** abstract base class, and behaves accordingly.

```python
from hashmap import HashMap

### Empty HashMap
hashmap = HashMap()

### Instantiate with dict 
hashmap = HashMap({1: "First value", "2": 1234, "Third key": [1, 2, 4]})

### Insert
hashmap["key"] = "value"

### Contains, Get
if "key" in hashmap:
  print(hashmap["key"])

### Delete
del hashmap["key"]

### Iterator
for key in hashmap:
  print(hashmap[key])
```

## Tests

Run test suites

```bash
pytest
```

The test inputs are generated by the hypothesis framework.  

To see all inputes for a given suite, uncomment this line:

```python
# settings(verbosity=Verbosity.verbose)
```

To see all inputs for a specific test, add this decorator:
```python
@settings(verbosity=Verbosity.verbose)
```

## Benchmarks

**Benchmarks.ipynb** contains plots of the relative performance of these implementations against python's dict.  Both implementations are about 6x slower than dict, but run in **constant time**.  The difference seems to be due to the extra calls needed to set up the chained objects. 

## License
[MIT](https://choosealicense.com/licenses/mit/)

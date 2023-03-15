# PascalArray

An implementation of an integer array that is constructed with custom lower and upper bound indexes.

Every slot in the array is initialized with value `0`.

```java

PascalArray posArray = new PascalArray(1, 5);
// posArray -> [0, 0, 0, 0, 0]
// indexes      1  2  3  4  5

PascalArray negArray = new PascalArray(-3, -1);
// negArray -> [0, 0, 0]
// indexes     -3 -2 -1

```
## `PascalArray.get(int "index")`

The `get()` class method get the value from the specified index. If the index is out of range this method will raise an Exception.

## `PascalArray.set(int "index", int "value")`

The `set()` class method sets a value in the specified index. If the index is out of range this method will raise an Exception.

```java

posArray.set(1, 42);
// posArray -> [42, 0, 0, 0, 0]

int value = posArray.get(1);
// value -> 42

```

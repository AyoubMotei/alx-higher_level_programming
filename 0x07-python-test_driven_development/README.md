# Python - Test-driven development

This project focuses on test-driven development in Python, utilizing the `docstring` and `unittest` modules.

## Tests :heavy_check_mark:

**tests**: This folder contains test files, including both Holberton-provided tests and independently-developed ones:
- [0-add_integer.txt](./tests/0-add_integer.txt)
- [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
- [3-say_my_name.txt](./tests/3-say_my_name.txt)
- [4-print_square.txt](./tests/4-print_square.txt)
- [5-text_indentation.txt](./tests/5-text_indentation.txt)
- [6-max_integer_test.py](./tests/6-max_integer_test.py)
- [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
- [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

This project includes the following function prototypes:

| File                   | Prototype                                |
| ---------------------- | ---------------------------------------- |
| `0-add_integer.py`     | `def add_integer(a, b=98):`              |
| `2-matrix_divided.py`  | `def matrix_divided(matrix, div):`       |
| `3-say_my_name.py`     | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`    | `def print_square(size):`                |
| `5-text_indentation.py`| `def text_indentation(text):`            |
| `100-matrix_mul.py`    | `def matrix_mul(m_a, m_b):`              |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`         |
| `102-python.c`         | `void print_python_string(PyObject *p);` |

## Tasks :page_with_curl:

### 0. Integers addition

- File: [0-add_integer.py](./0-add_integer.py)
- Description: This Python function returns the integer addition of two numbers.
- Error Handling:
  - If either `a` or `b` is not an `int` or `float`, it raises a `TypeError` with the message `a must be an integer` or `b must be an integer`.
  - If either `a` or `b` is a `float`, it is casted to an `int` before addition.

### 1. Divide a matrix

- File: [2-matrix_divided.py](./2-matrix_divided.py)
- Description: This Python function divides all elements of a matrix by a common divisor.
- Returns: It returns a new matrix representing the division of all elements of `matrix` by `div`.
- Error Handling:
  - If `matrix` is not a list of lists of `int`s or `float`s, it raises a `TypeError` with the message `matrix must be a matrix (list of lists) of integers/floats`.
  - If `matrix` contains rows of different lengths, it raises a `TypeError` with the message `Each row of the matrix must have the same size`.
  - If the divisor `div` is not an `int` or `float`, it raises a `TypeError` with the message `div must be a number`.
  - If `div` is `0`, it raises a `ZeroDivisionError` with the message `division by zero`.

### 2. Say my name

- File: [3-say_my_name.py](./3-sOops, it seems the text got cut off again. Here's the rest of the content:

```markdown
- File: [3-say_my_name.py](./3-say_my_name.py)
- Description: This Python function prints a name in the format "My name is \<first_name\> \<last_name\>".
- Error Handling:
  - If either `first_name` or `last_name` is not a `str`, it raises a `TypeError` with the message `first_name must be a string` or `last_name must be a string`.

### 3. Print square

- File: [4-print_square.py](./4-print_square.py)
- Description: This Python function prints a square using the `#` character.
- Parameters: The parameter `size` represents the height/width of the square.
- Error Handling:
  - If `size` is not an `int`, it raises a `TypeError` with the message `size must be an integer`.
  - If `size` is less than `0`, it raises a `ValueError` with the message `size must be >= 0`.

### 4. Text indentation

- File: [5-text_indentation.py](./5-text_indentation.py)
- Description: This Python function prints text with indentation.
- Error Handling:
  - If `text` is not a `str`, it raises a `TypeError` with the message `text must be a string`.
- Additional Details:
  - Two new lines are printed after any `.`, `?`, or `:` character.
  - No spaces are printed at the beginning or end of each printed line.

### 5. Max integer - Unittest

- File: [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)
- Description: This Python class/script runs unittests for the function `def max_integer(list=[]):` (provided by Holberton School).

### 6. Matrix multiplication

- File: [100-matrix_mul.py](./100-matrix_mul.py)
- Description: This Python function multiplies two matrices.
- Returns: It returns a new matrix representing the multiplication of `m_a` by `m_b`.
- Error Handling:
  - If either `m_a` or `m_b` is empty (i.e., `== []` or `== [[]]`), it raises a `ValueError` with the message `m_a can't be empty` or `m_b can't be empty`.
  - If either `m_a` or `m_b` is not a list, it raises a `TypeError` with the message `m_a must be a list` or `m_b must be a list`.
  - If either `m_a` or `m_b` is not a list of lists, it raises a `TypeError` with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
  - If either `m_a` or `m_b` is not a list of lists of `int`s or `float`s, it raises a `TypeError` with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`.
  - If either `m_a` or `m_b` contains rows of different lengths, it raises a `TypeError` with the message `each row of m_a must should be of the same size` or `each row of m_b must should be of the same size`.
  - If `m_a` and `m_b` cannot be multiplied (i.e., the row size of `m_a` does not match the column size of `m_b`), it raises aOops, it seems the text got cut off again. Here's the rest of the content:


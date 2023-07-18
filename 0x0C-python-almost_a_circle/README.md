
n - Almost a circle

In this project, I implemented a Python object-oriented programming solution by creating a trio of interconnected classes that serve to represent rectangles and squares. To ensure the reliability and accuracy of the classes, I developed a custom test suite utilizing the `unittest` module. The test suite thoroughly examines the functionality of each class.

The three classes make effective use of a range of essential Python tools and concepts, including but not limited to:
- Importing modules
- Handling exceptions
- Utilizing private attributes
- Implementing getter and setter methods
- Incorporating class and static methods
- Leveraging the power of inheritance
- Managing file input/output operations
- Utilizing `args` and `kwargs` for flexible argument handling
- Employing JSON and CSV serialization and deserialization techniques
- Conducting comprehensive unit testing using the `unittest` module

## Tests :heavy_check_mark:

- `tests/test_models`: This directory contains independently-developed test files for each class, namely:
  - `test_base.py`
  - `test_rectangle.py`
  - `test_square.py`

## Classes :cl:

### Base

The "base" class acts as the foundation for all other classes within the project. It encompasses the following key elements:

- A private class attribute known as `__nb_objects = 0`.
- A public instance attribute called `id`.
- A class constructor defined as `def __init__(self, id=None)`:
  - If `id` is left unspecified (i.e., `None`), it automatically increments the `__nb_objects` count and assigns the resulting value to the public instance attribute `id`.
  - Otherwise, if `id` is provided, it assigns the given value to the public instance attribute `id`.
- A static method named `def to_json_string(list_dictionaries):`, responsible for returning the JSON string serialization of a list of dictionaries.
  - In case the input `list_dictionaries` is either `None` or empty, the method returns the string "[]".
- A class method titled `def save_to_file(cls, list_objs):`, designed to write the JSON serialization of a list of objects to a file.
  - The method expects the parameter `list_objs` to be a list consisting of instances derived from the `Base` class.
  - If `list_objs` is `None`, the method saves an empty list.
  - The resulting file is saved with a name corresponding to the class name (e.g., `Rectangle.json`).
  - If the file already exists, it gets overwritten.
- A static method named `def from_json_string(json_string):`, responsible for deserializing a JSON string into a list of objects.
  - The method assumes that the input `json_string` represents a string of dictionaries.
  - If the `json_string` is either `None` or empty, the method returns an empty list.
- A class method titled `def create(cls, **dictionary):`, which facilitates the instantiation of an object with the provided attributes.
  - It creates an object using the attributes provided via the `**dictionary`.
- A class method called `def load_from_file(cls):`, responsible for returning a list of objects instantiated from a JSON file.
  - The method reads data from a JSON file named after the class (e.g., `Rectangle.json`).
  - If the file does not exist, the method returns an empty list.
- A class method known as `def save_to_file_csv(cls, list_objs):`, which writes the CSV serialization of a list of objects to a file.
  - The method expects the parameter `list_objs` to be a list comprising instances derived from the `Base` class.
  - If `list_objs` is `None`, the method saves an empty list.
  - The resulting file is saved with a name corresponding to the class name (e.g., `Rectangle.csv`).
  - Objects are serialized in the format `<id>,<width>,<height>,<x>,<y>` for Rectangle instances and `<id>,<size>,<x>,<y>` for Square instances.
- A class method titled `def load_from_file_csv(cls):`, designed to return a list of objects instantiated from a CSV file.
  - The method reads data from a CSV file named after the class (e.g., `Rectangle.csv`).
  - If the file does not exist, the method returns an empty list.
- A static method called `def draw(list_rectangles, list_squares):`, responsible for drawing instances of Rectangle and Square in a graphical user interface (GUI) window using the `turtle` module.
  - The method expects `list_rectangles` to be a list of Rectangle objects to be displayed.
  - Similarly, `list_squares` should be a list of Square objects to be displayed.

### Rectangle

The Rectangle class represents a rectangle and inherits from the Base class. It incorporates the following aspects:

- Private instance attributes, namely `__width`, `__height`, `__x`, and `__y`.
- Each private instance attribute has its own respective getter and setter methods.
- A class constructor defined as `def __init__(self, width, height, x=0, y=0, id=None)`:
  - In case any of the attributes (`width`, `height`, `x`, or `y`) is not an integer, the constructor raises a `TypeError` exception with the message `<attribute> must be an integer`.
  - If either the width or height is greater than or equal to 0, the constructor raises a `ValueError` exception with the message `<attribute> must be > 0`.
  - Similarly, if either the x or y is less than 0, the constructor raises a `ValueError` exception with the message `<attribute> must be >= 0`.
- A public method named `def area(self):`, responsible for calculating and returning the area of the Rectangle instance.
- A public method titled `def display(self):`, used to print the Rectangle instance to the standard output (stdout) using the `#` character.
  - The method prints new lines for the y coordinate and spaces for the x coordinate.
- An overridden `__str__` method that facilitates printing a Rectangle instance in the format `[Rectangle] (<id>) <x>/<y>`.
- A public method known as `def update(self, *args, **kwargs):`, which updates an instance of a Rectangle with the given attributes.
  - The method expects `*args` to be supplied in the following order:
    - 1st: id
    - 2nd: width
    - 3rd: height
    - 4th: x
    - 5th: y
  - If `**kwargs` is a double pointer to a dictionary containing new key/value attributes, it updates the Rectangle instance accordingly.
  - If `*args` is provided, `**kwargs` is skipped.
- A public method called `def to_dictionary(self):`, which returns the dictionary representation of a Rectangle instance.

### Square

The Square class represents a square and inherits from the Rectangle class. It incorporates the following elements:

- A class constructor defined as `def __init__(self, size, x=0, y=0, id=None)`:
  - The width and height attributes of the Rectangle superclass are assigned using the value of `size`.
- An overridden `__str__` method that enables the printing of a Square instance in the format `[Square] (<id>) <x>/<y>`.
- A public method titled `def update(self, *args, **kwargs):`, used to update an instance of a Square with the given attributes.
  - The method expects `*args` to be supplied in the following order:
    - 1st: id
    - 2nd: size
    - 3rd: x
    - 4th: y
  - If `**kwargs` is a double pointer to a dictionary containing new key/value attributes, it updates the Square instance accordingly.
  - If `*args` is provided, `**kwargs` is skipped.
- A public method known as `def to_dictionary(self):`, which returns the dictionary representation of a Square instance.

If you require any further clarification or have additional questions regarding this project, please feel free to inquire.


# alx-higher_level_programming

This repository contains Python programs and classes that cover various topics in higher-level programming. Each directory corresponds to a specific topic, and each file within the directory contains a program or class related to that topic.

## Directory: 0x08-python-more_classes

### File: 0-rectangle.py

This file contains an empty class `Rectangle` that defines a rectangle. The class does not import any modules.

### File: 1-rectangle.py

This file contains a class `Rectangle` that defines a rectangle with private instance attributes `width` and `height`. It includes getter and setter methods for these attributes, and it also allows instantiation with optional width and height.

### File: 2-rectangle.py

This file extends the `Rectangle` class from `1-rectangle.py` and adds public instance methods `area` and `perimeter`. These methods calculate the area and perimeter of the rectangle, respectively. The class also includes the same getter and setter methods for the width and height attributes.

### File: 3-rectangle.py

This file further extends the `Rectangle` class from `2-rectangle.py` and overrides the `__str__` method to provide a string representation of the rectangle using the character '#'. The `__str__` method is also used by the print function. Additionally, the class includes an `__repr__` method that returns a string representation of the rectangle that can be used to recreate a new instance using the eval function.

### File: 4-rectangle.py

This file extends the `Rectangle` class from `3-rectangle.py` and adds error handling to the setter methods for width and height. If the provided values are not integers or are less than 0, the methods raise `TypeError` or `ValueError` exceptions, respectively. The `__str__` and `__repr__` methods are also updated to return an empty string if the width or height is 0.

### File: 5-rectangle.py

This file extends the `Rectangle` class from `4-rectangle.py` and adds a message that is printed when an instance of `Rectangle` is deleted. The message "Bye rectangle..." is displayed using the `__del__` method.

### File: 6-rectangle.py

This file extends the `Rectangle` class from `5-rectangle.py` and adds a class attribute `number_of_instances` that keeps track of the number of instances of `Rectangle` created. The attribute is incremented during each new instance instantiation and decremented during each instance deletion.

### File: 7-rectangle.py

This file extends the `Rectangle` class from `6-rectangle.py` and overrides the `__str__` method to change the representation of the rectangle when using the print function. The rectangle is displayed using the character '#' repeated by the width and height values.


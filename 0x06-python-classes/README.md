<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <h1>Descriptions</h1>
    <p>
        In this series of tasks, the objective is to understand and practice object-oriented programming (OOP) concepts in Python while working with geometric shapes. The tasks involve creating classes to represent different shapes such as squares and rectangles, and implementing various functionalities for these shapes.
    </p>
    <ol>
        <li>
            <h2>Area of a circle</h2>
            <p>
                The task focuses on calculating the area of a circle given its radius, introducing the concept of class and method in Python.
            </p>
        </li>
        <li>
            <h2>Define a class called "MagicClass"</h2>
            <p>
                This task involves defining a class that has a single instance attribute and a method that computes and returns the area of a circle using the instance attribute.
            </p>
        </li>
        <li>
            <h2>Coordinates of a square</h2>
            <p>
                This task introduces the concept of class attributes and methods, along with getter and setter methods. It involves creating a class to represent a square, handling size and position attributes, and implementing a method to print the square's shape using "#" characters.
            </p>
        </li>
        <li>
            <h2>Area of a square</h2>
            <p>
                This task extends the previous one by adding a method to calculate the area of a square based on its size.
            </p>
        </li>
        <li>
            <h2>Evaluating a string</h2>
            <p>
                The task involves creating a class with a method that checks if a given string is a palindrome, demonstrating the use of class methods and the concept of palindrome.
            </p>
        </li>
        <li>
            <h2>Coordinates of a square (advanced)</h2>
            <p>
                This task builds upon the previous square representation, introducing error handling by raising exceptions when invalid values are provided for size or position.
            </p>
        </li>
        <li>
            <h2>Multiple squares</h2>
            <p>
                This task demonstrates the use of static methods within a class. It involves comparing the areas of two square objects and returning the square with the larger area.
            </p>
        </li>
        <li>
            <h2>Full rectangle</h2>
            <p>
                The task extends the concept by introducing a new shape, the rectangle. It involves creating a class to represent a rectangle, handling width and height attributes, and implementing a method to calculate the rectangle's area.
            </p>
        </li>
        <li>
            <h2>Square inheritance</h2>
            <p>
                This task explores inheritance by creating a square class that inherits from the rectangle class. It overrides the setter methods to ensure the square's integrity and utilizes the inherited "area" method.
            </p>
        </li>
    </ol>
    <h1>Tasks</h1>
    <ol>
        <li>
            <h2>Task 0: My first square</h2>
            <ul>
                <li>Description:</li>
                <li>Write an empty class Square that defines a square.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 0-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 1: Square with size</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 0.</li>
                <li>Add a private instance attribute size.</li>
                <li>Instantiation with size (no type/value verification).</li>
                <li>You are not allowed to import any module.</li>
                <li>The size attribute must be kept private.</li>
                <li>File: 1-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 2: Size validation</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 1.</li>
                <li>Add a private instance attribute size.</li>
                <li>Instantiation with optional size.</li>
                <li>Size must be an integer, otherwise, raise a TypeError exception with the message size must be an integer.</li>
                <li>If size is less than 0, raise a ValueError exception with the message size must be >= 0.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 2-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 3: Area of a square</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 2.</li>
                <li>Add a public instance method area that returns the current square area.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 3-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 4: Access and update private attribute</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 3.</li>
                <li>Add a getter and setter for the private instance attribute size.</li>
                <li>The setter should validate the assignment of size and raise errors if needed.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 4-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 5: Printing a square</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 4.</li>
                <li>Add a public instance method my_print that prints the square with the character '#'.</li>
                <li>If the size is equal to 0, print an empty line.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 5-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 6: Coordinates of a square</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square based on Task 5.</li>
                <li>Add a private instance attribute position.</li>
                <li>Instantiation with optional size and optional position.</li>
                <li>Position must be a tuple of 2 positive integers, otherwise, raise a TypeError exception with the message position must be a tuple of 2 positive integers.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 6-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 7: Singly linked list (Advanced)</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Node that defines a node of a singly linked list.</li>
                <li>Node has a private instance attribute data and a private instance attribute next_node.</li>
                <li>Write a class SinglyLinkedList that defines a singly linked.</li>
                <li>SinglyLinkedList has a private instance attribute head (representing the head node) and a private instance attribute next_node.</li>
                <li>The SinglyLinkedList class should have the following methods:</li>
                <li>__init__(self) - Initializes an empty linked list.</li>
                <li>__str__(self) - Prints the linked list in a specific format: [&lt;node1.data&gt;] -&gt; [&lt;node2.data&gt;] -&gt; ... -&gt; [&lt;nodeN.data&gt;] -&gt; None.</li>
                <li>sorted_insert(self, value) - Inserts a new Node into the linked list in ascending order based on the data attribute. If the linked list is empty or the new node has a value smaller than the head node, the new node becomes the new head. Otherwise, the new node is inserted at the correct position while maintaining the ascending order.</li>
                <li>__repr__(self) - Returns a string representation of the linked list, which can be used to recreate the linked list.</li>
                <li>The Node class should have the following methods:</li>
                <li>__init__(self, data, next_node=None) - Initializes a new Node with the given data and next_node.</li>
                <li>data(self) - Returns the data of the Node.</li>
                <li>next_node(self) - Returns the next node of the Node.</li>
                <li>You are not allowed to import any module.</li>
                <li>Files:</li>
                <li>100-singly_linked_list.py</li>
                <li>100-main.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 8: Print Square instance (Advanced)</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square with the following requirements:</li>
                <li>Private instance attribute: size:</li>
                <li>Property def size(self): to retrieve the size.</li>
                <li>Property setter def size(self, value): to set the size:</li>
                <li>size must be an integer, otherwise, raise a TypeError exception with the message size must be an integer.</li>
                <li>If size is less than 0, raise a ValueError exception with the message size must be >= 0.</li>
                <li>Private instance attribute: position:</li>
                <li>Property def position(self): to retrieve the position.</li>
                <li>Property setter def position(self, value): to set the position:</li>
                <li>position must be a tuple of 2 positive integers, otherwise, raise a TypeError exception with the message position must be a tuple of 2 positive integers.</li>
                <li>Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):</li>
                <li>Public instance method: def area(self): that returns the current square area.</li>
                <li>Public instance method: def my_print(self): that prints in stdout the square with the character #:</li>
                <li>If size is equal to 0, print an empty line.</li>
                <li>position should be use by using space - Don’t fill lines by spaces when position[1] &gt; 0.</li>
                <li>You are not allowed to import any module.</li>
                <li>File: 101-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 9: Compare 2 squares (Advanced)</h2>
            <ul>
                <li>Description:</li>
                <li>Write a class Square that defines a square with the following requirements:</li>
                <li>Private instance attribute: size:</li>
                <li>Property def size(self): to retrieve the size.</li>
                <li>Property setter def size(self, value): to set the size:</li>
                <li>size must be an integer, otherwise, raise a TypeError exception with the message size must be an integer.</li>
                <li>If size is less than 0, raise a ValueError exception with the message size must be >= 0.</li>
                <li>Private instance attribute: position:</li>
                <li>Property def position(self): to retrieve the position.</li>
                <li>Property setter def position(self, value): to set the position:</li>
                <li>position must be a tuple of 2 positive integers, otherwise, raise a TypeError exception with the message position must be a tuple of 2 positive integers.</li>
                <li>Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):</li>
                <li>Public instance method: def area(self): that returns the current square area.</li>
                <li>Public instance method: def my_print(self): that prints in stdout the square with the character #:</li>
                <li>If size is equal to 0, print an empty line.</li>
                <li>position should be use by using space - Don’t fill lines by spaces when position[1] &gt; 0.</li>
                <li>You are not allowed to import any module.</li>
                <li>Comparison:</li>
                <li>You can compare 2 squares (Squares) based on their area.</li>
                <li>You must use the == and != operators.</li>
                <li>Your method __eq__ should return True or False depending on the comparison result.</li>
                <li>Your method __ne__ should return True if self and other are not equal, or False if they are.</li>
                <li>File: 102-square.py</li>
            </ul>
        </li>
        <li>
            <h2>Task 10: ByteCode -> Python #5 (Advanced)</h2>
            <ul>
                <li>Description:</li>
                <li>Write the Python class MagicClass that does exactly the same as the following Python bytecode:</li>
                <pre>
                    <code>
                        def magic_calculation(a, b):
                            return 98 + (a ** b)
                    </code>
                </pre>
                <li>Your code should be written in the file 103-magic_class.py</li>
                <li>You are not allowed to use the type() function.</li>
                <li>Your code should use the same bytecode as the one shown above.</li>
                <li>You are not allowed to import any module.</li>
            </ul>
        </li>
    </ol>
</div>

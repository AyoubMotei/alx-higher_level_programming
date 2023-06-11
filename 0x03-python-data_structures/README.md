<!DOCTYPE html>
<html>

<head>
   
</head>

<body>
    <h1>0x03-python-data_structures</h1>
    <p>This repository contains solutions to the following tasks:</p>
    <ul>
        <li>
            <h3>0-print_list_integer.py</h3>
            <p>Write a function <code>print_list_integer(my_list=[])</code> that prints all integers of a list.</p>
            <ul>
                <li>Prototype: <code>def print_list_integer(my_list=[])</code></li>
                <li>Format: one integer per line.</li>
            </ul>
        </li>
        <li>
            <h3>1-element_at.py</h3>
            <p>Write a function <code>element_at(my_list, idx)</code> that retrieves an element from a list like in C.</p>
            <ul>
                <li>Prototype: <code>def element_at(my_list, idx)</code></li>
                <li>If idx is negative, the function should return None.</li>
                <li>If idx is out of range (> number of elements in my_list), the function should return None.</li>
                <li>You are not allowed to import any module.</li>
                <li>You are not allowed to use try/except.</li>
            </ul>
        </li>
        <li>
            <h3>2-replace_in_list.py</h3>
            <p>Write a function <code>replace_in_list(my_list, idx, element)</code> that replaces an element of a list at a specific position (like in C).</p>
            <ul>
                <li>Prototype: <code>def replace_in_list(my_list, idx, element)</code></li>
                <li>If idx is negative, the function should not modify anything, and returns the original list.</li>
                <li>If idx is out of range (> number of elements in my_list), the function should not modify anything, and returns the original list.</li>
                <li>You are not allowed to import any module.</li>
                <li>You are not allowed to use try/except.</li>
            </ul>
        </li>
        <li>
            <h3>3-print_reversed_list_integer.py</h3>
            <p>Write a function <code>print_reversed_list_integer(my_list=[])</code> that prints all integers of a list, in reverse order.</p>
            <ul>
                <li>Prototype: <code>def print_reversed_list_integer(my_list=[])</code></li>
                <li>Format: one integer per line.</li>
            </ul>
        </li>
        <li>
            <h3>4-new_in_list.py</h3>
            <p>Write a function <code>new_in_list(my_list, idx, element)</code> that replaces an element in a list at a specific position without modifying the original list (like in C).</p>
            <ul>
                <li>Prototype: <code>def new_in_list(my_list, idx, element)</code></li>
                <li>If idx is negative, the function should return a copy of the original list.</li>
                <li>If idx is out of range (> number of elements in my_list), the function should return a copy of the original list.</li>
                <li>You are not allowed to import any module.</li>
                <li>You are not allowed to use try/except.</li>
            </ul>
        </li>
        <li>
            <h3>5-no_c.py</h3>
            <p>Write a function <code>no_c(my_string)</code> that removes all characters c and C from a string.</p>
            <ul>
                <li>Prototype: <code>def no_c(my_string)</code></li>
                <li>The function should return the new string.</li>
                <li>You are not allowed to import any module.</li>
                <li>You are not allowed to use <code>str.replace()</code>.</li>
            </ul>
        </li>
        <li>
            <h3>6-print_matrix_integer.py</h3>
            <p>Write a function <code>print_matrix_integer(matrix=[[]])</code> that prints a matrix of integers.</p>
            <ul>
                <li>Prototype: <code>def print_matrix_integer(matrix=[[]])</code></li>
                <li>You are not allowed to import any module.</li>
                <li>You have to use <code>str.format()</code> to print integers.</li>
            </ul>
        </li>
        <li>
            <h3>7-add_tuple.py</h3>
            <p>Write a function <code>add_tuple(tuple_a=(), tuple_b=())</code> that adds 2 tuples.</p>
            <ul>
                <li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=())</code></li>
                <li>The function should return a tuple with 2 integers:</li>
                <ul>
                    <li>The first element should be the addition of the first element of each argument.</li>
                    <li>The second element should be the addition of the second element of each argument.</li>
                </ul>
                <li>You are not allowed to import any module.</li>
                <li>You can assume that the two tuples will only contain integers.</li>
                <li>If a tuple is smaller than 2, use the value 0 for each missing integer.</li>
                <li>If a tuple is bigger than 2.</li>
            </ul>
        </li>
        <li>
            <h3>8. More returns!</h3>
            <p>This script contains a function that returns a tuple with the length of a string and its first character. If the sentence is empty, the first character will be None. No module imports are allowed.</p>
        </li>
        <li>
            <h3>9. Find the max</h3>
            <p>This script contains a function that finds the biggest integer in a list. If the list is empty, None is returned. No module imports are allowed.</p>
        </li>
        <li>
            <h3>10. Only by 2</h3>
            <p>Description: This script contains a function that finds all multiples of 2 in a list. The function returns a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2. The new list has the same size as the original list. No module imports are allowed.</p>
        </li>
        <li>
            <h3>11. Delete at</h3>
            <p>This script contains a function that deletes the item at a specific position in a list. If the index (idx) is negative or out of range, nothing changes (the same list is returned). No module imports are allowed.</p>
        </li>
        <li>
            <h3>12. Switch</h3>
            <p>This script contains a program with source code to switch the values of variables a and b. The code should be inserted where the comment is, and the program should be exactly 5 lines long.</p>
        </li>
        <li>
            <h3>13. Linked list palindrome</h3>
            <p>This repository contains a C function that checks if a singly linked list is a palindrome. The function has the prototype <code>int is_palindrome(listint_t **head)</code>. It returns 0 if the list is not a palindrome, and 1 if it is a palindrome. An empty list is considered a palindrome.</p>
        </li>
        <li>
            <h3>14. CPython #0: Python lists</h3>
            <p>This C program prints some basic information about Python lists. The function <code>print_python_list_info(PyObject *p)</code> is implemented. The program is compiled into a shared library named <code>libPyList.so</code> using the provided command. The program is tested using the <code>100-test_lists.py</code> Python script.</p>
        </li>
    </ul>
</body>

</html>


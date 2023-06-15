<!DOCTYiPE html>
<html>
<head>
  <title></title>
</head>
<body>
  <h1>0x04-python-more_data_structures</h1>
  <p>
    This directory contains Python programs and a C file for the ALX Higher Level Programming curriculum's "0x04. Python - More Data Structures: Set, Dictionary" project. Each task focuses on different aspects of Python data structures and their manipulation.
  </p>
  <h2>Files</h2>
  <ul>
    <li>
      <strong>0-square_matrix_simple.py</strong><br>
      This file contains a function <code>square_matrix_simple(matrix)</code> that computes the square value of all integers in a matrix. The function takes a 2-dimensional matrix as input and returns a new matrix with each value being the square of the corresponding value in the input matrix. The input matrix remains unchanged. The function does not use any imported modules and can use regular loops, map, etc.
    </li>
    <li>
      <strong>1-search_replace.py</strong><br>
      This file contains a function <code>search_replace(my_list, search, replace)</code> that replaces all occurrences of an element <code>search</code> with another element <code>replace</code> in a new list. The function takes an initial list <code>my_list</code> as input and returns a new list with the specified replacements. The function does not use any imported modules.
    </li>
    <li>
      <strong>2-uniq_add.py</strong><br>
      This file contains a function <code>uniq_add(my_list)</code> that adds all unique integers in a list, considering each integer only once. The function takes a list <code>my_list</code> as input and returns the sum of all unique integers in the list. The function does not use any imported modules.
    </li>
    <li>
      <strong>3-common_elements.py</strong><br>
      This file contains a function <code>common_elements(set_1, set_2)</code> that returns a set of common elements between two sets. The function takes two sets <code>set_1</code> and <code>set_2</code> as input and returns a new set containing the common elements. The function does not use any imported modules.
    </li>
    <li>
      <strong>4-only_diff_elements.py</strong><br>
      This file contains a function <code>only_diff_elements(set_1, set_2)</code> that returns a set of elements that are present in only one of the two input sets. The function takes two sets <code>set_1</code> and <code>set_2</code> as input and returns a new set containing the elements that are unique to either set. The function does not use any imported modules.
    </li>
    <li>
      <strong>5-number_keys.py</strong><br>
      This file contains a function <code>number_keys(a_dictionary)</code> that returns the number of keys in a dictionary. The function takes a dictionary <code>a_dictionary</code> as input and returns the count of keys in the dictionary. The function does not use any imported modules.
    </li>
    <li>
      <strong>6-print_sorted_dictionary.py</strong><br>
      This file contains a function <code>print_sorted_dictionary(a_dictionary)</code> that prints the keys of a dictionary in alphabetical order. The function takes a dictionary <code>a_dictionary</code> as input and prints the keys in sorted order. The keys are sorted based on their alphabetic order. The function does not use any imported modules.
    </li>
    <li>
      <strong>7-update_dictionary.py</strong><br>
      This file contains a function <code>update_dictionary(a_dictionary, key, value)</code> that replaces or adds a key/value pair in a dictionary. The function takes a dictionary <code>a_dictionary</code>, a key <code>key</code>, and a value <code>value</code> as input. If the key exists in the dictionary, the corresponding value is replaced with the new value. If the key doesn't exist, a new key/value pair is added to the dictionary. The function does not use any imported modules.
    </li>
    <li>
      <strong>8-simple_delete.py</strong><br>
      This file contains a function <code>simple_delete(a_dictionary, key="")</code> that deletes a key from a dictionary. The function takes a dictionary <code>a_dictionary</code> and a key <code>key</code> (optional) as input. If the key exists in the dictionary, it is removed from the dictionary. If the key doesn't exist, the dictionary remains unchanged. The function does not use any imported modules.
    </li>
    <li>
      <strong>9-multiply_by_2.py (continued)</strong><br>
      This file contains a function <code>multiply_by_2(a_dictionary)</code> that returns a new dictionary with the same keys as the input dictionary <code>a_dictionary</code>, but with the corresponding values multiplied by 2. The function takes a dictionary <code>a_dictionary</code> as input and returns a new dictionary with the modified values. The input dictionary remains unchanged. The function does not use any imported modules.
    </li>
    <li>
      <strong>10-best_score.py</strong><br>
      This file contains a function <code>best_score(a_dictionary)</code> that returns the key with the highest integer value in a dictionary. The function takes a dictionary <code>a_dictionary</code> as input and returns the key with the highest value. If multiple keys have the same highest value, the function returns any of those keys. If the dictionary is empty, the function returns None. The function does not use any imported modules.
    </li>
    <li>
      <strong>11-mutiply_list_map.py</strong><br>
      This file contains a function <code>mutiply_list_map(my_list=[], number=0)</code> that multiplies all integers in a list by a specified number using the map() function. The function takes an optional list <code>my_list</code> and a number <code>number</code> as input. If no list is provided, an empty list is used. The function returns a new list with the multiplied values. The original list remains unchanged.
    </li>
    <li>
      <strong>12-roman_to_int.py</strong><br>
      This file contains a function <code>roman_to_int(roman_string)</code> that converts a Roman numeral string to an integer. The function takes a string <code>roman_string</code> as input and returns the corresponding integer value. If the input string is not a valid Roman numeral, the function returns 0. The function does not use any imported modules.
    </li>
    <li>
      <strong>100-weight_average.py</strong><br>
      This file contains a function <code>weight_average(my_list=[])</code> that calculates the weighted average of a list of tuples. Each tuple in the list represents a pair of values: the first value is a number and the second value is its weight. The function takes an optional list <code>my_list</code> as input. If no list is provided, an empty list is used. The function returns the weighted average as a float. If the list is empty, the function returns 0. The function does not use any imported modules.
    </li>
    <li>
      <strong>101-square_matrix_map.py</strong><br>
      This file contains a function <code>square_matrix_map(matrix=[])</code> that computes the square value of all integers in a matrix using the map() function. The function takes an optional matrix <code>matrix</code> as input. If no matrix is provided, an empty matrix is used. The function returns a new matrix with each value being the square of the corresponding value in the input matrix. The original matrix remains unchanged.
    </li>
    <li>
      <strong>102-complex_delete.py</strong><br>
      This file contains a function <code>complex_delete(a_dictionary, value)</code> that deletes keys from a dictionary based on their corresponding values. The function takes a dictionary <code>a_dictionary</code> and a value <code>value</code> as input. It removes all keys from the dictionary that have the specified value. If the value doesn't exist in the dictionary, the dictionary remains unchanged. The function does not use any imported modules.
    </li>
    <li>
      <strong>103-python.c</strong><br>
      This C program implements two functions, <code>print_python_list</code> and <code>print_python_bytes</code>, that provide basic information about Python lists and Python bytes objects, respectively. These functions are designed to be used with the CPython interpreter version 3.4. The program is compiled into a shared library <code>libPython.so</code> with the specified command line and includes restrictions on the usage of certain macros and functions.
    </li>
    <li>
      <strong>103-tests.py</strong><br>
      This Python script demonstrates the usage of the functions implemented in the <code>103-python.c</code> file. It imports the shared library <code>libPython.so</code> using the <code>ctypes</code> module and calls the functions with various test cases.
    </li>
  </ul>
  <p>
    For more information, refer to the GitHub repository <a href="https://github.com/alx-higher_level_programming">alx-higher_level_programming</a> and navigate to the directory <code>0x04-python-more_data_structures</code>. The specific file related to this task is <code>103-python.c</code>.
  </p>
</body>
</html>

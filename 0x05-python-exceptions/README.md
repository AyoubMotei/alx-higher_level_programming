<!DOCTYPE html>
<html>
<head>
  <title>alx-higher_level_programming</title>
</head>
<body>
  <h1>Description</h1>
  <p>
    This repository contains Python programs written for the ALX Higher Level Programming curriculum.
    The programs cover various topics, including exceptions handling, list manipulation, and function execution.
  </p>
  <h2>Files</h2>
  <ul>
    <li>
      <strong>0-safe_print_list.py:</strong>
      A Python function <code>safe_print_list(my_list=[], x=0)</code> that prints x elements of a list.
      The function uses <code>try</code> and <code>except</code> statements to handle errors and ensure safe printing.
      It does not use the <code>len()</code> function or import any modules.
    </li>
    <li>
      <strong>1-safe_print_integer.py:</strong>
      A Python function <code>safe_print_integer(value)</code> that prints an integer using the <code>"{:d}".format()</code> format specifier.
      The function returns <code>True</code> if the value is an integer and has been printed correctly, otherwise it returns <code>False</code>.
      It uses <code>try</code> and <code>except</code> statements to handle errors and does not import any modules.
    </li>
    <li>
      <strong>2-safe_print_list_integers.py:</strong>
      A Python function <code>safe_print_list_integers(my_list=[], x=0)</code> that prints the first x elements of a list, considering only integers.
      Non-integer elements are skipped without raising an error.
      The function uses <code>try</code> and <code>except</code> statements to handle errors and does not import any modules.
      It does not use the <code>len()</code> function.
    </li>
    <li>
      <strong>3-safe_print_division.py:</strong>
      A Python function <code>safe_print_division(a, b)</code> that divides two integers and prints the result using the <code>"{:d}".format()</code> format specifier.
      The function returns the value of the division, and if the division by zero occurs, it returns <code>None</code>.
      It uses <code>try</code>, <code>except</code>, and <code>finally</code> statements to handle errors.
    </li>
    <li>
      <strong>4-list_division.py:</strong>
      A Python function <code>list_division(my_list_1, my_list_2, list_length)</code> that divides two lists element by element.
      It returns a new list of length list_length with the division results.
      If the division is not possible due to zero division or incompatible types, it handles the corresponding errors and adds 0 to the result list.
      If the lists are too short, it raises an "out of range" error.
      The function uses <code>try</code>, <code>except</code>, and <code>finally</code> statements to handle errors and does not import any modules.
    </li>
    <li>
      <strong>5-raise_exception.py:</strong>
      A Python function <code>raise_exception()</code> that raises a type exception.
      It does not import any modules.
    </li>
    <li>
      <strong>6-raise_exception_msg.py:</strong>
      A Python function <code>raise_exception_msg(message="")</code> that raises a name exception with a specified message.
      It does not import any modules.
    </li>
    <li>
      <strong>100-safe_print_integer_err.py:</strong>
      A Python function <code>safe_print_integer_err(value)</code> that prints an integer using the <code>"{:d}".format()</code> format specifier.
      If an error occurs during printing, it returns <code>False</code> and prints the error message in stderr preceded by "Exception:".
      Otherwise, it returns <code>True</code>.
      The function uses <code>try</code> and <code>except</code> statements to handle errors and does not use the <code>type()</code> function or import any modules.
    </li>
    <li>
      <strong>101-safe_function.py:</strong>
      A Python function <code>safe_function(fct, *args)</code> that executes a function safely.
      It returns the result of the function if no errors occur, otherwise it returns <code>None</code> and prints the error message in stderr preceded by "Exception:".
      The function uses <code>try</code> and <code>except</code> statements to handle errors and does not import any modules.
    </li>
    <li>
      <strong>102-magic_calculation.py:</strong>
      A Python function <code>magic_calculation(a, b)</code> that performs the same operations as the provided Python bytecode.
      The bytecode includes variable assignments, loops, and exception handling.
      The function returns the final value of the variable.
    </li>
  </ul>
</body>
</html>

## Repository: alx-higher_level_programming

### Task 0: Read file
The `read_file` function reads a text file (UTF8) and prints its content to stdout. It uses the `with` statement to ensure proper file handling and does not require the management of file permissions or exceptions. The function takes an optional `filename` parameter, which specifies the name of the file to be read.

### Task 1: Write to a file
The `write_file` function writes a string to a text file (UTF8) and returns the number of characters written. It uses the `with` statement to ensure proper file handling and creates the file if it doesn't exist. If the file already exists, the function overwrites its content. The function takes two parameters: `filename`, which specifies the name of the file to write to, and `text`, which contains the string to be written.

### Task 2: Append to a file
The `append_write` function appends a string at the end of a text file (UTF8) and returns the number of characters added. If the file doesn't exist, it is created. The function uses the `with` statement to ensure proper file handling and takes two parameters: `filename`, which specifies the name of the file to append to, and `text`, which contains the string to be appended.

### Task 3: To JSON string
The `to_json_string` function returns the JSON representation of an object (string). It does not handle exceptions if the object can't be serialized. The function takes one parameter, `my_obj`, which represents the object to be serialized.

### Task 4: From JSON string to Object
The `from_json_string` function returns an object (Python data structure) represented by a JSON string. It does not handle exceptions if the JSON string doesn't represent an object. The function takes one parameter, `my_str`, which represents the JSON string to be deserialized.

### Task 5: Save Object to a file
The `save_to_json_file` function writes an object to a text file, using a JSON representation. It uses the `with` statement to ensure proper file handling and does not handle exceptions if the object can't be serialized. The function takes two parameters: `my_obj`, which represents the object to be serialized and saved, and `filename`, which specifies the name of the file to save the object to.

### Task 6: Create object from a JSON file
The `load_from_json_file` function creates an object from a JSON file. It uses the `with` statement to ensure proper file handling and does not handle exceptions if the JSON string doesn't represent an object. The function takes one parameter, `filename`, which specifies the name of the JSON file to load the object from.

### Task 7: Load, add, save
The `add_item` script adds all arguments to a Python list and then saves them to a file. It uses the `save_to_json_file` function from Task 5 to save the list as a JSON representation in a file named "add_item.json". If the file doesn't exist, it is created.

### Task 8: Class to JSON
The `class_to_json` function returns the dictionary description with a simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object. The function takes one parameter, `obj`, which is an instance of a Class. All attributes of the Class are serializable.

### Task 9: Student to JSON
The `Student` class defines a student by their first name, last name, and age. It has a public method `to_json` that retrieves a dictionary representation of a `Student` instance.

### Task 10: Student to JSON with filter
The `Student` class (based on Task 9) has an additional public method `to_json` with an optional `attrs` parameter. If `attrs` is a list of strings, only attribute names contained in this list are retrieved. Otherwise, all attributes are retrieved.

### Task 11: Student to disk and reload
The `Student` class (based on Task 10) has a public method `reload_from_json` that replaces all attributes of the `Student` instance with the values from a provided dictionary `json`. The class also has an additional public method `save_to_file` that saves the `Student` instance as a JSON representation in a file.

### Task 12: Pascal's Triangle
The `pascal_triangle` function returns a list of lists of integers representing Pascal's triangle of `n`. It returns an empty list if `n` is less than or equal to 0.

### Task 13: Search and update
The `append_after` function inserts a line of text into a file after each line containing a specific string. It uses the `with` statement to ensure proper file handling and does not require the management of file permission or file existence exceptions. The function takes three parameters: `filename`, which specifies the name of the file, `search_string`, which represents the string to search for, and `new_string`, which contains the line of text to be inserted.

### Task 14: Log parsing
The `log_parsing` script reads `stdin` line by line and computes metrics. It reads lines in the format `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`. Every 10 lines, or after a keyboard interruption (`CTRL + C`), it prints statistics based on the accumulated data. The statistics include the total file size and the number of lines by status code, only printing the status codes that appear in the input in ascending order.


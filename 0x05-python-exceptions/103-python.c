#include <Python.h>

void print_python_list(PyObject *list_obj);
void print_python_bytes(PyObject *bytes_obj);
void print_python_float(PyObject *float_obj);

/*
 * print_python_list - Prints basic information about Python lists.
 * @list_obj: A PyObject list object.
 */
void print_python_list(PyObject *list_obj)
{
	Py_ssize_t size, alloc, i;
	const char *elem_type;
	PyListObject *list = (PyListObject *)list_obj;
	PyVarObject *var = (PyVarObject *)list_obj;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python List Information\n");
	if (strcmp(list_obj->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List: %ld\n", size);
	printf("[*] Allocated: %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		elem_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, elem_type);
		if (strcmp(elem_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(elem_type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/*
 * print_python_bytes - Prints basic information about Python byte objects.
 * @bytes_obj: A PyObject byte object.
 */
void print_python_bytes(PyObject *bytes_obj)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)bytes_obj;

	fflush(stdout);

	printf("[.] Bytes Object Information\n");
	if (strcmp(bytes_obj->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  Size: %ld\n", ((PyVarObject *)bytes_obj)->ob_size);
	printf("  Trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)bytes_obj)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)bytes_obj)->ob_size + 1;

	printf("  First %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/*
 * print_python_float - Prints basic information about Python float objects.
 * @float_obj: A PyObject float object.
 */
void print_python_float(PyObject *float_obj)
{
	char *buffer = NULL;

	PyFloatObject *float_val = (PyFloatObject *)float_obj;

	fflush(stdout);

	printf("[.] Float Object Information\n");
	if (strcmp(float_obj->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_val->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  Value: %s\n", buffer);
	PyMem_Free(buffer);
}


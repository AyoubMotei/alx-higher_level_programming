#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Print information about Python bytes objects.
 * @p: Pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	size_t bytes_count, i;
	char *string;

	setbuf(stdout, NULL);
	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = ((PyBytesObject *)(p))->ob_sval;
	bytes_count = PyBytes_Size(p);
	printf("  Size: %ld\n  Trying string: %s\n", bytes_count, string);
	bytes_count >= 10 ? bytes_count = 10 : bytes_count++;
	printf("  First %ld bytes: ", bytes_count);
	for (i = 0; i < bytes_count - 1; i++)
		printf("%02hhx ", string[i]);
	printf("%02hhx\n", string[i]);
}

/**
 * print_python_float - Print information about Python float objects.
 * @p: Pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	char *string;
	double value;

	setbuf(stdout, NULL);
	printf("[.] Float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)(p))->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  Value: %s\n", string);
}

/**
 * print_python_list - Print information about Python list objects.
 * @p: Pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	size_t allocated, size, i;
	const char *type;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
		else if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
	}
}


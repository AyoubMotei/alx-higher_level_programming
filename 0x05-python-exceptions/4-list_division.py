def list_division(my_list_1, my_list_2, list_length):
    division_results = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("TypeError: Cannot divide different types")
            result = 0
        except ZeroDivisionError:
            print("ZeroDivisionError: Division by zero")
            result = 0
        except IndexError:
            print("IndexError: Lists are too short")
            result = 0
        finally:
            division_results.append(result)
    return division_results


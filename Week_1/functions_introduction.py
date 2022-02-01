# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
















#Everybody sees this?
#variables
my_var = 213
my_list = [1, 'cat', 'fray', my_var, print]
my_dict = {
    'cat': 'in the hat',
    'programmer': 'in his pajamas',
    'partner': 'in the bank'}

# data types: int, float, str, bool, etc...

# functions in python


def meet_and_greet(name, secondname):
    print(f"hello {name}, my name is {secondname}.\nHello {secondname}. how are you today?")
    return None
meet_and_greet('Ariel', 'Alisa')

def meet_and_greet(name_list: list) -> None:
    print(f"hello {name_list[0]}, my name is {name_list[1]}.\nHello {name_list[1]}. how are you today?")
    return None


meet_and_greet(['Ariel', 'Savana'])


def meet_and_greet(name_dict: dict) -> None:
    print(f"hello {name_dict['first_name']}, my name is {name_dict['second_name']}.\nHello {name_dict['second_name']}. how are you today?")
    return None

meet_and_greet({'first_name': 'max', 'second_name': 'moris'})

#classwork 1 Q1 A


def convert_metric(unit_value, unit_to_convert_to):
    mile_to_kilometer_conversion = 1.61
    kilometer_to_mile_conversion = 1 / mile_to_kilometer_conversion
    
    if unit_to_convert_to == 'k':
        return unit_value * mile_to_kilometer_conversion
    else:
        return unit_value * kilometer_to_mile_conversion


if __name__ == "__main__":
    print(convert_metric(20, 'k'))
    print(convert_metric(32.2, 'm'))
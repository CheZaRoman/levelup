a_int = 10
b_float = 10.5

# print(int(a_int+b_float))
# a = int(input('Input a = '))
# print(a)
#
# x_list = [1,2,3,4,5,6] # list()
# #x_list = list() # x_list = [] # list()
# x_list[0] = 10 # x_list = [] # list()
# print(x_list)
# x_tuple = (1,2,3,4,5,6) # tuple()
#
# x_set = {1,2,3,4,5,6,5,6}     #set
# print(x_set)
# x = {'key1': 100, 'key2': 200, 'key1': 150} # dict()
# print(x)

# a = 10

# def function():
#     global a
#     print(a)
#     a = 11
#
#
#
# function()
# print(a)

a = 10

def func_sum(a, b, c):
    print(a)
    print(b)
    print(c)
    return a+b+c


# print(func_sum(2, 3, 4))

def default_args(arg1, arg2, arg3=4):
    sum = arg1+arg2
    return sum+arg3


#print(default_args(10, 10, 5))

def func_args_kwargs(*args, **kwargs):
    print(args) # not named arguments <tuple>
    print(kwargs) # with names <dict>

# func_args_kwargs(1,2,3,4,5,6,7,8, a=100, b=200)


def func_args_kwargs_v2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args) # not named arguments <tuple>
    print(kwargs) # with names <dict>

#func_args_kwargs_v2(1,2,3,4,5,6,7,8, a=100, b=200)

# list_a = [1,2,3,4,5,6,7]
# dict_a = {'a': 200, 'b': 300}
#
#
# func_args_kwargs_v2(*list_a)
# # func_args_kwargs_v2(1,2,3,4,5,6,7,8)
# func_args_kwargs_v2(**dict_a)
# # func_args_kwargs_v2(a=200, b=300)


def func_print(msg):
    print(msg)

def return_msg(msg):
    return msg
#
# #1
# value = func_print('Hello')
# print('------------------')
# print(value)
#
# print('==================')
# #2
# value = return_msg('Return hello')
# print(value)

#
# def loop_list_search(list_a, item):
#     for i in list_a:
#         print(i)
#         if i == item:
#             return "Your item on position {index}, item = {}".format(
#                 i, index=list_a.index(i))
#
# #
# # print(loop_list_search([1,2,3,4,5,6,7,8,9,10], 4))
#
#
# def reverse_str(string_a):
#     empty_str = ''
#     string_a = list(string_a)
#     string_a.reverse()
#     return empty_str.join(string_a)
#
# #print(reverse_str('Hello'))
#
#
# def sum_lists(list_a, list_b):
#     result_list = []
#     if len(list_a) == len(list_b):
#         for i in range(len(list_a)):
#             result_list.append(list_a[i] + list_b[i])
#         return result_list
#     else:
#         return "Not allowed"
#
#
# print(sum_lists([1,2,3,4,5], [6,7,8,9,10]))
# print(sum_lists([1,2,3,4,5], [6,7,8,9,10, 11]))
#
#
# def return_dict(name, surname, phone, age):
#     return {'name': name, 'surname': surname, 'phone': phone, 'age': age}
#
# print(return_dict('Ivan', 'Ivanov', '+380991234567', '25'))
#
#
# a_list = ["1213", 123,12,3,4,5, 5.0, [1231, 1231], {'1':2}]
# print(a_list)
#
#
def function_convert(tmp_list):
    def general_function(type_str, default_dict, item):
        if type_str not in default_dict.keys():
            _list = []
            _list.append(item)
            default_dict.update({type_str: _list})
        else:
            default_dict.get(type_str).append(item)

    default_dict = {}
    for item in tmp_list:
        if isinstance(item, int):
            general_function('int', default_dict, item)
        elif isinstance(item, str):
            general_function('str', default_dict, item)
        elif isinstance(item, list):
            general_function('list', default_dict, item)
        elif isinstance(item, dict):
            general_function('dict', default_dict, item)
        elif isinstance(item, float):
            general_function('float', default_dict, item)
    print(default_dict)

# function_convert(a_list)

def my_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function ():
        print("Я - код, который отработает до вызова функции" )
        function_to_decorate()
        print("А я - код, срабатывающий после" )
    return the_wrapper_around_the_original_function


# @my_decorator
# def input_your_name():
#     name = input('Input your name: ')
#     print("Your name is {}".format(name))
#
# def func():
#     return 0
#
# input_your_name()

import os

# 1. Написать функцию, которая принимает в качетсве аргумента имя директории,
# и возвращает словарь вида
# 2. Написать функицю, которая принимает в качестве параметра
# путь к директории и тип файла (расширение). Нужно
# вывести список всех найденных файлов с таким расширением.
# Пример:
# * input args: '/home', '.mp3'
# * output: ['file1.mp3', 'file2.mp3', ... , 'fileN.mp3']
#/home/user/Рабочий стол/Treasure-Hunt
# 3. Создать функицю, которая принимает в качестве параметра - путь к папке
# и выполняет слудующие действия: файлы с общим расширением
# перемещаются в папку с названием расширения. Пример:
# * file.jpg, file2.jpg -> jpg (файлы с расширением .jpg попали в папку jpg)


def func_list_dir(dir_name):
    dict_ = {}
    if dir_name in os.listdir():
        for item in os.listdir(dir_name):
            ext = item.split('.')[1]
            if ext not in dict_.keys():
                dict_.update({ext: 1})
            else:
                dict_.update({ext: dict_.get(ext)+1})
        return dict_
    else:
        return 'Error'

print(func_list_dir('1'))
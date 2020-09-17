# -*- coding: utf8 -*-
# count = 0
#
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28*n + 30*k + 31*m == 365:
#                 count += 1
#                 print(f"#{count} - n = {n}, k = {k}, m = {m};")

# count = 0
# count2 = 0
#
# for x in range(1, 33):
#     for y in range(1, 33):
#         if x == y:
#             continue
#         for z in range(1, 33):
#             if y == z or x == z:
#                 continue
#             for c in range(1, 33):
#                 if x**3 + y**3 == z**3 + c**3 and x != y and x != z and x != c and y != z and y != c and z != c:
#                     count += 1
#                     print()
#                     print(f"#{count} - x = {x}, y = {y}, z = {z}, c = {c}, R = {x**3 + y**3};")
#                     print()
#                 else:
#                     if count2 == 300:
#                         print("*", end="")
#                         count2 = 0
#                     count2 += 1
#                     continue


# count = 0
#
# for n in range(1, 11):
#     for k in range(1, 21):
#         for m in range(1, 201):
#             if 10*n + 5*k + 0.5*m == 100 and n + k + m == 100:
#                 count += 1
#                 print(f"#{count} - n = {n}, k = {k}, m = {m};")
# n = 5
#
# for i in range(1, n+1):
#     for j in range(1, n+2):
#         if i == 1:
#             print(j)
#             break
#         elif i > 1 and j <= i:
#             print(j, end="")
#         elif i > 1 and j > i:
#             for k in range(i-1, 0, -1):
#                 print(k, end="")
#             print()
#             break

# a = int(input())
# b = int(input())
# num = 0
# max_summ = 0
# summ = 0

# for i in range(a, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             summ += j
#     if summ >= max_summ:
#         num = i
#         max_summ = summ
#     summ = 0
# print(num, max_summ)

# b = int(input())
# num = 0
# count = 0
#
# for i in range(1, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     print(i, count*"+", sep="")
#     count = 0

# n = int(input())
# now_num = 0
# summ = 0
# count = 0
#
# while count < 3:
#     while n != 0:
#         now_num = n % 10
#         summ += now_num
#         n = n // 10
#     count += 1
#     n = summ
#     summ = 0
# print(n)

# n = int(input())
# fact = 1
# summ = 0
#
# for j in range(1, n+1):
#     fact *= j
#     summ += fact
#
# print(summ)

# a = int(input())
# b = int(input())
# flag = True
#
# for i in range(a, b+1):
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             break
#     if i == 1:
#         continue
#     elif flag is True:
#         print(i)
#     flag = True

# n = int(input())
# s = 0
# now_num = 0
# while n != 0:
#     now_num = n % 10
#     if now_num % 2 == 0:
#         s += now_num
#     n //= 10
# print(s)


# n = 7
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = int(input())
#
# for i in range(1, n+1):
#     if i == 1:
#         print(19*"*")
#     elif i < n:
#         print("*" + 17*" " + "*")
#     elif i == n:
#         print(19 * "*")

# n = int(input())
# count_three = 0
# count_last = 0
# count_even = 0
# summ_big_five = 0
# multiply_big_seven = 1
# count_null_five = 0
#
# count = 0
#
#
# while n != 0:
#     count += 1
#     now_num = n % 10
#     if now_num == 3:
#         count_three += 1
#     if count == 1:
#         last_num = now_num
#     if now_num == last_num:
#         count_last += 1
#     if now_num % 2 == 0:
#         count_even += 1
#     if now_num > 5:
#         summ_big_five += now_num
#     if now_num > 7:
#         multiply_big_seven *= now_num
#     if now_num == 0 or now_num == 5:
#         count_null_five += 1
#     n //= 10
# print(count_three)
# print(count_last)
# print(count_even)
# print(summ_big_five)
# print(multiply_big_seven)
# print(count_null_five)

# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)
#
# s = input()
# count_star = 0
# count_plus = 0
#
# for i in s:
#     if i == "*":
#         count_star += 1
#     elif i == "+":
#         count_plus += 1
# print(f"Символ + встречается {count_plus} раз")
# print(f"Символ * встречается {count_star} раз")

# s = input()
# last_letter = None
# count = 0
# count_letters = 0
#
# for i in s:
#     count += 1
#     if count == 1:
#         last_letter = i
#     else:
#         if i == last_letter:
#             count_letters += 1
#             last_letter = i
#         else:
#             last_letter = i
# print(count_letters)


# s = input()
# s = s.lower()
# count_vowel = 0
# count_consonant = 0
#
# for i in s:
#     if i == "а" or i == "у" or i == "о" or i == "ы" or i == "и" or\
#             i == "э" or i == "я" or i == "ю" or i == "ё" or i == "е":
#         count_vowel += 1
#     elif i == "б" or i == "в" or i == "г" or i == "д" or i == "ж" or\
#         i == "з" or i == "й" or i == "к" or i == "л" or i == "м" or\
#             i == "н" or i == "п" or i == "р" or i == "с" or i == "т" or\
#             i == "ф" or i == "х" or i == "ц" or i == "ч" or i == "ш" or i == "щ":
#         count_consonant += 1
# print(f"Количество гласных букв равно {count_vowel}")
# print(f"Количество согласных букв равно {count_consonant}")

# num = int(input())
# next_num = None
# now_num_bin = None
# res = ""
# res2 = ""
#
# while num != 0:
#     next_num = num // 2
#     now_num_bin = num % 2
#     res += str(now_num_bin)
#     num = next_num
# for i in reversed(res):
#     res2 += i
# res = res2
# print(res)

# s = input()
#
# check_s = s[::-1]
# if s == check_s:
#     print("YES")
# else:
#     print("NO")

# s = input()
#
# print(len(s))
# print(3*s)
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:len(s)-1])
# print()
#
# print(s[2:3])
# print(s[-2:-1])
# print(s[:5])
# print(s[:len(s)-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

# s = input()
#
# count = len(s)
# part_count = len(s) // 2
# if count % 2 == 0:
#     print(s[part_count:]+s[:part_count])
# else:
#     print(s[part_count+1:]+s[:part_count+1])

# s = input()
#
# s_check = s.title()
# if s == s_check:
#     print("YES")
# else:
#     print("NO")

# s = input()
#
# print(s.swapcase())

# s = input()
#
# s = s.lower()
# if "хорош" in s:
#     print("YES")
# else:
#     print("NO")

# s = input()
# count = 0
#
# for i in s:
#     i_check = i.lower()
#     if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
#         if i == i_check:
#             count += 1
# print(count)

# s = input()
#
# print(s.count(" ")+1)

# s = input()
# s = s.lower()
#
# print(f'Аденин: {s.count("а")}')
# print(f'Гуанин: {s.count("г")}')
# print(f'Цитозин: {s.count("ц")}')
# print(f'Тимин: {s.count("т")}')

# num = int(input())
# count = 0
#
# for i in range(num):
#     s = input()
#     if s.count("11") >= 3:
#         count += 1
# print(count)

# s = input()
# count = s.count("0") + s.count("1") + s.count("2") + s.count("3") + s.count("4") + s.count("5") + \
#         + s.count("6") + s.count("7") + s.count("8") + s.count("9")
# print(count)

# s = input()
# if s.endswith(".com") is True or s.endswith(".ru") is True:
#     print("YES")
# else:
#     print("NO")

# s = input()
#
# if s.find("f") == s.rfind("f") and s.find("f") != (-1):
#     print(s.find("f"))
# elif s.find("f") < s.rfind("f"):
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("NO")

# s = input()
#
# begin_del = s.find("h")
# end_del = s.rfind("h")
#
# s = s[0:begin_del] + s[end_del+1:]
# print(s)

# start = int(input())
# end = int(input())
#
# for i in range(start, end+1):
#     print(chr(i), end=" ")

# s = input()
#
# for i in s:
#     print(ord(i), end=" ")

# num = int(input())
# s = input()
# for i in s:
#     n = ord(i)
#     n -= num
#     if n < 97:
#         n = 122 - (96 - n)
#         print(chr(n), end="")
#     else:
#         print(chr(n), end="")

# s = input()
# first = s.find("f")
# last = s.rfind("f")
#
# if first == last and first != -1:
#     print("-1")
# elif first < last:
#     print(s.find("f", first+1))
# elif first == -1:
#     print("-2")

# s = input()
# begin = s.find("h")
# end = s.rfind("h")
# # print(begin)
# # print(end)
# middle = s[begin:end+1]
# middle = middle[::-1]
# print(s[:begin], middle, s[end+1:], sep="", end="")

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[len(numbers)-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# print(numbers[1:len(numbers)-1])

# num = int(input())
# lang = []
#
# for i in range(num):
#     add = input()
#     lang.append(add)
#
# print(lang)

# abc = 'abcdefghijklmnopqrstuvwxyz'
# alpha = []
#
# for i in range(1, 27):
#     alpha.append(abc[i-1]*i)
#
# print(alpha)

# num = int(input())
# dels = []
#
# for i in range(1, num+1):
#     if num % i == 0:
#         dels.append(i)
# print(dels)

# num = int(input())
# num_now = None
# num_last = int(input())
# list_num = []
#
# for i in range(num-1):
#     num_now = int(input())
#     summ = num_now + num_last
#     list_num.append(summ)
#     num_last = num_now
# print(list_num)

# nums = int(input())
# list_nums = []
#
# for i in range(nums):
#     now_num = int(input())
#     list_nums.append(now_num)
#
# list_nums = list_nums[::2]
# print(list_nums)

# num = int(input())
# list_strings = []
#
# for i in range(num):
#     word = input()
#     list_strings.append(word)
#
# k = int(input()) - 1
# for i in range(len(list_strings)):
#     word = list_strings[i]
#     if k <= len(word):
#         print(word[k], end="")

# num = int(input())
# list_strings = []
#
# for i in range(num):
#     word = input()
#     list_strings.extend(word)
# print(list_strings)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summ = 0
#
# for num in numbers:
#     summ += num**2
# print(summ)

# num = int(input())
# digits = []
# func = []
#
# for i in range(num):
#     digit = int(input())
#     digits.append(digit)
#
# for i in digits:
#     res = i**2 + 2*i + 1
#     func.append(res)
#
# print(*digits, sep="\n")
# print()
# print(*func, sep="\n")

# num = int(input())
# list_nums = []
#
# for _ in range(num):
#     digit = int(input())
#     list_nums.append(digit)
#
# max_num = max(list_nums)
# min_num = min(list_nums)
#
# for i in range(0, len(list_nums)):
#     if list_nums[i] == max_num:
#         del list_nums[i]
#         break
# for i in range(0, len(list_nums)):
#     if list_nums[i] == min_num:
#         del list_nums[i]
#         break
#
# print(*list_nums)

# num = int(input())
# now_str = input()
# list_str = [now_str]
# num -= 1
# flag = True
#
# for i in range(num):
#     now_str = input()
#     for j in range(len(list_str)):
#         if list_str[j] == now_str:
#             flag = False
#             break
#     if flag is True:
#         list_str.append(now_str)
#     elif flag is False:
#         flag = True
#
# for i in list_str:
#     print(i)

# num = int(input())
# list_of_words = []
# list_of_search = []
# flag = False
#
# for _ in range(num):
#     word = input()
#     list_of_words.append(word)
#
# num = int(input())
# for _ in range(num):
#     find_request = input().lower()
#     list_of_search.append(find_request)
#
# for i in list_of_words:
#     i_lower = i.lower()
#     for search_word in list_of_search:
#         if i_lower.find(search_word) == -1:
#             flag = False
#             break
#         else:
#             flag = True
#     if flag is True:
#         print(i)
#         flag = False

# num = int(input())
# list_of_digit = []
#
# for _ in range(num):
#     digit = int(input())
#     list_of_digit.append(digit)
#
# for i in list_of_digit:
#     if i < 0:
#         print(i)
# for i in list_of_digit:
#     if i == 0:
#         print(i)
# for i in list_of_digit:
#     if i > 0:
#         print(i)

# string = input()
# list_of_words = string.split()
# for i in list_of_words:
#     print(i[0], end=".")

# string = input()
# list_of_words = string.split('\\')
# for i in list_of_words:
#     print(i)

# string = input()
# nums = string.split()
#
# for num in nums:
#     num = int(num)
#     print(num*"*")

# ip_adress = input()
# nums = ip_adress.split(".")
# flag = None
#
# for num in nums:
#     num = int(num)
#     if 0 <= num <= 255:
#         flag = True
#     else:
#         flag = False
#         break
# if flag is True:
#     print("ДА")
# else:
#     print("НЕТ")

# string = input()
# string = [char for char in string]
#
# sep = input()
# string = f"{sep}".join(string)
# print(string)

# nums = input()
# count = 0
# nums = nums.split()
# lenth = len(nums)
# nums_check = nums[1:lenth]
# del_num = None
#
# for num in nums:
#     for num_check in nums_check:
#         if num == num_check:
#             count += 1
#         else:
#             continue
#     del nums_check[0:1]
# print(count)

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)

# numbers = input()
# numbers = numbers.split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# min_num = min(numbers)
# max_num = max(numbers)
# pos_min = numbers.index(min_num)
# pos_max = numbers.index(max_num)
# numbers[pos_max] = min_num
# numbers[pos_min] = max_num
# for num in numbers:
#     print(num, end=" ")

# story = input()
# story = story.split()
# count = 0
# for i in range(len(story)):
#     story[i] = story[i].lower()
#     if story[i] == 'a' or story[i] == 'an' or story[i] == 'the':
#         count += 1
# print(f"Общее количество артиклей: {count}")


# num = input()
# num = num.replace("#", "")
# num = int(num)
#
# #print(num)
#
# for i in range(num):
#     code_str = input()
#     find_comms = code_str.find("#")
#     if find_comms == -1:
#         print(code_str)
#         continue
#     else:
#         code_str = code_str[:find_comms]
#         code_str = code_str.rstrip()
#     print(code_str)

# nums = input()
# nums = nums.split()
#
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# nums.sort()
# for num in nums:
#     res = ''
#     res += str(num)
# print()
# nums.sort(reverse=True)
# for num in nums:
#     print(num, end=" ")

# s = input().split()
#
# s.sort()
# print(*s)
#
# s.sort(reverse=True)
# print(*s)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [key[1:] for key in keywords]
#
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i for i in keywords if len(i) >= 5]
#
# print(new_keywords)

# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# num = int(input())
# nums = [i**2 for i in range(1, num+1)]
# for dig in nums:
#     print(dig)

# nums = input().split()
#
# for i in range(len(nums)):
#     nums[i] = int(nums[i])**3
#
# print(*nums)

# str = [print(word) for word in input().split()]

# nums = [print(int(i)**2, end=" ") for i in input().split() if int(i)**2 % 10 != 4 and int(i) % 2 == 0]

# a = [17, 24, 91, 96, 67]
#
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
#
# for i in range(len(a) - 1):
#         m = i
#         j = i + 1
#         while j < len(a):
#             if a[j] < a[m]:
#                 m = j
#             j = j + 1
#         a[i], a[m] = a[m], a[i]
#
# print(a)

# num = [i for i in range(2, int(input())+1, 2)]
# print(num)

# l_list = input().split()
# m_list = input().split()
# res_list = []
#
# for i in range(len(l_list)):
#     res_add = int(l_list[i]) + int(m_list[i])
#     res_list.append(res_add)
#
# for res in res_list:
#     print(res, end=" ")

# nums = input().split()
# summ = 0
#
# for i in range(len(nums)):
#     print(int(nums[i]), end="")
#     summ += int(nums[i])
#     if i < len(nums)-1:
#         print("+", end="")
#     elif i == len(nums)-1:
#         print("=", end="")
#         print(summ, end="")

# number = input().split("-")
# flag = None
#
# for i in range(len(number)):
#     check_num = number[i].split("")

# # объявление функции
# def draw_box(a, b):
#     a = a
#     b = b
#     for i in range(a):
#         if i == 0 or i == (a-1):
#             print("*"*b)
#         else:
#             print("*"+ " "*(b-2) + "*")
#
# # основная программа
# draw_box(14, 10)  # вызов функции

# # объявление функции
# def draw_triangle(num):
#     for i in range(num+1):
#         print("*"*i)
#
# # основная программа
# draw_triangle(10)  # вызов функции

# # объявление функции
# def draw_triangle(fill, base):
#     count = 0
#     part = base // 2 + 1
#     for i in range(1, base+1):
#         if i <= part:
#             count += 1
#             print(fill*count)
#         else:
#             count -= 1
#             print(fill*count)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)


# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep="")
#
# # считываем данные
# name, surname, patronymic = input(), input(), input(),
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# # объявление функции
# def print_digit_sum(num):
#     summ = 0
#     n = num
#     while n > 0:
#         last_num = n % 10
#         summ += last_num
#         n = n // 10
#     print(summ)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)

# # объявление функции
# def get_days(month):
#     if month == 2:
#         days = 28
#     elif (month % 2 == 0 and month <= 7) or (month % 2 == 1 and month > 7):
#         days = 30
#     elif (month % 2 == 1 and month <= 7) or (month % 2 == 0 and month >= 7):
#         days = 31
#     return days
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))

# # объявление функции
# def get_factors(num):
#     factors = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             factors += 1
#     return factors
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# # объявление функции
# def find_all(target, symbol):
#     list_sym = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             list_sym.append(i)
#     return list_sym
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# # объявление функции
# def merge(list1, list2):
#     for i in list2:
#         list1.append(i)
#         list1.sort()
#     return list1
#
#
# # вызываем функцию
# print(merge([1, 2, 3], [5, 6, 7, 8]))

# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
# num = int(input())
# list1 = [int(i) for i in input().split()]
#
# for i in range(num-1):
#     list_input = [int(i) for i in input().split()]
#     list1 = quick_merge(list1, list_input)
# print(*list1)


# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     a, b, c = side1, side2, side3
#     if a < b + c and b < a + c and c < a + b:
#         return True
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))

# # объявление функции
# def get_next_prime(num):
#     num += 1
#     while not is_prime(num):
#         num += 1
#     return num
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))

# # объявление функции
# def is_password_good(password):
#     have_big = False
#     have_small = False
#     have_num = False
#     if len(password) >= 8:
#         for sym in password:
#             uni_num = ord(sym)
#             if 65 <= uni_num <= 90:
#                 have_big = True
#             elif 97 <= uni_num <= 122:
#                 have_small = True
#             elif 48 <= uni_num <= 57:
#                 have_num = True
#         if have_big is True and have_small is True and have_num is True:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))

# # объявление функции
# def is_one_away(word1, word2):
#     is_len = False
#     is_only_one_sym_another = False
#     count = 0
#     if word1 == word2:
#         return False
#     elif len(word1) == len(word2):
#         is_len = True
#         for i in range(len(word1)):
#             for _ in range(len(word2)):
#                 if word1[i] == word2[i]:
#                     break
#                 else:
#                     count += 1
#                     is_only_one_sym_another = True
#                     if count > 1:
#                         return False
#                     break
#         if is_only_one_sym_another is True:
#             return True
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

# # объявление функции
# def is_palindrome(text):
#     text = text.lower()
#     for i in ",.!?&- ":
#         text = text.replace(i, "")
#     part_len = len(text) // 2
#     if text[:part_len+1] == text[:-part_len-2:-1]:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))


# # объявление функции
# def is_valid_password(password):
#     password = password.split(":")
#     if len(password) == 3 and is_palindrome(password[0]) is True \
#             and is_prime(password[1]) is True and is_even(password[2]):
#         return True
#     else:
#         return False
#
# def is_even(a):
#     a = int(a)
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
# def is_prime(num):
#     num = int(num)
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# def is_palindrome(text):
#     text = text.lower()
#     for i in ",.!?&- ":
#         text = text.replace(i, "")
#     part_len = len(text) // 2
#     if text[:part_len+1] == text[:-part_len-2:-1]:
#         return True
#     else:
#         return False
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

# # объявление функции
# def convert_to_python_case(text):
#     result = ""
#     text_lower = text.lower()
#     for i in range(len(text)):
#         if i == 0:
#             result += text_lower[i]
#         elif text[i] == text_lower[i]:
#             result += text_lower[i]
#         elif text[i] != text_lower[i]:
#             result += "_" + text_lower[i]
#     return result
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2)/2
#     y = (y1 + y2)/2
#     return x, y
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# from math import *
# # объявление функции
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius**2
#     return c, s
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)

# from math import *
# # объявление функции
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#
#     if d > 0:
#         x1 = (-b + sqrt(d)) / (2 * a)
#         x2 = (-b - sqrt(d)) / (2 * a)
#         return min(x1, x2), max(x1, x2)
#     elif d == 0:
#         x = -b / (2 * a)
#         return x, x
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# # объявление функции
# def draw_triangle():
#     count = 1
#     for i in range(7, -1, -1):
#         print(i*" " + count*"*")
#         count += 2
#
# # основная программа
# draw_triangle()  # вызов функции


# from math import *
# # объявление функции
# def compute_binom(n, k):
#     fact_n = factorial(n)
#     fact_k = factorial(k)
#     res = fact_n / (fact_k*(factorial(n - k)))
#     res = int(res)
#     return res
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))

# # -*- coding: utf8 -*-
# # объявление функции
# def number_to_words(num):
#     zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять']
#     return zero_to_ninety_nine[num]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))

# # объявление функции
# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november', 'december']
#     if language == "ru":
#         return lng_ru[number-1]
#     elif language == "en":
#         return lng_en[number-1]
#
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))

# # объявление функции
# def is_magic(date):
#     date = date.split(".")
#     part_1 = int(date[0]) * int(date[1])
#     part_2 = int(date[2]) % 100
#     if part_1 == part_2:
#         return True
#     else:
#         return False
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))

# # объявление функции
# def is_pangram(text):
#     text = text.lower()
#     for a in range(97, 123):
#         a = chr(a)
#         if a in text:
#             continue
#         else:
#             return False
#     return True
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

# from random import *
#
# up = int(input('Введите верхнюю границу: '))
# num = randint(1, up)
#
# print('Добро пожаловать в числовую угадайку')
#
#
# def is_valid(now_num):
#     if 1 <= now_num <= up:
#         return True
#     else:
#         return False
#
#
# def play_game(num):
#     while True:
#         now_num = int(input('Введите число: '))
#         if is_valid(now_num) is not True:
#             print(f'Введите число от 1 до {up}!')
#             continue
#         if now_num > num:
#             print('Слишком много, попробуйте еще раз')
#         elif now_num < num:
#             print('Слишком мало, попробуйте еще раз')
#         elif now_num == num:
#             print('Вы угадали, поздравляем!')
#             break
#
#
# play_game(num)

x = 0
y = 12
name = x or y
print(name)
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# a = []
# count = 0
# print(type(count))
# n = int(input("Введите натуральное число: n = "))
# [a.append(i+1) for i in range(n)]
# print(a)

# x = int(input("Введите число: x = "))

# for i in range(n):
#     if a[i] == x:
#         count += 1
# print(count)





# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input("N = "))
# if n > 0:
#     my_List = list()
#     for i in range(n):
#         my_List.append(i+1)
#     print(*my_List)

#     x = int(input("X = "))
#     min = abs(x - my_List[0])
#     index = 0
#     for i in range(1, n):
#         count = abs(x - my_List[i])
#         if count < min:
#             min = count
#             index = i

#     print(f'Число {my_List[index]} в списке A наиболее близко по величине к числу {x}')







# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# пример

# Ввод: ноутбук
# Вывод: 12


print("Добро пожаловать в игру 'Scrabble'!!!\n")
print("Выберите действие:\n")
print("\t1 : Начать игру на Английском (English).")
print("\t2 : Начать игру на Русском (Russion)")
print("\t3 : Выйти из игры,")

cmd =  input("Ваш выбор: ")
points = 0

def Count_Point(d, word, point):
    for k, v in d.items():
        if word in v:
            point += k
    return point

def Print_Point(points):
    print(f"Количество очков: {points}")

def Add_Dictionary(my_dict, key, value):
    my_dict[key] = (value) 
    return my_dict

    
if cmd == "1": 

    key = 1, 2, 3, 4, 5, 8, 10
    value = "A E I O U L N S T R", "D G", "B C M P", "F H V W Y", "K", "J X", "Q Z"
    d = dict()
    count_value = 0
    for i in key:
        print(Add_Dictionary(d, i, value[count_value]))
        count_value += 1

    print("Each letter has a certain value!")
    word = input("Input word: ").upper() 
    for i in word:
        points = Count_Point(d, i, points)
    Print_Point(points)

elif cmd == "2":
    key = 1, 2, 3, 4, 5, 8, 10
    value = "А В Е И Н О Р С Т", "Д К Л М П У", "Б Г Ё Ь Я", "Й, Ы", "Ж З Х Ц Ч", "Ш Э Ю", "Ф Щ Ъ"

    d = dict()
    count_value = 0
    for i in key:
        Add_Dictionary(d, i, value[count_value])
        count_value += 1

    print("Каждая буква имеет определенную ценность!")
    word = input("Введите слово: ").upper() 
    for i in word:
        points = Count_Point(d, i, points)
    Print_Point(points)

elif cmd == "3":
    print("Вы вышли из игры!")
    exit()

else:
    print(f"{cmd}\n Команда не существует!!!")


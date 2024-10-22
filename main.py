import time


def bubble_sort(arr):
    n = len(arr)
    # Проходим через все элементы массива
    for i in range(n):
        # Последние i элементов уже отсортированы, поэтому не нужно их проверять
        for j in range(0, n - i - 1):
            # Если элемент найденный больше следующего элемента, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    # Проходим через все элементы массива
    for i in range(n):
        # Находим индекс минимального элемента в оставшейся неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    # Проходим через все элементы массива начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]

        # Перемещаем элементы arr[0..i-1], которые больше key, на одну позицию вправо
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем ключ в правильную позицию
        arr[j + 1] = key

    return arr


def quick_sort(arr):
    # Базовый случай: массив из одного элемента или пустой
    if len(arr) <= 1:
        return arr
    else:
        # Определяем опорный элемент
        pivot = arr[len(arr) // 2]

        # Разделяем массив на три части: меньше, равно и больше опорного элемента
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Рекурсивно сортируем левую и правую часть, затем объединяем их
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Сливаем массивы, пока есть элементы в обоих
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Если остались элементы в левой половине, добавляем их
    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1

    # Если остались элементы в правой половине, добавляем их
    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1

    return sorted_array



user_input = input("Введите элементы списка, разделенные пробелом: ")

# Разбиваем введенную строку на элементы и преобразуем их в список
user_list = user_input.split()
int_list = [int(num) for num in user_list]

user_list_bubble = int_list
start_time = time.perf_counter()
bubble_sort(user_list_bubble)
end_time = time.perf_counter()
print(f"Пузырьковый метод сортировки", user_list_bubble)
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Время выполнения функции: {execution_time_microseconds:.2f} микросекунд")

user_list_selection = int_list
start_time = time.perf_counter()
selection_sort(user_list_selection)
end_time = time.perf_counter()
print(f"Метод сортировки выбором", user_list_selection)
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Время выполнения функции: {execution_time_microseconds:.2f} микросекунд")


user_list_insertion = int_list
start_time = time.perf_counter()
insertion_sort(user_list_insertion)
end_time = time.perf_counter()
print(f"Метод сортировки вставками", user_list_selection)
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Время выполнения функции: {execution_time_microseconds:.2f} микросекунд")

user_list_quick = int_list
start_time = time.perf_counter()
quick_sort(user_list_quick)
end_time = time.perf_counter()
print(f"Метод сортировки Быстрая сортировка", user_list_quick)
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Время выполнения функции: {execution_time_microseconds:.2f} микросекунд")

user_list_merge = int_list
start_time = time.perf_counter()
merge_sort(user_list_merge)
end_time = time.perf_counter()
print(f"Метод сортировки слиянием", user_list_merge)
execution_time_microseconds = (end_time - start_time) * 1_000_000
print(f"Время выполнения функции: {execution_time_microseconds:.2f} микросекунд")
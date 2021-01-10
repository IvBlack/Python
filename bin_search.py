def binary_search(list, item):
    low = 0 #нижняя граница поиска
    high = len(list) - 1 #верхняя граница поиска
    
    while low <= high:
        mid = (low + high) #проверяем средний элемент
        guess = list[mid]
        if guess == item: #значение найдено
            return mid
        if guess > item: #много
            high = mid - 1
        else:
            low = mid + 1 #мало
        return None #значение не существует
    
    list = [1, 3, 5, 7, 9, 15]
    
binary_search(list, -1)
print(binary_search)

binary_search(list, 5) #возвращается позиция элемента в массиве
print(binary_search)

#бинарный поиск  - алгоритм, на входе принимает ТОЛЬКО отсортированный массив.
#бинарный поиск возвращает позицию, в которой был найден элемент. Иначе - null

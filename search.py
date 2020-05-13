def binary_search(list, item):
    low = 0///
    high = len(list) - 1
    #в переменных low и high хранятся границы списка
    while low <= high: #в переменных low и high хранятся границы списка
        mid = (low + high) #проверяем средний элемент
        guess = list[mid]
        if guess == item: #значение найдено
            return mid
        if guess > item: #много
            high = mid - 1
        else:               #мало
            low = mid + 1
        return None #значения не существует
    
    my_list = [1, 3, 5, 7, 9, 45, 458]
    
    print binary_search(my_list, 7)
    print binary_search(my_list, -5)
    
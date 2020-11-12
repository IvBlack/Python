#для создания двусторонней очереди (дека) используется функция deque:
    
from collection import deque
search_queue = deque() #создание новой очереди
search_queue += graph['you'] #все соседи добавляются в очередь поиска, вернет список всех соседей

#алгоритм поиска "вширь"

while search_queue: #пока очередь НЕ пуста
    person = search_queue.popleft() #из очереди извлекается первый человек
    if person_is_seller(person): #проверяем человека, продавец ли он манго
        print person + " is a mango seller!" #да, это продавец
        return True
    else:
        search_queue += graph[person] #если нет - добавляем всех друзей этого человека в очередь поиска
return False #если выполнение пришло сюда - в очереди нет продавца манго


#определяем функцию person_is_seller. Она сообщает - является ли человек искомым продавцом.
#она проверяет - заканчивается ли имя на букву m, если - да, то это продавец
def person_is_seller(name):
    return name[-1] == 'm'



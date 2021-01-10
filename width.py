graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["claire"] = ["tom", "jonny"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []


#если заканчивается на m - это наш продавец
def person_is_seller(name):
    return name[-1] == 'm'

from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] #для отслеживания уже проверенных
    while search_queue:
        person = search_queue.popleft() #извлекаем первое тело
        if not person in searched: #если не проверялся ранее
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #помечается как уже проверенный
                print ("u r not the last one")
        
search("you")

#Алгоритм поиска 'вширину' относится к алгоритмам поиска и  отвечает на 2 вопроса:
#1. существует ли ауть от узла А к узлу В /есть ли продавец манго в нашей сети/
#2. как выглядит кратчайший путь от узла А к узлу В /кто из продавцов находится к нам ближе всего/




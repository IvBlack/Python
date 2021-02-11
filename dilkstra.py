#реализация алгоритма Дейкстры /простой случай/

#инициируем граф
graph = {}

#реализуем в графе соседей узла и веса к ним в другой хеш-таблице
#т.е. в одной хеш-таблице содержится другая
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

#для получения соседей a, b узла:
>>>print graph["start"].keys()
["a", "b"]

#узнать веса ребер к соседям a и b:
>>>print graph["start"]["a"]
2
>>>print graph["start"]["b"]
6

#включим в граф остальные узлы и их соседей:
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {} # у конечного узла нет соседей

#так же понадобится таблица costs для хранения всех стоимостей узлов:
#costs["fin"] для конечного узла стоимость неизвестна
infinity = float("inf")
costs = {}
costs["a"] = 6
costat["b"] = 2
costs["fin"] = infinity

#для родителей - отдельная таблица
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

#в коннце концов нам нужен массив для отслеживания всех обработанных узлов для 
#избежания дублирования

processed = []

#реализация
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
    
#функция поиска узла с наименьшей стоимостью:
def ind_lowest_cost_node(costs):
    lowest_cost = loat("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
return lowest_cost_node

#for node in costs - перебрать все узлы
#if cost < lowest_cost and node not in processed: - если это узел с наименьшей стоимостью 
#и он не был обработан....
# lowest_cost = cost - он назначается новым узлом с наименьшей стоимостью
    
    
    
    
    
    
    
    

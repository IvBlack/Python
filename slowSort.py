#def greet(name):
 #   print ("hello, " + name + "!")
 #   greet2(name)
 #   print ("getting ready to say bye...")
 #  
    #эта функция приветствует вас, после чего вызывает 2 другие:
    
  #  def greet2(name):
   #     print ("how r u " + name + "?")
    #    def bye():
     #       print ("ok, bye!")


            
#алгоритм сортировки выбором        
#функция поиска наименьшего элементв в массиве

def find Smallest(arr):
    smallest = arr[0] #для хранения наименьшего
    smallest_index = 0 #для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


#теперь на основе этой функции можно написать функцию сортировки выбором:

def selectionSort(arr): #сортирует массив
    newArr = []
    for i in range(len(arr)):
        smallest = indSmallesr(arr) #находит наименьший элемент
        newArr.append(arr.pop(smallest)) #и добавляет его в новый массив
return newArr

print selectionSort([5, 3, 6, 2, 10])
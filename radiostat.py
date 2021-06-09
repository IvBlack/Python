# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:14:40 2021

@author: Пользователь
"""

#states list, transform it into plurality
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#hash of the stations we choose for covering
#keys - names of the stations, values - names of the states 
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations['kfour'] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#final stations set
final_stations = set()

#covered - is a plurality that contains states present in both 'states_needed'
# and in 'states_for_station'. 
#than we check if this station covers more states than the current station
#and if it is right we save currenr station into best_station

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
states_needed -= states_covered
final_stations.add(best_station)
        
        
#let's print our result
print(final_stations)

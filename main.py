# Grayson Northrip CS 118 Final

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

HOTEL_BUDGET = 850


def route(x):
    i = 0
    lst = []
   # while i < len(x):
       # #if x[i][i] > x[i + 1][i]:
            #lst.append(x[i][i])
        #i += 1 


def cost_func(t):
    s = 0
    for i in t:
        s += hotel_rates[i]
    return s


list_cities = []
values = city_temps.values()
list_cities = list(map(list, zip(*values)))
perms = list(permutations(list_cities))
x = list(perms)

route(x)

hotels = list(hotel_rates.keys())
poss_rates = list(combinations_with_replacement(hotels, len(city_temps)))

ideal = min(poss_rates, key=lambda t: HOTEL_BUDGET - cost_func(t) if HOTEL_BUDGET >= cost_func(t) else HOTEL_BUDGET)

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    ideal2 = ', '.join(ideal)
    # ..
    print(f'Here is your best route: {None} the average of the daily max temp. is {None}F')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {ideal2}, totaling ${cost_func(ideal)}')



def max_candany(candies_list):
    candies_type = len(set(candies_list))
    count = int(len(candies_list) / 2)
    print(min([candies_type, count]))


max_candany([1, 1, 2, 2, 1, 1, 1, 9])
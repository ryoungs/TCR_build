import requests
import json

def get_all_acc_data():
    """Get animal Data from AACACC URL  - Note this gets ALL ACC animal data and returns a Json List
       Note there are two sources of data getRedemptionPets and loadAnimals the latter will have "interest: null" """

    url = 'https://aacoprod-inter.aacounty.org/AACOServicePublic/rest/AnimalControlImages/Y/getRedemptionPets'

    r = requests.get(url, timeout= 10)
    sB = r.content   # sB is a byte object!!  e.g. print(type(s0))
    sC = sB.decode()  # make it a string
    sD = sC.replace("getRedemptionPets([","[")  # Strip Leading stuff
    sE1 = sD.replace("])","]")   # strip trailing chars   
    data1 = json.loads(sE1)

    url = 'https://aacoprod-inter.aacounty.org/AACOServicePublic/rest/AnimalControlImages/R/loadAnimals'

    r = requests.get(url, timeout= 10)
    sB = r.content   # sB is a byte object!!  e.g. print(type(s0))
    sC = sB.decode()  # make it a string
    sD = sC.replace("loadAnimals([","[")  # Strip Leading stuff
    sE2 = sD.replace("])","]")   # strip trailing chars   
    data2 = json.loads(sE2)

    #data = [data1, data2]
    data = data1 + data2
    return data

# Use
if __name__ == '__main__':  
    new_data = get_all_acc_data()
    print(len(new_data))
    #print(len(new_data[1]))
    print(new_data)

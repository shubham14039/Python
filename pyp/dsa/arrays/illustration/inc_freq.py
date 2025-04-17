# Write a python program that sort the array elements in increasing order of their frequencies

# Steps:
    # find the frequency of each element and store them in a dictionary
    # Sort the dictionary based on values and not keys
    # initialize an empty array
    # append each key in array the no. of times its corresponding value in the dictionary


def sort_in_frequency(list):

    # method to create a dictionaary and store the frequency of each element in it
    frequency = {}
    for num in list:
        if num not in frequency.keys():
            frequency[num] = 1
        else:
            frequency[num] += 1
    # Returns the frequency of each element. WITHOUT ANY ORDER 
    
    
    # sorting the frequency dictionary
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item:item[1]))
    
    # return sorted_frequency

    # Initialize an empty array of len(list)
    aray = []
    
    # Looping over frequencies
    for key, value in sorted_frequency.items():
        for i in range(value):
            aray.append(key)
    return aray

list = [2,3,5,2,6,7,3,4,5,2,8,7,9,7,9,0,4,5,2,5,6,4,8,9]
print(sort_in_frequency(list))

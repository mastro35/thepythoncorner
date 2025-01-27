def concatenate(list: [str]):
    result = ""
    for string in list:
        result = result + "," + string

    return result
    
if __name__ == '__main__':
    import random
    import string
    import timeit

    my_list = []
    for _ in range(100):
        my_string = ""
        for _ in range(10):
            my_string = my_string + random.choice(string.ascii_uppercase) 
        my_list.append(my_string)

    print(timeit.timeit("concatenate(my_list)", globals=globals()))
    

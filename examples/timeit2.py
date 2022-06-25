def concatenate(list: [str]):
    return ",".join(list)
    
if __name__ == '__main__':
    import random
    import string
    import timeit

    my_list = ["".join(random.choice(string.ascii_uppercase) for _ in range(10)) for _ in range(100)]
    print(my_list)
    
    print(timeit.timeit("concatenate(my_list)", globals=globals()))
    

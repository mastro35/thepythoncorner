# json2.py
import json

my_list = ["this","is","a","simple","list",35]
with open("my_file", "w") as my_file:
    my_json_object = json.dump(my_list, my_file)

with open("my_file", "r") as my_file_read:
    my_second_list = json.load(my_file_read)

print(my_second_list)

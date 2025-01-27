# json1.py
import json

my_list = ["this","is","a","simple","list",35]
my_json_object = json.dumps(my_list)
print(my_json_object)

my_second_list = json.loads(my_json_object)
print(my_second_list)

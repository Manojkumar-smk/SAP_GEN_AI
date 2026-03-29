
from util.reuse import print_my_list_of_products, calculate_tax

products = [
    {"name" : "Apple", "price": 10, "quantity": 15, "category":"vegetable"},
    {"name" : "Orange", "price": 12, "quantity": 9, "category":"vegetable"}
]

print_my_list_of_products(products)


import json

json_data = '''[
   {"name" : "Orange", "price": 12, "quantity": 9, "category":"vegetable"}
]''' 

products_from_json = json.loads(json_data)
print_my_list_of_products(products_from_json)



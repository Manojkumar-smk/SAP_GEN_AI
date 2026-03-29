def print_my_list_of_products(products):
    for product in products:
        calculate_tax(product)
        print(f"product: {product['name']} {product['price']}")

def calculate_tax(product):
    product['price'] =  product['price'] * product['quantity'] * 0.9
    return product

if __name__ == "__main__":
    # if anyone want to test this file separately with sample data
    import json
    json_data = '''[
        {"name" : "Orange", "price": 12, "quantity": 9, "category":"vegetable"}
    ]''' 

    products_from_json = json.loads(json_data)

    print_my_list_of_products(products_from_json)
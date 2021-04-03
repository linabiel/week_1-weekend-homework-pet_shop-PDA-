def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, amount):
    pet_shop['admin']['pets_sold'] += amount

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed):
    pets_to_return = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            pets_to_return.append(pet)
    return pets_to_return

def find_pet_by_name(pet_shop, name_to_find):
    for pet in pet_shop['pets']:
        if pet['name'] == name_to_find:
            return pet

def remove_pet_by_name(pet_shop, pet_name_to_remove):
    pet = find_pet_by_name(pet_shop, pet_name_to_remove)
    pet_shop['pets'].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customers):
    return customers['cash']

def remove_customer_cash(customer, amount):
    customer['cash'] -= amount
    return customer['cash']

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    cash = get_customer_cash(customer)
    price = new_pet['price']
    if cash >= price:
        return True
    return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is None:
        return
    if customer['cash'] < pet['price']:
        return
    find_pet_by_name(pet_shop, pet['name'])
    remove_pet_by_name(pet_shop, pet['name'])
    add_pet_to_customer(customer, pet)
    increase_pets_sold(pet_shop, 1)
    remove_customer_cash(customer, pet['price'])
    add_or_remove_cash(pet_shop, pet['price'])




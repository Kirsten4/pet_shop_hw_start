# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]


def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]


def add_or_remove_cash(pet_shop_dict,cash):
    pet_shop_dict["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"]


def increase_pets_sold(pet_shop_dict,sold_pets):
    pet_shop_dict["admin"]["pets_sold"] += sold_pets


def get_stock_count(pet_shop_dict):
    return len(pet_shop_dict["pets"])


def get_pets_by_breed(pet_shop_dict,pet_breed):
    pets_of_specified_breed = []

    for pet in pet_shop_dict["pets"]:
        if pet["breed"] == pet_breed:
            pets_of_specified_breed.append(pet)
    
    return pets_of_specified_breed


def find_pet_by_name(pet_shop_dict,pet_name):
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop_dict,pet_name):
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == pet_name:
            pet_shop_dict["pets"].remove(pet)
    
    
def add_pet_to_stock(pet_shop_dict,new_pet):
    pet_shop_dict["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer,removed_cash):
    customer["cash"] -= removed_cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)
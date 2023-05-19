import pdb

# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# def add_or_remove_cash__remove(pet_shop, cash):
#     pet_shop["admin"]["total_cash"] -= cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_sold):
    pet_shop ["admin"]["pets_sold"] += pet_sold
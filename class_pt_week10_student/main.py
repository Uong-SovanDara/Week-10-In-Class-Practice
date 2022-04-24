from typing import Tuple
from db import *
from getname import random_name
from prettytable import PrettyTable


breeds = ["Ragdoll", "Scottish Fold", "Himalayan", "Siberian"]


def display_breed():
    print('''\nCat available breed''')
    for index, breed in enumerate(breeds):
        print(f"{index+1}. {breed}")


print("Welcome to Stray Cat Registration APP")
print("-------------------------------------\n")


menu_1 = '''Menu
1. Register Cat 😻
2. Listed Cat 🐈
3. Update Cat 😼
4. Remove Cat 🙀
5. Exit 🚪
'''
register_name_error = None
cat_gender_error = None
register_breed_error = None
cat_id_error = None
update_gender_error = None
update_breed_error = None

menu_2 = '''\nCat Name
1. Generate name
2. Enter name
'''
while True:
    print(menu_1)
    menu_one_input = input("enter menu number 1 -> 5: ")

    if menu_one_input == "1":

        print(menu_2)

        
        while register_name_error == None:
            register_name = input("enter menu number 1 -> 2: ")
            if register_name == "1":
                cat_name = random_name("cat")
                print(f"\nYour generated cat name: {cat_name}")
                register_name_error = True

            elif register_name == "2":
                cat_name = input("\nEnter cat name: ")
                register_name_error = True
            
            else:
                print("plase enter the correct input.")
                continue
        while cat_gender_error == None:
            cat_gender = input("\nCat gender (m/f): ").lower()
            if cat_gender == "m" or cat_gender == "f":
                cat_gender_error = True
            else:
                print("Please enter the correct input.")
                continue
        
        while register_breed_error == None:
            display_breed()
            try:
                register_breed = int(
                    input(f"\nenter menu number 1 -> {len(breeds)}: "))
                cat_breed = breeds[register_breed - 1]
                register_breed_error = True
            except ValueError:
                print("Please follow the direction given.")
                continue
            except IndexError:
                print("Please follow the direction given.")
                continue

        cat_dob = input(
            f"\nEnter {'her' if cat_gender == 'f' else 'his'} date of birth (yyyy-mm-dd): ")

        cat_description = input("\nAnything to note for this cat: ")

        cat_info = (cat_name, cat_gender, cat_breed, cat_dob, cat_description)

        register_cat(cat_info)

    elif menu_one_input == "2":
        all_cat = get_cats()
        cat_table = PrettyTable()
        cat_table.field_names = ["ID", "Name",
                                 "Gender", "Breed", "DOB", "Description"]
        cat_table.add_rows(all_cat)
        # print(all_cat)
        print(cat_table.get_string())

    elif menu_one_input == "3":
        while cat_id_error == None:
            try:
                all_cat = get_cats()
                cat_table = PrettyTable()
                cat_table.field_names = ["ID", "Name",
                                        "Gender", "Breed", "DOB", "Description"]
                cat_table.add_rows(all_cat)
                print(cat_table.get_string())
                update_cat_id = int(input("\nEnter cat ID for update: "))
                
                id, name, gender, breed, dob, description = get_cat(update_cat_id)
                cat_id_error = True
            except TypeError:
                print("Please enter the ID that's in our database.")
                continue
            except ValueError:
                print("Please enter the ID that's in our database.")
                continue

        update_name = input(f"Update Name ({name}): ")
        if update_name == '':
            update_name = name

        while update_gender_error == None:
            update_gender = input(f"Update Gender ({gender}): ").lower()
            if update_gender == '':
                update_gender = gender
                update_gender_error = True
            elif update_gender == "m" or update_gender == "f":
                update_gender_error = True
            else:
                print("Please enter the correct gender.")
                continue
        while update_breed_error == None:
            try:
                display_breed()
                update_breed = input(
                    f"\nenter menu number 1 -> {len(breeds)} ({breed}): ")
                if update_breed == '':
                    update_breed = breed
                    update_breed_error = True
                else:
                    update_breed = breeds[int(update_breed) - 1]
                    update_breed_error = True
            except ValueError:
                print("Please enter the correct Value given.")
                continue
            except IndexError:
                print("Please enter the correct number.")
                continue

        update_dob = input(f"Update DOB ({dob}): ")
        if update_dob == '':
            update_dob = dob

        update_description = input(f"Update Description ({description}): ")
        if update_description == '':
            update_description = description

        cat_update_data = (update_cat_id, update_name, update_gender,
                           update_breed, update_dob, update_description)

        update_cat(cat_update_data)

    elif menu_one_input == "4":
        all_cat = get_cats()
        cat_table = PrettyTable()
        cat_table.field_names = ["ID", "Name",
                                "Gender", "Breed", "DOB", "Description"]
        cat_table.add_rows(all_cat)
        print(cat_table.get_string())
        remove_cat_id = int(input("\nCat ID to be remove: "))
        remove_cat(remove_cat_id)

    elif menu_one_input == "5":
        break
    
    else:
        print("Invalid input. Please enter the correct input.")
        continue

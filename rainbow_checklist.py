from termcolor import colored
from os import system, name
from time import sleep

checklist = list()

def create(item):
    checklist.append(item)
    print("You added {} to the list.".format(color_text(item)))

def read(index):
    return "Reading index {}: {}".format(index, color_text(checklist[int(index)]))

def update(index, new_item):
    prev_item = checklist[index]
    checklist[index] = new_item
    print("You updated {} to {}".format(color_text(prev_item), color_text(new_item)))

def destroy(index):
    del_item = checklist[index]
    checklist.pop(int(index))
    print("You removed {} from the list.".format(color_text(del_item)))

def list_all_items():
    print("Printing all items: ")
    index = 0
    for item in checklist:
        print("Index {} - {}".format(index, color_text(item)))
        index += 1

def mark_complete(index):
    print("You marked {} as complete.".format(color_text(checklist[index])))
    checklist[index] = "√ {}".format(checklist[index])

def mark_uncomplete(index):
    checklist[index] = "{}".format(checklist[index].replace("√ ", ""))
    print("You marked {} as uncomplete.".format(color_text(checklist[index])))

def check_complete(index):
    if "√" in checklist[index]:
        return True
    return False

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def check_index(index):
    if index >= len(checklist):
        if len(checklist) == 1:
            print("There is only one item in the list. Please choose index 0.")
        else:
            print("The list has only {} items. Please enter a number between 0 to {}".format(len(checklist), len(checklist) - 1))
        return False
    return True

def color_text(item):
    colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    item_list = item.split(" ")
    for index in range(len(item_list)):
        if item_list[index] in colors:
            item_list[index] = colored(item_list[index], item_list[index])
    return " ".join(item_list)

# CREDITS GO TO GEEKS FOR GEEKS: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def select(function_code):
    print("-----------------------------------")

    if (function_code != "C" and function_code != "Q") and (len(checklist) == 0):
        print("Please pick an option from the list.")

    elif function_code == "C":
        input_item = user_input("Add item: ")
        create(input_item)

    elif function_code == "R":
        item_index = int(user_input("Item's index number to read: "))
        if check_index(item_index):
            print(read(item_index))

    elif function_code == "U":
        item_index = int(user_input("Item's index number to update: "))
        item_update = user_input("Replace index {} with: ".format(item_index))
        if check_index(item_index):
            update(item_index, item_update)

    elif function_code == "D":
        item_index = int(user_input("Item's index number to delete: "))
        if check_index(item_index):
            destroy(item_index)

    elif function_code == "M":
        item_index = int(user_input("Item's index number to mark complete: "))
        if check_index(item_index):
            if check_complete(item_index) == False:
                mark_complete(item_index)
            else:
                print("{} is already marked complete".format(color_text(checklist[item_index])))

    elif function_code == "N":
        item_index = int(user_input("Item's index number to mark uncomplete: "))
        if check_index(item_index):
            if check_complete(item_index):
                mark_uncomplete(item_index)
            else:
                print("{} is already marked uncomplete".format(color_text(checklist[item_index])))

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Please pick an option from the list.")

    return True

def main():
    prompt_begin = "-----------------------------------\nChoose one:\n"
    create_choice_prompt = "[C] Add an item to the list \n"
    read_choice_prompt = "[R] Read an item from the list \n"
    update_choice_prompt = "[U] Update an item \n"
    delete_choice_prompt = "[D] Delete an item \n"
    mark_complete_choice_prompt = "[M] Mark an item as complete \n"
    mark_uncomplete_choice_prompt = "[N] Mark an item as uncomplete \n"
    print_choice_prompt = "[P] Display all items \n"
    quit_choice_prompt = "[Q] Quit \n"
    prompt_end = "\nYour input: "

    user_select = True
    while user_select == True:
        if len(checklist) == 0:
            selection = user_input(prompt_begin + create_choice_prompt + quit_choice_prompt + prompt_end).upper()
        else:
            selection = user_input(prompt_begin + create_choice_prompt + read_choice_prompt + update_choice_prompt + delete_choice_prompt + mark_complete_choice_prompt + mark_uncomplete_choice_prompt + print_choice_prompt + quit_choice_prompt + prompt_end).upper()
        if selection != 'Q':
            sleep(1)
            clear()
        user_select = select(selection.upper())
    print("Goodbye! Thanks for using the Rainbow Checklist!")

# def test():
    # create("purple sox") # checklist == ["purple sox"]
    # create("red cloak") # checklist == ["purple sox", "red cloak"]

    # print(read(0)) # return "purple sox"
    # print(read(1)) # return "red cloak"

    # update(0, "purple socks") # checklist == ["purple socks", "red cloak"]
    # destroy(1) # checklist == ["purple socks"]

    # print(read(0)) # return "purple socks"
    # print(read(1)) # error
    # print(checklist)

    # list_all_items()

    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()
    # select("P")
    # list_all_items()
    # select("A")
    # list_all_items()

# test()

main()


# This is the default dictionary structure

# JSON_DICT = {
#     "omit_code": False,    
#     "tags": [],            
#     "type": "",            
#     "question": "",        
#     "options": [],         
#     "answer": 0,           
#     "difficulty": 0        

# }

default = False
default_list = []

# =========<IMPORTS>========= #

from os import system, path, makedirs, listdir, getcwd
from json import dump

# =========<FUNCTIONS>========= #

### the getter(JSON_DICT) function gathers the data of the question and modifies the given Dictionary.

def getter():

    global default, default_list
    
    # clear the console.
    system("cls")
    
# =========<VARIABLES>========= #

    types = ['multiple_choice', 'true_false', 'text']

    available_tags = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                    'inlinestatements', 'func', 'naming', 'syntax', 'scope']    

    new_dir = False

    JSON_DICT = {}

# =========<USERDATA>========= #

    if default == False:
        # asks user for creator name.
        CREATOR = input("\nEnter the username :: ")
        
        # checks if the user exists in the quizzes directory.
        if path.exists(f'quizzes\\{CREATOR}'):
            pass
        
        # if not then asks if the user wants to create a new directory.
        else:
            choice = input(f"\nDo you want to create a new directory {CREATOR}? [y|n] :: ")
            
            # if choice is in yes, then add the new directory.
            if choice.lower() in "yes":
                makedirs(f'quizzes\\{CREATOR}')
                new_dir = True
            else:
                return None, None

        # ask for ID as an integer.
        while True:

            # find the last known ID in the creator's directory.
            try:
                if new_dir != True: Last_ID = str(sorted(listdir(f'quizzes\\{CREATOR}\\'), key=len)[-1])[:-5]
                else: Last_ID = 0

                # show the last known ID for the user to
                # not make a mistake in overwriting an existing file.
                print("Last known ID :", Last_ID)
            except IndexError:
                print('Last known ID : ERROR')

            # ask for ID as int.
            ID = input("Enter the id of the question {int} ::  ")
            
            try: # try converting ID to integer
                ID = int(ID) 
                break

            except ValueError: # show user: must be integer error and ask for input again.
                print("\nThe ID can only be an integer.")
                ID = int(input("\nRe-enter the ID of the question :: "))

        # ask the useer if they'd want to set creator and id's to defaults.
        default = input("\nDo you want enable these as default values? [y|n] :: ")

        # if yes then change some vairables
        if default in 'yes':
            default = True

            # inform the user of the mode having being enabled
            # permanently unles user exists the script.
            print("<<< DEFAULT MODE : ENABLED >>>")
            default_list = [CREATOR, ID]
    else:
        CREATOR, ID = default_list

        # for every iteration: increment the ID value
        ID += 1
        

# =========<OMIT_CODE>========= #

    # ask the user if they want to exclude code from the question.
    omit_code = input('\nDoes your question have code snippet? [true|false] :: ').title()

    # if the user enters anything except 'true' then omit_code = False, else it is True
    if omit_code not in 'True':
        omit_code = True
    else:
        omit_code = False

    # modify the value in the dictionary.
    JSON_DICT["omit_code"] = omit_code    

    # inform the user of the change.
    print(f'<<< Omit_code set to : {omit_code} >>>')


# ===========<TAGS>=========== #

    # ask the user if they want to have tags for the question. 
    if input("\nDo you want to enable tags? [y|n] :: ").lower() not in 'yes':
        
        try: # if not yes then, remove the tags key and inform the user of the change.
            JSON_DICT.pop("tags")
            print("<<< Tags set to : Disabled >>>")
        except Exception: print("'tags' field not available.")
        
    else: # get tags from the user.
        tags = [] # a temporary tags list
        
        while True:
            try: # ask user for the total number of tags needed.
                total = int(input('\nTotal tags {int} :: '))
                
                # check if the total number of tags in not more than the total number of available_tags
                if total < len(available_tags)+1:
                    break
                else: # else inform user that they should not be greedy.
                    total = input("Total number of tags exceeds the\nnumber of available tags: Try again! :: ")
            except ValueError: # show user: must be integer error.
                print("Sorry you can only have integers as total number!")
                total = int(input('\nTry Again : Total tags {int} :: '))
                
        # show user: valid number of tags available.
        print(f"\nValid Tags: {str(available_tags)[1:-1]}")

        # take tag input
        for tagnum in range(total):
            tag = input(f'tag {tagnum + 1} :: ')   

            # if tag not in valid tags: then show and error and give user another try.
            while tag not in available_tags:
                print("\nSorry that tag is invalid Try Again")
                tag = input(f'tag {tagnum + 1} :: ') 
            # else add it to the temporary tags list.
            else:
                tags.append(tag)

        # modify the value in the dictionary.   
        JSON_DICT["tags"] = tags

        # inform the user of the change.
        print("<<< Tags set to : Enabled >>>")

# ===========<TYPE>=========== #

    # Show available types.
    print("\nType:")
        
    for num, Type in enumerate(types, start=1):
        print(f'[{num}] {Type}')

    # add some random value for selector: -1 is nice.
    selector = -1

    # ask user for selecting a type, until type is one of the options.
    while selector not in tuple(range(1,len(types)+1)):
        try:
            selector = int(input(f"\nSelect Type :: "))
            
            # if the selected option doesn't exist then inform the user that they are blind.
            if selector not in tuple(range(1,len(types)+1)):
                print(f"Sorry, you can only choose from [{str(tuple(range(1,len(types)+1)))[1:-1]}] !")
                
        except ValueError: # show user: must be integer error and give another try.
                print("Sorry you can only have integers as total number!")
                total = int(input(f'\nTry Again : Select Type [{str(tuple(range(1,len(types)+1)))[1:-1]}] {int} :: '))
            
    else:
        # modify the variable in the dictionary.
        JSON_DICT["type"] = types[selector-1]

        # inform the user of the change.
        print(f"<<< Type set to : {types[selector-1]} >>>")

    # if type is either `true_false` or `text` then remove "options" key from the dictionary.
    if JSON_DICT["type"] == 'true_false' or JSON_DICT["type"] == 'text':
        # inform the user of the change
        print(f"<<< Options set to : Disabled >>>")

# =========<QUESTION>========= #

    # ask useer for the question
    question = input('\nQuestion :: ')

    # modify the variable in the dictionary.
    JSON_DICT["question"] = question

    # if the type is of `text`, then check if a blank ahs been provide if not inform the user of the requirement.
    while JSON_DICT["type"] == "text" and JSON_DICT["question"].count(" ___ ") != 1:
        print("Sorry you missed adding a fill up blank {' ___ '} in your question\nthat is no more or less than exactly three consecutive underscores.\nMake sure there are spaces around it! Only one fill up currently supported")
        # give user another try at writing the question.
        JSON_DICT["question"] = input('\nQuestion :: ')

    # inform the user of the change.
    print(f"<<< Question set to : {question} >>>")

# =========<OPTIONS>========== #

    if JSON_DICT["type"] == types[0]: # option handling for `multiple_choice` type.
        options = [] # temporary options list

        while True: # ask user for total number of options.
            try:
                total = int(input('\n' + "Total options {int} :: "))
                break
            except ValueError:# show user: must be integer error.
                print("Sorry you can only have integers as total options!")

        # inform the user that they can make mistakes like a human and that they don't have to worry.
        print("\nType the options carefully,\nyou don't wanna go through the hassle of editing\nbut, don't worry if you did make a mistake\nyou can re-edit through an editor\nat the end of adding all the options\n")

        # take options.
        for optnum in range(total):
            option = input(f'option {optnum + 1} :: ') 
            options.append(option)

# =======<EDIT_OPTIONS>======== #

        # ask if the user has made a mistake and wants to edit the options.
        re_edit = input("\nDo you want to make changes\nto the addded options? [y|n] :: ").lower()

        while re_edit in 'yes': # if yes then show them the options
            for _index, _opt in enumerate(options):
                print(f"[{_index}] : {_opt}")

            index = None # temporary initiation
            # keep asking for which option to edit if the user is addament on not choosing proper options.
            while index not in tuple(range(len(options))):
                
                # ask for index of the option.
                index = input("\nEnter the index of the option you want to edit {int} :: ")
                
                try: # try to convert to int if not then
                    index = int(index)
                    if index not in tuple(range(len(options))):
                        print("Index Out of Range, Try Again!")
                
                except ValueError: # show user: must be integer error.
                    print("\nThe index can only be an integer and in between", tuple(range(len(options))))
                    index = int(input("\nRe-enter the index of the option you want to edit"))

            # get the edit.
            option = input(f"Editing [{index}] Option :: ")

            # make changes with the options list
            options[index] = option

            # ask if the user wants correct any more mistakes.
            re_edit = input("\nDo you want to make more\nchanges to the addded options? [y|n] :: ").lower()

        # modify the variable in the dictionary.
        JSON_DICT["options"] = options

# ==========<ANSWER>========== #

    if JSON_DICT["type"] == types[0]: ############ multiple_choice ############
        answer = -1

        # ask user for the answer of their question.
        print("\nGive the answer of this question {index}:\n" + f'{JSON_DICT["question"]}')
        # also show options for multiple choice types
        for _index, _opt in enumerate(JSON_DICT["options"]):
            print(f"[{_index}] : {_opt}")

        # keep asking the dumb user to give their answer to the question.
        while answer not in tuple(range(len(JSON_DICT["options"]))):

            # ask for answer
            answer = input('\n' + "Answer {int} :: ")
            try:
                answer = int(answer)

                # show user: index out of range.
                if answer not in tuple(range(len(JSON_DICT["options"]))):
                    print("Index Out of Range, Try Again!")

            # show user: must be integer error.
            except ValueError:
                print("\nThe index can only be an integer and in between", tuple(range(len(options))))

        # modify the variable in the dictionary.
        JSON_DICT["answer"] = answer

        # infor mthe user of the change.
        print(f"<<< Answer set to : {answer} >>>")


    elif JSON_DICT["type"] == types[1]: ############ true_false ############
        answer = None # temporary value
        # ask user for the answer of their question.
        print("\nGive the answer of this question {boolean}:\n" + JSON_DICT["question"])
      
        # keep asking the user to give the answer to the question.
        while answer not in (True, False):
            answer = input('\n' + "Answer {bool} :: ").title()
            try:
                answer = bool(answer)
                # show user: must be a boolean error
                if answer not in (True, False):
                    print("Answer must be a boolean [true|false]:")
            # show user: must be a boolean error
            except ValueError:
                print("Answer must be a boolean [true|false]:")
                
        # modify the variable in the dictionary.
        JSON_DICT["answer"] = answer

        # infor mthe user of the change.
        print(f"<<< Answer set to : {answer} >>>")
                    
    elif JSON_DICT["type"] == types[2]: ############ text ############

        # ask the user of the answer to the question.
        answer = input("\nGive the answer of this question {string}:\n" + JSON_DICT["question"] + " : Answer :: ")
        # ask the user if they are hundred percent sure.
        choice = input("\nAre you sure of this answer? [y|n] :: ")
        
        while choice.lower() != 'y':
            # give user another try.
            answer = input("\nRewrite the answer of this question {string}:\n" + JSON_DICT["question"] + " : Answer :: ")
            # ask for confirmation again.
            choice = input("\nAre you sure of this answer? [y|n] :: ")
        else:
            # modify the variable in the dictionary.
            JSON_DICT["answer"] = answer

            # infor mthe user of the change.
            print(f"<<< Answer set to : {answer} >>>")

# ==========<DIFFICULTY>========== #

    # temporarily set difficulty to be 0
    difficulty = 0

    # keep asking for difficulty unless they put the valid integer.
    while difficulty not in range(1,6):
        
        try: # ask the user of the difficulty of their question.
            difficulty = int(input('\n' + "difficulty {int} :: "))

            # show user: difficulty invalid error and give info about various levels.
            if difficulty not in range(1,6):
                print("\nDifficulty must range from 1 - 5:\n1 => just started learning python.\n2 => few weeks into python (2 - 7 weeks)\n3 => Average Python Developer\n4 => Advanced Python User\n5 => Veteran Python Hunters")

        # show user : must be integer error.
        except ValueError:
            print("Sorry you can only have integer as difficulty!")
    else:
        # mdify the variable in the dictionary
        JSON_DICT["difficulty"] = difficulty

        # inform the user of the changes.
        print(f"<<< Difficulty set to : {difficulty} >>>")

    # return required data.
    return JSON_DICT, (CREATOR, ID)

### json_dump(JSON_DICT, USER_DATA) function takes in a dictionary and creator, ID of the file and
### writes a json file from them, if the omit code is false then it also writes a temporary .py file of same ID.

def json_dump(JSON_DICT, USER_DATA):

    system("cls") # clear the console

    # open the file with creator and ID at specified directory and create a .json file if not exist.
    with open(f"quizzes\\{USER_DATA[0]}\\{USER_DATA[1]}.json", 'w') as File:

        try: # tries to write the dictionary into the json file with indent of 4 spaces.
            dump(JSON_DICT, File, indent=4)
            # notify success if done so.
            print(".json File written!")

        except Exception:
            # notify failure if not.
            print(".json File not written!")

    # if the question has omit code set to false then create a temporary .py file for user to edit.
    if JSON_DICT["omit_code"] == False:

        # open the file with creator and ID at specified directory and create a json file if not exist.
        with open (f"quizzes\\{USER_DATA[0]}\\{USER_DATA[1]}.py", 'w') as File:
                
            try: # try to write comments into the py file.
                File.writelines(["### Python File to be written ###","### Remove these comments once file is written onto ###"])
                # inform the user file has been created to be edited.
                print(".py File ready to be edited!")

            except Exception:
                # if not, show failure.
                print(".py File not written!")
    

# loop these indefinitely unless user asks to leave.
while True:

    # gather question data from getter() function.
    json_dict, user_data = getter()

    # if the user made a mistake in creator key, then restart.
    if json_dict == None:
        continue

    # write the gathered data into the specified file(s).
    json_dump(json_dict, user_data)

    # ask the user if they want to leave adding questions.
    if input("Do you want to continue adding questions? [y|n] :: ").lower() not in 'yes':
        # if yes then break out of the loop.
        break


JSON_DICT = {
    "omit_code": False,    # 0
    "tags": [],            # 1
    "type": "",            # 2
    "question": "",        # 3
    "options": [],         # 4
    "answer": 0,           # 5
    "difficulty": 0        # 6

}

from os import system, path, makedirs, listdir, getcwd

def getter(JSON_DICT):

    system("cls")
    
# =========<VARIABLES>========= #

    types = ['multiple_choice', 'true_false', 'text']

    available_tags = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                    'inlinestatements', 'func', 'naming', 'syntax', 'scope']    

# =========<USERDATA>========= #

    CREATOR = input("\ncreator :: ")
    
    # checks if the user exists in the quizzes directory.
    if path.exists(f'quizzes\\{CREATOR}'):
        pass
    # if not then asks if the user wants to create a new directory.
    else:
        choice = input(f"\nDo you want to create a new directory {CREATOR}? [y|n] :: ")
        
        if choice.lower() in "yes":
            makedirs(f'quizzes\\{CREATOR}')

    while True:

        Last_ID = str(sorted(listdir(f'quizzes\\{CREATOR}\\'), key=len)[-1])[:-5]

        print("Last known ID :", Last_ID)
        ID = input("id {int} ::  ")
        try:
            ID = int(ID)
            break

        except ValueError:
            print("\nThe ID can only be an integer.")
            ID = int(input("\nRe-enter the ID of the question :: "))


# =========<OMIT_CODE>========= #

    omit_code = input('\n' + "omit_code [true|false]" + ' :: ').title()
    if omit_code not in 'True':
        omit_code = False
    else:
        omit_code = True

    JSON_DICT["omit_code"] = omit_code    
    print(f'<<< Omit_code set to : {omit_code} >>>')


# ===========<TAGS>=========== #
            
    if input("\nDo you want to enable tags? [y|n] :: ").lower() not in 'yes':
        try:
            JSON_DICT.pop("tags")
            print("<<< Tags set to : Disabled >>>")
        except Exception: print("'tags' field not available.")
    else: # get tags from the user.
        tags = []
        
        while True:
            try:
                total = int(input('\n' + "Total tags {int}:: "))
                break
            except ValueError:
                print("Sorry you can only have integers as total number!")
                
        print("\nValid Tags: " + str(available_tags)[1:-1])
                
        for tagnum in range(total):
            tag = input(f'tag {tagnum + 1} :: ')   
            while tag not in available_tags:
                print("\nSorry that tag is invalid Try Again")
                tag = input(f'tag {tagnum + 1} :: ') 
            else:
                tags.append(tag)
        JSON_DICT["tags"] = tags
        print("<<< Tags set to : Enabled >>>")

# ===========<TYPE>=========== #

    print("\nType:")
        
    for num, Type in enumerate(types, start=1):
        print(f'[{num}] {Type}')

    selector = 5
    
    while selector not in [1,2,3]:
        try:
            selector = int(input('\n' + "Select Type [1|2|3]:: "))
        except:
            print("Sorry, you can only choose from '1', '2', '3'!")
    else:
        JSON_DICT["type"] = types[selector-1]
        print(f"<<< Type set to : {types[selector-1]} >>>")
    
    if JSON_DICT["type"] == 'true_false' or JSON_DICT["type"] == 'text':
        JSON_DICT.pop("options")
        print(f"<<< Options set to : Disabled >>>")

# =========<QUESTION>========= #

    question = input('\n' + "Question :: ")
    JSON_DICT["question"] = question

    while JSON_DICT["type"] == "text" and "___" not in JSON_DICT["question"].split():
        print("Sorry you missed adding a fill up blank {' ___ '} in your question\nthat is no more or less than exactly three consecutive underscores.\nMake sure there are spaces around it!")
        JSON_DICT["question"] = input('\n' + "Question :: ")

    print(f"<<< Question set to : {question} >>>")

# =========<OPTIONS>========== #

    if JSON_DICT["type"] == types[0]:
        options = []

        while True:
            try:
                total = int(input('\n' + "Total options {int} :: "))
                break
            except ValueError:
                print("Sorry you can only have integers as total options!")

        print("\nType the options carefully,\nyou don't wanna go through the hassle of editing\nbut, don't worry if you did make a mistake\nyou can re-edit through an editor\nat the end of adding all the options\n")
        for optnum in range(total):
            option = input(f'option {optnum + 1} :: ') 
            options.append(option)

# =======<EDIT_OPTIONS>======== #

        re_edit = input("\nDo you want to make changes\nto the addded options? [y|n] :: ").lower()

        while re_edit in 'yes':
            for _index, _opt in enumerate(options):
                print(f"[{_index}] : {_opt}")

            index = None
            while index not in tuple(range(len(options))):

                index = input("\nEnter the index of the option you want to edit {int} :: ")
                try:
                    index = int(index)
                    if index not in tuple(range(len(options))):
                        print("Index Out of Range, Try Again!")
                
                except ValueError:
                    print("\nThe index can only be an integer and in between", tuple(range(len(options))))
                    index = int(input("\nRe-enter the index of the option you want to edit"))

            option = input(f"Editing [{index}] Option :: ")
            options[index] = option
            re_edit = input("\nDo you want to make more\nchanges to the addded options? [y|n] :: ").lower()

        JSON_DICT["options"] = options

# ==========<ANSWER>========== #

    if JSON_DICT["type"] == types[0]: ############ multiple_choice ############
        answer = -1

        print("\nGive the answer of this question {index}:\n" + JSON_DICT["question"])
        for _index, _opt in enumerate(JSON_DICT["options"]):
            print(f"[{_index}] : {_opt}")

        while answer not in tuple(range(len(JSON_DICT["options"]))):
            answer = input('\n' + "Answer {int} :: ")
            try:
                answer = int(answer)
                if answer not in tuple(range(len(JSON_DICT["options"]))):
                    print("Index Out of Range, Try Again!")
            
            except ValueError:
                print("\nThe index can only be an integer and in between", tuple(range(len(options))))
                answer = int(input("\nRe-enter the index of the answer :: "))
        JSON_DICT["answer"] = answer
        print(f"<<< Answer set to : {answer} >>>")

    
    elif JSON_DICT["type"] == types[1]: ############ true_false ############
        answer = False
        print("\nGive the answer of this question {boolean}:\n" + JSON_DICT["question"])
      
        while True:
            answer = input('\n' + "Answer {bool} :: ").title()
            try:
                answer = bool(answer)
                break
                if answer not in [True, False]:
                    print("Answer must be a boolean [true|false]:")
            except ValueError:
                print("Answer must be a boolean [true|false]:")
        
        print(f"<<< Answer set to : {answer} >>>")
                    
    elif JSON_DICT["type"] == types[2]: ############ text ############
        answer = input("\nGive the answer of this question {string}:\n" + JSON_DICT["question"] + " : Answer :: ")
        choice = input("\nAre you sure of this answer? [y|n] :: ")
        while choice.lower() != 'y':
            answer = input("\nRewrite the answer of this question {string}:\n" + JSON_DICT["question"] + " : Answer :: ")
            choice = input("\nAre you sure of this answer? [y|n] :: ")
        else:
            JSON_DICT["answer"] = answer
            print(f"<<< Answer set to : {answer} >>>")

# ==========<DIFFICULTY>========== #

    difficulty = 0
    
    while difficulty not in range(1,6):
        try:
            difficulty = int(input('\n' + "difficulty {int} :: "))
            if difficulty not in range(1,6):
                print("\nDifficulty must range from 1 - 5:\n1 => just started learning python.\n2 => few weeks into python (2 - 7 weeks)\n3 => Average Python Developer\n4 => Advanced Python User\n5 => Veteran Python Hunters")
        except ValueError:
            print("Sorry you can only have integer as difficulty!")
    else:
        JSON_DICT["difficulty"] = difficulty
        print(f"<<< Difficulty set to : {difficulty} >>>")

    return JSON_DICT, (CREATOR, ID)





def setter(JSON_DICT):

    types = ['multiple_choice', 'true_false', 'text']
    
    JSON_FILE = "{"
    
    for index, field in enumerate(JSON_DICT.keys()):
        if field == 'omit_code':
            JSON_FILE += '\n\t' + '"omit_code"' + ': ' + str(JSON_DICT[field]).lower()
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','

        elif field == 'tags':
            temp_string = '[\n\t\t'
            if JSON_DICT[field] == []:
                temp_string = "[]"
            else:
                # clean style
                for _index, tag in enumerate(JSON_DICT[field]):
                    
                    if _index != (len(JSON_DICT[field])-1):
                        temp_string += f'"{tag}",\n\t\t'
                        
                    else:
                        temp_string += f'"{tag}"\n\t]'

            
            JSON_FILE += '\n\t' + '"tags"' + ': ' + temp_string
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','
            
        elif field == 'type':
            JSON_FILE += '\n\t' + '"type"' + ': ' + f'"{JSON_DICT[field]}"'
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','

        elif field == 'question':
            JSON_FILE += '\n\t' + '"question"' + ': ' + f'"{JSON_DICT[field]}"'
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','

        elif field == 'options':
            temp_string = '[\n\t\t'
            if JSON_DICT[field] == []:
                temp_string = "[]"
            else:
                # clean style
                for _index, option in enumerate(JSON_DICT[field]):
                    
                    if _index != (len(JSON_DICT[field])-1):
                        temp_string += f'"{option}",\n\t\t'
                        
                    else:
                        temp_string += f'"{option}"\n\t]'

            
            JSON_FILE += '\n\t' + '"options"' + ': ' + temp_string
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','

        elif field == 'answer':

            if JSON_DICT["type"] == types[0]:
                JSON_FILE += '\n\t' + '"answer"' + ': ' + str(JSON_DICT[field])
                if index != (len(JSON_DICT.keys()))-1:
                    JSON_FILE += ','

            elif JSON_DICT["type"] == types[1]:
                JSON_FILE += '\n\t' + '"answer"' + ': ' + str(JSON_DICT[field]).lower()
                if index != (len(JSON_DICT.keys()))-1:
                    JSON_FILE += ','

            elif JSON_DICT["type"] == types[2]:
                JSON_FILE += '\n\t' + '"answer"' + ': ' + f'"{JSON_DICT[field].lower()}"'
                if index != (len(JSON_DICT.keys()))-1:
                    JSON_FILE += ','

        elif field == 'difficulty':
            JSON_FILE += '\n\t' + '"difficulty"' + ': ' + str(JSON_DICT[field])
            if index != (len(JSON_DICT.keys()))-1:
                JSON_FILE += ','
        
    JSON_FILE += '\n}'
    
    return JSON_FILE



def json_writer(JSON_FILE, USER_DATA, JSON_DICT):

    with open(f"quizzes\\{USER_DATA[0]}\\{USER_DATA[1]}.json", 'w') as File:

        try:
            File.writelines(JSON_FILE)
            print(".json File written!")

        except Exception:
            print(".json File not written!")

    if JSON_DICT["omit_code"] == False:

        with open (f"quizzes\\{USER_DATA[0]}\\{USER_DATA[1]}.py", 'w') as File:
                
            try:
                File.writelines(["### Python File to be written ###","### Remove these comments once file is written onto ###"])
                print(".py File ready to be edited!")

            except Exception:
                print(".py File not written!")

while True:
    
    json_dict, user_data = getter(JSON_DICT)

    json_file = setter(json_dict)

    json_writer(json_file, user_data, json_dict)

    if input("Do you want to continue adding questions? [y|n] :: ").lower() not in 'yes':
        break

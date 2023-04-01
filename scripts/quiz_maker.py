
# -----------------<IMPORT MODULES>----------------- #

from os import system, path, mkdir, listdir
from json import dump

# --------------<GLOBAL VARIABLES>-------------- #

FIELDS = ["omit_code", 
          "tags",
          "type",
          "question",
          "options",
          "answer",
          "difficulty"
          ]
AVAILABLE_TYPES = ["multiple_choice", "true_false", "text"]
AVAILABLE_TAGS = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                    'inlinestatements', 'func', 'nameing', 'syntax', 'scope']
CURRENT_DATA = {}
CREATOR = ""
ID = 1

# --------------<DEFINE FUNCTIONS>-------------- #
def init():
    global CREATOR, ID

    system("cls")

    CREATOR = input("\nCreator :: ")

    if not path.exists(f"quizzes\{CREATOR}"):
        choice = input(f"\nDo you want to create a new directory {CREATOR}?[y|n] :: ").lower()

        while choice != "y":
            print("\nperhaps you typed the wrong creator name. wait you didn't?! see then I'll just have to make a new directory, that's just how it is, that's just how life is. Things don't always work the way you want them to be and to be completely honest, that's alright. Since, you're not always right, right? How many times have you regretted a decision you took? I don't know you personally but am sure that the answer must be many. That's just human nature. Hence, this universe has taken upon itself to do certain things according to it's own will.\nHere, try and type the creator name again!")
            CREATOR = input("\nCreator :: ")
            choice = input(f"\nDo you want to create a new directory {CREATOR}?[y|n] :: ").lower()

        mkdir(f"quizzes\{CREATOR}")
    
    prev_files = listdir(f"quizzes\{CREATOR}")
    json_ids = [int(file.removesuffix(".json")) for file in prev_files if file.endswith(".json")]
    if json_ids != []:
        ID = max(json_ids) + 1

    while True:
        get_info()
        write_json()
        if input("\nDo you want to add some more questions?[y|n] :: ").lower() != "y":
            break
    

def get_info():
    global CURRENT_DATA

    print("FILL OUT THE FOLLOWING FIELDS:")
    for field in FIELDS:
        if field == "omit_code":
            if input(f"\nDo you want to use code snippet?[y|n] :: ").lower() == "y":
                omit = False
            else:
                omit = True
            CURRENT_DATA[field] = omit
        elif field == "tags":
            if input(f"\nDo you want to enable tags?[y|n] :: ").lower() == "y":
                user_tags = []
                print(f"\nValid Tags: {AVAILABLE_TAGS}")

                for tagnum in range(int(input("\nTotal tags :: "))):
                    tag = input(f"Tag [{tagnum+1}] :: ").lower()

                    while tag not in AVAILABLE_TAGS:
                        print(f"\nInvalid Tag\nPlease choose a valid tag from {AVAILABLE_TAGS}")
                        tag = input(f"Tag [{tagnum+1}] :: ").lower()
                    user_tags.append(tag)

                CURRENT_DATA[field] = user_tags
        elif field == "type":
            print("\nType:")
            for num, type in enumerate(AVAILABLE_TYPES):
                print(f"\n[{num}] {type}")
            
            user_input = int(input("\nSelect Type :: "))
            while not (-1 < user_input < len(AVAILABLE_TYPES)):
                print("\nINVALID TYPE! Type Index out of range. Please chose a valid type from the following:")
                for num, type in enumerate(AVAILABLE_TYPES):
                    print(f"\n[{num}] {type}")
                user_input = int(input("\nSelect Type :: "))
                
            user_type = AVAILABLE_TYPES[user_input]
            CURRENT_DATA[field] = user_type
            if user_type == "multiple_choice":
                mcq()
            elif user_type == "true_false":
                true_false()
            elif user_type == "text":
                text()


def mcq():
    global CURRENT_DATA

    for field in FIELDS:
        if field == "question":
            user_que = input(f"\n{field}  :: ")
            CURRENT_DATA[field] = user_que
        elif field == "options":
            options = []
            for optnum in range(int(input("\nTotal Options :: "))):
                user_option = input(f"Option [{optnum}] :: ")
                options.append(user_option)
            CURRENT_DATA[field] = options
        elif field == "answer":
            user_answer = int(input("\nAnswer Num :: "))
            while not (-1 < user_answer < len(options)):
                print(f"\nInvalid Option [Index Out Of Options]\nPlease choose a number from {[(num, option) for num, option in enumerate(options)]}")
                user_answer = int(input("\nAnswer Num :: "))
            CURRENT_DATA[field] = user_answer
        elif field == "difficulty":
            user_diff = int(input("\nDifficulty[1-5] :: "))
            while user_diff not in range(1, 6): 
                print("\nInvalid Difficulty! Please input a difficulty level between 1 and 5.")
                user_diff = int(input("\nDifficulty[1-5] :: "))
            CURRENT_DATA[field] = user_diff

    
def true_false():
    global CURRENT_DATA

    for field in FIELDS:
        if field == "question":
            user_que = input(f"\n{field}  :: ")
            CURRENT_DATA[field] = user_que
        elif field == "answer":
            print("\nOptions:\nTrue [0]\nFalse[1]")
            user_answer = int(input("\nAnswer[0|1] :: "))
            while user_answer != 0 and user_answer != 1:
                print("\nInvalid Answer! Please input correct option from the following:")
                print("True [0]\nFalse[1]")
                user_answer = int(input("\nAnswer[0|1] :: "))
            if user_answer == 0:
                CURRENT_DATA[field] = True
            elif user_answer == 1:
                CURRENT_DATA[field] = False
        elif field == "difficulty":
            user_diff = int(input("\nDifficulty[1-5] :: "))
            while user_diff not in range(1, 6): 
                print("\nInvalid Difficulty! Please input a difficulty level between 1 and 5.")
                user_diff = int(input("\nDifficulty[1-5] :: "))
            CURRENT_DATA[field] = user_diff


def text():
    global CURRENT_DATA

    for field in FIELDS:
        if field == "question":
            user_que = input(f"\n{field}  :: ")
            while user_que.count("___") != 1:
                print('\nInvalid Text Question! Please add a "___" signifying a blank in text questions.')
                user_que = input(f"\n{field}  :: ")
            CURRENT_DATA[field] = user_que
        elif field == "answer":
            user_answer = input(f"\n{field}  :: ")
            CURRENT_DATA[field] = user_answer
        elif field == "difficulty":
            user_diff = int(input("\nDifficulty[1-5] :: "))
            while user_diff not in range(1, 6): 
                print("\nInvalid Difficulty! Please input a difficulty level between 1 and 5.")
                user_diff = int(input("\nDifficulty[1-5] :: "))
            CURRENT_DATA[field] = user_diff


def write_json():
    global ID

    with open(f"quizzes\{CREATOR}\{ID}.json", "w") as data_file:
        dump(CURRENT_DATA, data_file, indent=4)
        print("FILE WRITTEN SUCCESFULLY!")
        ID +=1


# --------------<FUNCTION CALLS>-------------- #
init()
print(CURRENT_DATA)#only for debugging
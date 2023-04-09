###### IMPORTS ######

from json import load, dump
from os import listdir

###### GLOBAL-VARIABLES ######

creators = ["_Wrayor", "b001", "ChatGPT", "Indently", "programizstudios"]
directories: list = [] 

def string_only_aplha(string:str) -> str:
    
    # a function that takes a string and removes all the non alpha characters and returns the clean string

    clean = ""

    for char in string:
        if char.isalpha(): clean += char
        else: clean += " "

    return clean


def tagger(string: str) -> str:
    
    # adding references for tag.

    tag_references = load(open('scripts\\tags\\tags_references.json', 'r'))

    # defining a set of tags.

    tag_list: set = {0,}
    tag_list.clear()

    string = string_only_aplha(string).lower()

    # checking for the tags in the string.

    for tags in tag_references.items():
        for tag in tags[1]:
            if tag in string:
                tag_list.add(tags[0])

    # returning the tags found.

    return tag_list


###### CREATOR-LOOP ######

for creator in creators:
    directories = [f for f in listdir(f"quizzes//{creator}") if f.endswith(".json")]

    # browsing each of the files.

    for directory in directories:

        with open(f'quizzes\\{creator}\\{directory}', 'r') as file:

            # gathered the dictionary from json file.

            print(creator, directory)
            
            data = load(file)

            tag_set:set = tagger(data["question"])

            # checking if the question has a .py file and reading that file to search for tags.

            if data["omit_code"] != True:
                with open(f'quizzes\\{creator}\\{directory[:-4]}py', 'r') as pyfile:
                    for line in pyfile:
                        tag_set = tag_set.union(tagger(line))

            data["tags"] = list(tag_set)
                        
            dump(data, open(f'quizzes\\{creator}\\{directory}', 'w'), indent=4)



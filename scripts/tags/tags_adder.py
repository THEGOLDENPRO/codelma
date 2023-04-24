###### IMPORTS ######

from json import load, dump
from os import listdir

###### GLOBAL-VARIABLES ######

creators = list(listdir('quizzes\\'))
directories: list = [] 

def string_only_alpha(string:str) -> str:
    
    # a function that takes a string and removes all the non alpha characters and returns the clean string

    clean = ""

    for char in string:
        if char.isalpha(): clean += char
        else: clean += " "

    return clean


def tagger(string: str, ref_json_file: str) -> str:
    
    # adding references for tag.

    tag_references = load(open(f'scripts\\tags\\{ref_json_file}.json', 'r'))

    # defining a set of tags.

    tag_list: set = {0,}
    tag_list.clear()

    string = string_only_alpha(string).lower()

    # checking for the tags in the string.

    for tags in tag_references.items():
        for tag in tags[1]:
            if tag in string:
                tag_list.add(tags[0])

    # returning the tags found.

    return tag_list


###### TAG-ADDING ######

for creator in creators:
    directories = [f for f in listdir(f"quizzes//{creator}") if f.endswith(".json")]

    # browsing each of the files.

    for directory in directories:

        with open(f'quizzes\\{creator}\\{directory}', 'r') as file:

            # gathered the dictionary from json file.

            # print(creator, directory) # testing purpose only
            
            data = load(file)

            tag_set:set = tagger(data["question"], 'tags_references')

            # checking if the question has a .py file and reading that file to search for tags.

            if data["omit_code"] != True:
                with open(f'quizzes\\{creator}\\{directory[:-4]}py', 'r') as pyfile:
                    for line in pyfile:
                        tag_set = tag_set.union(tagger(line, 'code_tags_references'))
                        
            # update the dictionary
            
            data["tags"] = list(tag_set)
                        
            dump(data, open(f'quizzes\\{creator}\\{directory}', 'w'), indent=4)

    print(f"Added  tags to {creator}'s quizzes ") # testing purpose only




JSON_DICT = {
    "omit_code": False,    # 0
    "tags": [],            # 1
    "type": "",            # 2
    "question": "",        # 3
    "options": [],         # 4
    "answer": 0,           # 5
    "difficulty": 2        # 6

}

def getter(JSON_DICT):

    types = ['multiple_choice', 'true_false', 'text']

    available_tags = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                    'inlinestatements', 'func', 'nameing', 'syntax', 'scope']    

    omit_code = bool(input('\n' + "omit_code" + ' :: ').title())
    if omit_code != True: omit_code = False
    JSON_DICT["omit_code"] = omit_code


            
    if input("\nDo you want to enable tags? y|n :: ").lower() not in 'yes':
        try:
            JSON_DICT.pop("tags")
        except Exception: print("'tags' field not available.")
    else: # get tags from the user.
        tags = []
        print("\nValid Tags:" + str(available_tags)[1:-1])
                
        for tagnum in range(int(input('\n' + "Total tags :: "))):
            tag = input(f'tag {tagnum + 1} :: ')
                    
            if tag in available_tags:
                tags.append(tag)
            else:
                print("\nInvalid tag!")    
        JSON_DICT["tags"] = tags

    print("\nType:")
        
    for num, Type in enumerate(types, start=1):
        print(f'[{num}] {Type}')

    selector = int(input('\n' + "Select Type :: "))
    JSON_DICT["type"] = types[selector-1]

    
    for index, item in enumerate(JSON_DICT.items()):
        print(index, item)

getter(JSON_DICT)
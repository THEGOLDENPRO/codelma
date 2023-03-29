
# -----------------<IMPORT MODULES>----------------- #

from os import system

# --------------<FUNCTION DEFINITIONS>-------------- #


# the default_start funtion sets the default values for mass addition of questions.
def default_start(fields, datatypes, types, available_tags):

    # ask the user if the ywant to use default values.
    choice = input("\nDo you want to start adding questions using default value? y|n :: ")
    if choice.lower() not in 'yes':return False, [], 0, fields, datatypes

    # global declaration of index values that get updated depending on whether tags exist or not.
    global Type_index, Tags_index, Code_index, Options_index

    default_data = [] # the default data is stored in this variable.
    
    for field in fields[:Type_index + 1]: # iterrating through all the fields.

        # asking the user the starting Id of the first question in mass adition.
        if field == "id":
            uni_data = int(input('\n' + 'Starting ID' + ' :: '))
            default_data.append(uni_data)

        # defaulting omit_code value to false if not mentioned.    
        elif field == "omit_code": 
            uni_data = input('\n' + field + ' :: ')
            if uni_data != 'true': uni_data = "false"
            default_data.append(uni_data)
            
        # asking if user wants to enable tags for the quiz.
        elif field == "tags":
            
            if input("\nDo you want to enable tags? y|n :: ").lower() not in 'yes':
                
                fields.pop(Tags_index)
                datatypes.pop(Tags_index)
                Type_index -= 1
                Options_index -= 1
                    
            else: # get tags from the user.
                tags = []
                print("\nValid Tags:" + str(available_tags)[1:-1])
                
                for tagnum in range(int(input('\n' + "Total tags :: "))):
                    tag = input(f'tag {tagnum + 1} :: ')
                    
                    if tag in available_tags:
                        tags.append(tag)
                    else:
                        print("\nInvalid tag!")    
                        
                default_data.append(tags)
        # selecting the type of quesiton that will be defaulted to.
        elif field == "type":
            print("\nType:")
            
            for num, Type in enumerate(types, start=1):
                print(f'[{num}] {Type}')

            selector = int(input('\n' + "Select Type :: "))
            default_data.append(types[selector-1])

        else:
            uni_data = input('\n' + field + ' :: ')
            default_data.append(uni_data)

    # returning required data for defaulting.
    return True, default_data, selector, fields, datatypes

    

# The getter function collects data from the user and returns a tuple
# containing the data, the fields and the datatype of those said fields.
def getter(fields, datatypes, types, available_tags, default):

    # global declaration of index values that get updated depending on whether tags exist or not.
    global Type_index, Tags_index, Code_index, Options_index
    
    meta_data = [] # inputed data will be stored in this variable.
    
    # if defaulting is disabled
    if default[0] != True:
        
        Code_index = 2
        Tags_index = 3
        Type_index = 4
        Options_index = 6
        
        for field in fields[:Type_index]: # loop through fields till type field.

            # defaulting omit_code value to false if not mentioned.
            if field == "omit_code": 
                uni_data = input('\n' + field + ' :: ')
                if uni_data != 'true': uni_data = "false"
                meta_data.append(uni_data)

            # asking if user wants to enable tags for the quiz.
            elif field == "tags":
                
                if input("\nDo you want to enable tags? y|n :: ").lower() not in 'yes':
                    fields.pop(Tags_index)
                    datatypes.pop(Tags_index)
                    Type_index -= 1
                    Options_index -= 1
                    
                else: # get tags from the user.
                    tags = []
                    print("\nValid Tags:" + str(available_tags)[1:-1])
                    
                    for tagnum in range(int(input('\n' + "Total tags :: "))):
                        tag = input(f'tag {tagnum + 1} :: ')
                        tags.append(tag)
                        
                        if tag in available_tags:
                            tags.append(tag)
                        else:
                            print("\nInvalid tag!")
                            
                    meta_data.append(tags)

            # other data do not default to anything and get appended to the data list.
            else:
                
                uni_data = input('\n' + field + ' :: ')
                meta_data.append(uni_data)

        # getting type from user
        print("\nType:")   
        for num, Type in enumerate(types, start=1):
            print(f'[{num}] {Type}')

        selector = int(input('\n' + "Select Type :: "))
        meta_data.append(types[selector-1])
        
    # if defaulting is enabled
    else:
        #unpack tuple of data from default function returns.
        default_data, default_selector, fields, datatypes = default[1:]

        # using the default values.
        meta_data += default_data

        # incrementing Id value for the next question.
        default_data[1] += 1

        # type value for type of question.
        selector = default_selector
        
        
    # for different types; different number of fields and datatypes are required. 
    # These are selected from these if statements.
    if selector == 1:
        final_data, final_fields, final_datatypes = multi_choice(fields, datatypes, meta_data)
            
    elif selector == 2:
        final_data, final_fields, final_datatypes = true_false(fields, datatypes, meta_data)
            
    elif selector == 3:
        final_data, final_fields, final_datatypes = text(fields, datatypes, meta_data)
            
    # returning the data, the fields and the datatype of those said fields.
    return final_data, final_fields, final_datatypes

        

# function to get data on selected fields for multi_choice type.
def multi_choice(fields, datatypes, data):
    data.append(input('\n' + 'question' + ' :: '))

    options = []

    # Ask user for total number of options and get the options.
    for optnum in range(int(input('\n' + "Total options :: "))):
        option = input(f'Option {optnum + 1} :: ')
        options.append(option)

    data.append(options)
    data.append(int(input('\n' + 'answer num' + ' :: ')))
    data.append(int(input('\n' + 'difficulty' + ' :: ')))
    return data, fields, datatypes

# function to get data on selected fields for true_false type.
def true_false(fields, datatypes, data):

    # global declaration of index values that get updated depending on whether tags exist or not.
    global Options_index
    
    data.append(input('\n' + 'question' + ' :: '))

    fields.pop(Options_index) # removing the options field for true_false type.
    datatypes.pop(Options_index) # removing the options datatype since options field not there.
    datatypes[-2] = 'bool'

    data.append(int(input('\n' + 'answer' + ' :: ')))
    data.append(int(input('\n' + 'difficulty' + ' :: ')))
    return data, fields, datatypes

# function to get data on selected fields for text type.
def text(fields, datatypes, data):

    # global declaration of index values that get updated depending on whether tags exist or not.
    global Options_index
    
    data.append(input('\n' + 'question' + ' :: '))

    fields.pop(Options_index) # removing the options field for text type.
    datatypes.pop(Options_index) # removing the options datatype since options field not there.
    datatypes[-2] = 'str' # datatype for fill up answer is a string.

    data.append(input('\n' + 'answer' + ' :: ')) 
    data.append(int(input('\n' + 'difficulty' + ' :: ')))
    return data, fields, datatypes

# The json_formattor function takes data, fields and their datatypes
# and arranges them into a json file format
# thus returning a string variable with the formatted data.
def json_formator(fields, datatypes, data): 

    # file start
    JSON_DATA = '{\n'

    # iterate through all the fields.
    for index, field in enumerate(fields):

        # if datatype string then put "" around the data.
        if datatypes[index] == 'str':
            data[index] = f'"{data[index]}"'

        # if datatype list then format in a clean way.
        if datatypes[index] == 'list':
            temp_string = '[\n\t\t'

            # clean style
            for _index, option in enumerate(data[index]):
                
                if _index != (len(data[index])-1):
                    temp_string += f'"{option}",\n\t\t'
                    
                else:
                    temp_string += f'"{option}"\n\t]'

            # update the current list to a string cleaned.
            data[index] = temp_string 

        # adding fields line by line.
        if index != len(fields)-1:
            JSON_DATA += f'\t"{field}": {data[index]},\n'
        # do not add a comma if it's the last field.
        else:
            JSON_DATA += f'\t"{field}": {data[index]}\n'

    # file end
    JSON_DATA += '}'

    # return the formatted JSON_DATA string
    return JSON_DATA

# the write_json_file function writes the provided string data
# into the specified location according to the creator and id number
def write_json_file(file_data, fields, data):
    
    with open(f"quizzes\\{data[0][1:-1]}\\{data[1]}.json", 'w')as File:
        
        try:
            File.writelines(file_data)
            print("File written!")
            
        except Exception:
            print("File not written!")
           
# the start function calls all the funcitons in order to
# start adding questions in a continuous loop until user exits.
def start():

    system("cls")
    
    # global declaration of index values that get updated depending on whether tags exist or not.
    global Code_index, Tags_index, Type_index, Options_index
    global Fields, Fields_Datatypes, Types, Available_Tags
    
    Code_index = 2
    Tags_index = 3
    Type_index = 4
    Options_index = 6
    #  --------------<DECLARED VARIABLES>--------------- #

    Fields = ['creator', 'id', 'omit_code', 'tags', 'type', 'question', 'options', 'answer', 'difficulty']
    Fields_Datatypes = ['str', 'int', 'bool', 'list', 'str', 'str', 'list', 'int', 'int']

    Types = ['multi_choice', 'true_false', 'text']

    Available_Tags = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                    'inlinestatements', 'func', 'nameing', 'syntax', 'scope']


    # gather the default values if user permits.
    DEFAULTS = default_start(Fields, Fields_Datatypes, Types, Available_Tags) 

    # Gather remaining data and format them into a json file adn writte them.
    while True:

        
        # Gather more data.
        __data__, __fields__, __datatypes__ = getter(Fields, Fields_Datatypes, Types, Available_Tags, DEFAULTS)

        # Format to JSON.
        File_data = json_formator(__fields__, __datatypes__, __data__)

        # Write to JSON.
        write_json_file(File_data, __fields__, __data__)

        # ask if want to add more questions.
        if input("\nDo you want to continue adding Questions y|n :: ").lower() in "no": break

# --------------<FUNCTION CALL>-------------- #

start()
    

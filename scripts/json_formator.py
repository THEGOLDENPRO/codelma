
# --------------<DECLARED VARIABLES>-------------- #

Fields = ['creator', 'id', 'omit_code', 'tags', 'type', 'question', 'options', 'answer', 'difficulty']
Fields_Datatypes = ['str', 'int', 'bool', 'list', 'str', 'str', 'list', 'int', 'int']
Types = ['multipleChoice', 'trueFalse', 'fillInTheBlank']

Available_Tags = ['list', 'str', 'dict', 'for', 'while', 'listcomp', 'dictcomp', 'eval',
                  'inlinestatements', 'func', 'nameing', 'syntax', 'scope']

Code_index = 2
Tags_index = 3
Type_index = 4
options_index = 6



# --------------<FUNCTION DEFINITIONS>-------------- #

# The getter function collects data from the user and returns a tuple
# containing the data, the fields and the datatype of those said fields.
def getter(fields, datatypes, types, code_index, type_index, available_tags):
    
    meta_data = [] # inputed data will be stored in this variable.
    
    for userinput in fields[:type_index]: # loop through fields till type field.

        # defaulting omit_code value to false if not mentioned.
        if userinput == "omit_code": 
            uni_data = input('\n' + userinput + ' :: ')
            if uni_data != 'true': uni_data = "false"
            meta_data.append(uni_data)

        # asking if user wants to enable tags for the quiz.
        elif userinput == "tags":
            
            if input("Do you want to enable tags? true/false :: ").lower() != 'true':
                fields.pop(Tags_index)
                datatypes(Tags_index)
                
            else: # get tags from the user.
                tags = []
                print("Available Tags:" + str(available_tags)[1:-1])
                for tagnum in range(int(input('\n' + "Total tags :: "))):
                    tag = input(f'tag {tagnum + 1} :: ')
                    tags.append(tag)
                meta_data.append(tags)

        # other data do not default to anything and get appended to the data list.
        else:
            uni_data = input('\n' + userinput + ' :: ')
            meta_data.append(uni_data)

    # getting type from user
    print("\nType:")   
    for num, Type in enumerate(types, start=1):
        print(f'[{num}] {Type}')

    selector = int(input('\n' + "Select Type :: "))
    meta_data.append(types[selector-1])

    # for different types; different number of fields and datatypes are required. 
    # These are selected from these if statements.
    if selector == 1:
        final_data, final_fields, final_datatypes = multipleChoice(fields, datatypes, meta_data, code_index)
        
    elif selector == 2:
        final_data, final_fields, final_datatypes = trueFalse(fields, datatypes, meta_data, code_index)
        
    elif selector == 3:
        final_data, final_fields, final_datatypes = fillInTheBlank(fields, datatypes, meta_data, code_index)
        
    # returning the data, the fields and the datatype of those said fields.
    return final_data, final_fields, final_datatypes

# function to get data on selected fields for multipleChoice type.
def multipleChoice(fields, datatypes, data, code_index):
    data.append(input('\n' + 'question' + ' :: '))

    options = []

    # Ask user for total number of options and get the options.
    for optnum in range(int(input('\n' + "Total options :: "))):
        option = input(f'Option {optnum + 1} :: ')
        options.append(option)

    data.append(options)
    data.append(int(input('\n' + 'answer' + ' :: ')))
    data.append(int(input('\n' + 'difficulty' + ' :: ')))
    return data, fields, datatypes

# function to get data on selected fields for trueFalse type.
def trueFalse(fields, datatypes, data, code_index):
    data.append(input('\n' + 'question' + ' :: '))

    fields.pop(options_index) # removing the options field for trueFalse type.
    datatypes.pop(options_index) # removing the options datatype since options field not there.

    data.append(int(input('\n' + 'answer' + ' :: ')))
    data.append(int(input('\n' + 'difficulty' + ' :: ')))
    return data, fields, datatypes

# function to get data on selected fields for fillInTheBlank type.
def fillInTheBlank(fields, datatypes, data, code_index):
    data.append(input('\n' + 'question' + ' :: '))

    fields.pop(options_index) # removing the options field for fillInTheBlank type.
    datatypes.pop(options_index) # removing the options datatype since options field not there.
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

    # itterate through all the fields.
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
        JSON_DATA += f'\t"{field}": {data[index]},\n'

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



# --------------<FUNCTION CALL>-------------- #

__data__, __fields__, __datatypes__ = getter(Fields, Fields_Datatypes, Types, Code_index, Type_index, Available_Tags)

File_data = json_formator(__fields__, __datatypes__, __data__)

write_json_file(File_data, __fields__, __data__)




    

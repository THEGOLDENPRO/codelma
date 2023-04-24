
from json import load
from os import listdir, system
import time

system("cls")


### Credit to Allosteric on Stack Overflow for this section ###

import ast
import copy

def convertExpr2Expression(Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset = 0)

        return result

def r_exec(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"),globals())

###############################################################


# execute_py() function opens a python file in memory and executes it to find a result.
def execute_py(FilePath):

    # Opens the python file in read mode.
    with open(FilePath, 'r') as pyfile:

        # try to execute the .py file.
        try: r_exec(pyfile.read())
        # if it fails then the code has an error.
        except Exception: print("Error in executing file")

# get_answer() function opens a json file in memory and searches for the given answer.
def get_answer(FilePath):

    # Opens the json file in read mode.
    with open(FilePath, 'r') as jsonfile:

        # load the json data in a dictionary.
        Dict = load(jsonfile)

        # if the question is of multiple choice question then use find the answer in the list of options
        if Dict['type'] == 'multiple_choice':
            print(Dict['options'][Dict['answer']])
        # else get the direct answer.
        else:
            print(Dict['answer'])

def log_defects(FilePath, external_header, error_type = 'Unidentified'):

    global log_written
    # File Path for the detected defected questions.
    LogPath = "logs\\"

    # File Path for the log file.
    File = f"log_defects_{external_header}.txt"

    # Type of defect.
    errors = ['mismatch', 'spelling', 'case', 'incorrect']
    types = ['m', 's', 'c', 'n']

    # Determining the type of defect.
    if error_type in types:
        error_type = errors[types.index(error_type)]

    # Check if the file has been writtne this session.
    if log_written:
        with open(f"{LogPath}{File}", "a" ) as LogFile:
            # Write the error file with sepcified errors.
            LogFile.writelines([f"{FilePath} Defect : {error_type.title()}\n\n"])
            
    # If not then create the file with the first line containing the session data.
    else:
        with open(f"{LogPath}{File}", "w") as LogFile:
            # Write the error file with sepcified errors.
            LogFile.writelines([f"Log File Dated : {external_header} : \n\n",
                                f"{FilePath} Defect : {error_type.title()}\n\n"]) 
            log_written = True # define Log file has been created this session
            

# Collect the names of quiz authors in a list.
creators = list(listdir('quizzes\\'))

# For logging the file
now = time.localtime()

# Logging session time. This is set at the time of checking the files.
ext = f"{now.tm_year}-{now.tm_mon}-{now.tm_mday}_{now.tm_hour}-{now.tm_min}-{now.tm_sec}"

log_written = False

# Loop through the directories of all the quizes.
for creator in creators:

    # collect the paths in a direcctory list.
    directories: list = sorted(listdir(f'quizzes\\{creator}\\'), key=len)

    # filter to only code files.
    directories = [f'{directory}' for directory in directories if directory.endswith('.py')]

    # Loop through each FilePath.
    for File in directories:

        # dynamic address - Path to the file.
        FilePath = f'quizzes\\{creator}\\{File}'

        # Show user quiz metadata.
        print(f"{creator} :: {File[:-3]}")

        # Show the question.
        print(load(open(f'{FilePath[:-3]}.json', 'r'))["question"])

        # Get result of Python File.
        print("Executing Py File ::")
        execute_py(FilePath)
        print()

        # Fetch Answer from JSON File.
        FilePath = f'{FilePath[:-3]}.json'
        print("Getting Anwser ::")
        get_answer(FilePath)

        # ask user if the quiz results properly or if it is incorrect then which type?
        choice = input("\nMark Correct:\n\nm     :  mismatch\ns     :  spelling\nc     :      case\nn     : incorrect\nenter :   correct\n\n:: ").lower()

        # loop through all the possible types of defined errors.
        for option in ['m', 's', 'c', 'n']:

            # if the inputed error is in the defined errors then.
            if choice == option:
                # log with defined error.
                log_defects(FilePath, ext, option)
                break
                
            # if the quiz is correct then leave the loop and don't log anything.
            elif choice == '': break
            
        # or if the user has not identified the error then log with unidentified.
        else:
            log_defects(FilePath, ext)
        
        
        system("cls")


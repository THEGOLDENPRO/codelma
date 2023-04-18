
from json import load
from os import listdir


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



def execute_py(FilePath):
    with open(FilePath, 'r') as pyfile:
        
        try: r_exec(pyfile.read())
        except Exception: print("Error in executing file")

def get_answer(FilePath):
    
    with open(FilePath, 'r+') as jsonfile:
        Dict = load(jsonfile)
        
        if Dict['type'] == 'multiple_choice':
            print(Dict['options'][Dict['answer']])
        else:
            print(Dict['answer'])

creators = list(listdir('quizzes\\'))

for creator in creators:
    
    directories: list = sorted(listdir(f'quizzes\\{creator}\\'), key=len)

    directories = [f'{directory}' for directory in directories if directory.endswith('.py')]

    for File in directories:
        
        FilePath = f'quizzes\\{creator}\\{File}'
        print(f"{creator} :: {File[:-3]}")
        
        print("Executing Py File ::")
        execute_py(FilePath)
        print()
        
        FilePath = f'{FilePath[:-3]}.json'
        print("Getting Anwser ::")
        get_answer(FilePath)
        
        print("\n\n")

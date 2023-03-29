
# !!! RUN ONLY ONCE FOR A FILE !!!

creator = 'programizstudios'
start_id = 1; final_id = 5

for num in range(start_id, final_id + 1):
    
    path = f'quizzes\\{creator}\\{num}.json'

    with open(path, 'r') as File:
        lines = File.readlines()
        lines.pop(1)
        lines.pop(1)
        
        with open(path, 'w') as _file:
            _file.writelines(lines)


    
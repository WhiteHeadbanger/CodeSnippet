import os

def save_code_to_file(code):
    code = code.replace("\r\n", "\n")
    with open('./syntax_highlight/temp/temp_code.py', 'w') as file:
        file.write(code)

def delete_code_file():
    os.remove('./syntax_highlight/temp/temp_code.py')



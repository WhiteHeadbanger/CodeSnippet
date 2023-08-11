import tokenize, token, keyword, os

def save_code_to_file(code):
    with open('./syntax_highlight/temp/temp_code.py', 'w') as file:
        file.write(code)

def delete_code_file():
    os.remove('./syntax_highlight/temp/temp_code.py')

def python_tokenizer():
    t = []
    
    with tokenize.open('./syntax_highlight/temp/temp_code.py') as f:
        tokens = tokenize.generate_tokens(f.readline)
        
        for _token in tokens:
            
            if _token.exact_type == token.NAME and _token.string in keyword.kwlist:
                t.append(('KEYWORD', _token.string))
            
            else:
                last_token = t[-1]
                if _token.exact_type == token.NAME and last_token[1] == 'class':
                    t.append(('CLASS_NAME', _token.string))
                    continue
                
                elif _token.exact_type == token.NAME and last_token[1] == 'def':
                    t.append(('FUNC_NAME', _token.string))
                    continue
                
                # if a function is already on the token list, then when we call or reference that function it should be a func name too, not a variable.
                elif any(_token.string == tok[1] for tok in t):
                    t.append(('FUNC_NAME', _token.string))
                    continue
                
                t.append((token.tok_name[_token.exact_type], _token.string))

    return t

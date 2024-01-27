import tokenize, token, keyword

TOKS = [
    token.NAME, 
    token.LPAR, 
    token.RPAR, 
    token.LBRACE, 
    token.RBRACE, 
    token.LSQB, 
    token.RSQB, 
    token.NL, 
    token.INDENT, 
    token.NEWLINE, 
    token.DOT, 
    token.EQUAL, 
    token.EQEQUAL,
    token.STRING
]

def tokenizer():
    t = []
    new_line_counter = 0
    with tokenize.open('./syntax_highlight/temp/temp_code.py') as f:
        tokens = tokenize.generate_tokens(f.readline)
        
        for _token in tokens:
            
            if _token.exact_type == token.NAME and _token.string in keyword.kwlist:
                t.append(('KEYWORD', _token.string))
                t.append(('SPACE', ' '))
                new_line_counter = 0
            
            else:
                last_token = t[-2]
                if _token.exact_type == token.NAME and last_token[1] == 'class':
                    t.append(('CLASS_NAME', _token.string))
                    new_line_counter = 0
                    continue
                
                elif _token.exact_type == token.NAME and last_token[1] == 'def':
                    t.append(('FUNC_NAME', _token.string))
                    new_line_counter = 0
                    continue
                
                # if a function is already on the token list, then when we call or reference that function it should be a func name too, not a variable.
                elif any('FUNC_NAME' == tok[0] and _token.string == tok[1] for tok in t):
                    t.append(('FUNC_NAME', _token.string))
                    new_line_counter = 0
                    continue

                elif token.tok_name[_token.exact_type] in ['NEWLINE', 'NL']:
                    new_line_counter += 1
                    if new_line_counter > 2:
                        continue
                    else:
                        t.append(('NEWLINE', '\n'))
                        continue

                t.append((token.tok_name[_token.exact_type], _token.string))
                new_line_counter = 0
                if _token.exact_type not in TOKS:
                    t.append(('SPACE', ' ')) 

    return t
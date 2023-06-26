def item(contents):
    """ traite de l'énumération"""
    text = []
    item_run = 0
    code_environment = "verbatim"
    in_code_environment = False
    for line in contents:
        if code_environment in line:
            in_code_environment = not in_code_environment

        if not "-" in line or in_code_environment:
            while item_run != 0:
                item_run -= 1
                text.append(r"\end{itemize}")
            text.append(line)

        else:
            nb_space = 0
            while line[nb_space] == " ":
                nb_space += 1
            
            if line[nb_space] == "-":

                n = item_run - 1 - nb_space // 2
                
                for _ in range(n):
                    text.append(r"\end{itemize}")
                    item_run -= 1
                
                for _ in range(-n):
                    text.append(r"\begin{itemize}")
                    item_run += 1
                
                text.append(r"\item" + line[nb_space + 1:])
            
            else:
                while item_run != 0:
                    item_run -= 1
                    text.append(r"\end{itemize}")
                text.append(line)
    
    return text
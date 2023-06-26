def special_caracter():
    """traite des caractaère spéciaux"""
    caracter = {}
    try:
        fic = open("src/dico.txt", 'r', encoding='utf8')
    except IOError:
        raise("error: can't open dico.txt")
    
    for line in fic:
        if line != "":
            caracter[line[0]] = line[2:-1]
    
    return caracter


def replace_special_caracter(line):
    dico = special_caracter()
    new_line = ""
    nb_dollars = 0

    for c in line:
        if c == "$":
            nb_dollars += 1
        
        if c in dico:
            if nb_dollars % 2 == 0:
                new_line += "$" + dico[c] + "$"
            else:
                new_line += dico[c]
        else:
            new_line += c
    return new_line
def section(line):
    """ traite les section, subsection et les subsubsection"""
    if len(line) >= 3 and line[0] == "#":
        if line[1] == "#":
            if line[2] == "#":
                return r"\subsubsection{" + line[4:] + "}"
            
            return r"\subsection{" + line[3:] + "}"
        
        return r"\section{" + line[2:] + "}"
    
    return line


def bold_and_it(line):
    """ traite du texte en gras ou en italique"""
    if "$" in line:
        return line
    # bold text
    if "**" in line:
        bold_line = ""
        cpt = 0

        if line[:2] == "**":
            bold_line += r"\textbf{"
            cpt += 1
        
        for i, split in enumerate(line.split("**")):
            bold_line += split
            if split != "" and i != len(line.split("**")) - 1:
                if cpt % 2 == 0:
                    bold_line += r"\textbf{"
                    cpt += 1
                else:
                    bold_line += "}"
                    cpt += 1
    else:
        bold_line = line

    # it text
    if "*" in bold_line:
        it_line = ""
        cpt = 0

        if line[:2] == "*":
            it_line += r"\textit{"
            cpt += 1
        
        for i, split in enumerate(bold_line.split("*")):
            it_line += split
            if split != "" and i != len(bold_line.split("*")) - 1:
                if cpt % 2 == 0:
                    it_line += r"\textit{"
                    cpt += 1
                else:
                    it_line += "}"
                    cpt += 1

    else:
        it_line = bold_line

    return it_line


def underscore(line):
    """add \ when there is an underscore"""
    #TODO: pb quand c'est dans un environement code ou url ou nom d'une image
    if '_' in line:
        new_line = ""
        for caracter in line:
            if caracter == '_':
                new_line += "\\"
            new_line += caracter
        return new_line
    return line


def check_skipline(line):
    if len(line) > 2 and line[-1] == "\\" and line[-2] != "\\" :
        return line + "\\"
    return line


def url(line):
    #TODO: pb dans les paranthes (see swarm project)
    https = 'https'
    if https in line and line[0] != "$":
        split_line = line.split(https)
        new_line = split_line[0]
        for split in split_line[1:]:
            new_line += r'\url{' + https

            # check the end of the url
            split_space = split.split(' ')
            split_parenthese = split.split(')')
            if len(split_space[0]) < len(split_parenthese[0]):
                "the end is with < >"
                new_line += split_space[0] + '}'
                for word in split_space[1:]:
                    new_line += word + ' '
            else:
                "the end is with <)>"
                new_line += split_parenthese[0] + '}'
                for word in split_parenthese[1:]:
                    new_line += word + ')'

        return new_line
    return line
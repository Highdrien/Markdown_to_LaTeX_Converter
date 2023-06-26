def table(contents):
    """ traite des tableaux"""
    text = []
    table_run = False
    for line in contents:
        if len(line) > 1 and line[0] == "|" and not(table_run):
            text.append(r"\begin{center}")
            text.append(r"\begin{tabular}{" + (occurance(line, "|") - 1) *"|l" + "|}")
            text.append(r"\hline")
            table_run = True
        
        if table_run and (len(line) < 1 or line[0] != "|"):
            table_run = False
            text.append(r"\end{tabular}")
            text.append(r"\end{center}")
        
        if table_run and occurance(line, "-") < 10:
            line_split = line.split("|")
            new_line = ""
            for split in line_split:
                if split != "":
                    new_line += split
                    new_line += " & "
            text.append(new_line[:-2] + "\\\\")
            text.append(r"\hline")
        
        if not(table_run):
            text.append(line)

    return text


def occurance(l, x):
    c = 0
    for y in l:
        if x == y:
            c += 1
    return c
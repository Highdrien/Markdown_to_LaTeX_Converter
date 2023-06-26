def begin(autor=None, title=None, language="english", margin=None):
    """ ajoute les package dans le document"""
    text = [r"\documentclass{article}", r"\usepackage[utf8]{inputenc}", "",
            r"\usepackage["+language+"]{babel}",  r"\usepackage{hyperref}", 
            r"\usepackage{graphicx}", r"\usepackage{listings}", ""]
    
    if margin != "big":
        set_margin = [r"\usepackage{geometry}", r"\geometry{hmargin=2.5cm,vmargin=1.5cm}", ""]
        text += set_margin

    text.append(r"\begin{document}")
    text.append("")

    if not autor is None:
        if type(autor) == str:
            text.append(autor)

        elif type(autor) == list:
            for x in autor:
                text.append(x+r'\\')
        
        text.append("")
    
    if not title is None:
        make_title=[r"\begin{center}", r"\Large", title, "\end{center}", r"\bigskip"]
        text += make_title
    
    text.append(r'\tableofcontents')
    text.append(r"\bigskip")
    text.append("")    

    return text


def end():
    return [r"\end{document}"]
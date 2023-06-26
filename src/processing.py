from src.table import table
from src.itemize import item
from src.begin_end import begin, end
from src.images_processing import check_image
from src.special_caracters import replace_special_caracter
from src.alt_96 import check_alt_96_inline, check_code_environment
from src.lines_processing import bold_and_it, section, check_skipline, underscore, url


def process(contents, autor=None, title=None, language="english", margin=None):
    """Turns a markdown line list into latex text
    :param contens: markdown line list
    :param autor: author(s), None, str or list str
    :param title: title
    :param language: language
    :param margin: margin None or "big"
    """
    text = []
    contents = check_image(contents)
    contents = check_code_environment(contents)
    code_environment = "verbatim"
    in_code_environment = False       
    
    for line in contents:
        if code_environment in line:
            in_code_environment = not in_code_environment
        
        if not in_code_environment:
            line = bold_and_it(line)
            line = section(line)
            line = check_alt_96_inline(line)
            line = check_skipline(line)
            line = underscore(line)
            line = replace_special_caracter(line)
            line = url(line)
        
        text.append(line)
        
        
    
    text = table(text)
    text = item(text)
    
    return begin(autor, title, language, margin) + text + end()




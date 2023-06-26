"""
check if there are the carater: `
2 cases:  

`word`          will be     \textit{word}

```bash                     \begin{lstlisting}
code            will be     code
```                         \end{lstlisting}
"""

def check_alt_96_inline(line):
    if '`' in line and not '```' in line:
        new_line = ''
        split_line = line.split('`')
        count = 1
        for i, words in enumerate(split_line):
            if i != 0:
                if count % 2 == 1:
                    new_line += r"\textit{" + words
                else:
                    new_line += "}" + words
                count += 1
            else:
                new_line += words

        if count % 2 == 0:
            new_line += "}"

        return new_line
    return line


def check_code_environment(contents):
    text = []
    table_run = False
    for line in contents:
        if '```' in line and not table_run:
            text.append(r"\begin{verbatim}")
            table_run = True
        elif '```' in line and table_run:
            text.append(r"\end{verbatim}")
            table_run = False
        else:
            text.append(line)
    return text


if __name__ == '__main__':
    line = check_alt_96_inline('You can find in the folder, the article in question: `Transitivity_on_subclasses_of_bipartite_graphs.pdf`, my slide for my presentation: `LaTeX_beamer.pdf`. I have also implemented the algorithms in the article in python, which you can also find in the `src` folder.')
    print(line)
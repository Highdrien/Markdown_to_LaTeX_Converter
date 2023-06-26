def check_image(content):
    new_content = []
    for line in content:
        if len(line) > 10 and line[:2] == "<p" and line[-4:] == "><p>":
            image = [r'\begin{figure}[h!]']
            if 'align="center"' in line:
                    image.append(r'\centering')
            src = line.split("src=")[-1].split('>')[0]
            image.append(r'\includegraphics[width=10cm]{' + src + '}')
            image.append(r'\caption{image}')
            image.append(r'\end{figure}')
            new_content += image
        else:
             new_content.append(line)
    return new_content
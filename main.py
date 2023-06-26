import os
import yaml
from easydict import EasyDict as edict
from src.processing import process


def load_config(path):
    stream = open(path, 'r')
    return edict(yaml.safe_load(stream))


def read_md(file, begin_line=1):
    contents = []
    try:
        fic = open(file, 'r', encoding='utf8')
    except IOError:
        raise('error can ont open the file')
    
    for line in fic:
        contents.append(line[:-1])

    return contents[begin_line - 1:]


def write_tex(file, contents):
    with open(file, 'w', encoding='utf8') as f:
        for line in contents:
            f.write(line + '\n')


def main(config_path):
    config = load_config(config_path)

    md_path = os.path.join(config.markdown.folder, config.markdown.file)
    contents = read_md(md_path, begin_line=config.param.begin_line)

    text = process(contents,
                   autor=config.param.autor,
                   title=config.param.title,
                   margin=config.param.margin,
                   language=config.param.language)
    
    latex_file = config.markdown.file[:-3] + '.tex'
    tex_path = os.path.join(config.latex.folder, latex_file)
    write_tex(tex_path, text)
    print('Done')
    print('The file was save in', tex_path)


if __name__ == "__main__":
    config_path = 'config.yaml'
    main(config_path)
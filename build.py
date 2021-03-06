"""
Description:
    this script is modified from localization.bat

Purposes:
    quick build "html" from "rst" files

How to run this script?

    1. you must prepare .pth file and put it on the PYTHON path, and .pth contains are like below:
        D:/GitServer/work_space/repcarsonlibrary
        ...

    2. pip install sphinx
        after you run this command, it will create {sphinx-build.exe, sphinx-intl.exe, sphinx-quickstart.exe ...} in your python Scripts directory.

"""

from stdafx import show_current_job_at_console  # just like the regular print function but decorated with special text.  (It's not necessary)
from subprocess import Popen, PIPE, DEVNULL
from os import scandir, path, startfile, remove
from shutil import rmtree
import configparser  # https://docs.python.org/3/library/configparser.html
from jinja2 import Environment, PackageLoader
import warnings


def show_job(job_desc, align='center', flag='*', flag_len=60):
    def deco(fun):
        def wrapper(*arg, **option):
            show_current_job_at_console(job_desc, align, flag, flag_len)
            return fun(*arg, **option)
        setattr(wrapper, '__name__', fun.__name__)
        return wrapper
    return deco


"""
def show_current_job_at_console(msg, align='center', flag='*', flag_len=60):
    msg_flag_len = int(flag_len/2) if align == 'center' else flag_len
    align_dict = dict(left='<', center='^', right='>')
    print(f"{flag * flag_len}\n{msg:{align_dict[align]}{msg_flag_len}}\n{flag * flag_len}")
    return True
"""


def run_cmd_command(cmd_list):
    print(f"run command:  {' '.join(cmd_list)}")
    # job = Popen(cmd_list, stdout=PIPE, stderr=PIPE, stdin=DEVNULL)  # for debug
    job = Popen(cmd_list, stdout=PIPE, stderr=DEVNULL, stdin=DEVNULL)
    result = job.communicate()
    return result[0].decode()


@show_job('create .pot: get all text from source/*.rst')
def get_text(src_dir, out_dir):
    # sphinx-build source gettext -b gettext
    print(run_cmd_command(["sphinx-build", src_dir, f"_gettext",
                           "-b", "gettext"]))
    input('Please press any key to continue...')


@show_job('available language list:', align='left', flag='-', flag_len=30)
def show_language_list(src_dir, local_dirs, pause_flag=True):
    locale_dirs = path.abspath(path.join(src_dir, local_dirs))
    if not path.exists(locale_dirs):
        print(f'File Not Found Error: {locale_dirs}')
        return []

    language_list = []
    for cur_dir_path in [entry.path for entry in scandir(locale_dirs) if entry.is_dir(follow_symlinks=False)]:
        lang = path.basename(cur_dir_path)
        print(lang)
        language_list.append(lang)
    if pause_flag:
        input('\nPlease press any key to continue...')
    return language_list


@show_job('create .po: from _gettext/*.pot to source/locale/*.po')
def get_po_file(locale_dir, lang_list):
    """
    REM sphinx-intl update -p _gettext  # If the language directory already exists, just using this command!
    sphinx-intl update -p _gettext -l zh_TW -l en -l zh-CN
    REM sphinx-intl update -p _gettext -l en  It't ok {-l multiple language}
    """

    if lang_list == "" and path.exists(locale_dir):
        print(run_cmd_command(["sphinx-intl", 'update', '-p', f"_gettext"]))
        input('Please press any key to continue...')
        return

    if lang_list == "":
        print('Language folder is empty. You must select a language before initial.')
        return

    for cur_lang in lang_list.split(','):
        print(run_cmd_command(["sphinx-intl", 'update', '-p', f"_gettext",
                               '-l', cur_lang]))
    input('Please press any key to continue...')


@show_job('build html.')
def sphinx_build_html(args):
    src_dir, out_dir, locale_dirs = args.src_dir, args.out_dir, args.locale_dirs
    # sphinx-build -b html source docs/zh_TW  -D language=zh_TW

    while 1:
        lang_list = show_language_list(src_dir, locale_dirs)

        if len(lang_list) == 0:
            print('empty language list')
            return

        response_lang = input('which language would you want to build (exit:-1)?')
        if response_lang == '-1':
            break

        if response_lang not in lang_list:
            print("input language not in language list")
            continue

        # sphinx-build -b html source docs/en  -D language=zh_TW
        user_response = input('rebuild (Y/N)?')
        cmd_list = ["sphinx-build.exe"]
        if user_response.upper() == 'Y':
            cmd_list.append("-E")
        cmd_list.extend(['-b', 'html',
                         src_dir, f"{out_dir}/{response_lang}",
                         '-D', f"language={response_lang}"])
        print(run_cmd_command(cmd_list))
        out_path = path.abspath(f'{out_dir}/{response_lang}')
        startfile(path.join(out_path, 'index.html'))
        if path.exists(path.join(out_path, '_sources')):
            rmtree(path.abspath(f'{out_dir}/{response_lang}/_sources'))
            print(f'remove _sources file')
        if path.exists(path.join(out_path, '.doctrees')):  # http://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-d
            # Since Sphinx has to read and parse all source files before it can write an output file, the parsed source files are cached as “doctree pickles”.
            rmtree(path.abspath(f'{out_dir}/{response_lang}/.doctrees'))
            print(f'remove unnecessary files: *.doctrees, *.pickle')
        input('Please press any key to continue...')


@show_job('create home index page')
def build_select_language_page(out_dir, ruby_dir):
    sass_bat_path = path.abspath(path.join(ruby_dir, 'sass.bat'))
    if not path.exists(sass_bat_path):
        warnings.warn(f'sass.bat are not exists. {sass_bat_path}', stacklevel=2)
        print(r'Please install ruby: https://rubyinstaller.org/downloads/  and set ruby. for example ruby: C:\Ruby25-x64\bin')
        return

    abspath = path.abspath
    input_scss_dir = abspath('_build/select_language.scss')
    output_css = abspath(out_dir + '/select_language.css')
    # sass.bat which location is at: {Ruby25-x64\bin\}. you must install ruby
    run_cmd_command(['sass.bat',  # you must give file extension: .bat otherwise, it will cause ambiguous because it has two files sass, sass.bat both with the same name: sass
                     '--style', 'compressed',
                     input_scss_dir, output_css])

    map_file = output_css+'.map'
    if path.exists(map_file):
        remove(map_file)
        print(f'remove unncessary file:{map_file}')

    language_html = path.abspath(f'{out_dir}/index.html')
    if path.exists(language_html):
        startfile(language_html)


@show_job('build_user_define_html')
def build_user_define_html(in_args, options):
    src_dir, out_dir, local_dir = in_args.src_dir, in_args.out_dir, in_args.locale_dirs
    env = Environment(loader=PackageLoader(src_dir))  # __init__ must exists in "src_dir"
    template = env.get_template('select_language.j2')  # this file be wrap at "templates". i.e. {src_dir}/templates/select_language.j2
    list_language = show_language_list(src_dir, local_dir, pause_flag=False)
    dict_language = dict()
    for lang in list_language:
        value = lang.replace('_', '-')
        if value == 'zh-TW':
            value += ' (繁體中文)'
        dict_language[lang] = value

    content = template.render(dict_language=dict_language, analytics_id=options.get('analytics_id'))
    out_file = path.join(out_dir, 'index.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)
    startfile(out_file)


def main():
    global args
    if show_current_job_at_console('your config:'):
        for attr_name in vars(args):
            print(f'{attr_name:<15}: {getattr(args, attr_name)}')

    dict_run = {
        0: ('Exit script', lambda: exit(0)),
        1: (get_text.__name__, lambda: get_text(args.src_dir, args.out_dir)),
        2: (show_language_list.__name__, lambda: show_language_list(args.src_dir, args.locale_dirs)),
        3: (get_po_file.__name__, lambda: get_po_file(path.abspath(path.join(args.src_dir, args.locale_dirs)), args.lang)),
        4: (sphinx_build_html.__name__, lambda: sphinx_build_html(args)),
        10: (build_select_language_page.__name__, lambda: build_select_language_page(args.out_dir, args.ruby_dir)),  # css
        11: (build_user_define_html.__name__, lambda: build_user_define_html(args, args.options)),
        99: (run_all_process.__name__, lambda: run_all_process(args)),  # this command (that run all procedure) usually used for the first building
    }
    while 1:
        if show_current_job_at_console('choice action:'):
            for case_number, action in dict_run.items():
                action_name = action[0]
                print(f'{case_number:<6} {action_name.replace("_", " ")}')

        start_action = None
        case = input('\n\ninput action number:')
        try:
            start_action = dict_run[int(case)][1]
        except Exception as e:
            print('action number not found')
        if start_action:
            start_action()


def run_all_process(args):
    get_text(args.src_dir, args.out_dir)
    get_po_file(args.out_dir, args.lang)
    sphinx_build_html(args)
    build_select_language_page(args.out_dir, args.ruby_dir)
    build_user_define_html(args, args.options)


if __name__ == '__main__':
    from argparse import ArgumentParser

    arg_parser = ArgumentParser()
    arg_parser.add_argument("-l", "--language", help="en,zh_TW... (LEARN MORE > http://www.sphinx-doc.org/en/master/usage/configuration.html)",
                            dest="lang", default="")
    arg_parser.add_argument("--src_dir", help="source ('source' is example but recommended)", dest="src_dir", default='source')
    arg_parser.add_argument("--out_dir", help="docs (if you are using GitHub Page, I strongly recommend you use docs.)", dest="out_dir", default='docs')
    arg_parser.add_argument("--locale_dirs", help="locale/  (it must same with variable locale_dirs that from conf.py)", dest="locale_dirs", default='locale/')
    arg_parser.add_argument("--config_file", help="build.ini (if you provide this file, then all of the other settings will be ignored)",
                            dest="config_file", default='build.ini')
    args = arg_parser.parse_args()
    args.__setattr__('ruby_dir', None)
    args.__setattr__('options', dict())
    if path.exists(args.config_file):
        config_file = path.abspath(args.config_file)
        assert path.exists(args.config_file), f'{config_file} are not exists!'
        config = configparser.ConfigParser()
        config.read(config_file)
        args.src_dir = config['PATH']['source']
        args.out_dir = config['PATH']['out_dir']
        args.locale_dirs = config['PATH']['locale_dirs']
        args.lang = config['LANGUAGE']['lang']

        args.ruby_dir = config['PATH'].get('ruby')
        if len(config.items('OPTIONS')):
            for key, value in config.items('OPTIONS'):
                args.options[key] = value
    main()

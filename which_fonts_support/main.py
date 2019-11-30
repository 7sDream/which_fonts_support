import collections
import functools
import subprocess


__all__ = ['available_fonts_for_codepoint']


def __make_lang_obj(items, langs):
    obj = collections.defaultdict(list)
    for lang, item in zip(langs, items):
        obj[lang].append(item)
    return obj


def __get_font_by_lang(items, langs, lang='en'):
    item = items[0]
    obj = __make_lang_obj(items, langs)
    if lang in obj:
        item = obj[lang][0]
    return item


def available_fonts_for_codepoint(codepoint, fc_list_exec):
    assert 0 < codepoint < 0x10FFFF

    charset_arg = ':charset=' + hex(codepoint)

    result = subprocess.run([
        fc_list_exec,
        '--format',
        '%{family}\t%{familylang}\t%{fullname}\t%{fullnamelang}\n',
        charset_arg],
        stdout=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(
            'run fc-list failed, please check your environment\n')

    descriptions = result.stdout.decode('utf-8', 'replace').split('\n')

    for line in descriptions:
        parts = list(map(functools.partial(str.split, sep=','), line.split('\t')))
        if len(parts) == 4 and all(map(lambda p: len(p) > 0, parts)):
            families, families_lang, fullnames, fullnames_lang = parts[0], parts[1], parts[2], parts[3]
            if len(families) == len(families_lang) and len(fullnames) == len(fullnames_lang):
                family = __get_font_by_lang(families, families_lang)
                fullname = __get_font_by_lang(fullnames, fullnames_lang)
                yield family.lstrip('.'), fullname.lstrip('.')

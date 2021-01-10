import re
import textwrap
import random


def displaymatch(match: re):
    if match is None:
        return None
    return '<Match: %r, group=%r?>' % (match.group(), match.groups())


def demo_displaymatch():
    valid = re.compile(r"^[a2-9tjqk]{5}$")
    print(displaymatch(valid.match("akt5q")))
    print(displaymatch(valid.match("akt5e")))
    print(displaymatch(valid.match("akt")))
    print(displaymatch(valid.match("727ak")))


def demo_backreferences():
    pair = re.compile(r".*(.).*\1")
    print(displaymatch(pair.match("717ak")))
    print(displaymatch(pair.match("718ak")))
    print(displaymatch(pair.match("354aa")))


def demo_group():
    pair = re.compile(r".*(.).*\1")
    print(pair.match("717ak").group(1))
    # this will return : Attr error because of NoneType
    # print(pair.match("718ak").group(1))
    print(pair.match("354aa").group(1))


def demo_search_vs_match():
    print(re.match('c', 'abcdef'))
    print(re.search('c', 'abcdef'))

    # however that in MULTILINE mode match() only matches at the beginning of the string,
    # whereas using search() with a regular expression beginning with '^' will match at the beginning of each line.
    print(re.match('X', 'A\nB\nX', re.MULTILINE))
    print(re.search('^X', 'A\nB\nX', re.MULTILINE))


def demo_making_phonebook():
    text = textwrap.dedent("""\
Ross McFluff: 834.345.1254 155 Elm Street
    
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way

Heather Albrecht: 548.326.4584 919 Park Place""")

    entries = re.split("\n+", text)
    print(entries)
    print([re.split(":? ", entry, 4) for entry in entries])


def repl(m):
    inner_word = list(m.group(2))
    print(inner_word)
    random.shuffle(inner_word)
    return m.group(1) + ''.join(inner_word) + m.group(3)


def demo_text_munge():
    text = "Professor Abdolmalek, please report your absences promptly."
    print(re.sub(r"(\w)(\w+)(\w)", repl, text))


def demo_finding_all_adverbs():
    text = "He was carefully disguised but captured quickly by police."
    print(re.findall(r"\w+ly", text))


def demo_finding_all_adverbs_and_their_positions():
    text = "He was carefully disguised but captured quickly by police."
    for m in re.finditer(r"\w+ly", text):
        print('{:02d}-{:02d}: {:s}'.format(m.start(), m.end(), m.group(0)))


def demo_raw_string_notation():
    # Raw string notation (r"text") keeps regular expressions sane.
    # Without it, every backslash ('\') in a regular expression would have to be prefixed with another one to escape it.
    print(re.match(r"\W(.)\1\W", " ff "))
    print(re.match("\\W(.)\\1\\W", " ff "))

    print(re.match(r"\\", r"\\"))
    print(re.match("\\\\", r"\\"))


def tokenizer(code):
    import collections

    Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER', r'\d+(\.\d*)?'),  # integer or decimal number
        ('ASSIGIN', r':='),  # assignment operator
        ('END', r';'),  # statement terminator
        ('ID', r'[A-Za-z]+'),  # Identifiers
        ('OP', r'[+\-*/]'),  # arithmetic operators
        ('NEWLINE', r'\n'),  # line endings
        ('SKIP', r'[ \t]+'),  # skip over spaces and tabs
        ('MISMATCH', r'.'),  # any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    print(tok_regex)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (value, line_num))
        else:
            if kind == 'ID' and value in keywords:
                kind = value
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)


def demo_tokenizer():
    statements = '''
        IF quantity THEN
            total := total + price * quantity;
            tax := price * 0.05;
        ENDIF;
    '''
    for token in tokenizer(statements):
        print(token)


if __name__ == '__main__':
    # demo_displaymatch()
    # demo_backreferences()
    # demo_group()
    # search_vs_match()
    # demo_making_phonebook()
    # demo_text_munge()
    # demo_finding_all_adverbs()
    # demo_finding_all_adverbs_and_their_positions()
    # demo_raw_string_notation()
    demo_tokenizer()

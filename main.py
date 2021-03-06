from interpreter_module.iparser import parser
from lexer_module.lexer import lexer


def main():
    filename = r'files\test.cb'
    with open(filename) as f:
        text_input = f.read()

    tokens = lexer.lex(text_input)
    parser.parse(tokens).eval()


if __name__ == '__main__':
    main()

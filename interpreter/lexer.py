# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, SIN, COS, TAN, CTG, SQRT, POW, LOG, LT, GT, LTE, GTE, STRING, COMMA, EQ, LB, LG, FLOAT = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'SIN', 'COS', 'TAN', 'CTG', 'SQRT', 'POW', 'LOG', 'LT',
    'GT', 'LTE', 'GTE', 'STRING', 'COMMA', 'EQ', 'LB', 'LG', 'FLOAT'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()

        return result

    def double(self):
        result = ''
        while self.current_char is not None and (self.current_char.isdigit or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result)

    def math_function(self):
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return str(result)

    def isLTE(self):
        if self.current_char == '<' and self.text[(self.pos + 1)] == '=':
            return True
        return False

    def isGTE(self):
        if self.current_char == '>' and self.text[(self.pos + 1)] == '=':
            return True
        return False

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                result = self.integer()
                if float(result).is_integer():
                    return Token(INTEGER, int(result))
                else:
                    return Token(FLOAT, float(result))

            if self.current_char.isalpha():
                result = self.math_function()
                return Token(STRING, result)
            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')
            if self.current_char == '=':
                self.advance()
                return Token(EQ, '=')
            if self.isGTE():
                self.advance()
                self.advance()
                return Token(GTE, '>=')
            if self.isLTE():
                self.advance()
                self.advance()
                return Token(LTE, '<=')
            if self.current_char == '>':
                self.advance()
                return Token(GT, '>')
            if self.current_char == '<':
                self.advance()
                return Token(LT, '<')
            self.error()
        return Token(EOF, None)

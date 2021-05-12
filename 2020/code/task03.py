from pycon_decorators import register
from pycon_decorators import REGISTERED


@register
def true_or_false(text):
    """Parse text to True or False"""
    tf_values = {
        True: {"true", "on", "yes", "1"},
        False: {"false", "off", "no", "0"},
    }
    for tf, values in tf_values.items():
        if text.lower() in values:
            return tf


@register
def reversed(text):
    """Reverse text"""
    return text[::-1].capitalize()


@register
def robber_language(text):
    """Translate text to robber language"""
    consonants = "bcdfghjklmnpqrstvwxyz"
    return "".join(f"{c}o{c.lower()}" if c.lower() in consonants else c for c in text)


text = input("Please input a text: ")
while True:
    print(f"Parsers: {', '.join(REGISTERED)}")
    parser = input("Choose a parser: ")
    if parser in REGISTERED:
        break

parser_func = REGISTERED[parser]
print(parser_func(text))

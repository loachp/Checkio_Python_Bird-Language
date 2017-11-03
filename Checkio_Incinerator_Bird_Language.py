def translate(phrase):
    import re
    letters = re.findall(r"a{3}|e{3}|i{3}|o{3}|u{3}|y{3}|[^aeiouy]", phrase)
    translated = "".join([letter[0] for letter in letters])
    return translated

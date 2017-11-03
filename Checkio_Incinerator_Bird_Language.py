def translate(phrase):
    import re
    letters = re.findall(r"a{3}|e{3}|i{3}|o{3}|u{3}|y{3}|[^aeiouy]", phrase)
    translated = "".join([letter[0] for letter in letters])
    return translated
    
translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"
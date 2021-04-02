import unicodedata


def utf8_to_ascii(string: str) -> str:
    normalized = unicodedata.normalize("NFKD", string)
    ascii_bytes = normalized.encode("ascii", "ignore")
    ascii_string = ascii_bytes.decode()
    return ascii_string


utf8_string = "Vous êtes le Père Noël ? s'étonna le petit garçon."
ascii_string = utf8_to_ascii(utf8_string)

print(ascii_string)

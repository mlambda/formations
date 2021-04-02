import re


charref = re.compile(
    r"""
        &[#]                  # Début d'une référence d'entité numérique
        (
              0[0-7]+         # Forme octale
            | [0-9]+          # Forme décimale
            | x[0-9a-fA-F]+   # Forme hexadécimale
        )
        ;                     # Point-virgule final
    """,
    re.VERBOSE,
)

charref = re.compile("&#(0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")

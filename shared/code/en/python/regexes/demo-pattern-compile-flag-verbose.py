import re

charref = re.compile(
    r"""
        &[#]                  # Start of a numerical entity reference
        (
              0[0-7]+         # Octal form
            | [0-9]+          # Decimal form
            | x[0-9a-fA-F]+   # Hexadecimal form
        )
        ;                     # Final semicolon
    """,
    re.VERBOSE,
)

charref = re.compile("&#(0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")

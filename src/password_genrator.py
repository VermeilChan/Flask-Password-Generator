from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_password(
    length=16,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special=True,
):
    characters = ""
    if include_uppercase:
        characters += ascii_uppercase
    if include_lowercase:
        characters += ascii_lowercase
    if include_digits:
        characters += digits
    if include_special:
        characters += punctuation
    generated_password = "".join(choice(characters) for _ in range(length))

    return generated_password

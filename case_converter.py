def convert_to_snake_case(pascal_or_camel_cased_string):
    

    # List comprehension with inline if/else inside it
    # Builds a list where uppercase letters are converted to '_'+lowercase
    # Non-uppercase letters are added as-is
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join list into a full string and strip leading underscore (if any)
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # Example usage: converting a PascalCase string to snake_case
    print(convert_to_snake_case('IAmAPascalCasedString'))
    # Output: i_am_a_pascal_cased_string


# Run the main function
main()



"""
    Converts a PascalCase or camelCase string to snake_case.

    🔍 Concept:
    - PascalCase / camelCase are naming styles where words are joined together and capital letters indicate word boundaries.
    - snake_case uses lowercase letters and underscores (_) to separate words.

    🛠 Python Concepts Used:
    - List Comprehension with inline if/else: A concise way to create a list with conditions inside.
      Syntax: [true_expr if condition else false_expr for item in iterable]
    - String Methods:
        - .isupper(): checks if a character is uppercase
        - .lower(): converts a character to lowercase
    - ''.join(): joins list elements into a single string
    - .strip('_'): removes any leading or trailing underscores

    🧠 How it works:
    - Iterates over each character in the input string
    - If the character is uppercase:
        - Converts it to lowercase
        - Adds an underscore before it
    - If it’s not uppercase:
        - Keeps it as it is
    - The resulting list is then joined into a string and cleaned up
    """
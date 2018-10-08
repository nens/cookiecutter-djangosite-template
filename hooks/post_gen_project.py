import random
import string
import os
import re


SECRET_KEY_REGEX = "(?<=^SECRET_KEY \= ).*$"


def find_settings():
    """
    Looks up settings.py in the current root.
    And returns it if it is the only one.
    """
    settings_files = [
        os.path.join(root, f) for root, _, filenames in os.walk('.')
        for f in filenames if f == 'settings.py'
    ]
    assert len(settings_files) == 1
    return settings_files[0]


def secret_gen():
    """Generates 50 character secret."""
    return ''.join(
        random.choice(string.printable[:94].replace('"', '')) for _ in
        range(50)
    )


def insert_secret_in_settings():
    """Finds settings.py and replaces its secret key phrase."""
    secret = secret_gen()
    settings_file = find_settings()

    with open(settings_file, 'r') as f:
        content = f.read()

    regex = re.compile(SECRET_KEY_REGEX, re.MULTILINE)
    settings_with_secret = regex.sub('"{}"'.format(secret), content)

    with open(settings_file, 'w') as f:
        f.write(settings_with_secret)


if __name__ == '__main__':
    insert_secret_in_settings()

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$')
TELEFONO_PY_REGEX = re.compile(r'^595[0-9]{9}$')

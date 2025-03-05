import re


def validate_select(query):
    select_pattern = re.compile(r"^\s*SELECT\s+(DISTINCT\s+)?[\w\*,\s]+\s+FROM\s+\w+(\s+WHERE\s+.+)?\s*$",
                                re.IGNORECASE)
    if select_pattern.match(query):
        return True
    else:
        return False

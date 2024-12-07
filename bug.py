def function_with_uncommon_error(data):
    if not data:
        return []
    result = [item for item in data if item > 0]
    return result
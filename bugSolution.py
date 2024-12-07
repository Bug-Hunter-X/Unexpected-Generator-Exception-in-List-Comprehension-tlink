def function_with_uncommon_error_solution(data):
    if not data:
        return []
    try:
        result = [item for item in data if item > 0]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return result
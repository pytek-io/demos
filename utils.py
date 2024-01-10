def merge_dicts(d1, d2):
    result = d1
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            merge_dicts(result[k], v)
        else:
            result[k] = v
    return result


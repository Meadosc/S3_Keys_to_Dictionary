# Error Handling and Preflight Check Functions


def check_parameters(keys_list):
    # could expand this later, but for now it's only checking for a root folder in keys_list
    possible_root = min(keys_list, key=len)

    for key in keys_list:
        if len(key) == len(possible_root) and key != possible_root:
            raise ValueError("keys_list must have a root key, similar to a directory")
        
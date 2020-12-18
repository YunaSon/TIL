def group_by_owners(files):
    result = {}
    for key, value in files.items():
        if value not in result.keys():
            # Insert the values into the resulting dictionary
            # by interchanging the key, values.
            result[value] = [key]
        else:
            # Append the othet file name if the owner is same.
            result[value].append(key)
    return result
if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))








def group_by_owners(files):
    result = {}
    for file, owner in files.items():  # use files.iteritems() on Python 2.x
        result[owner] = result.get(owner, []) + [file]  # you can use setdefault(), too
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
# {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}

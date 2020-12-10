def read_file_ints(path):
    with open(path, "r") as f:
        content = [int(line.rstrip()) for line in f]
    return content

def read_file_strings(path):
    with open(path, "r") as f:
        content = [line.rstrip() for line in f]
    return content

def read_file(path):
    with open(path, "r") as f:
        content = f.readlines()
    return content

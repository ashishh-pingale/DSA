def SimplifyPath(Path):
    stack = []

    for part in Path.split("/"):
        if not part or part == ".":
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


path = "/home/user/Documents/../Pictures"
print(SimplifyPath(path))
def group_anagram(strs):
    group = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in group:
            group[key] = []

        group[key].append(word)

    return list(group.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))


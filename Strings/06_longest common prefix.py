def longestCommonPrefix(strs):
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
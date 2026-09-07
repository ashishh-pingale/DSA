def strStr(haystack, needle):
    n = len(needle)

    for i in range(len(haystack) - n + 1):
        if haystack[i:i+n] == needle:
            return i

    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack,needle))
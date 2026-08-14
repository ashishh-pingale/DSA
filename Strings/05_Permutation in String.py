def permutation(s1,s2):
    if len(s1) > len(s2):
        return False

    freq = {}
    window = {}

    for char in s1:
        freq[char] = freq.get(char , 0) + 1
    left = 0

    for right in range(len(s2)):
        window[s2[right]] = window.get(s2[right] , 0) + 1

        if right - left + 1 > len(s1):
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1
        if freq == window:
            return True
    return False

s1 = "ab" 
s2 = "eidboaoo"

print(permutation(s1,s2))


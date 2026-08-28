def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    
    for i in range(len(s1)):
        freq1[s1[i]] = freq1.get(s1[i] , 0) + 1
    for j in range(len(s2)):
        freq2[s2[j]] = freq2.get(s2[j] , 0) + 1

    return freq1 == freq2

s = "anagram"
t = "nagaram"
print(anagram(s,t))
from collections import Counter

def maxNumberOfBalloons(text):
    cnt = Counter(text)
    
    return min(
        cnt['b'],
        cnt['a'],
        cnt['l'] // 2,
        cnt['o'] // 2,
        cnt['n']
    )

text = "nlaebolko"
print(maxNumberOfBalloons(text))
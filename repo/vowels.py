s = "programming"
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print(count)
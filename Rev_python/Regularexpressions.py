import re
p = r"a."
text= "aa aab asbs"
print(re.findall(p, text))  # Output: ['aa', 'a', 'a']
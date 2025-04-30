import re

text = "apple,banana,orange,grape,red,blue"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

import re

text = '''<div>
<span class="actionBar__text"> Showing 18 of 101

products.

</span>

</div>'''

#Regex pattern
pattern = r'\b(\d+)\b'

# Extract values that match regex pattern
matches = re.findall(pattern, text)

#Extracts the second number found in the string being 101
print(matches[1])

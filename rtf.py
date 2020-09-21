from striprtf.striprtf import rtf_to_text


with open('j.rtf', 'r') as f:
    data = f.read()

text = rtf_to_text(data)
print(text)

import pyperclip,re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #区号，可选，形式为010或（010）
    (\s|-)?
    (\d{3})
    (\s|-)?
    (\d{4})
    (\s*(ext|x|ext.)(\d{2,5}))?  
)''', re.VERBOSE|re.I)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
Regex1 = phoneRegex.findall(text)
Regex2 = emailRegex.findall(text)
match = []
for i in Regex1:
    if i[1] == '':
        phoneNum = '-'.join(["xxx",i[3],i[5]])
    else:
        phoneNum = '-'.join([i[1],i[3],i[5]])
    match.append(phoneNum)
for k in Regex2:
    match.append(k[0])
#print(match)
if len(match) > 0:
    pyperclip.copy('\n'.join(match))

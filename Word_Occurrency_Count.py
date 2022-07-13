def clean_Text(txt):
    txt = txt.replace("’s", ' ')
    txt = txt.replace("'s", ' ')
    txt = txt.replace(',', ' ')
    txt = txt.replace(".", ' ')
    txt = txt.replace('!', ' ')
    txt = txt.replace(';', ' ')
    txt = txt.replace('?', ' ')
    txt = txt.replace('-', ' ')
    txt = txt.replace('"', ' ')
    txt = txt.replace("'", ' ')
    txt = txt.replace('“', ' ')
    txt = txt.replace('”', ' ')
    txt = txt.replace('‘', ' ')
    txt = txt.replace('’', ' ')
    txt = txt.replace('\n', '')
    return txt

f = open('FOMC Statement June 2022.txt', 'r', encoding='UTF-8') 

# read lines
content = f.readlines()

f.close

contentLines = ''
 
characers = []
stat = {}

# Interate every line.
for raw in content:
    raw = clean_Text(raw)        # clean up the line
    raw = raw.upper()
    tmp_list = raw.split(' ')    # split by space

    if len(raw) == 0:
        continue
    contentLines = contentLines + raw

    for x in range(0, len(tmp_list)):
        # If the string is first showed, then put in the "character" list
        if not tmp_list[x] in characers:
            characers.append(tmp_list[x])
        # If str is first showed, then put in the "stat" dictionary
        if tmp_list[x] not in stat:
            stat[tmp_list[x]] = 1
        # If showed, then add 1
        stat[tmp_list[x]] += 1

print(f'This article has {len(contentLines)} words')

str = input('Enter a word to search: ')
str = str.strip(' ')
try:
    print(f'[{str}] shows {stat[str.upper()]} times.')
except KeyError:
    print(f'There is no [{str}] in this article.')

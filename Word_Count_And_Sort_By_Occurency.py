def clean_Text(txt):
    txt = txt.replace("’s", '')
    txt = txt.replace("'s", '')
    txt = txt.replace(',', '')
    txt = txt.replace(".", '')
    txt = txt.replace('!', '')
    txt = txt.replace(';', '')
    txt = txt.replace('?', '')
    txt = txt.replace('-', '')
    txt = txt.replace('"', '')
    txt = txt.replace("'", '')
    txt = txt.replace('“', '')
    txt = txt.replace('”', '')
    txt = txt.replace('‘', '')
    txt = txt.replace('’', '')
    txt = txt.replace('\n', '')
    return txt

fr = open('James Webb Telescope Images.txt', 'r', encoding='UTF-8') 

# read lines
content = fr.readlines()

fr.close

contentLines = ''
 
characers = []
stat = {}

# Interate every line.
for raw in content:
    raw = clean_Text(raw)        # clean up the line
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
    
stat = sorted(stat.items(), key = lambda e:e[1], reverse=True)        # Sort by number of occurrences, in reverse order

for i in stat:
    print(i[0], i[1])

print(f'This article has {len(contentLines)} words')
# -*- coding: utf-8 -*-
import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.rfind('<script>')
end = content.rfind('</script>')
js = content[start+8:end]

depth = 0
in_str = False
str_char = ''
for i, ch in enumerate(js):
    if in_str:
        if ch == str_char and (i == 0 or js[i-1] != '\\'):
            in_str = False
    elif ch in "'\"":
        in_str = True
        str_char = ch
    elif ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth < 0:
            print('EXTRA ] at char', i)
            print('CONTEXT:', repr(js[max(0,i-80):i+20]))
            break

if depth == 0:
    print('BRACKETS BALANCED')
elif depth > 0:
    print('MISSING', depth, '] - checking where...')
    depth2 = 0
    last_pos = 0
    for i, ch in enumerate(js):
        if not in_str and ch == '[': last_pos = i; depth2 += 1
    print('Last [ at', last_pos, 'context:', repr(js[max(0,last_pos-40):last_pos+40]))

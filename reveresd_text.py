import codecs
with codecs.open('uni.txt', 'r', encoding='utf-8', errors='surrogateescape') as f:
    
    content = f.read()
    reversed_content = content[::-1]
    
   

with open('בנייני האומה סקריפט.txt', 'w') as fout:
    fout.write(reversed_content)





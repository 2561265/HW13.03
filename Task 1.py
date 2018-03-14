text = open('your text.txt', 'r')
print('The number of lines in the file are: ', len(text.readlines()),'\n')
text.seek(0)
count = 0
for line in text.readlines():
    count += 1
    words = line.split(' ')
    print('The line %s has: %s - symbols and %s words!' % (count, len(line), len(words)))
text.close()
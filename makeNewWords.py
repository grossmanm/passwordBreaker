file = open('newWords.txt','w')
words = [line.strip().lower() for line in open('words.txt')]
for i in words:
    file.write(i + '\n')
    for j in words:
        file.write(i+j+'\n')

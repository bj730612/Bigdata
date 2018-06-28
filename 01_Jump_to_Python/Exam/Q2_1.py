f = open('learning_python.txt', 'r', encoding='utf-8')

text = f.read()
text = text.split()
f.close()

new_text = []
for word in text:
   new_text.append(word.replace('python', 'c'))

f = open('learning_python.txt', 'w', encoding='utf-8')
new_text = ' '.join(new_text)
f.write(new_text)
f.close()

f = open('learning_python.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

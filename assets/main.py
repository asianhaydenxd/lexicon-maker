def save(txt):
    with open('py/lexiconMaker/saves/' + txt + '.txt', 'w') as lexicon:
        for i in lex:
            lexicon.write(i + ':' + lex[i] + '\n')

print('Define the file you want to edit/create for your lexicon (no .txt at the end, just the name).')
txt = input('File: ')

lex = {}

try:
    with open('lexicon-maker/assets/saves/' + txt + '.txt', 'r') as lexicon:
        for i in lexicon.readlines():
            param = i.split(':')
            lex[param[0]] = param[1]
            lex[param[0]] = lex[param[0]].replace('\n','')
except:
    open('lexicon-maker/assets/saves/' + txt + '.txt', 'x')

while True:
    x = input('> ')
    x = x.split(' ')
    
    if x[0] == 'help':
        print('qread = quick read the unsaved dictionary on this specific run')
        print('read = read the saved dictionary as saved in the .txt file')
        print('write X Y = add or override word X with definition Y (X is one word while Y is as many as needed)')
        print('save = save the unsaved dictionary')
        print('quit = save the unsaved dictionary and quit')
    elif x[0] == 'qread':
        for i in lex:
            print(i + ':' + lex[i])
    elif x[0] == 'read':
        with open('lexicon-maker/assets/saves/' + txt + '.txt', 'r') as lexicon:
            print(''.join(lexicon.readlines()))
    elif x[0] == 'write':
        lex[x[1]] = ''.join(x[2:])
        print('Defined word \'' + x[1] + '\' as \'' + ''.join(x[2:]) + '\'')
    elif x[0] == 'save':
        print('Saving...')
        save(txt)
        print('Saved')
    elif x[0] == 'quit':
        print('Saving...')
        save(txt)
        print('Saved')
        print('Quitting...')
        break

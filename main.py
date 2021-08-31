from enum import Flag
import requests as req
import os.path
import re

print('__---### WELCOME ###---__')
start = input('please enter your encoded nmonic phrase for decoding or press Enter to encode your nmonic: ')

if(start==''):
    def createNmonicWordsListFile():
        print('creating english.txt...')

        url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'
        res = req.get(url)

        file = open('./english.txt', 'w')
        file.write(res.text)
    
    #TODO: check sha256 hash of english.text instead of ask for overriding every time
    if(os.path.isfile('./english.txt')):
        print('english.text nmonic words list file already exists.')
        answer = input('do you want to override? y/n ')
        if(answer == 'y'):
            createNmonicWordsListFile()
    else:
        createNmonicWordsListFile()


    nmonicPhrase = input('please enter your nmonic phrase: ')
    nmonicList = nmonicPhrase.split(' ')
    file = open('./english.txt', 'r').read()
    newNmonic = []

    for word in nmonicList:
        similar = '\n'.join(re.findall('^' + word[:1] + '.*', file, flags=re.M))

        w = ''
        for a in word:
            w += a
            fa = re.findall('^'+w+'.*', similar, flags=re.M)
            if(len(fa) > 1):
                continue
            else:
                newNmonic.append(w)
                break

    print(''.join(newNmonic))
else:
    print('decoding process...')
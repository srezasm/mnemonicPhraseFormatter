import requests as req
import os.path
import re
from hashlib import sha256


def createNmonicWordsListFile():
    url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'
    res = req.get(url)

    file = open('./english.txt', 'w')
    file.write(res.text)


def checkEnglishFile():
    if(os.path.isfile('./english.txt')):
        file = open('./english.txt', 'r').read()
        if (sha256(file.encode('utf-8')).hexdigest() != "2f5eed53a4727b4bf8880d8f3f199efc90e58503646d9ff8eff3a2ed3b24dbda"):
            print('english.text file has currupted!')
            print('remaking english.txt...')
            createNmonicWordsListFile()

    else:
        createNmonicWordsListFile()


print('__---### WELCOME ###---__')

checkEnglishFile()

start = input(
    'please enter your encoded nmonic phrase for decoding or press Enter to encode your nmonic: ')


if(start == ''):
    data = open('./english.txt', 'r').read()
    nmonicPhrase = input('please enter your nmonic phrase: ')
    nmonicList = nmonicPhrase.split(' ')
    newNmonic = []

    for word in nmonicList:
        similar = '\n'.join(re.findall(
            '^' + word[:1] + '.*', data, flags=re.M))

        w = ''
        for char in word:
            w += char
            found = re.findall('^'+w+'.*', similar, flags=re.M)
            if(len(found) > 1):
                continue
            else:
                newNmonic.append(w)
                break

    print('   ', ''.join(newNmonic))
else:
    data = open('./english.txt', 'r').read()
    word = ''
    nmonic = ['']
    for char in start:
        word += char

        found = re.findall('^' + word + '.*', data, flags=re.M)

        if (len(found) > 1):
            continue
        else:
            nmonic.append(found[0])
            word = ''

    print('  ', ' '.join(nmonic))

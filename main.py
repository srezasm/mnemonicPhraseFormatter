import requests as req
import os.path

# create nmonic words list file function
def createNmonicWordsListFile():
    print('creating english.txt...')

    url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'
    response = req.get(url)

    file = open("./english.txt", "w")
    file.write(response.text)

if(os.path.isfile('./english.txt')):
    print('english.text nmonic words list file already exists.')
    answer = input('do you want to override? y/n ')
    if(answer == 'y'):
        createNmonicWordsListFile()

createNmonicWordsListFile()

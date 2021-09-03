import requests as req
import os.path
import re
from hashlib import sha256

# request and get english mnemonic words from source
def create_mnemonic_words_file():
    url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'
    res = req.get(url)

    with open('./english.txt', 'w') as file:
        file.write(res.text)


# check mnemonic words file checksum
def check_english_file_checksum():
    if(os.path.isfile('./english.txt')):
        with open('./english.txt','r') as file:
            file_data = file.read()
            if (sha256(file_data.encode('utf-8')).hexdigest() != "2f5eed53a4727b4bf8880d8f3f199efc90e58503646d9ff8eff3a2ed3b24dbda"):
                print('english.text file has corrupted!')
                print('remaking english.txt...')
                create_mnemonic_words_file()

    else:
        create_mnemonic_words_file()


print('__---### WELCOME ###---__')

check_english_file_checksum()

start = input(
    'please enter your encoded mnemonic phrase to decode or press Enter to encode your mnemonic: ')

# open `english.txt` file globally
with open('./english.txt','r') as file:
    # read mnemonic words file data
    data = file.read()

    # check if user wants to recover the original mnemonic phrase or generate a new formatted one
    if(start == ''):            
        mnemonic_phrase = input('please enter your mnemonic phrase: ')
        mnemonic_list = mnemonic_phrase.split(' ')
        new_mnemonic = []

        # loop on entered mnemonic phrase words
        for word in mnemonic_list:
            # find all similar mnemonics
            similar = '\n'.join(re.findall(
                '^' + word[:1] + '.*', data, flags=re.M))

            w = ''
            # loop on every character in nth `word`
            for char in word:
                # add character to `w` variable
                w += char
                # find all words that starts with `w`
                found = re.findall('^'+w+'.*', similar, flags=re.M)
                # if found words are more than 1, go on, elsewise add the found word to `new_mnemonic` list
                if(len(found) > 1):
                    continue
                else:
                    new_mnemonic.append(w)
                    break

        # print the `new_mnemonic`
        print('   ', ''.join(new_mnemonic))
    else:
        word = ''
        original_mnemonic_words = ['']

        # loop on entered characters
        for char in start:
            # add character to `word` variable
            word += char

            # find all mnemonic words that start with `word`
            found = re.findall('^' + word + '.*', data, flags=re.M)

            # if found words are more than 1, go on, elsewise add the found word to `original_mnemonic_words` list
            if (len(found) > 1):
                continue
            else:
                original_mnemonic_words.append(found[0])
                word = ''

        # print the `original_mnemonic_words`
        print('  ', ' '.join(original_mnemonic_words))

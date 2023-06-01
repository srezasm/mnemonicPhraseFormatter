# Mnemonic Phrase Formatter

The Mnemonic Phrase Formatter is a tool that generates a digest-unreadable phrase from the words in the bip39 words list. Each individual mnemonic word in the list has a unique starter substring, and the tool splits the unique part out of each word and sticks them after one another in order to generate the phrase.

For example:

* abandon => aba
* arrive => arriv
* cave => cav
* era => era

This tool can be used to generate a new, unreadable phrase or to remake the original mnemonic phrase later on in the same way.

## Disclaimer

Please note that the Mnemonic Phrase Formatter is an experimental-fun project and may not be recommended for serious use. Therefore, all the responsibility of using it is on the user.

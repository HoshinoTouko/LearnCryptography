import vigenereCipher
import freqAnalysis
import vigenereDictionaryHacker
import vigenereHacker

def encrypt():
    # Read data
    dataFile = open('testData.txt', encoding='utf-8')
    data = dataFile.read()
    dataFile.close()
    # Generate a key
    key = 'JKGJKAHDSKLHJ'
    print('key: %s' % key)
    # Encrypt text
    secretData = vigenereCipher.encryptMessage(key, data)
    # print(secretData)
    dataFileSecret = open('testDataSecret.txt', 'w', encoding='utf-8')
    dataFileSecret.write(secretData)
    dataFileSecret.close()
    return secretData


def getFrequencyOrder(message):
    return freqAnalysis.getFrequencyOrder(message)

def main():
    secretData = encrypt()
    print(freqAnalysis.getLetterCount(secretData))
    # print(freqAnalysis.englishFreqMatchScore(secretData))
    print(getFrequencyOrder(secretData))
    # Try hack the secret text by dict
    # vigenereDictionaryHacker.hackVigenere(secretData)
    vigenereHacker.hackVigenere(secretData)


if __name__ == '__main__':
    main()

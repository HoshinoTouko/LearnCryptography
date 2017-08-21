import affineCipher, affineHacker

def main():
    # Read data
    dataFile = open('./testData.txt', encoding='utf-8')
    data = dataFile.read()
    dataFile.close()
    # Generate a random key
    key = affineCipher.getRandomKey()
    print('key: %d' % key)
    # Encrypt text
    secretData = affineCipher.encryptMessage(key, data)
    # print(secretData)
    input()
    # BF method to hack this text
    affineHacker.hackAffine(secretData)

if __name__ == '__main__':
    main()

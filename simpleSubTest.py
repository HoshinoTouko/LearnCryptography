import simpleSubCipher
import simpleSubHacker


def main():
    # Read data
    dataFile = open('./testData.txt', encoding='utf-8')
    data = dataFile.read()
    dataFile.close()
    # Generate a key
    key = simpleSubCipher.getRandomKey()
    print('key: %s' % key)
    # Encrypt text
    secretData = simpleSubCipher.encryptMessage(key, data)
    # print(secretData)
    input()
    # BF method to hack this text
    letterMapping = simpleSubHacker.hackSimpleSub(secretData)
    print(letterMapping)


if __name__ == '__main__':
    main()

def run():

    word = input('Write someting (only one word): ')
    plus = 0
    vowels = 'a', 'e', 'i', 'o', 'u'

    for i in range(len(word)):
        if word[i] in vowels:
            plus += 1

    print('Number of vowels: ', plus)

if __name__ == '__main__':
    run()
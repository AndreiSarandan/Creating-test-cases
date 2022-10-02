def main():
    print(shorten('andrei'))


def shorten(word):
    c = ''
    for letter in word:
        if letter not in 'aeiouAEIOU':
            c += letter
    return c


if __name__ == "__main__":
    main()

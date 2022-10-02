from twttr import shorten


def main():
    test_shorten()


# assert
def test_shorten():
    assert shorten("andrei") == "ndr"
    assert shorten("Andrei") == "ndr"
    assert shorten("Andrei1,") == "ndr1,"


# test units

def test_mihaela():
    if shorten("mihaela") != "mhl":
        x = shorten("andrei")
        print("Expected 'ndr' not "+x)
        return 0
    else:
        print('Corect!')
        return 1


def test_andrei2():
    if shorten("andrei") != "ndrs":
        x = shorten("andrei")
        print("Expected 'ndr' not "+x)
        return 0
    else:
        print('Corect!')
        return 1


if __name__ == "__main__":
    main()

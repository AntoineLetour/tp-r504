def puissance(a, b):
    if not isinstance(a, int):
        raise TypeError("Erreur : 'a' doit être un entier")
    if not isinstance(b, int):
        raise TypeError("Erreur : 'b' doit être un entier")

    result = 1

    if b < 0:
        for _ in range(-b):
            result *= a
        return 1 / result
    else:
        for _ in range(b):
            result *= a
        return result

def test_exc_1():
    with pytest.raises(Exception):
        puissance(0,-1)

def test_exc_2():
    with pytest.raises(Exception):
        puissance(0,b)


def puissance(a, b):
    if not isinstance(a, int):
        raise TypeError("Erreur : 'a' doit être un entier")
    if not isinstance(b, int):
        raise TypeError("Erreur : 'b' doit être un entier")
    if a == 0 and b < 0:
    raise Exception ("pas possible si = 0 ou <0)

    result = 1

    if b < 0:
        for _ in range(-b):
            result *= a
        return 1 / result
    else:
        for _ in range(b):
            result *= a
        return result


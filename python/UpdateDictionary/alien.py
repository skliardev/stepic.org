def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]

    dictionary.get(key[, value])
    value - значение которое будет возвращено если ключа нет
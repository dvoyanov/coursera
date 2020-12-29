def calculate(data, findall):
    matches = findall(r"([abc]{1})([-+]?)=([abc]?)([[+-]?\d+]?)?")  # Если придумать хорошую регулярку, будет просто
    print(matches)
    print(data)
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if s:
            data[v1] = data[v1] + (data.get(v2, 0) + int(n or 0))*int("{}1".format(s))
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)
        print("{}{}={}{}".format(v1, s, v2, n))
        print(data[v1])
    return data

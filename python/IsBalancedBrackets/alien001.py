def is_balanced(text, brackets="<>()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = {}
    it = 0
    for character in text:
        it += 1
        if character in opening:
            stack[it] = opening.index(character)
        elif character in closing:
            if stack:
                key, value = stack.popitem()
                if value != closing.index(character):
                    print(it)
                    return
            else:
                print(it)
                return
    if not stack:
        print('Success')
    else:
        key, value = stack.popitem()
        print(key)


is_balanced(input())

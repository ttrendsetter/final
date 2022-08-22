def cnt_letters():
    word = input('word: ').lower()
    res = dict.fromkeys(word, 0)
    for letter in word:
        res[letter] += 1
    print(max(res.items(), key=lambda x: x[1]))


def sq_root():
    num = int(input('number: '))
    prv, nxt, sqr = -1, 0, 0
    while sqr < num:
        prv, nxt = nxt, nxt + 1
        sqr = sqr + prv + nxt
    print(nxt if sqr == num else None)


def brace_checker():
    data = input()
    check = 0
    for brace in data:
        check += 1 if brace == '(' else -1
        if check < 0:
            break
    print(not check)


brace_checker()
cnt_letters()
sq_root()

import collections

def septets():
    """Returns a set of sets of all groups of 7 letters with pangrams."""
    sep = set()
    with open("enable.txt") as file_handle:
        for line in file_handle:
            letters = frozenset(line[0:-1])
            if len(letters) == 7 and 's' not in letters:
                sep.add(letters)
    return sep

def word_scores():
    """Returns a dict of all legal words and its score."""
    sc = {}
    with open("enable.txt") as file_handle:
        for line in file_handle:
            score = 0
            word = line[0:-1]
            if 's' in word: continue
            if len(word) < 4: continue
            letters = frozenset(word)
            if len(letters) > 7: continue
            if (l := len(word)) == 4:
                score = 1
            else:
                score = l
            if len(letters) == 7:
                score += 7
            sc[word] = score
    return sc

def letters(words):
    """Returns a dict with word keys and set of letters values."""
    lett =  {}
    for w in words:
        lett[w] = set(w)
    return lett

def board_counter():
    """Returns a collections.Counter object for easy sorting."""
    seps = septets()
    score = word_scores()
    chars = letters(score.keys())
    totals = collections.Counter()

    print((l := len(seps)), "letter septets for", 7 * l, "possible boards.")
    checked = 0

    for s in seps: # or in seps
        for center in s:
            outer = s - {center}
            k = (center, frozenset(outer))
            for w in score.keys():
                if center in chars[w] and s >= chars[w]:
                    totals[k] += score[w]
        checked += 1
        if checked % 100 == 0:
            print(checked, "septets checked.")
    return totals

def one_board_score(center, out):
    """c = letter in center, o = string of letters on outside"""
    score = word_scores()
    chars = letters(score.keys())
    total = 0
    s = set(center + out)
    outer = set(out)
    print(center, out)
    print('-' * 8)
    for w in score.keys():
        if center in chars[w] and s >= chars[w]:
            total += score[w]
            print(w, score[w])
    print('*** Total =', total)

# Execute the code.

print()

s = board_counter()
for i in s.most_common(20):
    b = i[0][0].upper()
    for j in i[0][1]:
        b += j
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c.upper() in b: print(c.upper(), end='')
        elif c in b: print(c, end='')
        else: print(end=' ')
    print(":", i[1])

print()

one_board_score((mc := s.most_common(1)[0][0])[0], "".join(mc[1]))

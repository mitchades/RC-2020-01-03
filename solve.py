# Requires Python 3.8 because I wanted to play around with the := operator.
import collections # for Counter

def septets():
    """Returns a set of sets of all groups of 7 letters with pangrams."""
    sep = set()
    with open("enable.txt") as file_handle:
        for line in file_handle:
            letters = frozenset(line[0:-1]) # strip the '\n' from the line
            if len(letters) == 7 and 's' not in letters:
                sep.add(letters)
    return sep

# If I had been raised as an OO programmer, there would be a GoodWord class.
# Methods would include letters and score.
# But I wasn't.

def word_scores():
    """Returns a dict of all legal words and its score."""
    sc = {}
    with open("enable.txt") as file_handle:
        for line in file_handle:
            # In this loop, we'll continue when we reach a word that can't
            # be an answer to a Spelling Bee board.
            score = 0
            word = line[0:-1]
            if 's' in word: continue # S is bad by our rules.
            if len(word) < 4: continue # 3-letter words don't count.
            letters = frozenset(word)
            if len(letters) > 7: continue # 8 different letters? Can't do.
            if (l := len(word)) == 4:
                score = 1
            else:
                score = l
            if len(letters) == 7:
                score += 7
            sc[word] = score
    return sc

# This will have the keys of word_scores() as input, so we know all the words are good.
def letters(words):
    """Returns a dict with word keys and set of letters values."""
    lett =  {}
    for w in words:
        lett[w] = set(w)
    return lett

# This is where most of the work gets done.

def board_counter():
    """Returns a collections.Counter object for easy sorting."""
    seps = septets()
    score = word_scores()
    chars = letters(score.keys())
    totals = collections.Counter()
    
    # Isn't the walrus operator cool? I don't have to call len twice or use 2 lines!
    print((l := len(seps)), "letter septets for", 7 * l, "possible boards.")
    
    checked = 0 # Since this takes a while to run, we'll print updates every 100 septets.

    for s in seps: # For each letter combo that makes a pangram:
        for center in s: # Taking each letter as the center hex:
            outer = s - {center}
            # This will be the key for our counter.
            # It has to be hashable, so it's a tuple of a char and a frozenset.
            k = (center, frozenset(outer))
            for w in score.keys(): # For every legal word:
                # If it has the center letter and all its letters are on the board:
                if center in chars[w] and s >= chars[w]:
                    totals[k] += score[w] # Add the word score to the running total.
        checked += 1
        if checked % 100 == 0:
            print(checked, "septets checked.") # This prints every 7-8 seconds for me.
    return totals

# This prints out every word and its score for a board.
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
    # This is a somewhat silly way to print this out, but I thought it was neat.
    b = i[0][0].upper()
    for j in i[0][1]:
        b += j
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c.upper() in b: print(c.upper(), end='')
        elif c in b: print(c, end='')
        else: print(end=' ')
    print(":", i[1])

print()

# One more use of := before we go. 
one_board_score((mc := s.most_common(1)[0][0])[0], "".join(mc[1]))

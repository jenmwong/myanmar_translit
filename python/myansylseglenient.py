# Clases:
#   0: consonnant only
#   1: vowel that can be independent when at the beginning
#   2: consonnant or medial depending on the position
#   3: consonnant or final (m, h)
#   4: dependant vowel only
#   5: independent sign
#   6: space
#   7: other
#   8: a
#   9: cut before
#  10: dependent sign
#  11: cut after

# Systems:
#   0: standard
#   1: simplified
#   2: lenient (no diacritics)
def createTokens(system):
    res = {"maxlen": 0}
    addOneToken(["k"], ["k"], [0], res, system)
    addOneToken(["kh"], ["kh"], [0], res, system)
    addOneToken(["g"], ["g"], [0], res, system)
    addOneToken(["gh"], ["gh"], [0], res, system)
    addOneToken(["c"], ["c"], [0], res, system)
    addOneToken(["ch"], ["ch"], [0], res, system)
    addOneToken(["j"], ["j"], [0], res, system)
    addOneToken(["jh"], ["jh"], [0], res, system)
    addOneToken(["nn"], ["nn"], [0], res, system)
    addOneToken(["ss"], ["ss"], [0], res, system)
    addOneToken(["t"], ["t"], [0], res, system)
    addOneToken(["th"], ["th"], [0], res, system)
    addOneToken(["d"], ["d"], [0], res, system)
    addOneToken(["dh"], ["dh"], [0], res, system)
    addOneToken(["n"], ["n"], [0], res, system)
    addOneToken(["p"], ["p"], [0], res, system)
    addOneToken(["ph"], ["ph"], [0], res, system)
    addOneToken(["b"], ["b"], [0], res, system)
    addOneToken(["bh"], ["bh"], [0], res, system)
    addOneToken(["m"], ["m"], [3], res, system)
    addOneToken(["y"], ["y"], [2], res, system)
    addOneToken(["r"], ["r"], [2], res, system)
    addOneToken(["l"], ["l"], [0], res, system)
    addOneToken(["v"], ["v"], [2], res, system)
    addOneToken(["s"], ["s"], [0], res, system)
    addOneToken(["h"], ["h"], [3], res, system)
    addOneToken(["a"], ["a"], [8], res, system)
    addOneToken(["i"], ["i"], [1], res, system)
    addOneToken(["u"], ["u"], [1], res, system)
    addOneToken(["e"], ["e"], [1], res, system)
    addOneToken(["o"], ["o"], [1], res, system)
    addOneToken(["au"], ["au"], [1], res, system)
    addOneToken(["ai"], ["au"], [4], res, system)
    addOneToken(["ui"], ["ui"], [4], res, system)
    addOneToken(["0"], ["0"], [5], res, system)
    addOneToken(["1"], ["1"], [5], res, system)
    addOneToken(["2"], ["2"], [5], res, system)
    addOneToken(["3"], ["3"], [5], res, system)
    addOneToken(["4"], ["4"], [5], res, system)
    addOneToken(["5"], ["5"], [5], res, system)
    addOneToken(["6"], ["6"], [5], res, system)
    addOneToken(["7"], ["7"], [5], res, system)
    addOneToken(["8"], ["8"], [5], res, system)
    addOneToken(["9"], ["9"], [5], res, system)
    addOneToken(["*n"], ["*n"], [5], res, system)
    addOneToken(["*r"], ["*r"], [5], res, system)
    addOneToken(["*l"], ["*l"], [5], res, system)
    addOneToken(["*e"], ["*e"], [5], res, system)
    addOneToken([" "], [""], [13], res, system)
    addOneToken(["ḥ", "ḥ"], ["ḥ", "h"], [10, 0], res, system)
    addOneToken(["ṁ", "ṁ", "ṃ", "ṃ"], ["ṁ", "m"], [10, 0], res, system)
    addOneToken(["·"], [""], [11], res, system)
    addOneToken(["."], [".", ""], [11], res, system)
    addOneToken(["·."], [".", ""], [11], res, system)
    # I'm not sure sh could work as it could be s + h
    addOneToken(["ñ", "ñ"], ["ñ", "n"], [0], res, system)
    addOneToken(["ññ", "ññ"], ["ññ", "nn"], [0], res, system)
    addOneToken(["ṭ", "ṭ"], ["ṭ", "t"], [0], res, system)
    addOneToken(["ṭh", "ṭh"], ["ṭh", "th"], [0], res, system)
    addOneToken(["ḍ", "ḍ"], ["ḍ", "d"], [0], res, system)
    addOneToken(["ḍh", "ḍh"], ["ḍh", "dh"], [0], res, system)
    addOneToken(["ṇ", "ṇ"], ["ṇ", "n"], [0], res, system)
    addOneToken(["ṅ", "ṅ"], ["ṅ", "n"], [0], res, system)
    addOneToken(["ḷ", "ḷ"], ["ḷ", "l"], [0], res, system)
    addOneToken(["'", "’", "ʼ", "ʹ", "‘", "ʾ", "°"], ["a", "a"], [8], res, system)
    addOneToken(["°"], ["", ""], [9], res, system)
    addOneToken(["ā", "ā"], ["ā", "a"], [1, 8], res, system)
    addOneToken(["ī", "ī"], ["ī", "i"], [1], res, system)
    addOneToken(["ū", "ū"], ["ū", "u"], [1], res, system)
    addOneToken(["ś", "ś"], ["ś", "s"], [0], res, system)
    addOneToken(["ṣ", "ṣ"], ["ṣ", "s"], [0], res, system)
    addOneToken(["r̥", "r̥"], ["r̥", "r"], [1, 2], res, system)
    addOneToken(["r̥̄", "r̥̄", "r̥̄"], ["r̥̄", "r"], [1, 2], res, system)
    addOneToken(["l̥", "l̥"], ["l̥", "l"], [1, 0], res, system)
    addOneToken(["l̥̄", "l̥̄", "l̥̄"], ["l̥̄", "l"], [1, 0], res, system)
    return res

def addOneToken(variants, tokenlist, cllist, tokens, system):
    # variants are all the possible forms of the token, lower case
    # tokenlist is a list of resulting tokens in the different systems:
    #  - 0 is simplified
    #  - 1 is lenient (no diacritics)
    #  - when there is just one element in the list, it is both lenient and simplified
    # cllist is the list of resulting class, with the same convention as res
    # tokens is the resulting result
    cl = cllist[0]
    if system == 2 and len(cllist) > 1:
        cl = cllist[1]
    token = tokenlist[0]
    if system == 2 and len(tokenlist) > 1:
        token = tokenlist[1]
    for v in variants:
        l = len(v)
        if l > tokens["maxlen"]:
            tokens["maxlen"] = l
        if l not in tokens:
            tokens[l] = {}
        tokens[l][v] = [cl, token]
        tc = v.title() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [cl, token]
        tc = v.upper() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [cl, token]

def getNextToken(s, idx, slen, tokens):
    if slen < idx+1:
        return None
    maxlen = tokens["maxlen"]
    for i in range(0, maxlen):
        nbchars = maxlen - i
        if slen < idx+nbchars:
            continue
        if nbchars not in tokens:
            continue
        possibletokens = tokens[nbchars]
        potentialtoken = s[idx:idx+nbchars]
        if potentialtoken in possibletokens:
            return [nbchars, possibletokens[potentialtoken]]
    # no match at all
    return [1, [11, s[idx:idx+nbchars]]]


# States:
# -1: initial state
# 0: after a first consonnant:
#    - consonnants/medials are appended
#    - if vowel, go to 1
#    - if non-consonnant, non-medial, non-subscriptable, go to 0
# 1: right after the vowel:
#    - if consonnant, add potential tokens, go to 2
#    - if ending (non-vowel, non-consonnant, non-sign): cut
#    - if vowel: stay in 1
# 2: after the vowel + something else:
#    - if consonnant, add potential tokens
#    - if ending (non-vowel, non-consonnant, non-sign): cut
#    - if vowel: break after the first vowel
# 3: non-Burmese / invalid
def getNextTransBreak(s, idx, slen, tokens):
    state = -1
    res = ""
    aftervowelidx = -1
    aftervowel = ""
    curidx = idx
    while curidx < slen:
        cinfo = getNextToken(s, curidx, slen, tokens)
        if not cinfo:
            #print("exiting bizarrely")
            state = -1
            break
        nbchars = cinfo[0]
        cl = cinfo[1][0]
        token = cinfo[1][1]
        #print("iteration: cl=%d, token=%s, state=%d" % (cl, token, state))
        cutbeforethis = curidx != idx and (cl in [5, 9] or (cl in [5, 7] and state in [0, 1, 2]) or (cl in [0, 1, 2, 3, 8] and state == 3))
        if cutbeforethis:
            return [res+aftervowel, curidx]
        cutaftervowel = aftervowelidx != -1 and (cl in [8, 4, 1])
        if cutaftervowel:
            return [res, aftervowelidx]
        # cut after this:
        if cl == 11:
            return [res+aftervowel+token, curidx+nbchars]
        if state == 0:
            res += token
            curidx += nbchars
            if cl in [1, 6, 8]:
                state = 1
        elif state == 1:
            # if we're after a vowel and we encounter another vowel, we cut after the first one
            if cl in [1, 6]:
                res += token
                curidx += nbchars
            elif cl == 8:
                # if there's an a, we cut before as it's an independent vowel
                return [res, curidx]
            else:
                aftervowelidx = curidx
                curidx += nbchars
                aftervowel += token
                state = 2
        elif state == 2:
            if cl in [1, 6, 8]:
                # if there's another vowel, we cut after the first one
                return [res, curidx]
            else:
                aftervowelidx = curidx
                curidx += nbchars
                aftervowelidx += nbchars
                aftervowel += token
        else:
            res += token
            curidx += nbchars
        if state == -1:
            if cl in [0, 2, 3]:
                state = 0
            elif cl in [1, 4, 8]:
                state = 1
            else:
                state = 3
    return [res+aftervowel, curidx]

TOKENS = {}

def getTrans(s, system):
    if system not in TOKENS:
        TOKENS[system] = createTokens(system)
    tokens = TOKENS[system]
    res = ""
    idx = 0
    lasttrans = ""
    slen = len(s)
    while idx < slen:
        nextinfo = getNextTransBreak(s, idx, slen, tokens)
        nextidx = nextinfo[1]
        nexttrans = nextinfo[0]
        #print("got nexttrans=%s, nextidx=%d" % (nexttrans, nextidx))
        res += nexttrans+'|'
        lasttrans = nexttrans
        if nextidx == -1:
            break
        idx = nextidx
    return res
# Implementation of the algorithm described in
# Zin Maung Maung and Yoshiki Makami,"A rule-based syllable segmentation of Myanmar Text", in Proceeding of the IJCNLP-08 workshop of NLP for Less Privileged Language, January, 2008, Hyderabad, India, pp. 51-58

# 0: consonnant only
# 1: vowel that can be independent when at the beginning
# 2: consonnant or medial depending on the position
# 3: consonnant or final (m, h)
# 4: dependant vowel only
# 5: sign
# 6: space
# 7: other
# 8: a
def createTokens():
    res = {"maxlen": 0}
    addOneToken(["k"], ["k"],0, res)
    addOneToken(["kh"], ["kh"], 0, res)
    addOneToken(["g"], "g", 0, res)
    addOneToken(["gh"], "gh", 0, res)
    addOneToken(["c"], "c", 0, res)
    addOneToken(["ch"], "ch", 0, res)
    addOneToken(["j"], "j", 0, res)
    addOneToken(["jh"], "jh", 0, res)
    addOneToken(["nn"], "nn", 0, res)
    addOneToken(["ss"], 0, res)
    addOneToken(["t"], "t", 0, res)
    addOneToken(["th"], "th", 0, res)
    addOneToken(["d"], "d", 0, res)
    addOneToken(["dh"], "dh" , 0, res)
    addOneToken(["n"], "n", 0, res)
    addOneToken(["p"], "p", 0, res)
    addOneToken(["ph"], "ph", 0, res)
    addOneToken(["b"], "b", 0, res)
    addOneToken(["bh"], "bh", 0, res)
    addOneToken(["m"], "m", 3, res)
    addOneToken(["y"], "y", 2, res)
    addOneToken(["r"], "r", 2, res)
    addOneToken(["l"], "l", 0, res)
    addOneToken(["v"], "v", 2, res)
    addOneToken(["s"], "s", 0, res)
    addOneToken(["h"], "h", 3, res)
    addOneToken(["a"], "a", 1, res)
    addOneToken(["i"], "i", 1, res)
    addOneToken(["u"], "u", 1, res)
    addOneToken(["e"], "u", 1, res)
    addOneToken(["o"], "u", 1, res)
    addOneToken(["au"], "u", 1, res)
    addOneToken(["ai"], "u", 4, res)
    addOneToken(["ui"], "ui", 4, res)
    addOneToken(["0"], "0", 5, res)
    addOneToken(["1"], "1", 5, res)
    addOneToken(["2"], "2", 5, res)
    addOneToken(["3"], "3", 5, res)
    addOneToken(["4"], "4", 5, res)
    addOneToken(["5"], "5", 5, res)
    addOneToken(["6"], "6", 5, res)
    addOneToken(["7", "7", 5, res)
    addOneToken("8", "8", 5, res)
    addOneToken("9", "9", 5, res)
    addOneToken("*n", "*n", 5, res)
    addOneToken("*r", "*r", 5, res)
    addOneToken("*l", "*l", 5, res)
    addOneToken("*e", "*e", 5, res)
    addOneToken(" ", "", 13, res)
    # I'm not sure sh could work as it's 
    addOneToken(["ñ", "ñ"], "ဉ", 0, res)
    addOneToken(["ññ", "ññ"], "ည", 0, res)
    addOneToken(["ṭ", "ṭ"], "ဋ", 0, res)
    addOneToken(["ṭh", "ṭh"], "ဌ", 0, res)
    addOneToken(["ḍ", "ḍ"], "ဍ", 0, res)
    addOneToken(["ḍh", "ḍh"], "ဎ", 0, res)
    addOneToken(["ṇ", "ṇ"], "ဏ", 0, res)
    addOneToken(["ṅ", "ṅ"], "င", 0, res)
    addOneToken(["ḷ", "ḷ"], "ဠ", 0, res)
    addOneToken(["'", "’", "ʼ", "ʹ", "‘", "ʾ", "°"], "အ", 10, res)
    addOneToken(["°"], "", ??, res)
    addOneToken(["ā", "ā"], "ာ", 1, res)
    addOneToken(["i"], "ိ", 1, res)
    addOneToken(["ī", "ī"], "ီ", 1, res)
    addOneToken(["u"], "ု", 1, res)
    addOneToken(["ū", "ū"], "ူ", 1, res)
    return res

def addOneToken(variants, cl, tokens):
    for v in variants:
        l = len(v)
        if l > tokens["maxlen"]:
            tokens["maxlen"] = l
        if l not in tokens:
            tokens[l] = {}
        tokens[l][v] = [cl]
        tc = v.title() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [cl]
        tc = v.upper() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [cl]

def getNextToken(s, idx, slen):
    global TOKENS
    if TOKENS is None:
        TOKENS = createTokens()
    if slen < idx+1:
        return None
    maxlen = TOKENS["maxlen"]
    for i in range(0, maxlen):
        nbchars = maxlen - i
        if slen < idx+nbchars:
            continue
        if nbchars not in TOKENS:
            continue
        possibletokens = TOKENS[nbchars]
        potentialtoken = s[idx:idx+nbchars]
        if potentialtoken in possibletokens:
            return [nbchars, possibletokens[potentialtoken]]
    # no match at all
    return [1, [s[idx:idx+nbchars], 11]]

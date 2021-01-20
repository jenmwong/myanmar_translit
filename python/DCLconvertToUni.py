
TOKENS = None

# classes:
# 0: consonnants (can have or be subscript)
# 1: vowels and other diacritics
# 2: amvat
# 3: independent signs (cannot have have or be subscript)
# 10: အ
# 11: other (non-Burmese, space, etc.)
# 12: medial or consonnant according to the context
# 13: space in the translitteration

def createTokens():
    res = {"maxlen": 0}
    addOneToken(["k"], "က", 0, res)
    addOneToken(["kh"], "ခ", 0, res)
    addOneToken(["g"], "ဂ", 0, res)
    addOneToken(["gh"], "ဃ", 0, res)
    addOneToken(["ṅ", "ṅ"], "င", 0, res)
    addOneToken(["c"], "စ", 0, res)
    addOneToken(["ch"], "ဆ", 0, res)
    addOneToken(["j"], "ဇ", 0, res)
    addOneToken(["jh"], "ဈ", 0, res)
    addOneToken(["ñ", "ñ"], "ဉ", 0, res)
    addOneToken(["ññ", "ññ"], "ည", 0, res)
    addOneToken(["ṭ", "ṭ"], "ဋ", 0, res)
    addOneToken(["ṭh", "ṭh"], "ဌ", 0, res)
    addOneToken(["ḍ", "ḍ"], "ဍ", 0, res)
    addOneToken(["ḍh", "ḍh"], "ဎ", 0, res)
    addOneToken(["ṇ", "ṇ"], "ဏ", 0, res)
    addOneToken(["t"], "တ", 0, res)
    addOneToken(["th"], "ထ", 0, res)
    addOneToken(["d"], "ဒ", 0, res)
    addOneToken(["dh"], "ဓ", 0, res)
    addOneToken(["n"], "န", 0, res)
    addOneToken(["p"], "ပ", 0, res)
    addOneToken(["ph"], "ဖ", 0, res)
    addOneToken(["b"], "ဗ", 0, res)
    addOneToken(["bh"], "ဘ", 0, res)
    addOneToken(["m"], "မ", 0, res)
    addOneToken(["y"], ["ယ", "ျ"], 12, res)
    addOneToken(["r"], ["ရ", "ြ"], 12, res)
    addOneToken(["l"], "လ", 0, res)
    addOneToken(["v"], ["ဝ", "ွ"], 12, res)
    addOneToken(["s"], "သ", 0, res)
    addOneToken(["h"], ["ဟ", "ှ"], 12, res)
    addOneToken(["a"], "", 13, res)
    addOneToken(["ḷ", "ḷ"], "ဠ", 0, res)
    addOneToken(["'", "’", "ʼ", "ʹ", "‘", "ʾ", "°"], "အ", 10, res)
    addOneToken(["'·", "’·", "ʼ·", "ʹ·", "‘·", "ʾ·" ], "္အ်", 1, res)
    # ဢ ? ဨ ?  "ါ ဳ  ဴ  ဵ
    addOneToken(["°i"], "ဣ", 3, res)
    addOneToken(["°ī", "°ī"], "ဤ", 3, res)
    addOneToken(["°u"], "ဥ", 3, res)
    addOneToken(["°ū", "°ū"], "ဦ", 3, res)
    addOneToken(["°e"], "ဧ", 3, res)
    addOneToken(["°o"], "ဩ", 3, res)
    addOneToken(["°au"], "ဪ", 3, res)
    addOneToken(["ā", "ā"], "ာ", 1, res)
    addOneToken(["i"], "ိ", 1, res)
    addOneToken(["ī", "ī"], "ီ", 1, res)
    addOneToken(["u"], "ု", 1, res)
    addOneToken(["ū", "ū"], "ူ", 1, res)
    addOneToken(["e"], "ေ", 1, res)
    addOneToken(["ai"], "ဲ", 1, res)
    addOneToken(["au"], "ော်", 1, res)
    addOneToken(["o"], "ော", 1, res)
    addOneToken(["ui"], "ို", 1, res)
    addOneToken(["ṁ", "ṁ", "ṃ", "ṃ", ""], "ံ", 1, res)
    addOneToken(["·"], "်", 2, res)
    addOneToken(["."], "့", 1, res)
    addOneToken(["·."], "့်", 2, res)
    addOneToken(["ḥ", "ḥ"], "း", 1, res)
    addOneToken(["ss"], "ဿ", 0, res)
    addOneToken(["0"], "၀", 3, res)
    addOneToken(["1"], "၁", 3, res)
    addOneToken(["2"], "၂", 3, res)
    addOneToken(["3"], "၃", 3, res)
    addOneToken(["4"], "၄", 3, res)
    addOneToken(["5"], "၅", 3, res)
    addOneToken(["6"], "၆", 3, res)
    addOneToken(["7"], "၇", 3, res)
    addOneToken(["8"], "၈", 3, res)
    addOneToken(["9"], "၉", 3, res)
    addOneToken(["*n"], "၌", 3, res)
    addOneToken(["*r"], "၍", 3, res)
    addOneToken(["*l"], "၎", 3, res)
    addOneToken(["*e"], "၏", 3, res)
    addOneToken(["ś", "ś"], "ၐ", 0, res)
    addOneToken(["ṣ", "ṣ"], "ၑ", 0, res)
    addOneToken(["°r̥", "°r̥"], "ၒ", 0, res)
    addOneToken(["°r̥̄", "°r̥̄", "°r̥̄"], "ၓ", 0, res)
    addOneToken(["°l̥", "°l̥"], "ၔ", 0, res)
    addOneToken(["°l̥̄", "°l̥̄", "°l̥̄"], "ၕ", 0, res)
    addOneToken(["r̥", "r̥"], "ၖ", 1, res)
    addOneToken(["r̥̄", "r̥̄", "r̥̄"], "ၗ", 1, res)
    addOneToken(["l̥", "l̥"], "ၘ", 1, res)
    addOneToken(["l̥̄", "l̥̄", "l̥̄"], "ၙ", 1, res)
    addOneToken(["_"], " ", 11, res)
    addOneToken([" "], "", 13, res)
    return res

def addOneToken(variants, trans, cl, tokens):
    for v in variants:
        l = len(v)
        if l > tokens["maxlen"]:
            tokens["maxlen"] = l
        if l not in tokens:
            tokens[l] = {}
        tokens[l][v] = [trans, cl]
        tc = v.title() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [trans, cl]
        tc = v.upper() # title case
        l = len(tc)
        if l not in tokens:
            tokens[l] = {}
        tokens[l][tc] = [trans, cl]

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

# mam'
# mama

# States:
# -1: initial state
# 0: after a first consonnant:
#    - consonnants are stacked
#    - medial/consonnant become medial
#    - if non-consonnant, non-medial, non-subscriptable, go to 0
# 1: after the vowel:
#    - if consonnant, go to 1
#    - medial/consonnant become consonnant
# 2: non-Burmese / invalid

def getNextTransBreak(s, idx, slen):
    state = -1
    res = ""
    curidx = idx
    prevrepl = None
    while curidx < slen:
        cinfo = getNextToken(s, curidx, slen)
        if not cinfo:
            #print("exiting bizarrely")
            state = -1
            break
        nbchars = cinfo[0]
        cl = cinfo[1][1]
        repl = cinfo[1][0]
        #print("iteration: cl=%d, repl=%s, state=%d" % (cl, repl, state))
        # cut before if:
        # - not the first char
        # - state == 2 && cl != 11
        # - state == (0 or 1) && cl == 11
        # - cl == 3
        cutbefore = curidx != idx and (cl == 3 or (cl == 11 and state in [0, 1]) or (cl != 11 and state == 2))
        if cutbefore:
            return [res, curidx]
        if state == 0:
            if cl == 0:
                if prevrepl == "င":
                    res += "်္"+repl    
                else:
                    res += "္"+repl
            elif cl == 12:
                res += repl[1]
            else:
                res += repl
                state = 1
        elif state == 1:
            if cl == 0:
                state = 0
            if cl == 12:
                res += repl[0]
                state = 0
            else:
                res += repl
        else:
            if cl == 12:
                res += repl[0]
            else:
                res += repl
        curidx += nbchars
        if state == -1:
            if cl in [0, 10, 12]:
                state = 0
            elif cl == 11:
                state = 2
            else:
                # this indicates some problem in the Unicode
                state = 1
        # cut after if:
        # - cl == 13
        # - cl == 11 && state != 2
        # - cl == 2
        if cl in [2, 13] or (cl == 11 and state != 2):
            return [res, curidx]
        prevrepl = repl
    return [res, curidx]

def getTrans(s):
    res = ""
    idx = 0
    lasttrans = ""
    slen = len(s)
    while idx < slen:
        nextinfo = getNextTransBreak(s, idx, slen)
        nextidx = nextinfo[1]
        nexttrans = nextinfo[0]
        #print("got nexttrans=%s, nextidx=%d" % (nexttrans, nextidx))
        res += nexttrans
        lasttrans = nexttrans
        if nextidx == -1:
            break
        idx = nextidx
    return res
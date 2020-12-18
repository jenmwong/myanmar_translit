# Implementation of the algorithm described in
# Zin Maung Maung and Yoshiki Makami,"A rule-based syllable segmentation of Myanmar Text", in Proceeding of the IJCNLP-08 workshop of NLP for Less Privileged Language, January, 2008, Hyderabad, India, pp. 51-58

# A = 0 = Asat
# C = 1
# D = 2
# E = 3
# F = 4
# G = 5
# I = 6
# M = 7
# P = 8
# S = 9 = Virama
# V = 10
# W = 11

CLASSES = {
    "က": 1, "ခ": 1, "ဂ": 1, "ဃ": 1, "င": 1, "စ": 1, "ဆ": 1, "ဇ": 1, "ဈ": 1, "ဉ": 1, "ည": 1,
    "ဋ": 1, "ဌ": 1, "ဍ": 1, "ဎ": 1, "ဏ": 1, "တ": 1, "ထ": 1, "ဒ": 1, "ဓ": 1, "န": 1, "ပ": 1,
    "ဖ": 1, "ဗ": 1, "ဘ": 1, "မ": 1, "ယ": 1, "ရ": 1, "လ": 1, "ဝ": 1, "သ": 1, "ဟ": 1, "ဠ": 1,
    "အ": 1, "ဢ": 1, 
    "ဣ": 3, 
    "ဤ": 6,
    "ဥ": 3, "ဦ": 3,
    "ဧ": 6,
    "ဨ": 3, "ဩ": 3,
    "ဪ": 6,
    "ါ": 10, "ာ": 10, "ိ": 10, "ီ": 10, "ု": 10, "ူ": 10, "ေ": 10, "ဲ": 10,
    "ဳ": 10, # not indicated in the article
    "ဴ": 10, # not indicated
    "ဵ": 10, # not indicated
    "ံ": 4, "့": 4, "း": 4, 
    "္": 9,
    "်": 0,
    "ျ": 7, "ြ": 7, "ွ": 7, "ှ": 7,
    "ဿ": 5,
    "၀": 2, "၁": 2, "၂": 2, "၃": 2, "၄": 2, "၅": 2, "၆": 2, "၇": 2, "၈": 2, "၉": 2,
    "၊": 8, "။": 8,
    "၌": 6, "၍": 6,
    "၎": 3,
    "၏": 6,
    "ၐ": 1, "ၑ": 1, "ၒ": 1, "ၓ": 1, "ၔ": 1, "ၕ": 1, "ၖ": 1, "ၗ": 1, "ၘ": 1, "ၙ": 1,
}

AUTO = [
# A = 0
[ -1, 12, 1, 1, 0, -1, 1, 0, 1, 0, 0, 1],
# C = 1
[ 0, 13, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
# D = 2
[ -1, 1, 0, 1, -1, -1, 1, -1, 1, -1, -1, 1],
# E = 3
[ -1, 13, 1, 1, 2, 0, 1, -1, 1, -1, 0, 1],
# F = 4
[ -1, 12, 1, 1, 2, -1, 1, -1, 1, -1, -1, 1],
# G = 5
[ -1, 1, 1, 1, 0, -1, 1, -1, 1, -1, 0, 1],
# I = 6
# Note that this won't work for Old Burmese (for instance ဧည့်)
[ -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1],
# M = 7
[ 2, 13, 1, 1, 0, 0, 1, 0, 1, -1, 0, 1],
# P = 8
[ -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1],
# S = 9
[ -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# V = 10
[ 2, 14, 1, 1, 0, 0, 1, -1, 1, -1, 0, 1],
# W = 11
[ -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 0],
# AC = FC = 12
[ 3, 1, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1],
# CC = EC = MC = 13
[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
# VC = 14
[ 0, 1, 1, 1, 1, 1, 1, 15, 1, 0, 1, 1],
# ACM = FCM = VCM = 15
[ 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def getNextTokenInfo(s, idx, slen):
    if slen < idx+1:
        return None
    if slen >= idx+2:
        nexttwo = s[idx:idx+2]
        # hack: āu = āe = o
        if nexttwo == "ော" or nexttwo == "ာေ":
            return [2, 10]
        # hack: Unicode specifies 102D (i) 102F (u) but translitteration says ui
        if nexttwo == "ို":
            return [2, 10]
        # hack: tone markers
        if nexttwo == "အ်":
            return [2, 4]
        if nexttwo == "ဝ်":
            return [2, 4]
        if nexttwo == "ဟ်":
            return [2, 4]
        if nexttwo == "့်" or nexttwo == "့်":
            return [2, 0]
    if slen >= idx+3:
        nextthree = s[idx:idx+3]
        if nextthree == "ော်":
            # assigning it 4 allows no further consonnant afterwards 
            return [3, 4]
        if nextthree == "္အ်":
            # assigning it 0 is a bit hacky but I don't think it will have damaging consequences
            return [3, 0]
    nextone = s[idx:idx+1]
    if nextone in CLASSES:
        return [1, CLASSES[nextone]]
    return [1, 11]

# -1: illegal character sequence
#  0: no break after first character
#  1: break after first character
#  2: break after second character
#  3: break after 3rd character
#  4: break after 4th character

def getNextBreak(s, idx, slen):
    state = None
    curidx = idx
    nbadditionalchars = 0
    while curidx < len(s):
        tinfo = getNextTokenInfo(s, curidx, slen)
        cl = tinfo[1]
        nbchars = tinfo[0]
        print("get token %s cl=%d, nbchars=%d, idx=%d" % (s[curidx:curidx+nbchars], cl, nbchars, idx))
        if state is None:
            state = cl
            curidx += nbchars
            idx = curidx
            nbadditionalchars = 0
            continue
        res = AUTO[state][cl]
        print("%d + %d = %d (additionalchars=%d) " % (state, cl, res, nbadditionalchars))
        if res > 5:
            state = res
            curidx += nbchars
            nbadditionalchars += nbchars-1
            # 12, 13 and 14 are 2 characters, 
            continue
        if res == -1:
            print("warning: illegal sequence")
            state = cl
            curidx += nbchars
            idx = curidx
            nbadditionalchars = 0
            continue
        if res == 0:
            state = cl
            curidx += nbchars
            idx = curidx
            nbadditionalchars = 0
            continue
        if res > 1:
            nbadditionalchars += nbchars-1
        finalidx = idx+res-1+nbadditionalchars
        print("return with res=%d, idx=%d, finalidx=%d" % (res, idx, finalidx))
        return finalidx
    # no further break, but we go out of intermediate states
    # by simulating a blank space afterwards
    if state > 5:
        res = AUTO[state][11]
        print("%d + 11 = %d (additionalchars=%d) " % (state, res, nbadditionalchars))
        if res > 0:
            finalidx = idx+res-1+nbadditionalchars
            print("return2 with res=%d, idx=%d, finalidx=%d" % (res, idx, finalidx))
            return finalidx
    print("return -1")
    return -1

def getTokens(s):
    res = []
    idx = 0
    slen = len(s)
    print("slen = %d" % slen)
    while idx < slen:
        nextidx = getNextBreak(s, idx, slen)
        if nextidx == -1:
            res.append(s[idx:])
            break
        print("nextidx=%d" %nextidx)
        res.append(s[idx:nextidx])
        idx = nextidx
    return res

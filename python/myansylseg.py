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
# There is a difference here with the article:
# In the article 6 + 1 = 1
# But we have 6 + 1 = 14
# This allows ဧအ် to be one syllable
[ -1, 14, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1],
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

def getTokenClass(c):
    if c in CLASSES:
        return CLASSES[c]
    return 11

# -1: illegal character sequence
#  0: no break after first character
#  1: break after first character
#  2: break after second character
#  3: break after 4th character

def getNextBreak(s, idx):
    state = None
    curidx = idx
    while curidx < len(s):
        cl = getTokenClass(s[curidx:curidx+1])
        if state is None:
            state = cl
            curidx += 1
            idx = curidx
            continue
        res = AUTO[state][cl]
        #print("%d + %d = %d " % (state, cl, res))
        if res > 5:
            state = res
            curidx += 1
            continue
        if res == -1:
            print("warning: illegal sequence")
            state = cl
            curidx += 1
            idx = curidx
            continue
        if res == 0:
            state = cl
            curidx += 1
            idx = curidx
            continue
        #print("return with res=%d, idx=%d" % (res, idx+res-1))
        return idx+res-1
    # no further break, but we go out of intermediate states
    # by simulating a blank space afterwards
    if state > 5:
        res = AUTO[state][11]
        if res > 0:
            return idx+res-1
    return -1

def getTokens(s):
    res = []
    idx = 0
    while idx < len(s):
        nextidx = getNextBreak(s, idx)
        if nextidx == -1:
            res.append(s[idx:])
            break
        res.append(s[idx:nextidx])
        idx = nextidx
    return res

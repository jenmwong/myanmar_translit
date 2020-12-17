import re

# Implementation of the algorithm described in
# Zin Maung Maung and Yoshiki Makami,"A rule-based syllable segmentation of Myanmar Text", in Proceeding of the IJCNLP-08 workshop of NLP for Less Privileged Language, January, 2008, Hyderabad, India, pp. 51-58

# A = 0 = Asat
# C = 1 = Consonnant
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
    "က": [ 1, "k"],
    "ခ": [ 1, "kh"],
    "ဂ": [ 1, "g"],
    "ဃ": [ 1, "gh"],
    "င": [ 1, "ṅ"],
    "စ": [ 1, "c"],
    "ဆ": [ 1, "ch"],
    "ဇ": [ 1, "j"],
    "ဈ": [ 1, "jh"],
    "ဉ": [ 1, "ñ"],
    "ည": [ 1, "ññ"],
    "ဋ": [ 1, "ṭ"],
    "ဌ": [ 1, "ṭh"],
    "ဍ": [ 1, "ḍ"],
    "ဎ": [ 1, "ḍh"],
    "ဏ": [ 1, "ṇ"],
    "တ": [ 1, "t"],
    "ထ": [ 1, "th"],
    "ဒ": [ 1, "d"],
    "ဓ": [ 1, "dh"],
    "န": [ 1, "n"],
    "ပ": [ 1, "p"],
    "ဖ": [ 1, "ph"],
    "ဗ": [ 1, "b"],
    "ဘ": [ 1, "bh"],
    "မ": [ 1, "m"],
    "ယ": [ 1, "y"],
    "ရ": [ 1, "r"],
    "လ": [ 1, "l"],
    "ဝ": [ 1, "v"],
    "သ": [ 1, "s"],
    "ဟ": [ 1, "h"],
    "ဠ": [ 1, "ḷ"],
    "အ": [ 1, "'"],
    "ဢ": [ 1, ""], 
    "ဣ": [ 3, "°i"], 
    "ဤ": [ 6, "°ī"],
    "ဥ": [ 3, "°u"],
    "ဦ": [ 3, "°ū"],
    "ဧ": [ 6, "°e"],
    "ဨ": [ 3, ""],
    "ဩ": [ 3, "°o"],
    "ဪ": [ 6, "°au"],
    "ါ": [ 10, "ā"],
    "ာ": [ 10, "ā"],
    "ိ": [ 10, "i"],
    "ီ": [ 10, "ī"],
    "ု": [ 10, "u"],
    "ူ": [ 10, "ū"],
    "ေ": [ 10, "e"],
    "ဲ": [ 10, "ai"],
    "ံ": [ 4, "ṁ"],
    "့": [ 4, "."],
    "း": [ 4, "ḥ"], 
    "္": [ 9, ""],
    "်": [ 0, "·"],
    "ျ": [ 7, "y"],
    "ြ": [ 7, "r"],
    "ွ": [ 7, "v"],
    "ှ": [ 7, "h"],
    "ဿ": [ 5, "ss"],
    "၀": [ 2, "0"],
    "၁": [ 2, "1"],
    "၂": [ 2, "2"],
    "၃": [ 2, "3"],
    "၄": [ 2, "4"],
    "၅": [ 2, "5"],
    "၆": [ 2, "6"],
    "၇": [ 2, "7"],
    "၈": [ 2, "8"],
    "၉": [ 2, "9"],
    "၊": [ 8, "၊"],
    "။": [ 8, "။"],
    "၌": [ 6, "*n"],
    "၍": [ 6, "*r"],
    "၎": [ 3, "*l"],
    "၏": [ 6, "*e"],
    "ၐ": [ 1, "ś"],
    "ၑ": [ 1, "ṣ"],
    "ၒ": [ 3, "°r̥"], # TODO: check if they are 3 or 6
    "ၓ": [ 3, "°r̥̄"],
    "ၔ": [ 3, "°l̥"],
    "ၕ": [ 3, "°l̥̄"],
    "ၖ": [ 10, "r̥"],
    "ၗ": [ 10, "r̥̄"],
    "ၘ": [ 10, "l̥"],
    "ၙ": [ 10, "l̥̄"],
    " ": [ 11, "_"], # transliterating space with a _
}

# TODO: Vowel_dep_signs with အ
#  priority combination ex င့်; asat ် replaced by median dot · # N.B. not standard unicode order

# -2: implicit a, no break after first character
# -1: illegal character sequence
#  0: no break after first character
#  1: break after first character
#  2: break after second character
#  4: break after 4th character

AUTO = [
# A = 0
[ -1, 12, 1, 1, 0, -1, 1, 0, 1, 0, 0, 1],
# C = 1
[ 0, 13, 1, 1, -2, 0, 1, 0, 1, 0, 0, 1],
# D = 2
[ -1, 1, 0, 1, -1, -1, 1, -1, 1, -1, -1, 1],
# E = 3
[ -1, 17, 1, 1, 2, 0, 1, -1, 1, -1, 0, 1],
# F = 4
[ -1, 12, 1, 1, 2, -1, 1, -1, 1, -1, -1, 1],
# G = 5
[ -1, 1, 1, 1, 0, -1, 1, -1, 1, -1, 0, 1],
# I = 6
[ -1, 14, 1, 1, 0, -1, 1, -1, 1, -1, -1, 1],
# M = 7
[ 2, 17, 1, 1, -2, 0, 1, 0, 1, -1, 0, 1],
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
# CC = 13
[ -2, 1, 1, 1, 16, 1, 1, 1, 1, -2, 1, 1],
# VC = 14
[ 0, 1, 1, 1, 1, 1, 1, 15, 1, 0, 1, 1],
# ACM = FCM = VCM = 15
[ 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# CCF = 16
[ -2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# EC = MC = 17
[ -2, 1, 1, 1, 18, 1, 1, 1, 1, -2, 1, 1],
# ECF = MCF = 18
[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]



def getNextTokenInfo(s, idx, slen):
    if slen < idx+1:
        return None
    if slen >= idx+2:
        nexttwo = s[idx:idx+2]
        # hack: āu = āe = o
        if nexttwo == "ော" or nexttwo == "ာေ":
            return [2, [10, "o"]]
        # hack: Unicode specifies 102D (i) 102F (u) but translitteration says ui
        if nexttwo == "ို":
            return [2, [10, "ui"]]
        # hack: tone markers
        if nexttwo == "အ်":
            return [2, [4, "°a·"]]
        if nexttwo == "ဝ်":
            return [2, [4, "v·"]]
        if nexttwo == "ဟ်":
            return [2, [4, "h·"]]
        if nexttwo == "့်" or nexttwo == "့်":
            return [2, [0, "·."]]
    if slen >= idx+3:
        nextthree = s[idx:idx+3]
        if nextthree == "ော်":
            # assigning it 4 allows no further consonnant afterwards 
            return [3, [4, "au"]]
        if nextthree == "္အ်":
            # assigning it 0 is a bit hacky but I don't think it will have damaging consequences
            return [3, [0, "'·"]]
    nextone = s[idx:idx+1]
    if nextone in CLASSES:
        return [1, CLASSES[nextone]]
    return [1, [11, nextone]]

def getNextTransBreak(s, idx):
    state = None
    curidx = idx
    ress = ""
    resrest = ""
    # the last replacement that made it into ress (not resrest)
    lastrepl = ""
    slen = len(s)
    seenVowel = False
    while curidx < slen:
        #print("start loop with curidx = %d : %s" % (curidx, s[curidx:]))
        cinfo = getNextTokenInfo(s, curidx, slen)
        if not cinfo:
            #print("exiting bizarrely")
            state = -1
            break
        nbchars = cinfo[0]
        cl = cinfo[1][0]
        repl = cinfo[1][1]
        if cl in [10, 3, 6]:
            #print("seenVowel = true")
            seenVowel = True
        # hack: အာ = °ā
        #print("ress=%s" %ress)
        if lastrepl == "'":
            #print("hacking အ")
            if repl == 'ā' or repl == 'ai':
                ress = ress[:-1]+"°"
                lastrepl = "°"
            elif cl == 0:
                ress = ress[:-1]+"°a"
                lastrepl = "°a"
                seenVowel = True
        #print("ress=%s" %ress)
        if state is None:
            state = cl
            curidx += nbchars
            idx = curidx
            ress += resrest+repl
            lastrepl = repl
            continue
        res = AUTO[state][cl]
        #print("trans = %s, cl=%s, repl=%s, lastrepl=%s, resrest = %s , %d + %d = %d " % (ress, cl, repl, lastrepl, resrest, state, cl, res))
        if res > 5:
            #print("test %s" % res)
            state = res
            curidx += nbchars
            resrest += repl
            continue
        if res == -1:
            #print("warning: illegal sequence")
            state = cl
            curidx += nbchars
            idx = curidx
            ress += resrest+repl
            resrest = ""
            lastrepl = repl
            continue
        if res == -2:
            #print("test -2, lastrepl=%s" % lastrepl)
            state = cl
            curidx += nbchars
            idx = curidx
            # the ' / ° dance of အ
            if lastrepl == "'":
                # replacing the last repl by °:
                ress = ress[:-1]+"°"
            if not seenVowel:
                ress += 'a'+resrest+repl
            else:
                ress += resrest+repl
            resrest = ""
            lastrepl = repl
            seenVowel = True
            continue
        if res == 0:
            state = cl
            curidx += nbchars
            idx = curidx
            ress += resrest+repl
            resrest = ""
            lastrepl = repl
            continue
        #print("return with trans=%s res=%d, idx=%d, state=%d" % (ress, res, idx+res-1, state))
        # 'a' after consonnant (cl=1, )
        if res == 1:
            # the ' / ° dance of အ
            if lastrepl == "'":
                # replacing the last repl by °:
                ress = ress[:-1]+"°"
            ress += 'a'
            seenVowel = True
        else:
            ress += resrest+repl
        #print("return2 with trans=%s idx=%d" % (ress, idx+res-1))
        return [idx+res-1, ress]
    # no further break, but we go out of intermediate states
    # by simulating a blank space afterwards
    #print("end: trans=%s, resrest=%s, state=%d" % (ress, resrest, state))
    if state > 5:
        res = AUTO[state][11]
        #print("res = %d" %res)
        if res == -1:
            ress = ress+resrest
            return [-1, ress]
        if res == -2:
            ress = ress+'a'#+resrest
            seenVowel = True
            # the ' / ° dance of အ
            if lastrepl == "'":
                # replacing the last repl by °:
                ress = ress[:-1]+"°"
            return [idx+res-1, ress]
        ress = ress#+resrest
        if not seenVowel:
            ress += 'a'
        return [idx+res-1, ress]
    if state == 1:
        # the ' / ° dance of အ
        if lastrepl == "'":
            # replacing the last repl by °:
            ress = ress[:-1]+"°"
        ress += 'a'+resrest
    else:
        ress += resrest
        if not seenVowel:
            ress += 'a'
    return [-1, ress]

def getTransTokens(s):
    res = []
    idx = 0
    while idx < len(s):
        nextidx = getNextTransBreak(s, idx)
        if nextidx == -1:
            res.append(s[idx:])
            break
        res.append(s[idx:nextidx])
        idx = nextidx
    return res


def getTrans(s):
    res = ""
    idx = 0
    lasttrans = ""
    while idx < len(s):
        nextinfo = getNextTransBreak(s, idx)
        nextidx = nextinfo[0]
        nexttrans = nextinfo[1]
        #print("got nexttrans=%s, nextidx=%d" % (nexttrans, nextidx))
        # °a conventionally sticks with the following syllable, as a nominalizer prefix
        if res and lasttrans != "°a":
            res += " "
        res += nexttrans
        lasttrans = nexttrans
        if nextidx == -1:
            break
        idx = nextidx
    return res
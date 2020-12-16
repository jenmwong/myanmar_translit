
TOKENS = {}

def createTokens():
    addOneToken(["k"], "က", 0)
    addOneToken(["kh"], "ခ", 0)
    addOneToken(["g"], "ဂ", 0)
    addOneToken(["gh"], "ဃ", 0)
    addOneToken(["ṅ", "ṅ"], "င", 0)
    addOneToken(["c"], "စ", 0)
    addOneToken(["ch"], "ဆ", 0)
    addOneToken(["j"], "ဇ", 0)
    addOneToken(["jh"], "ဈ", 0)
    addOneToken(["ñ", "ñ"], "ဉ", 0)
    addOneToken(["ññ", "ññ"], "ည", 0)
    addOneToken(["ṭ", "ṭ"], "ဋ", 0)
    addOneToken(["ṭh", "ṭh"], "ဌ", 0)
    addOneToken(["ḍ", "ḍ"], "ဍ", 0)
    addOneToken(["ḍh", "ḍh"], "ဎ", 0)
    addOneToken(["ṇ", "ṇ"], "ဏ", 0)
    addOneToken(["t"], "တ", 0)
    addOneToken(["th"], "ထ", 0)
    addOneToken(["d"], "ဒ", 0)
    addOneToken(["dh"], "ဓ", 0)
    addOneToken(["n"], "န", 0)
    addOneToken(["p"], "ပ", 0)
    addOneToken(["ph"], "ဖ", 0)
    addOneToken(["b"], "ဗ", 0)
    addOneToken(["bh"], "ဘ", 0)
    addOneToken(["m"], "မ", 0)
    addOneToken(["y"], "ယ", 12)
    addOneToken(["r"], "ရ", 12)
    addOneToken(["l"], "လ", 12)
    addOneToken(["v"], "ဝ", 12)
    addOneToken(["s"], "သ", 0)
    addOneToken(["h"], "ဟ", 12)
    addOneToken(["a"], "", 13)
    addOneToken(["ḷ", "ḷ"], "ဠ", 0)
    addOneToken(["'", "’", "ʼ", "ʹ", "‘", "ʾ", "°"], "အ", 10)
    # ဢ ? ဨ ?  "ါ ဳ  ဴ  ဵ
    addOneToken(["°i"], "ဣ", 0)
    addOneToken(["°ī", "°ī"], "ဤ", 0)
    addOneToken(["°u"], "ဥ", 0)
    addOneToken(["°ū", "°ū"], "ဦ", 0)
    addOneToken(["°e"], "ဧ", 0)
    addOneToken(["°o"], "ဩ", 0)
    addOneToken(["°au"], "ဪ", 0)
    addOneToken(["ā", "ā"], "ာ", 1)
    addOneToken(["i"], "ိ", 1)
    addOneToken(["ī", "ī"], "ီ", 1)
    addOneToken(["u"], "ု", 1)
    addOneToken(["ū", "ū"], "ူ", 1)
    addOneToken(["e"], "ေ", 1)
    addOneToken(["ai"], "ဲ", 1)
    addOneToken(["ṁ", "ṁ", "ṃ", "ṃ", ""], "ံ", 1)
    addOneToken(["."], "့", 1)
    addOneToken(["·"], "်", 2)    
    addOneToken(["ss"], "ဿ", 0)
    addOneToken(["0"], "၀", 0)
    addOneToken(["1"], "၁", 0)
    addOneToken(["2"], "၂", 0)
    addOneToken(["3"], "၃", 0)
    addOneToken(["4"], "၄", 0)
    addOneToken(["5"], "၅", 0)
    addOneToken(["6"], "၆", 0)
    addOneToken(["7"], "၇", 0)
    addOneToken(["8"], "၈", 0)
    addOneToken(["9"], "၉", 0)
    addOneToken(["*n"], "၌", 0)
    addOneToken(["*r"], "၍", 0)
    addOneToken(["*l"], "၎", 0)
    addOneToken(["*e"], "၏", 0)
    addOneToken(["ś", "ś"], "ၐ", 0)
    addOneToken(["ṣ", "ṣ"], "ၑ", 0)
    addOneToken(["°r̥", "°r̥"], "ၒ", 0)
    addOneToken(["°r̥̄", "°r̥̄", "°r̥̄"], "ၓ", 0)
    addOneToken(["°l̥", "°l̥"], "ၔ", 0)
    addOneToken(["°l̥̄", "°l̥̄", "°l̥̄"], "ၕ", 0)
    addOneToken(["r̥", "r̥"], "ၖ", 1)
    addOneToken(["r̥̄", "r̥̄", "r̥̄"], "ၗ", 1)
    addOneToken(["l̥", "l̥"], "ၘ", 1)
    addOneToken(["l̥̄", "l̥̄", "l̥̄"], "ၙ", 1)
    addOneToken(["_"], " ", 2)
    addOneToken([" "], "", 11)
    # complex cases: y, r, v, a, h, space


def addOneToken(variants, trans, cl):
    global TOKENS
    for v in variants:
        l = len(v)
        if l not in TOKENS:
            TOKENS[l] = {}
        TOKENS[l][v] = [trans, cl]
        tc = v.title() # title case
        l = len(tc)
        if l not in TOKENS:
            TOKENS[l] = {}
        TOKENS[l][tc] = [trans, cl]
        tc = v.upper() # title case
        l = len(tc)
        if l not in TOKENS:
            TOKENS[l] = {}
        TOKENS[l][tc] = [trans, cl]

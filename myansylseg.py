import re

# Initial code from https://github.com/ye-kyaw-thu/sylbreak/blob/master/python/sylbreak.py
# Apache 2 license
# converted to Python3


# TODO: get the tests from https://github.com/swanhtet1992/ReSegment/blob/master/resegment.py

myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'

#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])")

def addcharatsyllbreaks(s, c):
	return BreakPattern.sub(c + r"\1", s).strip(c)

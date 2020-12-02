# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import sys
import string

# usage python3 > output.txt
# transliterates text file myfile.txt to output file output.txt

def translitcons(string):
	cons_indep_signs = {
		'\u1000': 'ka', '\u1001': 'kha', '\u1002': 'ga', '\u1003': 'gha', '\u1004': 'ṅa', #ကခဂဃင
		'\u1005': 'ca', '\u1006': 'cha', '\u1007': 'ja', '\u1008': 'jha', '\u1009': 'ña', '\u100a': 'ñña', # စဆဇဈဉည
		'\u100b': 'ṭa', '\u100c': 'ṭha', '\u100d': 'ḍa', '\u100e': 'ḍha', '\u100f': 'ṇa', # ဋဌဍဎဏ
		'\u1010': 'ta', '\u1011': 'tha', '\u1012': 'da', '\u1013': 'dha', '\u1014': 'na', # တထဒဓန
		'\u1015': 'pa', '\u1016': 'pha', '\u1017': 'ba', '\u1018': 'bha', '\u1019': 'ma', # ပဖဗဘမ
		'\u101a': 'ya', '\u101b': 'ra', '\u101c': 'la', '\u101d': 'va', '\u101e': 'sa', # ယရလဝသ
		'\u101f': 'ha', '\u1020': 'ḷa', '\u1021': 'ʔa', # ဟဠအ
		'\u1023': 'ʔi',  '\u1024': 'ʔī', '\u1025': 'ʔu', '\u1026': 'ʔū', '\u1027': 'ʔe', # ဣဤဥဦဧ
		'\u1028': 'ʔe', # ဨ MON E
		'\u1029': 'ʔo', '\u102a': 'ʔau', # ဩ  ဪ
		'\u103f': 'ssa', # ဿ
		'\u1040': '0', '\u1041': '1', '\u1042': '2', '\u1043': '3', '\u1044': '4', # ၀၁၂၃၄
		'\u1045': '5', '\u1046': '6', '\u1047': '7', '\u1048': '8', '\u1049': '9', # ၅၆၇၈၉
		'\u104a': '|', '\u104b': '||', # ၊ ။
		'\u104c': "n*", '\u104d': 'r*', '\u104e': 'l*', '\u104f': 'ʔe*', # ၌၍၎၏
		'\u1050': 'śa', '\u1051': 'ṣa', '\u1052': 'r̥', '\u1053': 'r̥̄', '\u1054': 'ḷ', '\u1055': 'ḹ', # pali & sanskrit extensions ၐၑၒၓၔၕ
		'\u105a': 'ṅa', #  ၚ MON NGA
		'\u105b': 'jha', # ၛ  MON JHA
		'\u105c': 'ḅa', # ၜ MON BBA  
		'\u105d': 'mba', # ၝ MON BBE  
		# Other signs
		'\u14da': '~', #  ᓚ	~ Canadian syllabics la
		'\u0c3d': '~', # ఽ	~ Telugu sign avagraha
		'\u1d698': '𝚘', # 𝚘	Mathematical monospace small 𝚘
		'\u25c7': '◇', # ◇	◇
		'\u1f33c': '🌼', # 🌼	🌼
		'\u0e4f': '๏', # ๏	๏
		'\u2e2d': '⸭', # ⸭  ⸭
		'\u10fb': '჻', # ჻  ჻
		'\u22ee': '⋮', # ⋮	⋮		゠U+30a0
		'\u30a0': '゠', # ゠  Katakana double hyphen can be used for this punctuation mark
		'\ua831': '½', # ꠱
		'\u1690': '¼', # Ogham letter ailm ᚐ
		'\u03c6': '¼', #  GREEK SMALL LETTER PHI φ 
		'\u10ab': '¼', # Georgian capital letter man: Ⴋ
		'\u10bb': '¼', # Georgian capital letter jil: Ⴛ
		'\u2ac2': '¾', # Superset with multiplication sign below: ⫂
		'\u15bb': '⅛', # Canadian syllabics blackfoot na: ᖻ
		'\u156e': '¹⁄₁₆', # Canadian syllabics ttha: ᕮ
		'\u13c0': '¹⁄₃₂', # Ꮐ Cherokee letter nah: Ꮐ
		'\u146a': '¹⁄₃₂' # Canadian syllabics tta: ᑪ
		'\u1293': 'û' # Unicode Character 'ETHIOPIC SYLLABLE NAA' (U+1293) for au vowel hook
	}

	translit_string = ""
	for index, char in enumerate(string):
		if char in cons_indep_signs.keys():
			char = cons_indep_signs[char]
		translit_string += char
	return translit_string

def translitmedials(string):
	medials = {
		'\u103b': 'ya', '\u103c': "ra", '\u103d': 'va', '\u103e': 'ha',  # MEDIALS ျ ြ ွ ှ
		'\u105e': 'na', '\u105f': 'ma', '\u1060': 'la' # MON MEDIALS ၞ ၟ ၠ
	}

	translit_string = ""
	for index, char in enumerate(string):
		if char in medials.keys():
			if index > 0 and translit_string[index-1] == 'a':
				translit_string = translit_string[:-1]
			char = medials[char]
		translit_string += char
	return translit_string

def translitcompvow(string):
	compound_vowels = {
		'\u1031\u102b': 'o', # ော
		'\u1031\u102c': 'o', # ေါ
		'\u102d\u102f': 'ui' # ို
	}
	translit_string = ""
	for index, char in enumerate(string):
		if index < len(string)-1:
			compound =  char + string[index+1]
		else:
			compound = char;
		if index == 0:
			translit_string += char
			index =+ 1
		elif compound in compound_vowels.keys():
			if index > 1 and string[index-1] == 'a':
				translit_string = translit_string[:-1]
			compound = compound_vowels[compound]
			translit_string += compound
		elif index > 0 and char == '\u102f' and string[index-1] == '\u102d':
			continue
		elif index > 0 and char == '\u102c' and string[index-1] == '\u1031':
			continue
		elif index > 0 and char == '\u102b' and string[index-1] == '\u1031':
			continue
		else: 
			translit_string += char
#		print("Translit string %r" % (translit_string))
	return translit_string

def translitdepends(string):
	vowel_dep_signs = {
		'\u102b': 'ā', '\u102c': "ā", # ာ ါ
		'\u102d': 'i', '\u102e': 'ī', # ိ ီ
		'\u102f': 'u', '\u1030': 'ū', # ု ူ
		'\u1031': 'e', '\u1032': 'ai', # ေ ဲ
		'\u1033': 'ī', '\u1034': 'o', '\u1035': 'e', # ဳ MON II  ဴ MON O ဵ E ABOVE
		'\u1036': 'ṃ', # ံ ANUSVARA 
		'\u1037': 'ɂ', # dot below aukmyit ့ replaced by ɂ 
		'\u1038': 'ḥ', # း VISARGA  
		'\u1039': '', # virama replaced by nothing just remove previous inherent 'a' vowel
		'\u103a': '\u02bb', # asat ် replaced by ʻ MODIFIER LETTER TURNED COMMA
		'\u1056': 'r̥', '\u1057': 'r̥̄', '\u1058': 'ḷ', '\u1059': 'ḹ' # pali & sanskrit vowel extensions ၖ ၗ ၘ ၙ
	}

	translit_string = ""
	for index, char in enumerate(string):
		if char in vowel_dep_signs.keys():
			if index > 1 and string[index-1] == 'a':
				translit_string = translit_string[:-1]
			char = vowel_dep_signs[char]
		translit_string += char
	return translit_string

if __name__ == "__main__":
	f = codecs.open('myfile.txt', "r", "utf-8")
	lines = f.readlines()
	for line in lines:
#		textline = u"ကိုမြစေတီဘုရားကျောက်စာ၊ မြန်မာ၊ ကို"
		print(line)
# replace consonants	
		textc = translitcons(line)
#		print(textc)
# replace a+medials  
		textcm = translitmedials(textc)
#		print(textcm)
#replace compound vowels
		textcmcv = translitcompvow(textcm)
#		print(textcmcv)
# replace a+vowels translitdepends
		textcmcvd = translitdepends(textcmcv)
		print(textcmcvd) 
	f.close()

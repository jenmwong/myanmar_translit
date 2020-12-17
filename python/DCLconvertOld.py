
FIRSTREPLS = {
	"\x{1000}": "ka",
	"\x{1001}": "kha",
	"\x{1002}": "ga",
	"\x{1003}": "gha",
	"\x{1004}": "ṅa",
	"\x{1005}": "ca",
	"\x{1006}": "cha",
	"\x{1007}": "ja",
	"\x{1008}": "jha",
	"\x{1009}": "ña",
	"\x{100a}": "ñña", # not on page 5
	"\x{100b}": "ṭa",
	"\x{100c}": "ṭha",
	"\x{100d}": "ḍa",
	"\x{100e}": "ḍha",
	"\x{100f}": "ṇa",
	"\x{1010}": "ta",
	"\x{1011}": "tha",
	"\x{1012}": "da",
	"\x{1013}": "dha",
	"\x{1014}": "na",
	"\x{1015}": "pa",
	"\x{1016}": "pha",
	"\x{1017}": "ba",
	"\x{1018}": "bha",
	"\x{1019}": "ma",
	"\x{101a}": "ya",
	"\x{101b}": "ra",
	"\x{1050}": "śa",
	"\x{1051}": "ṣa",
	"\x{101e}": "sa",
	"\x{1020}": "ḷa",
	"\x{1023}": "°i",
	"\x{1024}": "°ī",
	"\x{1025}": "°u",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
	"": "",
}

def toRom(s):

		$string =~ s/\x{101d}\x{103a}/v·/g; # ဝ် # priority combination
		$string =~ s/\x{101d}/va/g; #ဝ
		
		$string =~ s/\x{101f}\x{103a}/h/g; #ဟ် # priority combination
		$string =~ s/\x{101f}/ha/g; #ဟ

		$string =~ s/\x{1021}\x{103a}/°A·/g; #အ် # priority combination (tone marker)
		$string =~ s/\x{1021}/°a/g; #အ
		
		# N.B. in Unicode အာ is a combination of independant အ and dependant vowel ာ, 
		# the latter is transliterated later
		$string =~ s/\x{1023}/°i/g; #ဣ
		$string =~ s/\x{1024}/°ī/g; #ဤ
		
		$string =~ s/\x{1025}/°u/g; #ဥ
		$string =~ s/\x{1026}/°ū/g; #ဦ

		$string =~ s/\x{1052}/°r̥/g; #ၒ
		$string =~ s/\x{1053}/°r̥̄/g; #ၓ
		$string =~ s/\x{1054}/°ḷ/g; #ၔ
		$string =~ s/\x{1055}/°ḹ/g; #ၕ	
				
		$string =~ s/\x{1027}/°e/g; #ဧ
		# N.B. in Unicode အဲ is a combination of independant အ and dependant vowel ဲ, 
		# the latter is transliterated later
		$string =~ s/\x{1029}/°o/g; #ဩ
		$string =~ s/\x{102a}/°au/g; #ဪ
		
		$string =~ s/\x{103f}/ssa/g; # ဿ ??
		$string =~ tr/၀-၉/0-9/; # ၀၁၂၃၄... ??
		$string =~ s/\x{104a}/၊/g; # superfluous (not replaced)
		$string =~ s/\x{104b}/။/g; # superfluous (not replaced)
		$string =~ s/\x{104f}/*e/g; #၏
		$string =~ s/\x{104e}/*l/g; #၎
		$string =~ s/\x{104c}/*n/g; #၌
		$string =~ s/\x{104d}/*r/g; #၍

		
		# Replace (a+)Medials
		$string =~ s/a*\x{103b}/ya/g; # ျ
		$string =~ s/a*\x{103c}/ra/g; # ြ
		$string =~ s/a*\x{103d}/va/g; # ွ
		# N.B. In Unicode ္လ is a combination of္ and လ, not a single codepoint
		$string =~ s/a*\x{103e}/ha/g; # ှ
		
		# Replace (a+)Compound_vowels
		$string =~ s/°a*\x{1031}\x{102c}\x{103a}/'au/g;  # ော် # priority combination
		$string =~ s/a*\x{1031}\x{102c}\x{103a}/au/g;  # ော် # priority combination
		$string =~ s/°a*\x{1031}\x{102c}/'o/g;  # ော  #
		$string =~ s/a*\x{1031}\x{102c}/o/g;  # ော  #
		$string =~ s/°a*\x{1031}\x{102b}/'o/g;  # ေါ  #
		$string =~ s/a*\x{1031}\x{102b}/o/g;  # ေါ  #
		$string =~ s/°a*\x{102d}\x{102f}/'ui/g; # ို 
		$string =~ s/a*\x{102d}\x{102f}/ui/g; # ို

		# Vowel_dep_signs
		# with အ
		$string =~ s/°a*\x{102c}/°ā/g; # ာ
		$string =~ s/°a*\x{102b}/°ā/g; #  ါ
		$string =~ s/°a*\x{102d}/'i/g; # ိ
		$string =~ s/°a*\x{102e}/'ī/g; # ီ
		$string =~ s/°a*\x{102f}/'u/g; # ု  
		$string =~ s/°a*\x{1030}/'ū/g; # ူ
		$string =~ s/°a*\x{1056}/'r̥/g; # ၖ 
		$string =~ s/°a*\x{1057}/'r̥̄/g;# ၗ
		$string =~ s/°a*\x{1058}/'ḷ/g;# ၘ
		$string =~ s/°a*\x{1059}/'ḹ/g; # ၙ
		$string =~ s/°a*\x{1031}/'e/g; # ဲ
		$string =~ s/°a*\x{1032}/°ai/g; #  ဲ
		
		# Vowel_dep_signs with other consonant signs
		$string =~ s/a*\x{102c}/ā/g; # ာ
		$string =~ s/a*\x{102b}/ā/g; #  ါ
		$string =~ s/a*\x{102d}/i/g; # ိ
		$string =~ s/a*\x{102e}/ī/g; # ီ
		$string =~ s/a*\x{102f}/u/g; # ု
		$string =~ s/a*\x{1030}/ū/g; # ူ
		$string =~ s/a*\x{1056}/r̥/g; # ၖ 
		$string =~ s/a*\x{1057}/r̥̄/g;# ၗ
		$string =~ s/a*\x{1058}/ḷ/g;# ၘ
		$string =~ s/a*\x{1059}/ḹ/g; # ၙ
		$string =~ s/a*\x{1031}/e/g; # ဲ
		$string =~ s/a*\x{1032}/ai/g; #  ဲ

		#$string =~ s/\x{1036}/ṃ/g; # ံ ANUSVARA  -ṁ/-ṃ ??
		$string =~ s/\x{1036}/ṁ/g; # ံ ANUSVARA  -ṁ/-ṃ ??
		$string =~ s/a\x{1037}\x{103a}/·./g; #  priority combination ex င့်; asat ် replaced by median dot · # N.B. not standard unicode order
		$string =~ s/a\x{1039}°A·/'·/g; # remove a vowel before priority combination with virama ex ယ္အ်		
		$string =~ s/\x{1037}/./g; # dot below, aukmyit ့  
		$string =~ s/\x{1038}/ḥ/g; # း VISARGA 
		$string =~ s/a*\x{1039}//g; # virama replaced by nothing just remove previous inherent a vowel
		$string =~ s/a\x{103a}/·/g; # asat ် replaced by median dot · 
		$string =~ s/A/a/g;
		$string =~ s/aā/ā/g;
		$string =~ s/aa/a/g;
		
		return $string;
}


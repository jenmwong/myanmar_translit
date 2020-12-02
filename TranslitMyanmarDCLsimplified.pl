#!/usr/bin/perl
use strict;
use warnings;
use utf8;


binmode(STDOUT, ":utf8");

my $text = "။ၐြီ။ နမော ဗုဒ္ဓါယ။ ပုရှာသ္ခင် သာသနာ အနှစ် တစ်ထောင် ခြောက်ရျာ နှစ်ဆာယ ဟေတ်နှစ် လောန် လိယ်ဗြီရကာ။ ";

print transliterate($text)."\n"; 


sub transliterate{

		my($string) = shift(@_);
		
		# Replace Consonants
		$string =~ s/\x{1000}/ka/g; #က
		$string =~ s/\x{1001}/kha/g; #ခ
		$string =~ s/\x{1002}/ga/g; #ဂ
		$string =~ s/\x{1003}/gha/g; #ဃ
		$string =~ s/\x{1004}/ṅa/g; #င
		
		$string =~ s/\x{1005}/ca/g; #စ
		$string =~ s/\x{1006}/cha/g; #ဆ
		$string =~ s/\x{1007}/ja/g; #ဇ
		$string =~ s/\x{1008}/jha/g; #ဈ
		$string =~ s/\x{1009}/ña/g; #ဉ
		$string =~ s/\x{100a}/ñña/g; #ည   not on page 5
		
		$string =~ s/\x{100b}/ṭa/g; #ဋ
		$string =~ s/\x{100c}/ṭha/g; #ဌ
		$string =~ s/\x{100d}/ḍa/g; #ဍ
		$string =~ s/\x{100e}/ḍha/g; #ဎ
		$string =~ s/\x{100f}/ṇa/g; #ဏ
		
		$string =~ s/\x{1010}/ta/g; #တ
		$string =~ s/\x{1011}/tha/g; #ထ
		$string =~ s/\x{1012}/da/g; #ဒ
		$string =~ s/\x{1013}/dha/g; #ဓ
		$string =~ s/\x{1014}/na/g; #န
		
		$string =~ s/\x{1015}/pa/g; #ပ
		$string =~ s/\x{1016}/pha/g; #ဖ
		$string =~ s/\x{1017}/ba/g; #ဗ
		$string =~ s/\x{1018}/bha/g; #ဘ
		$string =~ s/\x{1019}/ma/g; #မ

		$string =~ s/\x{101a}/ya/g; #ယ
		$string =~ s/\x{101b}/ra/g; #ရ
		$string =~ s/\x{101c}/la/g; #လ
		$string =~ s/\x{101d}\x{103a}/v/g; # ဝ် # priority combination
		$string =~ s/\x{101d}/va/g; #ဝ
		
		$string =~ s/\x{1050}/śa/g; #ၐ
		$string =~ s/\x{1051}/ṣa/g; #ၑ
		$string =~ s/\x{101e}/sa/g; #သ
		
		$string =~ s/\x{101f}\x{103a}/h/g; #ဟ် # priority combination
		$string =~ s/\x{101f}/ha/g; #ဟ
		$string =~ s/\x{1020}/ḷa/g; #ဠ
		$string =~ s/\x{1021}\x{102d}\x{102f}/aui/g; #အို # priority combination
		$string =~ s/\x{1021}\x{103a}/a/g; #အ် # priority combination
		$string =~ s/\x{1021}/a/g; #အ
		
		# N.B. in Unicode အာ is a combination of independant အ and dependant vowel ာ, 
		# the latter is transliterated later
		$string =~ s/\x{1023}/i/g; #ဣ
		$string =~ s/\x{1024}/ī/g; #ဤ
		
		$string =~ s/\x{1025}/u/g; #ဥ
		$string =~ s/\x{1026}/ū/g; #ဦ

		$string =~ s/\x{1052}/r̥/g; #ၒ
		$string =~ s/\x{1053}/r̥̄/g; #ၓ
		$string =~ s/\x{1054}/ḷ/g; #ၔ
		$string =~ s/\x{1055}/ḹ/g; #ၕ	
				
		$string =~ s/\x{1027}/e/g; #ဧ
		# N.B. in Unicode အဲ is a combination of independant အ and dependant vowel ဲ, 
		# the latter is transliterated later
		$string =~ s/\x{1029}/o/g; #ဩ
		$string =~ s/\x{102a}/au/g; #ဪ
		
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
		$string =~ s/a*\x{1031}\x{102c}\x{103a}/au/g;  # ော် # priority combination
		$string =~ s/a*\x{1031}\x{102c}/o/g;  # ော  #
		$string =~ s/a*\x{1031}\x{102b}/o/g;  # ေါ  #
		$string =~ s/a*\x{102d}\x{102f}/ui/g; # ို
		
		# Vowel_dep_signs
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

		$string =~ s/\x{1036}/ṃ/g; # ံ ANUSVARA  -ṁ/-ṃ ??
		$string =~ s/\x{1037}/./g; # dot below, aukmyit ့  
		$string =~ s/\x{1038}/ḥ/g; # း VISARGA 
		$string =~ s/a*\x{1039}//g; # virama replaced by nothing just remove previous inherent a vowel
		$string =~ s/a\x{103a}/·/g; # asat ် replaced by median dot · or nothing ??

		
		return $string;
}


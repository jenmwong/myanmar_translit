#!/usr/bin/perl
use strict;
use warnings;
use utf8;


binmode(STDOUT, ":utf8");

my $text = "။ၐြီ။ နမော ဗုဒ္ဓါယ။ ပုရှာသ္ခင် သာသနာ အနှစ် တစ်ထောင် ခြောက်ရျာ နှစ်ဆာယ ဟေတ်နှစ် လောန် လိယ်ဗြီရကာ။";

print transliterate($text)."\n"; 


sub transliterate{
		my($string) = shift(@_);
		# Replace Consonants
		$string =~ s/\x{1000}/ka/g; #ကခဂဃင
		$string =~ s/\x{1001}/kha/g;
		$string =~ s/\x{1002}/ga/g;
		$string =~ s/\x{1003}/gha/g;
		$string =~ s/\x{1004}/ṅa/g;
		$string =~ s/\x{1005}/ca/g;  # စဆဇဈဉည
		$string =~ s/\x{1006}/cha/g;
		$string =~ s/\x{1007}/ja/g;
		$string =~ s/\x{1008}/jha/g;
		$string =~ s/\x{1009}/ña/g;
		$string =~ s/\x{100a}/ñña/g;
		$string =~ s/\x{100b}/ṭa/g; # ဋဌဍဎဏ
		$string =~ s/\x{100c}/ṭha/g;
		$string =~ s/\x{100d}/ḍa/g;
		$string =~ s/\x{100e}/ḍha/g;
		$string =~ s/\x{100f}/ṇa/g;
		$string =~ s/\x{1010}/ta/g; # တထဒဓန
		$string =~ s/\x{1011}/tha/g;
		$string =~ s/\x{1012}/da/g;
		$string =~ s/\x{1013}/dha/g;
		$string =~ s/\x{1014}/na/g;
		$string =~ s/\x{1015}/pa/g; # ပဖဗဘမ
		$string =~ s/\x{1016}/pha/g;
		$string =~ s/\x{1017}/ba/g;
		$string =~ s/\x{1018}/bha/g;
		$string =~ s/\x{1019}/ma/g;
		$string =~ s/\x{101a}/ya/g; # ယရလဝသ
		$string =~ s/\x{101b}/ra/g;
		$string =~ s/\x{101c}/la/g;
		$string =~ s/\x{101d}/va/g;
		$string =~ s/\x{101e}/sa/g;
		$string =~ s/\x{101f}/ha/g; # ဟဠအ
		$string =~ s/\x{1020}/ḷa/g;
		$string =~ s/\x{1021}/ʔa/g;
		$string =~ s/\x{1023}/ʔi/g; # ဣဤဥဦဧ
		$string =~ s/\x{1024}/ʔī/g;
		$string =~ s/\x{1025}/ʔu/g;
		$string =~ s/\x{1026}/ʔū/g;
		$string =~ s/\x{1027}/ʔe/g;
		$string =~ s/\x{1028}/ʔe/g; # ဨ MON E
		$string =~ s/\x{1029}/ʔo/g; # ဩ  ဪ
		$string =~ s/\x{102a}/ʔau/g;
		$string =~ s/\x{103f}/ssa/g; # ဿ
		$string =~ tr/၀-၉/0-9/; # ၀၁၂၃၄...
		$string =~ s/\x{104a}/|/g; # ၊ ။
		$string =~ s/\x{104b}/||/g;
		$string =~ s/\x{104c}/n*/g; # ၌၍၎၏
		$string =~ s/\x{104d}/r*/g;
		$string =~ s/\x{104e}/l*/g;
		$string =~ s/\x{104f}/ʔe*/g;
		$string =~ s/\x{1050}/śa/g; # pali & sanskrit extensions ၐၑၒၓၔၕ
		$string =~ s/\x{1051}/ṣa/g;
		$string =~ s/\x{1052}/r̥/g;
		$string =~ s/\x{1053}/r̥̄/g;
		$string =~ s/\x{1054}/ḷ/g;
		$string =~ s/\x{1055}/ḹ/g;
		$string =~ s/\x{105a}/ṅa/g; #  ၚ MON NGA
		$string =~ s/\x{105b}/jha/g; # ၛ  MON JHA
		$string =~ s/\x{105c}/ḅa/g; # ၜ MON BBA  
		$string =~ s/\x{105d}/mba/g; # ၝ MON BBE  
		
		# Substitutes for other signs not yet in Unicode
		$string =~ s/\x{14da}/~/g; #  ᓚ ~ Canadian syllabics la
		$string =~ s/\x{0c3d}/~/g; # ఽ ~ Telugu sign avagraha
		$string =~ s/\x{30a0}/゠/g; # ゠  Katakana double hyphen can be used for this punctuation mark
		$string =~ s/\x{a831}/½/g; # ꠱
		$string =~ s/\x{1690}/¼/g; # Ogham letter ailm ᚐ
		$string =~ s/\x{03c6}/¼/g; #  GREEK SMALL LETTER PHI φ 
		$string =~ s/\x{10ab}/¼/g; # Georgian capital letter man=> Ⴋ
		$string =~ s/\x{10bb}/¼/g; # Georgian capital letter jil=> Ⴛ
		$string =~ s/\x{2ac2}/¾/g; # Superset with multiplication sign below=> ⫂
		$string =~ s/\x{15bb}/⅛/g; # Canadian syllabics blackfoot na=> ᖻ
		$string =~ s/\x{156e}/¹⁄₁₆/g; # Canadian syllabics ttha=> ᕮ
		$string =~ s/\x{13c0}/¹⁄₃₂/g; # Ꮐ Cherokee letter nah=> Ꮐ
		$string =~ s/\x{146a}/¹⁄₃₂/g;  # Canadian syllabics tta=> ᑪ
		
		# Replace (a+)Medials
		$string =~ s/a*\x{103b}/ya/g; # ျ ြ ွ ှ
		$string =~ s/a*\x{103c}/ra/g;
		$string =~ s/a*\x{103d}/va/g;
		$string =~ s/a*\x{103e}/ha/g;
		$string =~ s/a*\x{105e}/na/g; # MON MEDIALS ၞ ၟ ၠ
		$string =~ s/a*\x{105f}/ma/g;
		$string =~ s/a*\x{1060}/la/g; 
		
		# Replace (a+)Compound_vowels
		$string =~ s/a*\x{1031}\x{102b}/o/g;  # ော
		$string =~ s/a*\x{1031}\x{102c}/o/g;  # ေါ
		$string =~ s/a*\x{102d}\x{102f}/ui/g; # ို
		
		# Vowel_dep_signs
		$string =~ s/a*\x{102b}/ā/g; # ာ ါ
		$string =~ s/a*\x{102c}/ā/g;
		$string =~ s/a*\x{102d}/i/g; # ိ ီ
		$string =~ s/a*\x{102e}/ī/g;
		$string =~ s/a*\x{102f}/u/g; # ု ူ
		$string =~ s/a*\x{1030}/ū/g;
		$string =~ s/a*\x{1031}/e/g; # ေ ဲ
		$string =~ s/a*\x{1032}/ai/g;
		$string =~ s/a*\x{1033}/ī/g; # ဳ MON II  ဴ MON O ဵ E ABOVE
		$string =~ s/a*\x{1034}/o/g;
		$string =~ s/a*\x{1035}/e/g;
		$string =~ s/\x{1036}/ṃ/g; # ံ ANUSVARA 
		$string =~ s/\x{1037}/ɂ/g; # dot below, aukmyit ့ replaced by ɂ 
		$string =~ s/\x{1038}/ḥ/g; # း VISARGA 
		$string =~ s/\x{1293}/û/g; # Old Burmese au vowel substitute ና U+1293 ETHIOPIC SYLLABLE NAA
		$string =~ s/a*\x{1039}//g; # virama replaced by nothing just remove previous inherent a vowel
		$string =~ s/a*\x{103a}/\x{02bb}/g; # asat ် replaced by ʻ MODIFIER LETTER TURNED COMMA
		$string =~ s/a*\x{1056}/r̥/g; # pali & sanskrit vowel ex{tensions ၖ ၗ ၘ ၙ
		$string =~ s/a*\x{1057}/r̥̄/g;
		$string =~ s/a*\x{1058}/ḷ/g;
		$string =~ s/a*\x{1059}/ḹ/g; 
		
		return $string;
}


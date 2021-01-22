import DCLconvert
import DCLconvertToUni
import myansylseg
import myansylseglenient
import UnicodeNorm
import csv

def testonetranslation(uni, expected):
    res = DCLconvert.getTrans(uni)
    if res != expected:
        print("converting %s : got %s but expected %s" % (uni, res, expected))

def testtranslation(fname):
    print("testing Unicode -> transliteration in %s" % fname)
    with open(fname,  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter='\t')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            testonetranslation(row[0], row[1])
            #break

def testtranslationToUnicode(fname):
    print("testing transliteration -> Unicode in %s" % fname)
    with open(fname,  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter='\t')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            res = DCLconvertToUni.getTrans(row[1])
            if res != row[0]:
                print("converting %s : got %s but expected %s" % (row[1], res, row[0]))

def testnormalization(fname):
    print("testing Unicode normalization in %s" % fname)
    with open(fname,  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter=',')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            res = UnicodeNorm.canon(row[0])
            if res != row[1]:
                print("normalizing %s : got %s but expected %s" % (row[0], res, row[1]))

def testsegmentationfile(fname):
    print("testing syllable segmentation in %s" % fname)
    with open(fname,  newline='') as fp:
        for line in fp:
            expected = line.strip(' \n_')
            expected = UnicodeNorm.canon(expected)
            if expected.startswith("#") or len(expected) == 0:
                continue
            base = expected.replace('_', '')
            tokens = myansylseg.getTokens(base)
            res = '_'.join(tokens)
            if res != expected:
                print("segmenting %s : got %s but expected %s" % (base, res, expected))
            break

def testlenienttokenizer(fname):
    print("testing lenient tokenization in %s" % fname)
    with open(fname,  newline='') as fp:
        for line in fp:
            expected = line.strip(' \n_')
            if expected.startswith("#") or len(expected) == 0:
                continue
            base = expected.replace('|', '')
            res = myansylseglenient.getTrans(base, 1)
            if res != expected:
                print("tokenizing %s : got %s but expected %s" % (base, res, expected))
            break

def testmedialorder():
    for s in ["mhrva", "mrvha", "mvrha", "mhvra", "mrhva"]:
        res = DCLconvertToUni.getTrans(s)
        if res != "မြွှ":
            print("medial order: converting %s, expected %s but got %s" % (s, "မြွှ", res))
    for s in ["mhyva", "myvha", "mvyha"]:
        res = DCLconvertToUni.getTrans(s)
        if res != "မျွှ":
            print("medial order: converting %s, expected %s but got %s" % (s, "မျွှ", res))

#testsegmentationfile('../tests/syllableseg.txt')
testtranslationToUnicode('../tests/TranslitMyanmarDCLexamples.tsv')
testtranslation('../tests/TranslitMyanmarDCLexamples.tsv')
testmedialorder()
#testnormalization('../tests/normalizations.csv')
#testlenienttokenizer('../tests/lenienttokens.csv')

teststr="""khau _ kkhā _ khkā _  ǁ Athūḥ thūḥ so tuiṅḥ krīḥ praññ krīḥ thīḥ choṅ maṅḥ apoṅḥ tui. kui acuiḥ ra tau mū so bhunḥ tau alvan krīḥ mrat tau mū lha so re mre ashyaṅḥ chaddan chaṅ maṅḥ sa khaṅ chaṅ phrū myāḥ rhaṅ lak nak cakrā sa khaṅ ashyaṅḥ bhava rhaṅ maṅḥ tarāḥ krīḥ bhurāḥ saññ sakkarāj 1214 khu ǁ"""
print(DCLconvertToUni.getTrans(teststr))
#print(DCLconvertToUni.getTrans("caṅkraṃ"))
#print(UnicodeNorm.canon("ဂျော့ချ်"))

import DCLconvert
import DCLconvertToUni
import myansylseg
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
            #break

testsegmentationfile('../tests/syllableseg.txt')
testtranslationToUnicode('../tests/TranslitMyanmarDCLexamples.tsv')
testtranslation('../tests/TranslitMyanmarDCLexamples.tsv')
testnormalization('../tests/normalizations.csv')
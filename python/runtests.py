import DCLconvert
import DCLconvertToUni
import myansylseg
import UnicodeNorm
import csv

def testonetranslation(uni, expected):
    res = DCLconvert.getTrans(uni)
    if res != expected:
        print("converting %s : got %s but expected %s" % (uni, res, expected))

def testtranslation():
    with open('../tests/curtest.tsv',  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter='\t')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            testonetranslation(row[0], row[1])
            #break

def testtranslationToUnicode():
    with open('../tests/curtest.tsv',  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter='\t')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            res = DCLconvertToUni.getTrans(row[1])
            if res != row[0]:
                print("converting %s : got %s but expected %s" % (row[1], res, row[0]))

def testnormalization():
    with open('../tests/normalizations.csv',  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter=',')
        for row in srcreader:
            if not row[0] or row[0].startswith("#"):
                continue
            res = UnicodeNorm.canon(row[0])
            if res != row[1]:
                print("normalizing %s : got %s but expected %s" % (row[0], res, row[1]))

def testsegmentationfile(fname):
    with open(fname,  newline='') as fp:
        for line in fp:
            expected = line.strip(' \n_')
            if expected.startswith("#") or len(expected) == 0:
                continue
            base = expected.replace('_', '')
            tokens = myansylseg.getTokens(base)
            res = '_'.join(tokens)
            if res != expected:
                print("segmenting %s : got %s but expected %s" % (base, res, expected))
            #break

def testsegmentation():
    #testsegmentationfile('../tests/syllableseg.txt')
    testsegmentationfile('../tests/PaliTest-ShwegugyiInscriptionBeg.txt')
    #testsegmentationfile('../tests/MixPaliBurTest-RajakumarInscriptionBeg.txt')

#testsegmentation()
#testtranslation()
testtranslationToUnicode()

#testnormalization()
import DCLconvert
import myansylseg
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
testtranslation()
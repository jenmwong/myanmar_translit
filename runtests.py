import TranslitMyanmarOBI
import myansylseg
import csv

def testonetranslation(uni, expected):
    res = TranslitMyanmarOBI.translit(uni)
    if res != expected:
        print("converting %s : got %s but expected %s" % (uni, res, expected))

def testtranlation():
    with open('tests/dcl-simple.csv',  newline='') as csvfile:
        srcreader = csv.reader(csvfile, delimiter=',')
        for row in srcreader:
            testtranslation(row[0], row[1])


def testsegmentation():
    with open('tests/syllableseg.txt',  newline='') as fp:
        for line in fp:
            expected = line.strip(' \n')
            base = expected.replace('_', '')
            tokens = myansylseg.getTokens(base)
            res = '_'.join(tokens)
            if res != expected:
                print("segmenting %s : got %s but expected %s" % (base, res, expected))
            #break

testsegmentation()
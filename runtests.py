import TranslitMyanmarOBI
import myansylseg
import csv

def testtranslation(uni, expected):
    res = TranslitMyanmarOBI.translit(uni)
    if res != expected:
        print("converting %s : got %s but expected %s" % (uni, res, expected))

with open('tests/dcl-simple.csv',  newline='') as csvfile:
    srcreader = csv.reader(csvfile, delimiter=',')
    for row in srcreader:
        testtranslation(row[0], row[1])


with open('tests/syllableseg.txt',  newline='') as fp:
    for line in fp:
        expected = line.strip(' \n')
        base = expected.replace('_', '')
        res = myansylseg.addcharatsyllbreaks(base, '_')
        if res != expected:
            print("segmenting %s : got %s but expected %s" % (base, res, expected))

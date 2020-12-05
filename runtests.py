import TranslitMyanmarOBI
import csv

def testtranslation(uni, trans):
	res = TranslitMyanmarOBI.translit(uni)
	if res != trans:
		print("converting %s : got %s but expected %s" % (uni, res, trans))

with open('tests/dcl-simple.csv',  newline='') as csvfile:
    srcreader = csv.reader(csvfile, delimiter=',')
    for row in srcreader:
        testtranslation(row[0], row[1])

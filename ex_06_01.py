text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find('0')
#print(text[startpos:])
extdata = float(text[startpos:])
print(extdata)

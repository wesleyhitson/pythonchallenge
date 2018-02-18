# Quick and dirty

def shift(letters):
    l = ""
    for letter in letters:
        l += chr(ord(letter) + 2)
    return l

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"""

print(shift(s))


# applied to the url, we get map -> ocr 

import re
import functools

# This code comes from http://unicode.org/notes/tn11/ :
# Hosken, M. Representing Myanmar in Unicode, Details and Examples Version 4
# Terms of Use of Unicode probably apply: http://www.unicode.org/copyright.html

def collation_preprocess(s):
    s = re.sub(r'(\u1029)(\u1031\u102C)?((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A ]))?', r"\u1021\4\5\u1031\u102C")
    s = re.sub(r'(\u102A)((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u1031\u102C\u103A")
    s = re.sub(r'(\u1023)((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u102D")
    s = re.sub(r'(\u1024)((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u102E")
    s = re.sub(r'(\u1025)((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u102F")
    s = re.sub(r'(\u1026)((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u1030")
    s = re.sub(r'([\u1027\u1028])((\u1004\u103A|[\u1000-\u1021])([\u1039\u103A]))?', r"\u1021\3\4\u1031")
    s = re.sub(r'(\u1031\u102C|\u1031\u102B|\u102D\u102F|[\u102B-\u102D\u102F\u1031])(\u1004\u103A|[\u1000-\u1021])([\u1039\u103A])', r"\2\3\1")

class MymrUnitable(object) :
    reorder_class = 3
    reorder = 12
    extending = 16
    seqflag = 32
    orders = (( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 9,
                9, 7, 8, 8, 8, 8, 8, 11, 12, 1, 2, 3, 4, 5, 6, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 3, 3,
                6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 5, 0, 7, 8, 10, 12, 12, 12, 12, 12, 12, 12, 0, 12,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 8, 0, 0),
               (0, 0, 0, 0, 0, 8, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 0, 0))
    flags = (   0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                2, 0, 8, 0, 0, 0, 8, 1, 0, 16, 4, 0, 0, 0, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 32, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    seqs = {
        0x1004: [[2, 0xFF, 0x103A, 0x1039]],
        0x101B: [[2, 0xFF, 0x103A, 0x1039]],
        0x105A: [[2, 0xFF, 0x103A, 0x1039]]
    }

    def order(self, num) :
        if 0x1000 <= num < 0x10A0 :
            return self.orders[0][num - 0x1000]
        elif 0xAA60 <= num < 0xAA80 :
            return self.orders[1][num - 0xAA60]
        elif 0xA9E0 <= num < 0xAA00 :
            return self.orders[2][num - 0xA9E0]
        else :
            return 0

    def flag(self, num) :
        if 0x1000 <= num < 0x10A0 :
            return self.flags[num - 0x1000]
        return 0

def get_vals(table, text, index) :
    num = ord(text[index])
    order = table.order(num)
    flags = table.flag(num)
    length = 1
    if flags & table.extending :
        length = 2
    elif flags & table.seqflag :
        for r in table.seqs[num] :
            # we use a generic lookup here
            if r[0] + index > len(text) : 
                continue
            hit = True
            for i in range(r[0]) :
                if ord(text[index + 1 + i]) != r[2 + i] :
                    hit = False
                    break
            if hit :
                length = r[0] + 1
                order = r[1]
    return (order, flags, length)

def cmp_0(a, b):
    return (a > b) - (a < b)

def canon_subsort(table, text, orders, flags, start, end) :
    def canon_cmp(x, y) :
        if orders[x] == orders[y] :
            return cmp_0(x, y)
        else :
            return cmp_0(orders[x], orders[y])

    indices = sorted(range(end - start), key=functools.cmp_to_key(canon_cmp))
    final = len(indices) - 1
    i = 0
    while i < final :
        f = (flags[indices[i]] & table.reorder) >> 2
        if f :
            j = i + 1
            num = ord(text[start + indices[j]])
            if j + 1 <= final and text[start + indices[j]] == '\u1082' and text[start + indices[j+1]] == '\u1060' :
                i = j + 2
                continue
            while j <= final and f & flags[indices[j]] :
                (indices[j-1], indices[j]) = (indices[j], indices[j-1])
                j += 1
            if j > i + 1 and i > 0 :
                i -= 2
        i += 1
    substr = map(lambda x: text[start + x], indices)
    return text[:start] + "".join(substr) + text[end:]

MUMRUT = MymrUnitable()

def canon(text, table=MUMRUT) :
    index = 0
    while index < len(text) :
        (order, f, length) = get_vals(table, text, index)
        if order :
            start = index
            flags = [f] * length
            keys = [order] * length
            index += length
            while index < len(text) and order :
                (order, f, length) = get_vals(table, text, index)
                keys.extend([order] * length)
                flags.extend([f] * length)
                if order : 
                    index += length
            text = canon_subsort(table, text, keys, flags, start, index)
        index += 1
    return text
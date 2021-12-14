rules = '''NS -> H
FS -> O
PO -> C
NV -> N
CK -> B
FK -> N
PS -> C
OF -> F
KK -> F
PP -> S
VS -> K
VB -> V
BP -> P
BB -> K
BF -> C
NN -> V
NO -> F
SV -> C
OK -> N
PH -> P
KV -> B
PN -> O
FN -> V
SK -> V
VC -> K
BH -> P
BO -> S
HS -> H
HK -> S
HC -> S
HF -> B
PC -> C
CF -> B
KN -> H
CS -> N
SP -> O
VH -> N
CC -> K
KP -> N
NP -> C
FO -> H
FV -> N
NC -> F
KB -> N
VP -> O
KO -> F
CP -> F
OH -> F
KC -> H
NB -> F
HO -> P
SC -> N
FF -> B
PB -> H
FB -> K
SN -> B
VO -> K
OO -> N
NF -> B
ON -> P
SF -> H
FP -> H
HV -> B
NH -> B
CO -> C
PV -> P
VV -> K
KS -> P
OS -> S
SB -> P
OC -> N
SO -> K
BS -> B
CH -> V
PK -> F
OB -> P
CN -> N
CB -> N
VF -> O
VN -> K
PF -> P
SH -> H
FH -> N
HP -> P
KF -> V
BK -> H
OP -> C
HH -> F
SS -> V
BN -> C
OV -> F
HB -> P
FC -> C
BV -> H
VK -> S
NK -> K
CV -> K
HN -> K
BC -> K
KH -> P'''

pair_insertions = dict([x.strip().split(" -> ") for x in rules.split("\n")])

import string


template = "CO"
sentence = "COPBCNPOBKCCFFBSVHKO"
s_pairs = [f"{a}{b}" for a, b in zip(sentence, sentence[1:])]
unique_vals = sorted(set(pair_insertions.values()))

print(s_pairs)
result = [0 for _ in range(len(unique_vals))]
offset = [0 for _ in range(len(unique_vals))]

for template in s_pairs:
    start = template
    offset[unique_vals.index(start[1])] += 1
    for step in range(1, 11):
        pairs = zip(template, template[1:])
        template = ""
        for pair in pairs:
            template += pair[0] + pair_insertions[''.join(pair)]
        template += pair[1]
    c = ([template.count(x) for x in unique_vals])
    result = [a+b for a,b in zip(result, c)]
    print(f"Template: {start} -> {c} {sum(c)}", end =" || ")
    b = sorted([template.count(x) for x in string.ascii_uppercase if template.count(x) > 0])
    print(f"Answer: {b[-1]-b[0]}")
offset[unique_vals.index(start[1])] -= 1
result = [a-b for a, b in zip(result, offset)]


print(sorted( 
    [(x, y, z) for x, y, z in zip(unique_vals, result, offset)]
    , key=lambda x: x[1]
))
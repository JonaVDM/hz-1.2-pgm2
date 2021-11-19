#
# wk7ex1c.py - uniekheid controleren  (voor de random-number generator in Hmmm)
#    De functie test(s) staat hier al in (onderaan).
#
# Naam:
#
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
95
8
81
14
7
60
73
46
79
72
25
38
11
44
37
90
3
76
9
2
55
68
41
74
67
20
33
6
39
32
85
98
71
4
97
50
63
36
69
62
15
28
1
34
27
80
93
66
99
92
45
58
31
64
57
10
23
96
29
22
75
88
61
94
87
40
53
26
59
52
5
18
91
24
17
70
83
56
89
82
35
48
21
54
47
0
13
86
19
12
65
78
51
84
77
30
43
16
49
42
"""


def unique(L):
    """
    This should be your uniqueness-tester, written for week 7
    Usually, it uses the recursive pattern:

    if ...      # handle base case
    elif ...    # check whether L[0] re-appears
    else ...    # otherwise...
    """
    if len(L) < 1:
        return True

    u = L[1:]
    if L[0] in u:
        return False

    return unique(u)

def test(s):
    """test accepts a triple-quoted string, s,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if s is empty); otherwise it returns False
    """
    s = s.strip()                 # haal alle spaties aan het begin en eind van s weg
    list_of_strings = s.split()   # splits s op elke spatie en nieuwe regel
    list_of_integers = [int(s) for s in list_of_strings]  # converteer ze allemaal naar ints
    return unique(list_of_integers)


# Uitproberen!
result = test(NUMBERS)
print("\nTest op uniekheid:  Het resultaat is", result)

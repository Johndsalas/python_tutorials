
# cannot use unknown variables with named tuple
# does not work



import collections
from collections import namedtuple

wordlist = [line.strip() for line in open('/usr/share/dict/words')]

word = "some"

alpha_num = namedtuple('alpha_num', 'a b c d e f g h i j k l m n o p q r s t u v w x y z')

alpha_num = alpha_num(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)

for word in wordlist:

    alpha = word[0]

    print(alpha)

    target = alpha_num.alpha

    print(target)
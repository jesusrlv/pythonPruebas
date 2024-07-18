## regular expression ##

import re

my_string = "esta lección es la 7: Exp. reg."
my_string_2 = "SI, esta lección es la 7: Exp. reg."
print(re.match("esta lección es",my_string, re.I))
print(re.match("esta lección es",my_string_2))
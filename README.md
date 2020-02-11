This is a simle python library for counting calculating error.
Starting test.py will start something like command line;
The commands are usual python commands, but you can write (x?y), also possible as (x±y), to make a number
a special number with error, where x is value, and y is error.
There are some extra commands(except usual +; -; /; *;) —
some functions for working with numbers(also possible to work with usual floats):
ln(x); log(x, a); sin(x); cos(x); tg(x); ctg(x); arctg(x).

For example, with "test.py" started you can write

import random \n
x = (5?1) \n
for i in range(10): \n
	v1 = random.random() \n
	v2 = random.random() \n
	x+=(v1?v2) \n
\n
print(ln(x)) \n
#/ answer will be like (2.311793133261718±0.20251518569197163)

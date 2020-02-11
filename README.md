This is a simle python library for counting calculating error.
Starting test.py will start something like command line;
The commands are usual python commands, but you can write (x?y), also possible as (x±y), to make a number
a special number with error, where x is value, and y is error.
There are some extra commands(except usual +; -; /; *;) —
some functions for working with numbers(also possible to work with usual floats):
ln(x); log(x, a); sin(x); cos(x); tg(x); ctg(x); arctg(x).

For example, with "test.py" started you can write

import random
x = (5?1)
for i in range(10):
	v1 = random.random()
	v2 = random.random()
	x+=(v1?v2)

print(ln(x))
\# answer will be like (2.311793133261718±0.20251518569197163)

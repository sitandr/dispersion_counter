from dispersion.dispersed_value import *
import re
NO_SYMPY = False
try:
        import sympy
except:
        print("You have no \"sympy\" library. You can still use the library, but the calculations will be much less accurate.")
        print("If you install it, you will be able yo use command 'eval_with_diff(<some expression, there may be variables (both floats and dispersed values), constants and some functions (but only basic yet, probablly, such opportunity will be added soon)>)'")
        NO_SYMPY = True
def sin(a):
        if type(a) == dispersed_value:
                return a.__sin__()
        else:
                return math.sin(a)


def cos(a):
        if type(a) == dispersed_value:
                return a.__cos__()
        else:
                return math.cos(a)


def tg(a):
        if type(a) == dispersed_value:
                return a.__tg__()
        else:
                return math.tan(a)


def ctg(a):
        if type(a) == dispersed_value:
                return a.__ctg__()
        else:
                return 1 / math.tan(a)


def log(a, b):
        if type(a) == dispersed_value:
                return a.__log__(b)
        else:
                return math.log(a, b)


def ln(a):
        if type(a) == dispersed_value:
                return a.__ln__()
        else:
                return math.log(a)


def arctg(a):
        if type(a) == dispersed_value:
                return a.__arctg__()
        else:
                return math.atan(a)


def console_text(text):
        strings = text.split('\n')

        for i in strings:
                t += i
                if is_not_full(i):
                        t += '\n'
                        continue
                console(t)
                t = ''


def console(string):
        """
        Just input usual python commands. If you want to add a
        value with dispersion, input (x?y) or (x±y)
        """
        last = 0
        string = string.replace('±', '?')
        values = {}
        while True:
                i = string.find('?', last)
                if i == -1:
                        break
                last = i
                j_1 = string.rfind('(', 0, i)
                j_2 = string.rfind(')', i)
                if j_1 != -1 and j_2 != -1:
                        #if NO_SYMPY:
                        string = (string[:j_1] + 'dispersed_value' + string[j_1:i] + ',' + string[i + 1:])
                        #else:
                                #values['x'+str(len(values))] = dispersed_value(eval(string[j_1:i]), eval(string[i + 1:j2]))
                else:
                        print('Syntax Error, please, add brackets to ± value.')
                        return
        # print(string)
        #if not NO_SYMPY:
                
        exec(string, globals())


def console_mode():
        """ Inputted text will be read using 'console' command """
        t = ''
        while True:
                string = input()
                t += string
                if string.strip() == 'exit()':
                        break
                if is_not_full(string):
                        t += '\n'
                        continue
                console(t)
                t = ''


def is_not_full(string):
        return len(string) > 0 and (string.strip()[-1] == ':' or
                                    string[0] == '\t' or
                                    (len(string) >= 4 and string[:4] == '    '))
if not NO_SYMPY:
        from sympy.abc import _clash
        def eval_with_diff(eq):
                var = {}
                i = 0
                while True:
                        s = re.search('\w[\w\d]*', eq[i:])
                        if s == None:
                                break
                        s = s.group(0)
                        ind = eq[i:].index(s)+i
                        ind2 = ind + len(s)
                        i = ind2
                        try:
                                res = eval(s)
                        except NameError:
                                continue
                        if type(res) == dispersed_value:
                                var[s] = res
                        else:
                                eq = eq[:ind] + str(res) + eq[ind2:]
                #print('request:',eq, var)
                return second_executor(eq, var)
                
        def second_executor(eq, var):
                s = 0
                v_var = {i: var[i].value for i in var}
                d_var = {i: var[i].dispersion for i in var}
                
                for v in var:

                        s += (sympy.diff(sympy.sympify(eq, locals = _clash),
                                         (_clash[v] if v in _clash else sympy.Symbol(v))).evalf(subs = v_var)
                              *d_var[v])**2
                
                
                return dispersed_value(sympy.sympify(eq, locals = _clash).evalf(subs = v_var), s**0.5)

if __name__ == '__main__':
        console_mode()

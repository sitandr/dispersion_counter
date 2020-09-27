import math

# TODO: fix self staticmethod; fix add dispersion
from typing import Union

def mean_square(value1, value2):
    return math.sqrt((float(value1) ** 2 + float(value2) ** 2) / 2)

def linear_operation_quadratic_dispersion(dispersion1, dispersion2):
    return mean_square(dispersion1, dispersion2) * math.sqrt(2)

def arithmetic_mean(value1, value2):
    return (value1 + value2) / 2


class dispersed_value:
    value : float = 0
    dispersion : float = 0

    def __init__(self, value, dispersion : Union[int, float] = 0.):
        assert dispersion >= 0

        self.value = float(value)
        self.dispersion = float(dispersion)

    def relative_dispersion(self):
        assert self.dispersion >= 0

        if self.value != 0:
            return self.dispersion / abs(self.value)
        else:
            return 1

    def __add__(self, other):
        return dispersed_value(
            self.value + get_value(other), linear_operation_quadratic_dispersion(self.dispersion, get_dispersion(other))  # self.dispersion + get_dispersion(other)
        )

        # Num_value(self.value + get_value(other), (self.dispersion ** 2 + get_dispersion(other) ** 2) ** 0.5)

    def __radd__(self, other):
        return self.__add__(other)
        # return Num_value(self.value + get_value(other), (self.dispersion ** 2 + get_dispersion(other) ** 2) ** 0.5)

    def __sub__(self, other):
        return dispersed_value(
            self.value - get_value(other), linear_operation_quadratic_dispersion(self.dispersion, get_dispersion(other))  # , self.dispersion + get_dispersion(other)
        )

        # Num_value(self.value - get_value(other), (self.dispersion ** 2 + get_dispersion(other) ** 2) ** 0.5)

    def __rsub__(self, other):
        self.__sub__(other)
        # return Num_value(get_value(other) - self.value, (self.dispersion ** 2 + get_dispersion(other) ** 2) ** 0.5)

    def __mul__(self, other):
        res_value = self.value * get_value(other)
        rel_dispersion = self.relative_dispersion() + get_relative_dispersion(other)

        return dispersed_value(res_value, res_value * rel_dispersion)

    def __rmul__(self, other):
        return self.__mul__(other)
        # v = self.value * Num_value.get_value(other)
        # return Num_value(v,
        #                  v * (self.relative_dispersion() + Num_value.get_relative_dispersion))

    def __truediv__(self, other):
        res_value = self.value / get_value(other)
        rel_dispersion = self.relative_dispersion() + get_relative_dispersion(other)

        return dispersed_value(res_value, res_value * rel_dispersion)

    def __rtruediv__(self, other):
        return self.__truediv__(other)
        # v = Num_value.get_value(other) / self.value
        # return Num_value(v,
        #                  v * (self.relative_dispersion() + Num_value.get_relative_dispersion))

    def __pow__(self, other):
        res_value = self.value ** get_value(other)
        #            return Num_value(res_value,
        #                             res_value*Num_value.get_v(other)*self.w())
        return dispersed_value(res_value,
                               get_value(other) * (self.value ** (get_value(other) - 1)) * self.dispersion)


    def __sin__(self):
        return dispersed_value(math.sin(self.value),
                               math.cos(self.value) * self.dispersion)

    def __cos__(self):
        return dispersed_value(math.cos(self.value),
                               math.sin(self.value) * self.dispersion)

    def __tg__(self):
        return dispersed_value(math.tan(self.value),
                               self.dispersion / math.cos(self.value) ** 2)

    def __ctg__(self):
        return dispersed_value(1 / math.tan(self.value),
                               self.dispersion / math.sin(self.value) ** 2)

    def __ln__(self):
        return dispersed_value(math.log(self.value),
                               self.relative_dispersion())

    def __log__(self, a : Union[float, int]):
        return self.__ln__() / math.log(float(a))

    def __arctg__(self):
        return dispersed_value(math.atan(self.value),
                               self.dispersion / (1 + self.value))
    # Conversion to string
    def __str__(self):
        return '(' + str(self.value) + '±' + str(self.dispersion) + ')'

    def __repr__(self):
        return str(self)



def get_value(obj: Union[dispersed_value, float, int]):
    if type(obj) == dispersed_value:
        return obj.value
    if type(obj) in [float, int]:
        return float(obj)
    else:
        raise TypeError


def get_dispersion(obj : Union[dispersed_value, float, int]):
    if type(obj) == dispersed_value:
        return obj.dispersion
    if type(obj) in [float, int]:
        return 0


def get_relative_dispersion(obj : Union[dispersed_value, float, int]):
    if type(obj) == dispersed_value:
        return obj.relative_dispersion()
    if type(obj) in [float, int]:
        return 0

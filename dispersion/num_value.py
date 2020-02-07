import math

class Num_value:

      def __init__(self, value, dispersion = 0):
            self.value = float(value)
            self.dispersion = float(dispersion)
            
      def __add__(self, other):
            
            return Num_value(self.value + Num_value.get_v(other),
                             (self.dispersion**2+Num_value.get_d(other)**2)**0.5)
      def __radd__(self, other):
            
            return Num_value(self.value + Num_value.get_v(other),
                             (self.dispersion**2+Num_value.get_d(other)**2)**0.5)
      def __sub__(self, other):
            
            return Num_value(self.value - Num_value.get_v(other),
                             (self.dispersion**2+Num_value.get_d(other)**2)**0.5)
      def __rsub__(self, other):
            
            return Num_value( Num_value.get_v(other) - self.value,
                             (self.dispersion**2+Num_value.get_d(other)**2)**0.5)
      def __mul__(self, other):
            v = self.value*Num_value.get_v(other)
            return Num_value(v,
                             v*(self.w()+Num_value.get_w(other)))
      def __rmul__(self, other):
            v = self.value*Num_value.get_v(other)
            return Num_value(v,
                             v*(self.w()+Num_value.get_w(other)))
      def __truediv__(self, other):
            v = self.value/Num_value.get_v(other)
            return Num_value(v,
                             v*(self.w()+Num_value.get_w(other)))
      def __rtruediv__(self, other):
            v = Num_value.get_v(other)/self.value
            return Num_value(v,
                             v*(self.w()+Num_value.get_w(other)))
      def __pow__(self, other):
            v = self.value**Num_value.get_v(other)
#            return Num_value(v,
#                             v*Num_value.get_v(other)*self.w())
            return Num_value(v,
                             Num_value.get_v(other)*
                             (self.value**(Num_value.get_v(other)-1))
                             *self.dispersion)
      def __str__(self):
            return '('+str(self.value)+'±'+str(self.dispersion)+')'
      def __repr__(self):
            return str(self)
      
      def __sin__(self):
            return Num_value(math.sin(self.value),
                             math.cos(self.value)*self.dispersion)
      def __cos__(self):
            return Num_value(math.cos(self.value),
                             math.sin(self.value)*self.dispersion)
      def __tg__(self):
            return Num_value(math.tan(self.value),
                             self.dispersion/math.cos(self.v)**2)
      def __ctg__(self):
            return Num_value(1/math.tan(self.value),
                             self.dispersion/math.sin(self.v)**2)
      def __ln__(self):
            return Num_value(math.log(self.value),
                             self.w())
      def __log__(self, a):
            return self.__ln__()/math.log(a)

      def __arctg__(self):
            return Num_value(math.atan(self.value),
                             self.dispersion/(1+self.value))
      
      def get_v(obj):
            if type(obj) == Num_value:
                  return obj.value
            if type(obj) in [float, int]:
                  return float(obj)
      def get_d(obj):
            if type(obj) == Num_value:
                  return obj.dispersion
            if type(obj) in [float, int]:
                  return 0
      def get_w(obj):
            if type(obj) == Num_value:
                  return obj.w()
            if type(obj) in [float, int]:
                  return 0
      def w(self):
            if self.value !=0 :
                  return self.dispersion/self.value
            else:
                  return 1

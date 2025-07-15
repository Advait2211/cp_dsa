class temp:
    def __init__(self, temp):
        self._temp = temp

    @property
    def celsius(self):
        return self._temp
    
    @celsius.setter
    def celsius(self, val):
        if val < -273.15:
            raise ValueError
        else:
            self._temp = val

    @property
    def fahrenheit(self):
        return (self._temp * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, val):
        raise ValueError
    
    def __str__(self):
        return f"celsius: {self._temp}, fahrenheit: {self.fahrenheit}"
    
t = temp(20)
t.celsius = 25
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

# t.celsius = -300      # ❌ Should raise ValueError
# t.fahrenheit = 100

print(t)


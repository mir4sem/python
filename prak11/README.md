Реализовать конечный автомат Мили в виде класса. Начальным состоянием автомата является A. Методы возвращают числовые значения.

Если вызываемый метод не реализован для некоторого состояния, необходимо вызвать пользовательское исключение MealyError. При возникновении исключения должно передаваться имя метода, вызвавшего это исключение.

Реализовать в отдельной функции test автоматическое тестирование автомата Мили на основе покрытия ветвей. Требуемая степень покрытия: 100%.

![image](https://github.com/mir4sem/python/assets/70198995/fec291c6-f9ff-4c0c-a163-b3e77fd8ecf1)

В примерах ниже функция main возвращает объект созданного класса. Далее последовательно вызываются методы полученного объекта.

Пример 1
```
o = main()
o.scan() # 0
o.scan() # 1
o.scan() # 3
o.scan() # 4
o.scan() # 6
o.erase() # 9
o.erase() # 9
o.get() # 8
o.scan() # 0
o.scan() # 1
o.scan() # 3
o.erase() # 5
```

Пример 2
```
o = main()
o.scan() # 0
o.scan() # 1
o.scan() # 3
o.get() # MealyError
o.scan() # 4
o.scan() # 6
o.erase() # 9
o.get() # 8
o.erase() # MealyError
o.scan() # 0
o.erase() # 2
```

```python
class MealyError(Exception):
    pass
 
 
def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None
 
 
class StateMachine:
    def __init__(self):
        self.state = "A"
 
    def scan(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 1
        elif self.state == "C":
            self.state = "D"
            return 3
        elif self.state == "D":
            self.state = "E"
            return 4
        elif self.state == "E":
            self.state = "F"
            return 6
        elif self.state == "F":
            self.state = "G"
            return 7
        else:
            raise MealyError("scan")
 
    def erase(self):
        if self.state == "B":
            self.state = "G"
            return 2
        elif self.state == "D":
            self.state = "G"
            return 5
        elif self.state == "F":
            self.state = "F"
            return 9
        else:
            raise MealyError("erase")
 
    def get(self):
        if self.state == "F":
            self.state = "A"
            return 8
        else:
            raise MealyError("get")
 
 
def main():
    return StateMachine()
 
 
def test():
    o = main()
    assert o.scan() == 0
    assert o.scan() == 1
    assert o.scan() == 3
    assert o.scan() == 4
    assert o.scan() == 6
    assert o.erase() == 9
    assert o.scan() == 7
 
    o = main()
    o.state = "D"
    assert o.erase() == 5

    o = main()
    o.state = "B"
    assert o.erase() == 2
 
    o = main()
    o.state = "F"
    assert o.get() == 8
 
    o = main()
    raises(lambda: o.get(), MealyError)
    raises(lambda: o.erase(), MealyError)
    o.state = "B"
    raises(lambda: o.get(), MealyError)
    o.state = "C"
    raises(lambda: o.erase(), MealyError)
    raises(lambda: o.get(), MealyError)
    o.state = "D"
    raises(lambda: o.get(), MealyError)
    o.state = "E"
    raises(lambda: o.erase(), MealyError)
    raises(lambda: o.get(), MealyError)
    o.state = "G"
    raises(lambda: o.scan(), MealyError)
    raises(lambda: o.erase(), MealyError)
    raises(lambda: o.get(), MealyError)

```

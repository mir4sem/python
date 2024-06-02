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

### Недостаточное тестовое покрытие ветвей (98.6667%)
```python
class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name

    def __str__(self):
        return f"MealyError: {self.method_name} method called in invalid state"


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def scan(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'A'
            return 0
        else:
            raise MealyError("scan")

    def erase(self):
        if self.state == 'B':
            self.state = 'A'
            return 2
        elif self.state == 'D':
            self.state = 'G'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 9
        elif self.state == 'G':
            self.state = 'G'
            return 9
        else:
            raise MealyError("erase")

    def get(self):
        if self.state == 'D':
            self.state = 'A'
            return 8
        else:
            raise MealyError("get")


def main():
    return MealyMachine()


def test_scan():
    o = main()
    assert o.scan() == 0  # A -> B
    assert o.scan() == 1  # B -> C
    assert o.scan() == 3  # C -> D
    assert o.scan() == 4  # D -> E
    assert o.scan() == 6  # E -> F
    assert o.scan() == 7  # F -> G
    assert o.scan() == 0  # G -> A


def test_erase():
    o = main()
    try:
        o.erase()  # A -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: erase method called in invalid state"
    assert o.scan() == 0  # A -> B
    assert o.erase() == 2  # B -> A
    assert o.scan() == 0  # A -> B
    assert o.scan() == 1  # B -> C
    assert o.scan() == 3  # C -> D
    assert o.erase() == 5  # D -> G
    assert o.scan() == 0  # G -> A
    assert o.scan() == 0  # A -> B
    assert o.scan() == 1  # B -> C
    assert o.scan() == 3  # C -> D
    assert o.scan() == 4  # D -> E
    assert o.scan() == 6  # E -> F
    assert o.erase() == 9  # F -> G
    assert o.erase() == 9  # G -> G


def test_get():
    o = main()
    try:
        o.get()  # A -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.scan() == 0  # A -> B
    try:
        o.get()  # B -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.scan() == 1  # B -> C
    try:
        o.get()  # C -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.scan() == 3  # C -> D
    assert o.get() == 8  # D -> A
    try:
        o.get()  # A -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.scan() == 0  # A -> B
    assert o.scan() == 1  # B -> C
    assert o.scan() == 3  # C -> D
    assert o.scan() == 4  # D -> E
    try:
        o.get()  # E -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.scan() == 6  # E -> F
    try:
        o.get()  # F -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"
    assert o.erase() == 9  # F -> G
    try:
        o.get()  # G -> MealyError
    except MealyError as e:
        assert str(e) == "MealyError: get method called in invalid state"


def test():
    test_scan()
    test_erase()
    test_get()


test()

```

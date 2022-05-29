from app.calculator import Calculator

class TestCalc:
    def setup(self):                      # подключение тестируемого калькулятора
        self.calc = Calculator

    def test_multiply_pass(self):         # тест на правильность функции
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_pass(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_pass(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding_pass(self):
        assert self.calc.adding(self, 4, 2) == 6

def multiply(x, y):             # функция которую тестируем
    return x * y

def test_multiply_pass():       # тест на корректность
    assert multiply(2, 2) == 4

def division(x, y):             # функция которую тестируем
    return x / y

def test_division_pass():
    assert division(4, 2) == 2

def subtraction(x, y):           # функция которую тестируем
    return x - y

def test_subtraction_pass():
    assert subtraction(4, 2) == 2

def adding(x, y):                # функция которую тестируем
    return x + y

def test_adding_pass():
    assert adding(4, 2) == 6

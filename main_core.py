import math

class CalcCore:
    def __init__(self):
        self.functions = {
            'sqrt': math.sqrt,
            'cbrt': lambda x: x**(1/3)
        }

    def calculate(self, expression):
        try:
            if not self.validate_expression(expression):
                return "Ошибка: Некорректное выражение"

            expression = self.process_functions(expression)
            return eval(expression)
        except Exception as e:
            return f"Ошибка: {e}"

    def process_functions(self, expression):
        for func_name, func in self.functions.items():
            while f'{func_name}(' in expression:
                start = expression.find(f'{func_name}(') + len(f'{func_name}(')
                end = expression.find(')', start)
                num = float(expression[start:end])
                expression = expression.replace(f'{func_name}({num})', str(func(num)))
        return expression

    def validate_expression(self, expression):
        return all(c.isdigit() or c in "+-*/. ()" for c in expression)

class Calculator:
    # Class attribute (خاص بالكلاس كله)
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not depend on class or instance data"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Has access to class attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

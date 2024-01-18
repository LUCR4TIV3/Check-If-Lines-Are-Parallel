
class Line:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def set_variable(self, variable_name) -> None:
        setattr(self, variable_name, self._get_input_from_user(variable_name))

    def get_slope(self) -> int:
        return self.a / self.b

    def _sign(self) -> int:
        return '+' if self.b >= 0 else ''

    def __repr__(self):
        return f"{self.a}x{self._sign()}{self.b}y={self.c}"

    def __str__(self):
        return f"{self.a}x{self._sign()}{self.b}y={self.c}"

    def __eq__(self, other):
        return isinstance(other, Line) or self.a == other.a and self.b == other.b and self.c == other.c

    def _get_input_from_user(self, coefficient: str) -> int:
        try:
            val = int(input(
                f"What's your {coefficient} coefficient, in the line, with the form ax+by=c: "))
            return val
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return self.get_input_from_user()


class ParallelLinesChecker:
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def is_parallel(self) -> bool:
        if self.line1 == self.line2:
            print(
                f"The lines {self.line1} and {self.line2} are parallel to themselves.")
        else:
            try:
                slope = self.line1.get_slope()
                slope2 = self.line2.get_slope()
            except ZeroDivisionError:
                if self.line1.b == 0 or self.line2.b == 0:
                    print("The line is vertical, and the slope is undefined.")
            return slope == slope2


if __name__ == '__main__':
    line1 = Line()
    line2 = Line()

    line1.set_variable("a")
    line1.set_variable("b")
    line1.set_variable("c")

    print(f"Line 1: {line1} \n")

    line2.set_variable("a")
    line2.set_variable("b")
    line2.set_variable("c")

    print(f"Line 2: {line2} \n")

    parallel_line_checker = ParallelLinesChecker(line1, line2)

    if parallel_line_checker.is_parallel():
        print(
            f"The lines {line1} and {line2} are parallel to each other.")
    else:
        print(
            f"The lines {line1} and {line2} are not parallel to each other.")

from enum import Enum


class Color(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    END = "\033[0m"

    BLUE = "\033[34m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    GRAY = "\033[90m"

    @staticmethod
    def colorize_feedback(feedback: str) -> str:
        """Colorize feedback string,
        where C is green,
        c is yellow,
        and - is red"""
        colored = ""
        for char in feedback:
            if char == "C":
                colored += f"{Color.GREEN.value}{char}{Color.END.value}"
            elif char == "c":
                colored += f"{Color.YELLOW.value}{char}{Color.END.value}"
            elif char == "-":
                colored += f"{Color.RED.value}{char}{Color.END.value}"
        return colored

    @staticmethod
    def _color_result(result: str) -> str:
        """Colorize game result,
        either victory or defeat"""
        return (
            f"{Color.GREEN.value}Victory{Color.END.value}"
            if result
            else f"{Color.RED.value}Defeat{Color.END.value}"
        )

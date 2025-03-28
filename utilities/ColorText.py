from enum import Enum
class Color(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    END = "\033[0m"

    BLUE = "\033[34m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


    @staticmethod
    def _colorize_feedback(feedback: str):
        """Colorize feedback string"""
        colored = ""
        for char in feedback:
            if char == "C":
                colored += f"{Color.GREEN.value}{char}{Color.END.value}"
            elif char == "c":
                colored += f"{Color.YELLOW.value}{char}{Color.END.value}"
            elif char == "-":
                colored += f"{Color.RED.value}{char}{Color.END.value}"
        return colored
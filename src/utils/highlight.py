def highlight_text(text: str) -> str:
    return f"\033[30;47m {text} \033[0m"

def highlight_warning(text: str) -> str:
    return f"\033[30;43m {text} \033[0m"

def highlight_error(text: str) -> str:
    return f"\033[37;41m {text} \033[0m"
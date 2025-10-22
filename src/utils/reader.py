def reader(path: str) -> str:
    with open(path, "rt", encoding="utf-8") as file:
        return file.read()
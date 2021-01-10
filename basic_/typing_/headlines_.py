def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(79, '#')


print(headline("python type checking"))

print(headline("python type checking", align=False))
# print(headline("python type checking", align="center"))

### doing type checking using pycharm or Mypy

## install

# pip3 install mypy

## run type checking

# mypy headlines_.py


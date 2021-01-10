import parse

def parse_name(text: str) -> str:
    patterns = (
        "my name is {name}",
        "i'm {name}",
        "i am {name}",
        "call me {name}",
        "{name}",
    )
    for pattern in patterns:
        result = parse.parse(pattern, text)
        if result:
            return result
            # return result['name']
    return ""

answer = input("What is your name? ")
name = parse_name(answer)
print(f"Hi {name}, nice to meet you!")


'''
# The error in line 14 will not checked by mypy, you can try:
mypy parse_name.py --ignore-missing-imports
    
# or a better work around(known as stub):
mkdir -p /home/$USER/python/stubs/
cat <<EOF > /home/$USER/python/stubs/parse.pyi
# parse.pyi

from typing import Any, Mapping, Optional, Sequence, Tuple, Union

class Result:
    def __init__(
        self,
        fixed: Sequence[str],
        named: Mapping[str, str],
        spans: Mapping[int, Tuple[int, int]],
    ) -> None: ...
    def __getitem__(self, item: Union[int, str]) -> str: ...
    def __repr__(self) -> str: ...

def parse(
    format: str,
    string: str,
    evaluate_result: bool = ...,
    case_sensitive: bool = ...,
) -> Optional[Result]: ...
EOF

export MYPYPATH=/home/$USER/python/stubs/ 
mypy parse_name.py

or even more better way:
- Typeshed
- Other Static Type Checkers
'''
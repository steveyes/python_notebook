from typing import Callable


def feeder(get_next_item: Callable[[], str]) -> None:
    ...


def async_query(
        on_success: Callable[[int], None],
        on_error: Callable[[int, Exception], None],
) -> None: ...


from typing import Callable


def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))


def create_greeting(name: str) -> str:
    return f"Hello {name}"


do_twice(create_greeting, "Jekyll")


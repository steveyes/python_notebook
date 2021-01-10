from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> str:
    ...


# typechecks
user_a = get_user_name(UserId(524313))

# does not typecheck; an int is not a UserId
user_b = get_user_name(-1)

# You may still perform all int operations on a variable of type UserId,
# but the result will always be of type int.
# This lets you pass in a UserId wherever an int might be expected,
# but will prevent you from accidentally creating a UserId in an invalid way:
output = UserId(23413) + UserId(54341)


# derived UserId
ProUserId = NewType('ProUserId', UserId)
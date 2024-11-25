from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportInt(Protocol):
    def __int__(self) -> int:
        pass

def convert_to_int(value: SupportInt) -> int:
    if not isinstance(value, SupportInt):
        raise TypeError(f"{value!r} cannot be converted to an integer")
    return int(value)

if __name__ == "__main__":
    print(convert_to_int(1.5))
    print(convert_to_int([]))
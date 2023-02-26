from enum import Enum
from typing import Any, List, Optional, Type, TypeVar

_T = TypeVar('_T')

class EnumBase(Enum):
    @classmethod
    def values(cls) -> Any:
        return [x.value for x in enum_class] # type: ignore
    
    @classmethod
    def parse(cls, value: str) -> _T:
        parsed: Optional[_T] = cls.safe_parse(value)

        if parsed is None:
            raise ValueError(
                f"Invalid value of '{value}'. Values must be a valid member of the enum: {cls.__name__}"
            )

        return parsed

    @classmethod
    def safe_parse(cls, value: str) -> Optional[_T]:
        try:
            return cls[value]
        except KeyError:
            pass

        parsed: Optional[_T] = cls.safe_parse_by_value(value)

        return parsed
    
    @classmethod
    def safe_parse_by_value(cls, value: Any) -> Optional[_T]:
        values = cls.values()

        if matched := [x for x in values if str(x).upper() == str(value).upper()]:
            return cls(matched[0])

        return None

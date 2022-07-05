from typing import Dict, List
from System import Array, Object
from System.Collections.Generic import Dictionary, KeyValuePair


class Converter:
    @staticmethod
    def to_dotnet__dictionary__str_to_str(source: Dict[str, str]) -> Dictionary[str, str]:
        return Dictionary[str, str](
            Converter.to_dotnet__list__kvp_str_str([KeyValuePair[str, str](key, value) for key, value in source.items()])
        )

    @staticmethod
    def to_dotnet__list__str(source: List[str]) -> Array[str]:
        return Array[str](source)

    @staticmethod
    def to_dotnet__list__kvp_str_str(source: List[KeyValuePair[str, str]]) -> Array[str]:
        return Array[KeyValuePair[str, str]](source)

    @staticmethod
    def to_python__dictionary__str_object(source: Dictionary[str, Object]) -> Dict[str, object]:
        return {pair.Key: pair.Value for pair in source}

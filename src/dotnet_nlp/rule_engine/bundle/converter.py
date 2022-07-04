from typing import Dict, List
from System import Array
from System.Collections.Generic import Dictionary, KeyValuePair


class Converter:
    @staticmethod
    def convert_dictionary__str_to_str(source: Dict[str, str]) -> Dictionary[str, str]:
        return Dictionary[str, str](
            Converter.convert_list__kvp_str_str([KeyValuePair[str, str](key, value) for key, value in source.items()])
        )

    @staticmethod
    def convert_list__str(source: List[str]) -> Array[str]:
        return Array[str](source)

    @staticmethod
    def convert_list__kvp_str_str(source: List[KeyValuePair[str, str]]) -> Array[str]:
        return Array[KeyValuePair[str, str]](source)

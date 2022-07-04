def initialize_pythonnet():
    import sys
    import os
    import dotnet_nlp.rule_engine.bundle

    package_root = os.path.dirname(os.path.dirname(dotnet_nlp.rule_engine.bundle.__file__))

    sys.path.append(os.path.join(package_root, "dlls"))

    from clr_loader import get_coreclr
    from pythonnet import set_runtime
    set_runtime(get_coreclr(os.path.join(package_root, "runtimeconfig.json")))


def load_rule_engine():
    import clr
    clr.AddReference("DotnetNlp.RuleEngine.Core")
    clr.AddReference("DotnetNlp.RuleEngine.Mechanics.Peg")
    clr.AddReference("DotnetNlp.RuleEngine.Mechanics.Regex")
    clr.AddReference("DotnetNlp.RuleEngine.Bundle")


def initialize_and_load():
    initialize_pythonnet()
    load_rule_engine()


def convert_dictionaries(dictionary: dict):
    from System.Collections.Generic import Dictionary, KeyValuePair

    return Dictionary[str, str]([KeyValuePair[str, str](key, value) for key, value in dictionary.items()])

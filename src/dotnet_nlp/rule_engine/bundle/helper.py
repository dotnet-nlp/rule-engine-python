def initialize_pythonnet():
    import sys
    sys.path.append("dlls")

    from clr_loader import get_coreclr
    from pythonnet import set_runtime
    set_runtime(get_coreclr("runtimeconfig.json"))


def load_dotnet_library():
    import clr
    clr.AddReference("DotnetNlp.RuleEngine.Core")
    clr.AddReference("DotnetNlp.RuleEngine.Mechanics.Peg")
    clr.AddReference("DotnetNlp.RuleEngine.Mechanics.Regex")


def initialize_and_load():
    initialize_pythonnet()
    load_dotnet_library()

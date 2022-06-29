import sys
import os

sys.path.append('/opt/release')

from clr_loader import get_coreclr
from pythonnet import set_runtime

rt = get_coreclr("/opt/runtimeconfig.json")
set_runtime(rt)

import clr

clr.AddReference("System.Runtime")
clr.AddReference("DotnetNlp.RuleEngine.Core")
from DotnetNlp.RuleEngine.Core import RuleSpaceFactory, MechanicsBundle

print(list(AppDomain.CurrentDomain.GetAssemblies()))
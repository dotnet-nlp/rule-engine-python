from typing import Optional, Dict
from DotnetNlp.RuleEngine.Core.Evaluation.Cache import IRuleSpaceCache
import DotnetNlp.RuleEngine.Core.Evaluation.Rule
from DotnetNlp.RuleEngine.Core.Evaluation.Rule import IRuleMatcher
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Projection.Arguments import RuleArguments
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Result import RuleMatchResultCollection
from DotnetNlp.RuleEngine.Bundle import Factory


class RuleSpaceWrapper(Dict[str, IRuleMatcher]):
    def __init__(self, rule_sets: Dict[str, str], rules: Dict[str, str]):
        super().__init__({pair.Key: pair.Value for pair in Factory.Create(ruleSets=rule_sets, rules=rules)})

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        self.__setitem__(name, value)


class RuleMatcherWrapper():
    def __init__(self, source: IRuleMatcher):
        self.source = source

    def has_match(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasMatch(phrase.split(' '), first_symbol_index, rule_arguments, cache)

    def has_any_match(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasAnyMatch(phrase.split(' '), first_symbol_index, rule_arguments, cache)

    def match_and_project(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProject(phrase.split(' '), first_symbol_index, rule_arguments, cache)

    def match_and_project_all(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProjectAll(phrase.split(' '), first_symbol_index, rule_arguments, cache)

from typing import Optional, List, Dict
from DotnetNlp.RuleEngine.Core.Evaluation.Cache import IRuleSpaceCache
import DotnetNlp.RuleEngine.Core.Evaluation.Rule
from DotnetNlp.RuleEngine.Core.Evaluation.Rule import IRuleMatcher
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Input import RuleInput
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Projection.Arguments import RuleArguments
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Result import RuleMatchResultCollection
from DotnetNlp.RuleEngine.Bundle import Factory


class RuleSpaceWrapper(Dict[str, IRuleMatcher]):
    def __init__(self, rule_sets: List[str], rules: List[str]):
        # self.rule_space =
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
            first_symbol_index: int,
            rule_arguments: RuleArguments,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasMatch(RuleInput(phrase.split(' ')), first_symbol_index, rule_arguments, cache)

    def has_any_match(
            self,
            phrase: str,
            first_symbol_index: int,
            rule_arguments: RuleArguments,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasAnyMatch(RuleInput(phrase.split(' ')), first_symbol_index, rule_arguments, cache)

    def match_and_project(
            self,
            phrase: str,
            first_symbol_index: int,
            rule_arguments: RuleArguments,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProject(RuleInput(phrase.split(' ')), first_symbol_index, rule_arguments, cache)

    def match_and_project_all(
            self,
            phrase: str,
            first_symbol_index: int,
            rule_arguments: RuleArguments,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProjectAll(RuleInput(phrase.split(' ')), first_symbol_index, rule_arguments, cache)

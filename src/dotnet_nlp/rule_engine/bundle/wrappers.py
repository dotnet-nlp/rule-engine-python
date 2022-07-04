from typing import Optional, Dict
from DotnetNlp.RuleEngine.Core.Evaluation.Cache import IRuleSpaceCache
import DotnetNlp.RuleEngine.Core.Evaluation.Rule
from DotnetNlp.RuleEngine.Core.Evaluation.Rule import IRuleMatcher
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Projection.Arguments import RuleArguments
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Result import RuleMatchResultCollection
from DotnetNlp.RuleEngine.Bundle import Factory
from dotnet_nlp.rule_engine.bundle.converter import Converter
from dotnet_nlp.rule_engine.bundle.wrappers import RuleMatcherWrapper


class RuleSpaceWrapper(Dict[str, RuleMatcherWrapper]):
    def __init__(self, rule_sets: Dict[str, str], rules: Dict[str, str]):
        def create():
            return Factory.Create(
                ruleSets=Converter.convert_dictionary__str_to_str(rule_sets),
                rules=Converter.convert_dictionary__str_to_str(rules)
            )
        super().__init__({pair.Key: RuleMatcherWrapper(pair.Value) for pair in create()})


class RuleMatcherWrapper:
    def __init__(self, source: IRuleMatcher):
        self.source = source

    def has_match(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasMatch(
            Converter.convert_list__str(phrase.split(' ')),
            first_symbol_index,
            rule_arguments,
            cache
        )

    def has_any_match(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.HasAnyMatch(
            Converter.convert_list__str(phrase.split(' ')),
            first_symbol_index,
            rule_arguments,
            cache
        )

    def match_and_project(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProject(
            Converter.convert_list__str(phrase.split(' ')),
            first_symbol_index,
            rule_arguments,
            cache
        )

    def match_and_project_all(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollection:
        return self.source.MatchAndProjectAll(
            Converter.convert_list__str(phrase.split(' ')),
            first_symbol_index,
            rule_arguments,
            cache
        )

from typing import Optional, Dict, Set
from DotnetNlp.RuleEngine.Core.Evaluation.Cache import IRuleSpaceCache
from DotnetNlp.RuleEngine.Core.Evaluation.Rule import IRuleMatcher
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Projection.Arguments import RuleArguments
from DotnetNlp.RuleEngine.Core.Evaluation.Rule.Result import RuleMatchResult, RuleMatchResultCollection
from DotnetNlp.RuleEngine.Bundle import Factory, Strategy
from dotnet_nlp.rule_engine.bundle.converter import Converter


class RuleMatchResultWrapper:
    def __init__(self, rule_match_result: RuleMatchResult):
        self.source = ' '.join([symbol for symbol in rule_match_result.Source])
        self.first_used_symbol_index = rule_match_result.FirstUsedSymbolIndex
        self.last_used_symbol_index = rule_match_result.LastUsedSymbolIndex
        self.captured_variables = Converter.to_python__dictionary__str_object(rule_match_result.CapturedVariables) if rule_match_result.CapturedVariables is not None else None
        self.explicitly_matched_symbols_count = rule_match_result.ExplicitlyMatchedSymbolsCount
        self.marker = rule_match_result.Marker
        self.lazy_result = rule_match_result.Result

    def get_result(self):
        return self.lazy_result.Value


class RuleMatchResultCollectionWrapper(Set[RuleMatchResultWrapper]):
    def __init__(self, rule_match_result_collection: RuleMatchResultCollection):
        super().__init__({RuleMatchResultWrapper(rule_match) for rule_match in rule_match_result_collection})
        self.best = RuleMatchResultWrapper(rule_match_result_collection.Best(Strategy.Default))


class RuleMatcherWrapper:
    def __init__(self, source: IRuleMatcher):
        self.source = source

    def has_match(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> bool:
        return self.source.HasMatch(
            Converter.to_dotnet__list__str(phrase.split(' ')),
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
    ) -> bool:
        return self.source.HasAnyMatch(
            Converter.to_dotnet__list__str(phrase.split(' ')),
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
    ) -> RuleMatchResultCollectionWrapper:
        return RuleMatchResultCollectionWrapper(
            self.source.MatchAndProject(
                Converter.to_dotnet__list__str(phrase.split(' ')),
                first_symbol_index,
                rule_arguments,
                cache
            )
        )

    def match_and_project_all(
            self,
            phrase: str,
            first_symbol_index: int = 0,
            rule_arguments: Optional[RuleArguments] = None,
            cache: Optional[IRuleSpaceCache] = None
    ) -> RuleMatchResultCollectionWrapper:
        return RuleMatchResultCollectionWrapper(
            self.source.MatchAndProjectAll(
                Converter.to_dotnet__list__str(phrase.split(' ')),
                first_symbol_index,
                rule_arguments,
                cache
            )
        )


class RuleSpaceWrapper(Dict[str, RuleMatcherWrapper]):
    def __init__(self, rule_sets: Dict[str, str], rules: Dict[str, str]):
        def create():
            return Factory.Create(
                ruleSets=Converter.to_dotnet__dictionary__str_to_str(rule_sets),
                rules=Converter.to_dotnet__dictionary__str_to_str(rules)
            )

        super().__init__({pair.Key: RuleMatcherWrapper(pair.Value) for pair in create()})

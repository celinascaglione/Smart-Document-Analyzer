from extractors.extractor_factory import ExtractorFactory
from extractors.regex_extractor import RegexExtractor


def test_factory_returns_regex_extractor():
    extractor = ExtractorFactory.create("regex")

    assert isinstance(extractor, RegexExtractor)


def test_factory_rejects_invalid_extractor():
    try:
        ExtractorFactory.create("invalid")
        assert False
    except ValueError:
        assert True
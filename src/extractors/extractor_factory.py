from extractors.regex_extractor import RegexExtractor
from extractors.openai_extractor import OpenAIExtractor


class ExtractorFactory:

    @staticmethod
    def create(extraction_mode):

        if extraction_mode == "regex":
            return RegexExtractor()

        if extraction_mode == "openai":
            return OpenAIExtractor()

        raise ValueError(
            f"Unsupported extraction mode: {extraction_mode}"
        )
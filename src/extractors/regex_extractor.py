from analyzer import extract_metadata_from_text
from extractors.base_extractor import BaseExtractor


class RegexExtractor(BaseExtractor):

    def extract(self, text):
        return extract_metadata_from_text(text)
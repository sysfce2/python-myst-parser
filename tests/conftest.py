import pytest
from docutils.nodes import Element


@pytest.fixture(scope="function", autouse=True)
def patch_pformat(monkeypatch):
    """In sphinx v7.1 `translation_progress` was added to doctree elements,
    and `translated` was added to paragraphs etc.
    This patch allows the current tests to pass,
    put should perhaps be removed at a later date.
    """

    def _pformat(self, indent="    ", level=0):
        self.attributes.pop("translation_progress", None)
        self.attributes.pop("translated", None)
        tagline = f"{indent * level}{self.starttag()}\n"
        childreps = (c.pformat(indent, level + 1) for c in self.children)
        return "".join((tagline, *childreps))

    monkeypatch.setattr(Element, "pformat", _pformat)

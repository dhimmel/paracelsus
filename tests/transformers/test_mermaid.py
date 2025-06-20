from paracelsus.transformers.mermaid import Mermaid

from ..utils import mermaid_assert


def test_mermaid(metaclass):
    mermaid = Mermaid(metaclass=metaclass, column_sort="key-based")
    graph_string = str(mermaid)
    mermaid_assert(graph_string)


def test_mermaid_column_sort_preserve_order(metaclass, mermaid_full_string_preseve_column_sort):
    mermaid = Mermaid(metaclass=metaclass, column_sort="preserve-order")
    assert str(mermaid) == mermaid_full_string_preseve_column_sort


def test_mermaid_keep_comments(metaclass):
    mermaid = Mermaid(metaclass=metaclass, column_sort="key-based", omit_comments=False)
    assert "True if post is published" in str(mermaid)


def test_mermaid_omit_comments(metaclass):
    mermaid = Mermaid(metaclass=metaclass, column_sort="key-based", omit_comments=True)
    assert "True if post is published" not in str(mermaid)

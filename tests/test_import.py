"""Test helpgen."""

import helpgen


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(helpgen.__name__, str)

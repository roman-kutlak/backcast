import unittest
from unittest import mock

import backcast.main


class TestMain(unittest.TestCase):
    """Test that `main` runs and all packages/modules load."""

    def test_communicate(self):
        """Run the `communicate` function and mock the rest."""
        app = backcast.main.BackCast()
        app.lexicaliser = mock.MagicMock()
        app.aggregator = mock.MagicMock()
        app.realiser = mock.MagicMock()
        app.communicate(mock.MagicMock())
        app.lexicaliser.assert_called()

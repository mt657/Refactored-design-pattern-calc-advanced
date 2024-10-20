"""Configuration file for pytest fixtures."""

from io import StringIO
from unittest.mock import patch
import pytest
from app.main import calculator

@pytest.fixture
def calculator_input_output():
    """Fixture to capture calculator input and output."""
    def _calculator_input_output(user_input):
        with patch("builtins.input", side_effect=[user_input, "exit"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            calculator()  # Call the calculator function
        return mock_stdout.getvalue()  # Capture the output

    return _calculator_input_output

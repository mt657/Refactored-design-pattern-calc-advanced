# pylint: disable=redefined-outer-name
"""Unit tests for the SingletonCalculator."""

import pytest
from app.operations.operation_factory import OperationFactory
from app.calculator.calculator_singleton import SingletonCalculator

@pytest.fixture(scope='function')
def singleton_calculator():
    """Fixture to provide a SingletonCalculator instance."""
    calc = SingletonCalculator()
    yield calc
    # Clear history after each test
    calc.get_history().clear()  # Clear the history using the main.py method

@pytest.mark.parametrize("operation_str, a, b, expected_result", [
    ("add", 1, 2, 3),
    ("subtract", 5, 3, 2),
    ("multiply", 2, 4, 8),
    ("divide", 8, 2, 4),
])
def test_perform_operation(singleton_calculator, operation_str, a, b, expected_result):
    """Test performing a calculation and checking if history is updated."""
    operation = OperationFactory.create_operation(operation_str)
    result = singleton_calculator.perform_operation(operation, a, b)  # Perform operation
    history = singleton_calculator.get_history()  # Retrieve history

    assert result == expected_result, (
        f"The result of {operation_str} should be {expected_result}."
    )
    assert len(history) == 1, "History should contain one calculation."

    # Ensure we compare the operation type correctly
    assert (
        history[0].operation.__class__.__name__.lower() ==
        operation.__class__.__name__.lower()
    ), "History should contain the correct operation."

def test_get_history(singleton_calculator):
    """Test getting the history of calculations."""
    operation = OperationFactory.create_operation('multiply')
    singleton_calculator.perform_operation(operation, 4, 2)  # Perform multiplication
    history = singleton_calculator.get_history()  # Retrieve history

    assert len(history) == 1, (
        "History should contain one calculation after performing an operation."
    )

def test_clear_history(singleton_calculator):
    """Test that the history can be cleared."""
    operation = OperationFactory.create_operation('divide')
    singleton_calculator.perform_operation(operation, 10, 2)  # Perform division
    assert len(singleton_calculator.get_history()) == 1, (
        "History should contain one calculation before clearing."
    )

    # Simulate user input to clear history as per main.py logic
    user_input = 'clear'
    if user_input.lower() == "clear":
        history = singleton_calculator.get_history()
        history.clear()  # Clear the history using the main.py method

    assert len(singleton_calculator.get_history()) == 0, (
        "History should be empty after clearing."
    )

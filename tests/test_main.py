"""Unit tests for the calculator operations."""

import pytest
from app.operations.calculation import Calculation
from app.operations.operation_factory import OperationFactory  # Assuming you have this factory

@pytest.mark.parametrize("operation_str, num1, num2, expected_result", [
    ("add", 5, 3, 8.0),          # Valid addition
    ("subtract", 10, 4, 6.0),    # Valid subtraction
    ("multiply", 2, 3, 6.0),     # Valid multiplication
    ("divide", 10, 2, 5.0),      # Valid division
])
def test_valid_operations(operation_str, num1, num2, expected_result, calculator_input_output):
    """Test valid calculator operations."""
    user_input = f"{operation_str} {num1} {num2}"
    output = calculator_input_output(user_input)  # Use the fixture to call calculator

    # Check the output
    assert f"Result: {expected_result}" in output

    # Test __repr__ coverage for Calculation class
    operation = OperationFactory.create_operation(operation_str)  # Fixed method call
    calculation = Calculation(operation=operation, operand1=num1, operand2=num2)

    # Updated representation check to match the current implementation
    assert repr(calculation) == (
        f"Calculation({num1}, {operation.__class__.__name__.lower()}, {num2})"
    )

@pytest.mark.parametrize("operation_str, num1, num2", [
    ("divide", 10, 0),          # Division by zero
    ("unknown", 1, 1),          # Unknown operation
])
def test_invalid_operations(operation_str, num1, num2, calculator_input_output):
    """Test invalid calculator operations."""
    user_input = f"{operation_str} {num1} {num2}"
    output = calculator_input_output(user_input)  # Use the fixture to call calculator

    # Check the output for unknown operation
    if operation_str == "divide":
        assert "Invalid input. Please enter a valid operation and two numbers." in output
    else:
        assert f"Unknown operation '{operation_str}'." in output

@pytest.mark.parametrize("user_command, expected_output", [
    ("help", "Available commands:"),
    ("list", "No calculations in history."),
    ("clear", "History cleared."),
])
def test_commands(user_command, expected_output, calculator_input_output):
    """Test commands for the calculator."""
    user_input = f"{user_command}"
    output = calculator_input_output(user_input)  # Use the fixture to call calculator

    # Check if the expected output is in the output
    assert expected_output in output

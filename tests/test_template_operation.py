"""Unit tests for TemplateOperation and its concrete implementations."""

import pytest
from app.operations.template_operation import TemplateOperation

# Define a concrete subclass for testing purposes
class ConcreteOperation(TemplateOperation):
    """Concrete implementation of TemplateOperation for testing purposes."""

    def execute(self, a: float, b: float) -> float:
        """Perform addition on two numbers."""
        return a + b  # Simple implementation for testing

def test_validate_inputs():
    """Test that validate_inputs raises ValueError for invalid inputs."""
    operation = ConcreteOperation()  # Instantiate the concrete class to test validate_inputs
    with pytest.raises(ValueError):
        operation.validate_inputs(1, "a")  # Invalid input
    with pytest.raises(ValueError):
        operation.validate_inputs("b", 2)  # Invalid input

def test_log_result(caplog):
    """Test that log_result logs the expected message."""
    operation = ConcreteOperation()  # Instantiate the concrete class to test log_result
    operation.log_result(2, 3, 5)  # Call log_result with sample values
    assert (
        "Operation performed: 2 and 3 -> Result: 5"
        in caplog.text
    ), "Log message is incorrect."  # Add an assertion message for clarity

def test_concrete_operation_execute():
    """Test that the concrete implementation of execute works as expected."""
    operation = ConcreteOperation()
    result = operation.execute(3, 4)
    assert result == 7  # Confirm that the result of the addition is correct

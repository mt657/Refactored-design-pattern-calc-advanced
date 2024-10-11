# Welcome to the Ultimate OOP Masterclass with Design Patterns, Logging, and Debugging!
# In this program, we will learn about Object-Oriented Programming (OOP), design patterns, and the importance of logging and debugging.
# Logging helps us track what happens in our program, while debugging helps us find and fix errors when things go wrong.
# Let’s dive in and explain everything step-by-step with detailed comments!

import logging  # Importing Python's built-in logging module for logging events.
import pdb  # Importing Python's built-in debugger for debugging.
from abc import ABC, abstractmethod  # This allows us to create abstract classes and methods.
from dataclasses import dataclass  # Dataclasses make it easy to store structured data.
from typing import List  # We use List to tell Python when we are working with lists (like a list of calculations).

# ------------------------------------------------------------------------------
# SETUP LOGGING
# ------------------------------------------------------------------------------

# First, we set up logging so that we can record what happens in our program.
# Logging is a way to record messages while the program is running. These messages can help us understand what the program is doing.
# We will log important events (like operations being performed or errors happening) to a file called `calculator.log`.

logging.basicConfig(
    filename='calculator.log',  # This is the file where logs will be saved.
    level=logging.DEBUG,  # We are setting the logging level to DEBUG, which means we will capture detailed logs.
    format='%(asctime)s - %(levelname)s - %(message)s'  # This defines the format of our log messages.
)

# ------------------------------------------------------------------------------
# PART 1: OPERATION CLASSES (Command and Template Method Patterns with Logging)
# ------------------------------------------------------------------------------

# Let's start by creating **Operation** classes using the **Command Pattern** and **Template Method Pattern**.
# A command is like an instruction (e.g., "Add these two numbers"). We want each operation (like addition or subtraction)
# to be treated as a command that the calculator can "execute."

# We'll also use the **Template Method Pattern** here. This allows us to define a "template" or structure for how all
# operations are performed (e.g., validate inputs, perform operation, log result). Each specific operation 
# (like addition or subtraction) will just fill in the details for the calculation part.

class TemplateOperation(ABC):
    """Abstract class representing a mathematical operation using the Template Method pattern."""
    
    # This method defines the overall structure (template) for performing a calculation:
    # 1. Validate inputs to make sure they’re numbers.
    # 2. Perform the specific operation (like adding or multiplying).
    # 3. Log the result.
    def calculate(self, a: float, b: float) -> float:
        """Template method that defines the structure for performing an operation."""
        self.validate_inputs(a, b)  # Step 1: Validate the inputs.
        result = self.execute(a, b)  # Step 2: Perform the operation.
        self.log_result(a, b, result)  # Step 3: Log the result.
        return result

    def validate_inputs(self, a: float, b: float):
        """Common validation for all operations to ensure inputs are numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logging.error(f"Invalid input: {a}, {b} (Inputs must be numbers)")  # Log the error if inputs are not numbers.
            raise ValueError("Both inputs must be numbers.")  # If either input is not a number, raise an error.

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Perform the specific operation. This method will be defined by each subclass."""
        pass

    def log_result(self, a: float, b: float, result: float):
        """Log the result of the calculation."""
        logging.info(f"Operation performed: {a} and {b} -> Result: {result}")  # Log the operation and the result.

# Now, we’ll create specific operation classes that follow this template.
# Each operation class will provide its own version of the `execute` method.

class Addition(TemplateOperation):
    """Class to represent the addition operation."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b  # Simple addition.

class Subtraction(TemplateOperation):
    """Class to represent the subtraction operation."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b  # Simple subtraction.

class Multiplication(TemplateOperation):
    """Class to represent the multiplication operation."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b  # Simple multiplication.

class Division(TemplateOperation):
    """Class to represent the division operation."""
    
    def execute(self, a: float, b: float) -> float:
        """Return the quotient of two numbers. Raise an error if dividing by zero."""
        if b == 0:
            logging.error("Attempted to divide by zero.")  # Log an error if there is an attempt to divide by zero.
            raise ValueError("Division by zero is not allowed.")  # Can't divide by zero!
        return a / b  # Simple division.

# Logging inside these operation classes helps us track which operations are being performed
# and when errors (like division by zero) occur.

# ------------------------------------------------------------------------------
# PART 2: FACTORY PATTERN FOR CREATING OPERATIONS (with Logging)
# ------------------------------------------------------------------------------

# Now let’s add the **Factory Pattern**. This pattern allows us to create objects (in this case, math operations)
# without having to manually specify which class to use each time. It’s like a "machine" that creates the correct 
# object based on a user’s request (e.g., 'add' or 'subtract').

class OperationFactory:
    """Factory class to create instances of operations based on the operation type."""
    
    @staticmethod
    def create_operation(operation: str) -> TemplateOperation:
        """Return an instance of the appropriate Operation subclass based on the operation string."""
        # A dictionary (menu) that maps operation names to their respective classes.
        operations_map = {
            "add": Addition(),
            "subtract": Subtraction(),
            "multiply": Multiplication(),
            "divide": Division(),
        }
        # Log the operation request.
        logging.debug(f"Creating operation for: {operation}")
        # The factory will return the appropriate operation object based on the string provided by the user.
        return operations_map.get(operation.lower())

# The Factory Pattern keeps our code flexible. If we want to add more operations later (like squaring a number),
# we only need to add them to this factory instead of changing the whole program.

# ------------------------------------------------------------------------------
# PART 3: OBSERVER PATTERN FOR TRACKING HISTORY (with Logging)
# ------------------------------------------------------------------------------

# Next, let’s implement the **Observer Pattern**. This pattern allows us to notify other parts of the program 
# when something important happens. In our case, when a new calculation is added, we can notify any "observers" 
# that are "watching" for updates. Think of it like a "news system" – when a new story (calculation) is added, 
# we notify all subscribers (observers).

class HistoryObserver:
    """Observer that gets notified whenever a new calculation is added to history."""
    
    def update(self, calculation):
        """Called when a new calculation is added."""
        logging.info(f"Observer: New calculation added -> {calculation}")  # Log when an observer is notified.

# We will now integrate this observer into our calculator class, so that every time a new calculation is added,
# the observer gets notified.

class CalculatorWithObserver:
    """Calculator class with observer support for tracking calculation history."""
    
    def __init__(self):
        self._history: List[Calculation] = []  # A list to store the calculation history.
        self._observers: List[HistoryObserver] = []  # A list of observers (people watching for updates).

    def add_observer(self, observer: HistoryObserver):
        """Add an observer to be notified when history is updated."""
        self._observers.append(observer)
        logging.debug(f"Observer added: {observer}")  # Log when an observer is added.

    def notify_observers(self, calculation):
        """Notify all observers when a new calculation is added."""
        for observer in self._observers:
            observer.update(calculation)  # Notify the observer.
            logging.debug(f"Notified observer about: {calculation}")  # Log when an observer is notified.

    def perform_operation(self, operation: TemplateOperation, a: float, b: float):
        """Perform the operation, store it in history, and notify observers."""
        calculation = Calculation(operation, a, b)
        self._history.append(calculation)  # Add the calculation to the history.
        self.notify_observers(calculation)  # Notify all observers that a new calculation has been added.
        logging.debug(f"Performed operation: {calculation}")  # Log the operation performed.
        return operation.calculate(a, b)  # Use the Template Method to calculate the result.

# The **Observer Pattern** is great because it lets us extend our system to notify other parts (like a UI or log system)
# when something important happens, like adding a new calculation.

# ------------------------------------------------------------------------------
# PART 4: SINGLETON PATTERN FOR ENSURING ONE CALCULATOR INSTANCE
# ------------------------------------------------------------------------------

# Now let’s add the **Singleton Pattern**. This pattern ensures that only one instance of a class exists throughout the program.
# For example, if there’s only one vending machine in the office, everyone has to use the same machine. The Singleton 
# Pattern is useful when you want to share resources (like calculation history) across the whole program.

class SingletonCalculator:
    """A calculator using the Singleton pattern to ensure only one instance exists."""
    _instance = None  # This is where we store the single instance of the class.

    def __new__(cls):
        """Override __new__ to ensure only one instance of the class is created."""
        if cls._instance is None:
            cls._instance = super(SingletonCalculator, cls).__new__(cls)  # Create the single instance.
            cls._history = []  # Initialize the history here.
            logging.info("SingletonCalculator instance created.")  # Log the creation of the Singleton instance.
        return cls._instance

    def perform_operation(self, operation: TemplateOperation, a: float, b: float) -> float:
        """Perform the given operation and store the calculation in history."""
        calculation = Calculation(operation, a, b)
        self._history.append(calculation)  # Add the calculation to the history.
        logging.debug(f"SingletonCalculator: Performed operation -> {calculation}")  # Log the operation performed.
        return operation.calculate(a, b)  # Use the Template Method to calculate the result.

    def get_history(self):
        """Return the history of calculations."""
        pdb.set_trace()  # This line will trigger the debugger.

        return self._history  # Return the shared history.

# The **Singleton Pattern** makes sure there is only one instance of the calculator, so the history is shared across 
# all uses. Every time you use the calculator, you’re working with the same instance!

# ------------------------------------------------------------------------------
# PART 5: STRATEGY PATTERN FOR OPERATION SELECTION
# ------------------------------------------------------------------------------

# The **Strategy Pattern** lets us choose the appropriate operation (strategy) dynamically, based on user input.
# The user doesn’t need to know how each operation works – they just tell the calculator what they want to do (e.g., 'add'),
# and the correct strategy is selected.

@dataclass
class Calculation:
    """Represents a single calculation using the Strategy Pattern (choosing the correct operation)."""
    operation: TemplateOperation  # The operation to be performed (strategy).
    operand1: float
    operand2: float

    def __repr__(self) -> str:
        return f"Calculation({self.operand1}, {self.operation.__class__.__name__.lower()}, {self.operand2})"

    def __str__(self) -> str:
        # Dynamically calculate the result by calling the operation's calculate method.
        result = self.operation.calculate(self.operand1, self.operand2)
        return f"{self.operand1} {self.operation.__class__.__name__.lower()} {self.operand2} = {result}"

# The **Strategy Pattern** lets us swap different operations in and out easily. The calculator just uses whatever operation 
# (strategy) is selected by the user without needing to know how it works internally.

# ------------------------------------------------------------------------------
# PART 6: MAIN CALCULATOR PROGRAM (REPL Interface with Debugging)
# ------------------------------------------------------------------------------

# Now, let's build the **REPL** (Read-Eval-Print Loop), where the user can interact with the calculator.
# We’ll also add debugging using the `pdb` (Python Debugger) module.

def calculator():
    """Interactive REPL for performing calculator operations."""
    
    # Create a new instance of the calculator with observer support.
    calc = CalculatorWithObserver()
    
    # Create an observer to track history.
    observer = HistoryObserver()
    calc.add_observer(observer)
    
    print("Welcome to the OOP Calculator! Type 'help' for available commands.")
    
    while True:
        # Ask the user for input.
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or a command (help, list, clear, exit): ")
        
        # Handle the "help" command to show available commands.
        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("  add <num1> <num2>       : Add two numbers.")
            print("  subtract <num1> <num2>  : Subtract the second number from the first.")
            print("  multiply <num1> <num2>  : Multiply two numbers.")
            print("  divide <num1> <num2>    : Divide the first number by the second (cannot divide by zero).")
            print("  list                    : Show the calculation history.")
            print("  clear                   : Clear the calculation history.")
            print("  exit                    : Exit the calculator.\n")
            continue

        # Handle the "exit" command to quit the program.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Handle the "list" command to show calculation history.
        if user_input.lower() == "list":
            if not calc._history:
                print("No calculations in history.")
            else:
                for calc_item in calc._history:
                    print(calc_item)
            continue

        # Handle the "clear" command to clear the calculation history.
        if user_input.lower() == "clear":
            calc._history.clear()
            logging.info("History cleared.")  # Log when history is cleared.
            print("History cleared.")
            continue

        # Otherwise, assume the user entered an operation.
        try:
            # Use the debugger to inspect the input before parsing it.
            
            operation_str, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

            # Use the Factory to get the correct operation.
            operation = OperationFactory.create_operation(operation_str)

            # If the operation exists, perform it.
            if operation:
                result = calc.perform_operation(operation, num1, num2)
                print(f"Result: {result}")
            else:
                print(f"Unknown operation '{operation_str}'. Type 'help' for available commands.")

        except ValueError as e:
            logging.error(f"Invalid input or error: {e}")  # Log any errors encountered.
            print("Invalid input. Please enter a valid operation and two numbers. Type 'help' for instructions.")

if __name__ == "__main__":
    calculator()

# ------------------------------------------------------------------------------
# Summary of the Design Patterns and Debugging Techniques Used:
# 1. **Factory Pattern**: We used the Factory to create different operation objects (like Addition or Subtraction) based on user input.
# 2. **Command Pattern**: Each operation (Addition, Subtraction, etc.) is treated as a command that the calculator can execute.
# 3. **Strategy Pattern**: The calculator selects the appropriate operation dynamically at runtime based on user input.
# 4. **Template Method Pattern**: We defined a common structure for performing operations (validate, execute, log) and let each operation define its own calculation.
# 5. **Observer Pattern**: We created observers that get notified whenever a new calculation is added to the history.
# 6. **Singleton Pattern**: We used the Singleton Pattern to ensure that there is only one instance of the calculator, ensuring shared history across all uses.
#
# Logging:
# - We added logging to track key events, such as operations being performed, errors (e.g., division by zero), and history being cleared.
# - Logs are written to a file called `calculator.log`.
#
# Debugging:
# - We added `pdb.set_trace()` to pause the program execution and inspect the input before parsing it. This allows us to step through the code, inspect variables, and debug any issues interactively.
#
# This is the ultimate masterclass in OOP, design patterns, logging, and debugging techniques!

"""
Entry point for the CI/CD demo application.
"""

from app import add_numbers


def main():
    """Main function to demonstrate the add_numbers functionality."""
    num1 = 10
    num2 = 25
    
    result = add_numbers(num1, num2)
    print(f"Adding {num1} + {num2} = {result}")
    
    # Additional examples
    result2 = add_numbers(3.5, 2.5)
    print(f"Adding 3.5 + 2.5 = {result2}")


if __name__ == "__main__":
    main()

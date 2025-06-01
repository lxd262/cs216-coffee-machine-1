class CoffeeMachine:
    """A coffee machine simulator for CS216 Lab 2."""

    def __init__(self):
        """
        Initialize the coffee machine with starting ingredients and settings.

        Sets up the machine with default ingredient levels and operational parameters.
        """
        # Initial ingredient levels
        self.ingredients = {
            'water': 1000,  # milliliters
            'coffee_beans': 500,  # grams
            'milk': 800  # milliliters
        }

        # Machine operational parameters
        self.machine_settings = {
            'max_water': 1500,  # maximum water capacity (ml)
            'max_beans': 1000,  # maximum bean capacity (grams)
            'max_milk': 1200,  # maximum milk capacity (ml)
            'min_water_alert': 100,  # low water warning threshold (ml)
            'min_beans_alert': 50,  # low beans warning threshold (grams)
            'min_milk_alert': 100,  # low milk warning threshold (ml)
            'is_on': True,  # machine power status
            'temperature': 85  # brewing temperature (celsius)
        }

        # Transaction tracking
        self.daily_stats = {
            'drinks_made': 0,  # number of drinks brewed today
            'total_revenue': 0.00,  # total money earned today
            'ingredients_refilled': 0  # number of times ingredients were refilled
        }

    # BREW FUNCTIONS

    def check_ingredients(self):
        """
        Check current ingredient levels in the coffee machine.

        Returns:
            dict: Current ingredient amounts and status alerts
            {
                'water': int,           # milliliters remaining
                'coffee_beans': int,    # grams remaining
                'milk': int,           # milliliters remaining
                'alerts': list,        # list of low ingredient warnings
                'can_operate': bool    # True if machine has minimum ingredients
            }
        """
        # TODO: Implement this function
        pass

    def add_ingredients(self, ingredient, amount):
        """
        Add ingredients to the coffee machine.

        Args:
            ingredient (str): Type of ingredient to add
                Valid options: 'water', 'coffee_beans', 'milk'
            amount (int): Amount to add
                - For water/milk: milliliters
                - For coffee_beans: grams

        Returns:
            dict: Result of adding ingredients
            {
                'success': bool,     # True if successfully added
                'new_amount': int,   # Total amount after adding
                'message': str,      # Status message
                'overflow': int      # Amount that couldn't be added due to capacity limits
            }
        """
        # TODO: Implement this function

        pass

    # PAYMENT FUNCTIONS

    def process_payment(self, amount, cost):
        """
        Process customer payment for coffee order.

        Args:
            amount (float): Amount of money customer paid (in dollars)
            cost (float): Cost of the coffee order (in dollars)

        Returns:
            dict: Payment processing result
            {
                'success': bool,     # True if payment sufficient
                'change': float,     # Change to return to customer
                'message': str       # Payment status message
            }
        """
        # TODO: Implement this function
        pass

    def calculate_cost(self, coffee_type, size):
        """
        Calculate the cost of a coffee order.

        Args:
            coffee_type (str): Type of coffee
                Valid options: 'espresso', 'americano', 'latte'
            size (str): Size of the coffee
                Valid options: 'small', 'medium', 'large'

        Returns:
            dict: Cost breakdown
            {
                'total_cost': float,    # Total price in dollars
                'base_price': float,    # Base price for coffee type
                'size_extra': float,    # Additional cost for size
                'valid': bool          # True if valid coffee type and size
            }
        """
        # TODO: Implement this function
        pass

    # FUNCTION YOU MUST IMPLEMENT TOGETHER

    def brew_coffee(self, coffee_type, size):
        """
        Brew a coffee drink (MUST BE IMPLEMENTED BY BOTH PARTNERS TOGETHER).

        This function combines ingredient checking, cost calculation, and brewing.
        Both partners must collaborate on this implementation using Git branching
        and pull requests.

        Args:
            coffee_type (str): Type of coffee to brew
                Valid options: 'espresso', 'americano', 'latte'
            size (str): Size of the coffee
                Valid options: 'small', 'medium', 'large'

        Returns:
            dict: Brewing result
            {
                'success': bool,        # True if coffee was brewed successfully
                'message': str,         # Status message
                'cost': float,          # Total cost of the coffee
                'ingredients_used': dict, # Ingredients consumed in brewing
                'error': str or None    # Error message if success=False
            }

        Implementation Notes:
            - Use check_ingredients() to verify sufficient ingredients
            - Use calculate_cost() to determine the price
            - Update ingredient levels after successful brewing
            - Handle all error cases (invalid inputs, insufficient ingredients)
            - Both partners must contribute to this function using Git workflow
        """
        # TODO: IMPLEMENT TOGETHER
        pass


# SAMPLE USAGE

def main():
    """
    Sample usage of the CoffeeMachine class.
    This shows how to interact with the coffee machine.
    """
    # Create a new coffee machine
    machine = CoffeeMachine()

    # Check initial status
    print("Coffee Machine Status\n")
    ingredients = machine.check_ingredients()
    print(f"Ingredients: {ingredients}")

    # Try to make a coffee
    print("Making Coffee\n")
    result = machine.brew_coffee('latte', 'medium')
    print(f"Brew result: {result}")

    # Check ingredients after brewing
    print("Status After Brewing\n")
    ingredients = machine.check_ingredients()
    print(f"Ingredients: {ingredients}")

    # Add more ingredients
    print("Refilling Ingredients\n")
    refill = machine.add_ingredients('milk', 300)
    print(f"Refill result: {refill}")


if __name__ == "__main__":
    main()

# RECIPE AND PRICING CONSTANTS

RECIPES = {
    'espresso': {
        'small': {'water': 30, 'coffee_beans': 18, 'milk': 0},
        'medium': {'water': 60, 'coffee_beans': 25, 'milk': 0},
        'large': {'water': 90, 'coffee_beans': 32, 'milk': 0}
    },
    'americano': {
        'small': {'water': 150, 'coffee_beans': 18, 'milk': 0},
        'medium': {'water': 200, 'coffee_beans': 25, 'milk': 0},
        'large': {'water': 250, 'coffee_beans': 32, 'milk': 0}
    },
    'latte': {
        'small': {'water': 30, 'coffee_beans': 18, 'milk': 120},
        'medium': {'water': 60, 'coffee_beans': 25, 'milk': 180},
        'large': {'water': 90, 'coffee_beans': 32, 'milk': 240}
    }
}

PRICES = {
    'espresso': {'small': 2.50, 'medium': 3.00, 'large': 3.50},
    'americano': {'small': 3.00, 'medium': 3.50, 'large': 4.00},
    'latte': {'small': 4.00, 'medium': 4.50, 'large': 5.00}
}

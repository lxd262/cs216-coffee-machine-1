# Coffee Machine Part 1 Instructions

## check_ingredients()

Check current ingredient levels in the coffee machine.

**Returns:**
- `dict`: Current ingredient amounts
  ```python
  {
      'water': int,        # milliliters remaining
      'coffee_beans': int, # grams remaining
      'milk': int         # milliliters remaining
  }
  ```

**Example:**
```python
>>> machine.check_ingredients()
{'water': 800, 'coffee_beans': 450, 'milk': 600}
```

## add_ingredients(ingredient, amount)

Add ingredients to the coffee machine.

**Args:**
- `ingredient` (str): Type of ingredient to add
    - Valid options: 'water', 'coffee_beans', 'milk'
- `amount` (int): Amount to add
    - For water/milk: milliliters
    - For coffee_beans: grams

**Returns:**
- `dict`: Result of adding ingredients
  ```python
  {
      'success': bool,     # True if successfully added
      'new_amount': int,   # Total amount after adding
      'message': str       # Status message
  }
  ```

**Examples:**
```python
>>> machine.add_ingredients('water', 200)
{'success': True, 'new_amount': 1000, 'message': 'Added 200ml water'}

>>> machine.add_ingredients('invalid', 100)
{'success': False, 'new_amount': 0, 'message': 'Invalid ingredient type'}
```

## calculate_cost(coffee_type, size)

Calculate the cost of a coffee order.

**Args:**
- `coffee_type` (str): Type of coffee
    - Valid options: 'espresso', 'americano', 'latte'
- `size` (str): Size of the coffee
    - Valid options: 'small', 'medium', 'large'

**Returns:**
- `dict`: Cost breakdown
  ```python
  {
      'total_cost': float,    # Total price in dollars
      'base_price': float,    # Base price for coffee type
      'size_extra': float,    # Additional cost for size
      'valid': bool          # True if valid coffee type and size
  }
  ```

**Examples:**
```python
>>> machine.calculate_cost('latte', 'medium')
{'total_cost': 4.50, 'base_price': 4.00, 'size_extra': 0.50, 'valid': True}

>>> machine.calculate_cost('invalid', 'small')
{'total_cost': 0.00, 'base_price': 0.00, 'size_extra': 0.00, 'valid': False}
```

## process_payment(amount, cost)

Process customer payment for coffee order.

**Args:**
- `amount` (float): Amount of money customer paid (in dollars)
- `cost` (float): Cost of the coffee order (in dollars)

**Returns:**
- `dict`: Payment processing result
  ```python
  {
      'success': bool,     # True if payment sufficient
      'change': float,     # Change to return to customer
      'message': str       # Payment status message
  }
  ```

**Examples:**
```python
>>> machine.process_payment(5.00, 4.50)
{'success': True, 'change': 0.50, 'message': 'Payment successful'}

>>> machine.process_payment(3.00, 4.50)
{'success': False, 'change': 0.00, 'message': 'Insufficient payment'}
```

## brew_coffee(coffee_type, size)

Brew a coffee drink. This function combines ingredient checking, cost calculation, and brewing. Both partners must collaborate on this implementation using Git branching and pull requests.

**Args:**
- `coffee_type` (str): Type of coffee to brew
    - Valid options: 'espresso', 'americano', 'latte'
- `size` (str): Size of the coffee
    - Valid options: 'small', 'medium', 'large'

**Returns:**
- `dict`: Brewing result
  ```python
  {
      'success': bool,        # True if coffee was brewed successfully
      'message': str,         # Status message
      'cost': float,          # Total cost of the coffee
      'ingredients_used': dict, # Ingredients consumed in brewing
      'error': str or None    # Error message if success=False
  }
  ```

**Examples:**
```python
>>> machine.brew_coffee('latte', 'medium')
{
    'success': True,
    'message': 'Medium latte ready!',
    'cost': 4.50,
    'ingredients_used': {'water': 60, 'coffee_beans': 25, 'milk': 180},
    'error': None
}

>>> machine.brew_coffee('latte', 'large')  # Not enough milk
{
    'success': False,
    'message': 'Cannot brew coffee',
    'cost': 0.00,
    'ingredients_used': {},
    'error': 'Not enough milk. Please refill.'
}
```

**Implementation Notes:**
- Use `check_ingredients()` to verify sufficient ingredients
- Use `calculate_cost()` to determine the price
- Update ingredient levels after successful brewing
- Handle all error cases (invalid inputs, insufficient ingredients)
- Both partners must contribute to this function using Git workflow
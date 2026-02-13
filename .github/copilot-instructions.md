# AI Coding Agent Instructions for ITM 352 - Python Labs

## Project Overview
This is an educational Python course (ITM 352, Spring 2026) organized progressively across labs focusing on core Python concepts:
- **Lab 2:** Basic I/O and operations
- **Lab 3:** Functions and modules  
- **Lab 4:** Lists, tuples, string manipulation
- **Lab 5:** Dictionaries
- **Lab 6:** (Upcoming exercises)

## File Organization & Naming
- **Exercise files:** Named `ex1.py`, `ex2.py`, etc. within each Lab directory
- **Utility modules:** Reusable code like `HandyMath.py`, `ShoppingList.py`, `Dictionary.py` live in their respective labs
- **Example files:** Demonstration code uses descriptive names (`function_example_.py`, `scope_example.py`)

## Code Style & Conventions

### File Headers
Every file must start with a comment block containing:
```python
# [Brief description of what the code does]
# Name: Ethan Mayer
# Date: [Date in Month. Day, Year format]
```

### Python Style
- **String formatting:** Prefer f-strings (modern style): `f"Value: {variable}"`  
  - Also understand alternative methods (%, .format()) as they appear in earlier exercises
- **Variable naming:** Use snake_case: `valued_entered`, `squared_value`, not camelCase
- **Functions:** Include docstrings using triple quotes:
  ```python
  def midpoint(num1, num2):
      """Calculate the midpoint between two numbers."""
      return (num1 + num2) / 2
  ```

## Module Usage Pattern
When creating reusable modules:
1. Define functions with clear docstrings (see [Lab 3/HandyMath.py](Lab%203/HandyMath.py))
2. Import in other files using alias: `import HandyMath as HM`
3. Call functions via alias: `HM.midpoint(num1, num2)`

This pattern enables code reuse across exercise files within a lab.

## Common Student Patterns
- **Progressive exploration:** Code shows multiple approaches (e.g., [Lab 4a/ex1.py](Lab%204a/ex1.py) shows 4 different string formatting methods)
- **Interactive programs:** Use `input()` for user interaction; focus on clear prompts
- **Basic Python only:** No external dependencies or async patterns—keep it simple and learning-focused

## When Adding New Code
- Follow the existing file header convention
- Maintain chronological progression (Lab 5 doesn't revisit Lab 2 concepts)
- Keep functions small and focused for educational clarity
- Add comments explaining the "why" not just the "what"
- Test outputs with simple print statements

## Key Files to Reference
- [Lab 3/HandyMath.py](Lab%203/HandyMath.py) — Function documentation patterns
- [Lab 3/UseModule.py](Lab%203/UseModule.py) — Module import and usage pattern
- [Lab 4a/ex1.py](Lab%204a/ex1.py) — String manipulation and formatting examples
- [Lab 5/Dictionary.py](Lab%205/Dictionary.py) — Dictionary operations reference

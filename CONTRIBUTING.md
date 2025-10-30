# Contributing to Python Calculator 🎉

Thank you for considering contributing to the Python Calculator project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs 🐛

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Python version and OS

### Suggesting Enhancements 💡

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Why this feature would be useful
- Examples of how it would work

### Pull Requests 🚀

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/Calculator-Python-Language.git
   cd Calculator-Python-Language
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow Python PEP 8 style guidelines
   - Add comments where necessary
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python -m unittest test_calculator.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of your changes

## Coding Standards

### Python Style Guide
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Keep functions focused and small
- Add docstrings to all functions
- Include type hints where appropriate

### Example:
```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
```

### Testing
- All new features should include unit tests
- Ensure all existing tests pass
- Aim for high code coverage
- Test edge cases and error conditions

### Documentation
- Update README.md if you add new features
- Add inline comments for complex logic
- Include docstrings for all functions
- Update CONTRIBUTING.md if you change the workflow

## Feature Ideas 🌟

Looking for something to work on? Here are some ideas:

### Easy 🟢
- [ ] Add keyboard shortcuts for common operations
- [ ] Improve error messages
- [ ] Add more unit tests
- [ ] Improve code documentation

### Medium 🟡
- [ ] Add equation solver (solve for x)
- [ ] Add matrix operations
- [ ] Add graphing capabilities
- [ ] Add conversion features (temperature, currency, etc.)
- [ ] Create a GUI interface (tkinter/PyQt)

### Hard 🔴
- [ ] Add symbolic computation
- [ ] Add calculus operations (derivatives, integrals)
- [ ] Add statistics functions
- [ ] Create a web interface
- [ ] Add support for complex numbers

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all.

### Our Standards
- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## Questions?

Feel free to:
- Open an issue for questions
- Reach out to maintainers
- Check existing issues and PRs

## Hacktoberfest Guidelines 🎃

If you're contributing for Hacktoberfest:
- Ensure your PR is meaningful and not spam
- Follow all guidelines above
- Label your PR appropriately
- Be patient while waiting for review

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Happy Coding! 🚀**

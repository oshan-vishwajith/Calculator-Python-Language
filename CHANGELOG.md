# Changelog

All notable changes to the Python Calculator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-10-31

### Added - Major Feature Release 🎉

#### Scientific Functions
- Square root calculation
- Trigonometric functions (sine, cosine, tangent) with degree input
- Logarithm functions (base-10 and natural logarithm)
- Factorial calculation with integer validation
- Absolute value function

#### Memory Operations
- Memory Clear (MC) - Clear stored memory
- Memory Recall (MR) - Retrieve stored value
- Memory Add (M+) - Add to memory
- Memory Subtract (M-) - Subtract from memory
- Memory Store (MS) - Store new value

#### History Features
- Automatic calculation history tracking with timestamps
- View calculation history command
- Clear history command
- Export history to JSON file functionality

#### Testing & Quality
- Comprehensive unit test suite with 40+ tests
- Tests for all basic operations
- Tests for all scientific functions
- Tests for memory operations
- Edge case and error condition testing

#### Documentation
- Enhanced README with feature showcase
- CONTRIBUTING.md with detailed guidelines
- requirements.txt for optional dependencies
- .gitignore for Python projects
- MIT License file
- This CHANGELOG

#### User Experience
- Improved UI with better formatting and emojis
- Enhanced error messages with clear feedback
- Operation reference menu at startup
- Better input validation

### Changed
- Upgraded calculator interface with better visual design
- Reorganized code structure with clear function categories
- Improved error handling across all operations
- Enhanced command-line prompts and output

### Technical Improvements
- Added `math` module for scientific calculations
- Added `json` module for history export
- Added `datetime` module for timestamps
- Implemented global variables for memory and history
- Added comprehensive docstrings to all functions

## [1.0.0] - Previous Version

### Initial Release
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Power and modulus operations
- Simple command-line interface
- Basic error handling for division by zero
- Input validation for numeric values

---

## Future Versions (Planned)

### [2.1.0] - Planned
- GUI interface using tkinter
- Complex number support
- More trigonometric functions (arcsin, arccos, arctan)
- Hyperbolic functions

### [2.2.0] - Planned
- Matrix operations
- Statistical functions (mean, median, mode, std dev)
- Unit conversion features
- Currency conversion

### [3.0.0] - Planned
- Web interface
- Graphing capabilities
- Equation solver
- Calculus operations (derivatives, integrals)

---

**Note**: Dates follow the YYYY-MM-DD format (ISO 8601)

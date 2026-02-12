# Contributing to Facebook Ads Creative Manager

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Provide detailed information:**
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages/logs

### Suggesting Features

1. **Check existing issues** first
2. **Describe the feature:**
   - What problem does it solve?
   - How would it work?
   - Why is it important?

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes:**
   ```bash
   streamlit run app.py
   ```
5. **Commit with clear messages:**
   ```bash
   git commit -m "Add: description of changes"
   ```
6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request** with:
   - Clear title
   - Description of changes
   - Related issues

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/fb-ads-creative-manager.git
cd fb-ads-creative-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your Supabase credentials

# Run the app
streamlit run app.py
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

## Testing

- Test your changes locally
- Test with both Chinese and English versions
- Test on different devices/browsers if possible

## Documentation

- Update README if adding features
- Add docstrings to functions
- Include examples for new features

## Commit Message Guidelines

- Use clear, descriptive messages
- Start with action word: Add, Fix, Update, Remove, etc.
- Reference related issues: "Fixes #123"

Examples:
```
Add: Creative filtering by date range
Fix: Performance data calculation error
Update: Documentation for Supabase setup
Remove: Deprecated performance metrics
```

## Pull Request Process

1. Update documentation if needed
2. Add/update tests if applicable
3. Ensure code follows project style
4. Keep PR focused on one feature/fix
5. Be responsive to review comments

## Questions?

- Check existing documentation
- Review closed issues for similar questions
- Open a new issue to discuss

---

Thank you for contributing! 🙏

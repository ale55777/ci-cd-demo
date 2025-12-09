# CI/CD Demo Project

A production-quality Python project demonstrating CI/CD best practices with GitHub Actions.

## 📋 Project Overview

This project demonstrates a complete CI/CD pipeline using:
- **Python 3.10** for application code
- **pytest** for unit testing with code coverage
- **GitHub Actions** for automated testing and deployment

## 🏗️ Project Structure

```
ci-cd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD pipeline
├── tests/
│   └── test_app.py         # Unit tests
├── app.py                  # Main application module
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🚀 Features

- **Core Functionality**: `add_numbers(a, b)` function with type validation
- **Comprehensive Testing**: 8 unit tests covering positive, negative, and edge cases
- **CI/CD Pipeline**: Automated testing and deployment on push/PR to main branch
- **Code Coverage**: Integrated coverage reporting with pytest-cov

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd ci-cd-demo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests Locally

### Run all tests:
```bash
pytest tests/ -v
```

### Run tests with coverage:
```bash
pytest tests/ -v --cov=. --cov-report=term-missing
```

### Run tests with HTML coverage report:
```bash
pytest tests/ --cov=. --cov-report=html
```
Then open `htmlcov/index.html` in your browser.

## 🏃 Running the Application

```bash
python main.py
```

Expected output:
```
Adding 10 + 25 = 35
Adding 3.5 + 2.5 = 6.0
```

## 🔄 CI/CD Pipeline

The GitHub Actions pipeline automatically:

### On Push/Pull Request to `main`:
1. ✅ Checks out the code
2. ✅ Sets up Python 3.10
3. ✅ Installs dependencies
4. ✅ Runs all tests with coverage
5. ✅ Displays test summary

### On Push to `main` (after tests pass):
6. 🚀 Deploys the application (currently echoes deployment message)

## 📤 Pushing to GitHub

1. **Create a new repository on GitHub** (don't initialize with README)

2. **Initialize and push your local repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: CI/CD demo project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ci-cd-demo.git
   git push -u origin main
   ```

3. **View the pipeline**:
   - Go to your GitHub repository
   - Click on the "Actions" tab
   - Watch your CI/CD pipeline run automatically!

## 🔧 Customization

### Modify the CI/CD Pipeline
Edit `.github/workflows/ci.yml` to:
- Add more jobs (linting, security scanning, etc.)
- Deploy to actual environments (AWS, Azure, Heroku, etc.)
- Add notification steps (Slack, email, etc.)

### Add More Tests
Add new test files in the `tests/` directory following the `test_*.py` naming convention.

### Extend Functionality
Add new functions to `app.py` and corresponding tests to `tests/test_app.py`.

## 📊 Code Quality

This project maintains high code quality standards:
- ✅ Type validation for function inputs
- ✅ Comprehensive docstrings
- ✅ 100% test coverage
- ✅ Clean, readable code structure
- ✅ Production-ready error handling

## 📝 License

This is a demo project for educational purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Built with ❤️ as a CI/CD demonstration project**

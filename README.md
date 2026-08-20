# SauceDemo SDET Assignment

## Overview
This repository contains my QA/SDET testing work for the SauceDemo e-commerce application. The assignment demonstrates a complete testing lifecycle, including manual exploratory testing, test planning, bug reporting, and automated UI testing using Python and Selenium.

**Submitted By:** Humna Ahmed

## Application Under Test
- **Website:** [SauceDemo](https://www.saucedemo.com)
- **Type:** E-Commerce Web Application

## Test Environment
- **OS:** Windows 11
- **Device:** Dell Latitude 7420
- **Browser:** Google Chrome
- **Language:** Python 3.x
- **Frameworks:** Selenium WebDriver, pytest

## Project Structure
```text
saucedemo-sdet/
├── README.md
├── test_plan.md
├── bug_reports.md
├── requirements.txt
└── tests/
    ├── test_login.py
    ├── test_checkout.py
    └── test_locked_user.py
```

## Manual Testing
Manual exploratory testing was performed using the provided SauceDemo user accounts (standard_user, problem_user, locked_out_user, performance_glitch_user).

- **Test Plan:** Detailed test cases, risk assessment, and exit criteria are documented in `test_plan.md`.
- **Bug Reports:** Five distinct, reproducible bugs were discovered during exploratory testing and are documented in `bug_reports.md`. These cover UI issues, functional failures, and missing input validations.

## Automated Testing
The automated test suite verifies core business workflows using Python and Selenium. The following three test flows are implemented:

- **Automated Flow 1 (Valid Login):** Verifies that a valid user (standard_user) can successfully authenticate and reach the Products page.
- **Automated Flow 2 (End-to-End Checkout):** Verifies the complete shopping journey: authentication, adding a product to the cart, navigating to checkout, providing user details, and confirming the final order completion.
- **Automated Flow 3 (Locked-Out User):** Verifies that a locked-out account is restricted from accessing the system and receives the correct validation error message.

## Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
```bash
git clone https://github.com/HumnaAhmed/saucedemo-sdet-assignment.git
cd saucedemo-sdet
```

2. **Create and activate a virtual environment:**
```bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
```

3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Tests
To execute the automated test suite, ensure your virtual environment is active and run the following command in your terminal:

```bash
pytest -v
```

## Test Results
- **Execution Date:** August 20, 2026
- **Result:** 3 passed (All automated test flows executed successfully without errors).

## Video Demonstrations
The following Loom video recordings explain my testing approach and demonstrate the actual bug reproduction:

- **Video 1 - Test Plan & Automation Overview:** https://www.loom.com/share/99e4e57878004688be74931e8945194d
- **Video 2 - Manual Bug Discovery Demo:** https://www.loom.com/share/195a4e04fa8b45d2a2b213df0729418e

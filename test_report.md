# Task-03: Automated Login Test Report

This document summarizes the test cases and results for automated login testing performed using Python and Selenium WebDriver.

---

## ✅ Test Cases Performed

| Test Case Description                        | Type      | Expected Result                | Actual Result    | Status  |
|---------------------------------------------|-----------|--------------------------------|------------------|---------|
| Valid email and password                    | Positive  | Redirects to dashboard         | Redirected       | Passed  |
| Invalid email                                | Negative  | Show error message             | Error shown      | Passed  |
| Invalid password                             | Negative  | Show error message             | Error shown      | Passed  |
| Both fields empty                            | Negative  | Show required field messages   | Error shown      | Passed  |
| Email without "@" or domain                  | Negative  | Validation error               | Error shown      | Passed  |
| SQL injection attempt (`' OR 1=1 --`)        | Negative  | Should not log in              | Access denied    | Passed  |

---

## 🔧 Tools Used

- Python 3.10  
- Selenium WebDriver  
- Chrome browser  
- ChromeDriver  

---

## 🧪 Summary

All core test cases were executed successfully. The login page responded appropriately to valid and invalid inputs, and security validation was in place for SQL injection.

Test automation ensures consistent, repeatable login validation and saves time in regression testing.

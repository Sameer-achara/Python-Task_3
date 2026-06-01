<div align="center">

# 🐍 Python Internship Program — Task 3

### Functions & Code Reusability

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Functions-FF6B35?style=for-the-badge)
![Concepts](https://img.shields.io/badge/Concepts-Recursion%20%7C%20Lambda%20%7C%20Scope-6A0DAD?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Internship%20Project-28A745?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<br/>

*A comprehensive exploration of Python functions — from basic definitions to recursion, lambda expressions, variable scope, and functional programming.*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Learning Objectives](#-learning-objectives)
- [Theory Notes](#-theory-notes)
  - [Function Definition](#1-function-definition)
  - [Parameters & Arguments](#2-parameters-and-arguments)
  - [Return Values](#3-return-values-and-data-types)
  - [Default Arguments](#4-default-arguments)
  - [Variable-Length Arguments](#5-variable-length-arguments-args)
  - [Lambda Functions](#6-lambda-functions)
  - [Recursion](#7-recursion)
  - [Variable Scope](#8-variable-scope)
  - [Code Reusability](#9-code-reusability)
- [Programs Implemented](#-programs-implemented)
- [File Structure](#-file-structure)
- [Key Concepts Covered](#-key-concepts-covered)
- [Conclusion](#-conclusion)
- [Author](#-author)

---

## 🌟 Overview

This repository contains Python programs created as part of **Task 3** of the Python Internship Program. The objective of this task is to understand the concept of **functions** and how they improve code reusability, readability, and maintainability.

The task covers function creation, parameters, return values, recursion, lambda functions, variable scope, and reusable program design through practical implementations.

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Understand function definition and scope |
| 2 | Work with parameters and arguments |
| 3 | Use return statements effectively |
| 4 | Learn default arguments |
| 5 | Implement variable-length arguments using `*args` |
| 6 | Understand lambda functions |
| 7 | Learn recursion concepts |
| 8 | Understand local, global, and nonlocal variables |
| 9 | Improve code reusability through modular programming |

---

## 📚 Theory Notes

### 1. Function Definition

A **function** is a reusable block of code that performs a specific task. Functions help reduce code duplication and improve program organization.

**Syntax**

```python
def function_name():
    pass
```

**Example**

```python
def greet():
    print("Hello")
```

**Advantages**

| Advantage | Description |
|-----------|-------------|
| ♻️ Code Reusability | Write once, use many times |
| 📖 Better Readability | Cleaner, more organized code |
| 🐛 Easier Debugging | Isolate and fix issues in one place |
| 🧩 Modular Programming | Break programs into manageable pieces |

---

### 2. Parameters and Arguments

**Parameters** are variables defined in a function declaration, while **arguments** are the actual values passed during function calls.

**Example**

```python
def greet(name):
    print("Hello", name)

greet("Sameer")
```

> Here, `name` is a **parameter** and `"Sameer"` is an **argument**.

---

### 3. Return Values and Data Types

A function can return a value using the `return` statement.

**Example**

```python
def add(a, b):
    return a + b

result = add(5, 10)
```

**Benefits**

- ✅ Makes functions reusable
- ✅ Allows storing and processing results
- ✅ Improves program flexibility

---

### 4. Default Arguments

Default arguments allow a function to work even if no value is supplied.

**Example**

```python
def greet(name="User"):
    print("Hello", name)
```

**Output**

```
Hello User
Hello Sameer
```

---

### 5. Variable-Length Arguments (`*args`)

`*args` allows a function to accept **multiple arguments** of varying lengths.

**Example**

```python
def add_numbers(*args):
    return sum(args)
```

**Advantages**

- 🔄 Flexible input handling
- 📦 Useful when number of inputs is unknown

---

### 6. Lambda Functions

A **lambda function** is a small anonymous function defined in a single line.

**Syntax**

```python
lambda arguments : expression
```

**Example**

```python
square = lambda x: x*x
```

**Advantages**

| Advantage | Detail |
|-----------|--------|
| ✏️ Short and concise | Single-line definition |
| ⚡ Functional use | Works seamlessly with `map()`, `filter()`, `reduce()` |

---

### 7. Recursion

**Recursion** is a technique where a function calls itself to solve a problem.

**Example**

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)
```

**Advantages**

- 🧠 Simplifies complex problems
- 🌲 Useful in tree traversal and mathematical calculations

---

### 8. Variable Scope

Variable scope determines where a variable can be accessed.

| Scope Type | Description | Example |
|------------|-------------|---------|
| **Local** | Declared inside a function | `def demo(): x = 10` |
| **Global** | Declared outside all functions | `x = 10` (top level) |
| **Nonlocal** | Used inside nested functions | `nonlocal x` inside `inner()` |

**Examples**

```python
# Local Variable
def demo():
    x = 10
```

```python
# Global Variable
x = 10
```

```python
# Nonlocal Variable
def outer():
    x = 10

    def inner():
        nonlocal x
```

---

### 9. Code Reusability

**Code reusability** means writing code once and using it multiple times.

Functions are one of the most effective ways to achieve code reusability.

**Benefits**

| Benefit | Impact |
|---------|--------|
| 📉 Less duplication | Cleaner, leaner codebase |
| 🚀 Faster development | Build on existing functions |
| 🔧 Easier maintenance | Fix in one place, fixed everywhere |
| 👁️ Better readability | Self-documenting, named blocks of logic |

---

## 💻 Programs Implemented

### 1. 🏋️ BMI Calculator

**Description:** Calculates Body Mass Index (BMI) using height and weight and determines the health category.

| Concept Used | Detail |
|--------------|--------|
| Functions | Core logic encapsulated in functions |
| Parameters | Accepts height and weight as inputs |
| Return Values | Returns BMI value and health category |
| Conditional Statements | Determines health classification |

---

### 2. 💰 EMI Calculator

**Description:** Calculates monthly EMI based on Loan Amount, Interest Rate, and Loan Tenure.

| Concept Used | Detail |
|--------------|--------|
| Functions | Modular design |
| Mathematical Formula | EMI formula implementation |
| Return Statement | Returns computed EMI value |

---

### 3. 🔢 Recursive Factorial Program

**Description:** Calculates factorial using recursion.

| Concept Used | Detail |
|--------------|--------|
| Recursion | Function calls itself |
| Base Case | Stops recursion at `n == 0` |
| Function Calls | Self-referential call stack |

---

### 4. 🌀 Fibonacci Series Generator

**Description:** Generates Fibonacci sequence using functions.

| Concept Used | Detail |
|--------------|--------|
| Functions | Encapsulates sequence logic |
| Loops | Iterates to build series |
| Sequence Generation | Builds the Fibonacci sequence |

---

### 5. 🔍 Prime Number Checker

**Description:** Checks whether a number is prime or not.

| Concept Used | Detail |
|--------------|--------|
| Functions | Prime check logic in a function |
| Loops | Iterates divisors |
| Conditional Logic | Determines primality |

---

### 6. 🛠️ List Operations Using `map()`, `filter()`, `reduce()`

**Description:** Demonstrates Python functional programming concepts.

| Operation | Behaviour |
|-----------|-----------|
| `map()` | Applies a function to every element |
| `filter()` | Filters elements based on a condition |
| `reduce()` | Combines all elements into a single value |

---

## 📁 File Structure

```
Task-3/
│
├── 📄 bmi_calculator.py          # BMI Calculator
├── 📄 emi_calculator.py          # EMI Calculator
├── 📄 factorial_recursion.py     # Recursive Factorial
├── 📄 fibonacci.py               # Fibonacci Series Generator
├── 📄 prime_checker.py           # Prime Number Checker
├── 📄 map_filter_reduce.py       # Functional Programming Demo
├── 📄 default_arguments.py       # Default Arguments Example
├── 📄 args_example.py            # Variable-Length Arguments (*args)
├── 📄 lambda_example.py          # Lambda Functions Example
├── 📄 variable_scope.py          # Variable Scope Demo
└── 📄 README.md                  # Project Documentation
```

---

## 🧠 Key Concepts Covered

| # | Concept | Description |
|---|---------|-------------|
| 1 | **Functions** | Reusable blocks of named code |
| 2 | **Parameters** | Variables defined in function signature |
| 3 | **Arguments** | Actual values passed during function call |
| 4 | **Return Statements** | Sending values back from a function |
| 5 | **Default Arguments** | Fallback values when no argument is supplied |
| 6 | **Variable-Length Arguments** | Accepting arbitrary number of inputs with `*args` |
| 7 | **Lambda Functions** | Compact, anonymous single-line functions |
| 8 | **Recursion** | Functions that call themselves |
| 9 | **Variable Scope** | Local, global, and nonlocal variable visibility |
| 10 | **Code Reusability** | Writing once, using many times |
| 11 | **Functional Programming** | `map()`, `filter()`, `reduce()` paradigms |

---

## ✅ Conclusion

This task helped in understanding how **functions improve program structure, maintainability, and code reusability**. Various concepts such as recursion, lambda functions, parameter passing, variable scope, and functional programming techniques were implemented through practical examples.

The programs developed in this repository demonstrate **modular programming practices** and provide a strong foundation for writing efficient and reusable Python code.

> 💡 *Functions are not just a feature of Python — they are the foundation of writing clean, scalable, and professional code.*

---

## 👨‍💻 Author

<div align="center">

**Sameer Achara**

*Python Internship Program — Task 3*

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Internship](https://img.shields.io/badge/Program-Internship-FF6B35?style=flat-square)

</div>

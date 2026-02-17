# Python Async

This project introduces asynchronous programming in Python using the `asyncio` library.  
You will learn how to write non-blocking code, run multiple coroutines concurrently, create tasks, and measure execution time.

---

## 📘 Learning Objectives

By the end of this project, you should be able to explain:

- The `async` and `await` syntax
- How to execute an async program with `asyncio.run()`
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the `random` module

---

## 🛠 Requirements

- Python 3.9 on Ubuntu 20.04 LTS
- All files must be executable
- First line of every file must be:
- Code must follow **pycodestyle 2.5.x**
- All functions and coroutines must be **type-annotated**
- All modules and functions must contain proper documentation strings
- A `README.md` file is mandatory

---

# 📝 Tasks

## **0. The basics of async**
Write an asynchronous coroutine `wait_random` that takes an integer `max_delay` (default 10).  
It waits for a random delay between 0 and `max_delay` seconds and returns the delay.

---

## **1. Let's execute multiple coroutines at the same time with async**
Write an async routine `wait_n(n, max_delay)` that calls `wait_random` **n times** concurrently.  
Return a list of delays in **ascending order** without using `sort()`.

---

## **2. Measure the runtime**
Write a function `measure_time(n, max_delay)` that measures the total runtime of `wait_n(n, max_delay)`  
and returns the **average time per coroutine**.

---

## **3. Tasks**
Write a regular function `task_wait_random(max_delay)` that returns an `asyncio.Task`  
wrapping the coroutine `wait_random(max_delay)`.

---

## **4. Tasks**
Write an async routine `task_wait_n(n, max_delay)` similar to `wait_n`,  
but using `task_wait_random` instead of `wait_random`.

---

# 📂 Project Structure

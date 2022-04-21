# 00 Basics

This example provides the most basic test that you can create with *behave*.

It just test that the file *README.md* exists into the example directory.

## I want to run something !

If you are in a hurry and cannot wait to see this example working, here are the steps:

```bash
# Install from the github to get the lastest cool features
pip install git+https://github.com/behave/behave

# Go into the example directory
cd 00_basics

# Just run this command
behave
```

## How does it works ?

First I advice to create 2 directories:

- *features*: to store the features of your product
- *steps*: to store the implementation of each test scenario step

Behave will automatcally search for those directories to run. By default, behave run all the scenarios of all features in the directory.

Each scenario step must be implemented in python

```gherkin
Given we are working in the 00_basics directory
```

Can be implemented by a function 'step' using the python decorator @given. Be carefull the step string must be exactly the same to allow behave to match both.

```python
@given('we are working in the 00_basics directory')
def step(context):
    # ... implementation
```


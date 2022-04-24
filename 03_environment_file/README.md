# 03 Environment File

This example is based on the previous example and introduce the environment file.

## Environment.py

This file will be imported by behave before any test execution.

Initialization common to all features can be declared in this file.

## Before and After

Behave provides 2 special functions (before and after) for the following object:

- step
- scenario
- feature
- all: the all test session

This example print messages on each of those functions to show you the execution order


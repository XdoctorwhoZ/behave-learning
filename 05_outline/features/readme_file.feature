Feature: Documentation file
    As a user, I want some documentation in my learning example

    Scenario Outline: The learning example must have a "<file>" file
        Given we are working in the "<directory>" directory
        Then the "<file>" file exists

        Examples: Example files
        | directory         | file              |
        | 05_outline        | README.md         |
        | 05_outline        | behave.ini        |
        | 05_outline        | environment.py    |


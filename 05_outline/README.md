# 05 Scenario Outline

New problem ! You want to check more than one file inside the directory.

You could use step parameter and copy/paste the step multiple times, but there is a better option.

## The solution

To solve this you can use the *scenario outline* feature.

With outlines, you can run the same scenario, for each entry of the table you provide as *Examples*.

```gherkin
    Scenario Outline: The learning example must have a "<file>" file
        Given we are working in the "<directory>" directory
        Then the "<file>" file exists

        Examples: Example files
        | directory         | file              |
        | 05_outline        | README.md         |
        | 05_outline        | behave.ini        |
        | 05_outline        | environment.py    |
```

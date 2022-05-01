Feature: Documentation file
    As a user, I want some documentation in my learning example

    @use.file.check1
    Scenario Outline: The learning example must have a "<file>" file
        Given we are working in the "<directory>" directory
        Then the "<file>" file exists

        Examples: Example files
        | directory         | file              |
        | 06_tags_fixtures  | README.md         |
        | 06_tags_fixtures  | behave.ini        |
        | 06_tags_fixtures  | environment.py    |


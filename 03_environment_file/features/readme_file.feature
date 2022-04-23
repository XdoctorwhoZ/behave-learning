Feature: Documentation file
    As a user, I want some documentation in my learning example

    Scenario: The learning example must have a README file
        Given we are working in the 03_environment_file directory
        Then the README file exists

    Scenario: Fake scenario
        Given the context does not contain cwd from the last scenario

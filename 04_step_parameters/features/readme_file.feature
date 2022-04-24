Feature: Documentation file
    As a user, I want some documentation in my learning example

    Scenario: The learning example must have a README file
        Given we are working in the "04_step_parameters" directory
        Then the README file exists

    Scenario: Fake scenario
        Given we are working in the "not_exist" directory

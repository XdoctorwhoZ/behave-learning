Feature: Step and scenario fail, log print in report

    Scenario: A first scenario pass
        Given a step passes
        When a script log data

    Scenario: A second scenario Fail
        Given First step passes
		When a script log data
		Then another step fails
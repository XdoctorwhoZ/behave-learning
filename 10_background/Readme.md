# 10 background 

## Scenario background
Background concept allow execute a number of steps before each scenario.
[exemple](https://jenisys.github.io/behave.example/tutorials/tutorial09.html)

Note that fixture cannot be associate to background. 
However it is possible for backround step to access fixture of scenario.

Advantage: Allow to gather in one place all set-up step require for the test environment.
Setting up environment in step is a good practice as error will be clearly raise by behave with all logs.
(If an error occur in fixtures, less information are recover as the error will only appear as a HOOK-ERROR)

## Feature background
There is way to simulate background at feature level.

If fixtures are set before the feature declaration they will be apply once for all scenarios in the feature.
This allow to have a first "set-up" scenario that will configure our environnement.
And execute all others scenario without having to set back the environment.
This can be helpfull if a scenario has to be repeat multiple time without changing anything in the environnement.

Feature exemple:
```feature
#fixture set on feature so that env is set-up for all scenario
@fixture.x
@fixture.y
Feature: Demarrage nominal de la carte
    Ce test vérifie les conditions et état des discrets lors du cycle de démarrage nominal de la carte CHAM. 

    #equivalent to background steps
    Scenario: L'environnement de test doit être mis en place
        Given A step to link x to y
        And   another step

    #example of repetition scenario
    Scenario Outline: Test Y
        Given Repetition <index>
        Then  Do a step

        Examples: Number of repeatition
            | index |
            | 0     |
            | 1     |
            | 2     |
```

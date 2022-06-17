# 10 background 

Background concept allow execute a number of steps before each scenario.
[exemple](https://jenisys.github.io/behave.example/tutorials/tutorial09.html)

Note that fixture cannot be associate to background. 
However it is possible for backround step to access fixture of scenario.

Advantage: Allow to gather in one place all set-up step require for the test environment.
Setting up environment in step is a good practice as error will be clearly raise by behave with all logs.
(If an error occur in fixtures, less information are recover as the error will only appear as a HOOK-ERROR)

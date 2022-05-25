# 09 Logging

Behave is able to capture log / stdout / stderr.
When developping the test it is better to deactivate those capture features using:
```bash
--no-logcapture --no-capture --no-capture-stderr
```
or by setting in behave.ini:
```
log_capture=False
stderr_capture=False
stdout_capture=False
```

However once test is ended it is better to let behave capture every thing. That way html report will be able to display captured log and stdout associate to the failing scenario.

Logging capture can configure through multiple config attribut:
- logging_level: 

Specify a level to capture logging at. The default is INFO. Set to DEBUG to capture every log.
- logging_clear_handlers:

 remove all existing handlers
- logging_datefmt:

 Specify custom date/time format to print statements. Uses the same format as used by standard logging handlers.
- logging_filter:

 Specify which statements to filter in/out. By default, everything is captured. If the output is too verbose, use this option to filter out needless output. Example: –logging-filter=foo will capture statements issued ONLY to foo or foo.what.ever.sub but not foobar or other logger. Specify multiple loggers with comma: filter=foo,bar,baz. If any logger name is prefixed with a minus, eg filter=-foo, it will be excluded rather than included.
- setup_logging:

 allow to used a logging.ini file
- logging_format

Specify custom format to print statements. Uses the same format as used by standard logging handlers. The default is “%(levelname)s:%(name)s:%(message)s”.

Logging configuration must be done by behave. Either in behave.ini or in before_all().


__Capture Logging in Hooks__
If you wish to capture any logging generated during an environment hook function’s invocation, you may use the capture() decorator, like:

```
# -- FILE:features/environment.py
from behave.log_capture import capture

@capture
def after_scenario(context):
    ...
```
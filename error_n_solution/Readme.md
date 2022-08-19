# List of encounter error and their solutions

## Ambiguous Step definitions
Error log:
```bash
Exception AmbiguousStep: @step('xxx "{param1}" "{param2}"') has already been defined in existing step @step('xxx "{param1}"') at steps/Firmware/Trampoline_steps.py:17
```
> [solution](https://github.com/behave/behave/issues/435#issuecomment-219141835)
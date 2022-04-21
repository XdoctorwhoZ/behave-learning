# 01 Print and Logging

The question that comes very quickly after discovering behave is : how do I see my print ?

Indeed, by default, behave capture output logs stdout & stderr.

## How do I display my debug print ?

To display the print, 2 things:

1. Create the file **behave.ini** and append the following section

```ìni
[behave]
stderr_capture=False
stdout_capture=False
```

2. Do not forget to put '\n' at the end of your print

```python
print(f"Current directory: {cwd}", "\n")
```

## How do I display my application logs ?

To display the logs generated by the *logging* module, just append **log_capture=false** on the behave.ini

```ìni
[behave]
log_capture=false
stderr_capture=False
stdout_capture=False
```
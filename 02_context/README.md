# 02 context

This example is based on the previous example and use the context.

## The problem

In the previous example there is a problem: in both step implementations we perform the action *os.getcwd()*.

```python
# @given('we are working in the 01_print_and_logging directory')
cwd = os.getcwd()

# @then('the README file exists')
filepath = os.path.join(os.getcwd(), 'README.md')
```

It would be nice if the first step find and control the directory and pass it to the second step.

## The solution

The solution is in the title, the *context* :tada: Surprise :tada:

This step parameter is in the examples from the start but we currently did not use it.

Context parameter contains some usefull data shared across the steps of the same scenario.

```python
@given('we are working in the 02_context directory')
def step(context):
    context.cwd = os.getcwd()
```

With this, you can now pass the *cwd* from the first scenario to the second.

### Warning 1 : context cannot share data across scenarios

To show you this, I have create the *Fake scenario*. In the step of this scenario *cwd* is not present anymore.

### Warning 2 : context already contains some attributes

Those attributes are injected by behave, don't use them.

Here are information from behave documentation [tutorial](https://behave.readthedocs.io/en/stable/tutorial.html):

- **table**: This holds any table data associated with a step.
- **text**: This holds any multi-line text associated with a step.
- **failed**: This is set at the root of the context when any step fails. It is sometimes useful to use this combined with the --stop command-line option to prevent some mis-behaving resource from being cleaned up in an after_feature() or similar (for example, a web browser being driven by Selenium.)

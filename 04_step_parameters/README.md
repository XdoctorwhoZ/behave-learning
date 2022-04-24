# 04 Step Parameters

Have you noticed that on the previous example we had to change to name of the current directory everytime ?
Not just on the feature file but also in the step implementation and it is pretty boring to change it everywhere each time.

## The solution

To solve this problem you can use a parameter by changing the implementation step.

```python
@given('we are working in the "{example_directory}" directory')
def step(context, example_directory):
```

That way the directory name can be extracted as a varibale and the step become generic.

```gherkin
Given we are working in the "04_step_parameters" directory

Given we are working in the "not_exist" directory
```

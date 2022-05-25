# Behave Python Learning

This repository provides stuctured steps to learn how to use behave and gherkin:

## What is it my precious ?

Behave is a python framework for the BDD technique

https://behave.readthedocs.io/en/stable/

> Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. We have a page further describing this philosophy.

Check also the cucumber project to get some usefull information

https://cucumber.io/docs/bdd/history/

You can also find other examples in the following links:

https://jenisys.github.io/behave.example/index.html

## Learning Steps

This repository provides an initiation to behave though the following examples. Those examples does not explore the all power of behave. You can see them as a smooth initiation.

Each step is based on the previous one, improving the way it is done by a new behave concept.

- [00 basics](./00_basics) : Minimal getting started with Behave and Gherkin
- [01 print and logging](./01_print_and_logging) : Introduce behvae.ini and how to display some debug logs.
- [02 context](./02_context) : Introduce the context attribute
- [03 environment file](./03_environment_file) : Introduce the environment file and special functions (before and after)
- [04 step parametrization](./04_step_parameters) : Introduce step parametrization
- [05 scenario outline](./05_outline) : How to run the same scenario multiple times with parameters ?
- [06 tags and fixtures](./06_tags_fixtures) : How to inject fixture with tags ?
- [07 html report](./07_html_report) : Generate html report
- [08 hamcrest](./08_hamcrest) : Hamcrest
- [09 advanced logging](./09_logging) : How to use the logging capture to fill the test report

## Install Dependencies

```bash
# Install from the github to get the lastest cool features
pip install git+https://github.com/behave/behave
# Install the html formater, for your bosses :-)
pip install behave-html-formatter
# Top Asserts !
pip install PyHamcrest
```

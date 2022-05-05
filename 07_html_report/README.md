# 07 Generate a html report

To generate a html report first install the official formatter

```bash
# Install the html formater, for your bosses :-)
pip install behave-html-formatter
```

Then declare a new formatter in the behave.ini

```ini
[behave.formatters]
html = behave_html_formatter:HTMLFormatter
```

Finally run behave with the formatter option

```bash
behave -f html -o report.html
```


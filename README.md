# Ota-Template

*Copyright © 2023 by Boston Consulting Group. All rights reserved*
# SmartBanking PLotting tool

## Setup

### Requirements

* Python (>=3.6)

### Development environment

Create a virtual environment by running:

```shell
python -m venv .venv
```

The virtual environment should be activated every time you start a new shell session before running subsequent commands:

> On Linux/MacOS:
> ```shell
> source .venv/bin/activate
> ```
> On Windows:
> ```shell
> .venv\Scripts\activate.bat
> ```

Then install the packages listed in the requirements.txt
```shell
pip install -r requirements.txt
```

Then install the repository locally
```shell
pip install -e .
```


for confusion on linting missing imports
linting https://github.com/orgs/community/discussions/46885
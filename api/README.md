# Financier API

AI-powered personal finance management API

## ⚙️ Installation

The project is managed with `poetry`.
Make sure to install `poetry` with `pipx`!

1. Create a `.venv` folder in the `financier/api` folder. I just do this so `poetry` installs the new environment to a place that's easy for me.
1. Install the requirements,
   ```
   poetry install
   ```
   I did not separate the dev-dependencies and the main dependencies since everything in the `pyproject.toml` is only for DEV'ing. The requirements needed for the Lambda code is found in `financier/api/layers/requirements.txt`.
1. Create an `.env` file with the following contents,
   ```
   STAGE=<stage>
   APP_NAME=<whatever name you want>
   AWS_DEFAULT_REGION=<aws region>
   PYTHONPATH=${workspaceDirectory}/financier/api/financier
   ```
   - PYTHONPATH is highly recommended. I use it for my VS Code Python path settings, plus the building and the Lambda code itself looks for it as the main root.
1. [TODO] Define your Lambda layer. ⚠️ I am manually creating the lambda layer deployment .zip for now, but creating site-packages used by the handler code. Note that the project is using `pyndantic` and the lambdas deployed are based on `arm64` architecture. Also, make sure to compile using `python 3.12`. We must build the lib using this,
   ```
   pip install --platform manylinux2014_x86_64 --implementation cp --python-version 3.12 --only-binary=:all: --upgrade pydantic --target <directory>
   ```
   Here is the [source](https://docs.pydantic.dev/latest/integrations/aws_lambda/#installing-python-libraries-for-aws-lambda-functions).

## 🧪 Testing

The API use `pytest`, `pytest-sugar`, and `pytest-cov` for the testing suites. They are already listed as dependencies, so you can just run it like any other projects you test with them.

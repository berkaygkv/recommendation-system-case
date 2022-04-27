# test-case
Requires [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Setup

```sh
# NOTE: if running ploomber <0.16, remove the --create-env argument
ploomber install --create-env
# activate conda environment
conda activate test-case

```

## Code editor integration

* If using Jupyter, [click here](https://docs.ploomber.io/en/latest/user-guide/jupyter.html)
* If using VSCode, PyCharm, or Spyder, [click here](https://docs.ploomber.io/en/latest/user-guide/editors.html)


## Install libraries

```sh
pip install pandas numpy pycaret[full] sklearn
```

## Install local libraries

```sh
pip install -e .
```

## Data instructions
Navigate to the root folder in the command prompt -> Place the csv files inside the 'raw' folder under 'input_data' directory


## Running the pipeline

```sh
ploomber build -e pipeline.yaml
```

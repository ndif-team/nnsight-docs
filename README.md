# NNsight Docs

## Getting Started

This project uses `uv` as a default python environment. You can get started [here](https://docs.astral.sh/uv/getting-started/installation/).

From root, run `uv sync` to set up the required packages. `nnsight` isn't included as a package, but you'll need to have `nnsight` in your `.venv` to build the project. I suggest cloning `nnsight`, then running `uv pip install -e .` from the `nnsight` package while in the docs environment.

Then, start a hotreloading webserver by running `bash run.sh`.


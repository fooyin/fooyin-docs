# fooyin Documentation

The source for the official **fooyin** documentation, built with **Sphinx** and deployed on **Read the Docs**.

The published documentation is available at [fooyin.readthedocs.io](https://fooyin.readthedocs.io/).

## Requirements

- Python 3.10 or newer
- pip
- Make
- Git

### Arch Linux

Install the required packages:

```bash
sudo pacman -S --needed git make python python-pip
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/fooyin/fooyin-docs.git
cd fooyin-docs
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the documentation dependencies:

```bash
python -m pip install -r docs/requirements.txt
```

## Local Development

Build the HTML documentation:

```bash
make -C docs html
```

Open the generated site at:

```text
docs/build/html/index.html
```

To rebuild from scratch:

```bash
make -C docs clean html
```

Build with warnings treated as errors before submitting changes:

```bash
make -C docs html SPHINXOPTS="-W --keep-going"
```

## Project Structure

```text
.
├── .readthedocs.yaml       # Read the Docs build configuration
├── docs/
│   ├── Makefile            # Sphinx build commands for Unix-like systems
│   ├── make.bat            # Sphinx build commands for Windows
│   ├── requirements.txt    # Python documentation dependencies
│   ├── source/
│   │   ├── conf.py         # Sphinx configuration
│   │   ├── index.rst       # Documentation landing page and navigation
│   │   ├── quick-start/    # Getting-started guides
│   │   ├── scripting/      # FooScript reference
│   │   └── searching/      # Query-language reference
│   └── build/              # Generated documentation (not committed)
└── LICENSE
```

## Deployment

Changes pushed to the `master` branch are automatically built and published by **Read the Docs**.

# Titanic ML Collaboration Project

## Overview

This project is a reproducible machine learning project based on the Titanic dataset.

The goal is to build a binary classification model that predicts whether a Titanic passenger survived.

The project demonstrates Git-based collaboration, DVC data versioning, reproducible ML pipelines, automated testing, CI, and production release practices.

## Project Goals

* Version project code with Git and GitHub
* Version datasets and ML artifacts with DVC
* Build a reproducible machine learning pipeline
* Track parameters and experiments
* Create exploratory data analysis using Jupyter and Jupytext
* Write automated tests with pytest
* Run code-quality and security checks with pre-commit
* Run automated CI checks with GitHub Actions
* Produce a reproducible production release

## Team

* Abdullah — ML development, pipeline, CI, repository management
* Talha Ali Bhatti — testing, EDA, and collaborative development

## Dataset

**Dataset:** Titanic dataset
**Task:** Binary classification
**Target:** `Survived`

The dataset contains passenger information such as passenger class, sex, age, fare, and embarkation port.

The dataset source and complete reproducibility information are documented in `REPORT.md`.

## Machine Learning Pipeline

The project uses a DVC pipeline with three stages:

```text
Raw Titanic Dataset
        ↓
Prepare
        ↓
Train
        ↓
Evaluate
        ↓
metrics.json
```

### Prepare

Splits the dataset into training and testing sets using a fixed random seed.

### Train

Trains a Logistic Regression model using:

* Numerical feature imputation
* Standard scaling
* Categorical feature imputation
* One-hot encoding
* Logistic Regression

### Evaluate

Evaluates the trained model using:

* Accuracy
* Precision
* Recall
* F1-score

## Reproducibility

The project uses:

* Git and GitHub for source-code versioning
* DVC for dataset and ML artifact versioning
* Pinned Python dependencies
* Fixed random seeds
* `params.yaml` for experiment parameters
* `dvc.yaml` for the ML pipeline
* `dvc.lock` for reproducible pipeline state
* Jupytext for notebook/code synchronization
* Pre-commit for code-quality and security checks
* GitHub Actions for continuous integration

To reproduce the pipeline:

```bash
dvc pull
dvc repro
```

## Project Structure

```text
titanic-ml-collab/
│
├── configs/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── src/
├── tests/
├── .github/
│   └── workflows/
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── dvc.yaml
├── dvc.lock
├── params.yaml
├── requirements.txt
├── metrics.json
├── README.md
└── REPORT.md
```

## Code Quality and Security

Pre-commit checks include:

* Ruff linting
* Ruff formatting
* Notebook output stripping with nbstripout
* Large-file detection
* Private-key detection

Large files above 1 MB are blocked from commits.

## Testing

Tests are written using pytest.

Run tests with:

```bash
pytest -q
```

## Continuous Integration

GitHub Actions runs checks on pull requests targeting:

* `dev`
* `staging`
* `main`

CI checks include:

* Dependency installation
* Ruff code-quality checks
* Automated tests
* Dataset presence checks
* ML pipeline smoke test

## Branch Strategy

The project follows a Git-based collaboration workflow:

```text
main
  ↑
staging
  ↑
dev
  ↑
feature / data / experiment branches
```

Main branches:

* `main` — production/released models
* `staging` — release candidate
* `dev` — integration branch
* `feat/<name>` — feature development
* `data/<name>` — dataset changes
* `exp/<member>-<idea>` — experiments
* `fix/<name>` — production hotfixes

## Collaboration

All production changes are made through pull requests.

The project uses Conventional Commits and squash merging.

Pull requests are reviewed before merging according to the project collaboration workflow.

## Release

The production release will be tagged using:

```text
model-v1.0
```

The release process includes:

1. Merge `dev` into `staging`
2. Reproduce the pipeline from a fresh clone
3. Verify the final metrics
4. Merge `staging` into `main`
5. Create the `model-v1.0` tag

## Project Status

The core ML pipeline, DVC dataset versioning, exploratory analysis, automated testing, pre-commit checks, and CI workflow have been implemented.

The final release and project report will document the complete reproducibility and collaboration evidence.

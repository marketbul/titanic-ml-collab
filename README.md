# Titanic ML Collaboration Project

## Overview

This project is a reproducible machine learning project based on the Titanic dataset.

The goal is to build a binary classification model that predicts whether a Titanic passenger survived.

## Project Goals

* Version the project code with Git and GitHub
* Version the dataset and models with DVC
* Build a reproducible machine learning pipeline
* Track experiments and parameters
* Run automated tests and checks with GitHub Actions
* Produce a reproducible production release

## Project Structure

```text
titanic-ml-collab/
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
├── CONTRIBUTING.md
├── README.md
└── requirements.txt
```

## Dataset

Dataset: Titanic

Task: Binary classification

Target: Passenger survival

The dataset source and starter-code source will be documented in `REPORT.md`.

## Reproducibility

The project will use:

* Git for source-code versioning
* DVC for data and model versioning
* A pinned Python environment
* Fixed random seeds
* DVC pipeline stages
* Automated CI checks

## Status

Project setup in progress.

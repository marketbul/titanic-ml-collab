# Contributing Guide

## Branching Strategy

This project follows the assignment branching model:

* `main` — production and released models
* `staging` — release candidate
* `dev` — integration branch
* `feat/<name>` — feature and production-code changes
* `data/<name>` — dataset changes tracked with DVC
* `exp/<member>-<idea>` — experiments
* `fix/<name>` — production fixes

Changes should move toward production through:

```text
feature/data/experiment
        ↓
       dev
        ↓
     staging
        ↓
       main
```

## Commit Convention

We use Conventional Commits.

Examples:

```text
feat: add preprocessing step
data: track Titanic dataset with DVC
test: add preprocessing tests
ci: add GitHub Actions workflow
docs: update README
exp: test random forest parameters
fix: correct preprocessing bug
```

## Pull Requests

Pull requests should explain:

1. What changed
2. Why the change was made
3. Metrics before and after, when applicable
4. Testing performed
5. Any data or model changes

## Code Quality

Before submitting changes:

* Run the project tests
* Run linting and formatting checks
* Do not commit secrets
* Do not commit datasets directly to Git
* Use DVC for versioned datasets and models
* Do not use hardcoded absolute paths

## Merge Strategy

For this project, pull requests will use **squash merging** so that each completed change is represented by a clean commit on the target branch.

## Reproducibility

Every experiment and released model should record:

* Code version
* Parameters
* Dataset version
* Random seed
* Environment/dependency versions
* Final metrics

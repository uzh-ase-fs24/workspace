# findMe development Workspace 🤖

## Quick Access Links

- [wiki](https://github.com/uzh-ase-fs24/workspace/wiki)
- [findme-backend](https://github.com/uzh-ase-fs24/backend)
- [findme-frontend](https://github.com/uzh-ase-fs24/frontend)
- [findme-shared](https://github.com/uzh-ase-fs24/shared)

## Overview

The development workspace is configured as a pycharm project. It is intended to be used as the project folder.
Each repository used for development will be cloned inside this workspace.

```yaml
workspace
-- .idea # pycharm project configuration
-- scripts # configuration / commit scripts
  # findme repositories
-- backend
-- frontend
-- shared
-- workspace.wiki # findme wiki
docker-compose.yml # to run application locally
```

## Setup

### Prerequisites

- python3.12
- [pre-commit](https://pre-commit.com/#installation)
- [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
- check each repository for their prerequisites

### Initialization

After cloning this repository run `python scripts/initialize_project.py` this will:

- configure your git config
- clone all necessary repositories
- initialize pre-commit checks in each repository (you can do it manually by running `pre-commit install` in each
  repository)

## Running the application

For pycharm users the run configurations are already set up. use `start:findme:local` to launch both frontend and
backend.

Alternatively, the findme application can be started locally by running `docker compose up` from this root directory.

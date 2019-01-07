#!/usr/bin/env bash

set -e

mypy .
python -m unittest tests
flake8 .

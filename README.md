# Severe Weather Diagnostics

A Python package for analyzing severe weather environments using sounding data.

## Overview

`severe_weather_diagnostics` provides the tools to calculate key atmospheric variable used in severe weather forecasting. This includes wind shear, lapse rate, composite indices, and risk evaluation, as well as plotting tools for sounding profiles.

## Features

- Calculate bulk wind shear between atmospheric layers
- Compute environmental lapse rate
- Estimate a simplified STP severe weather index
- Evaluate the severe weather risk (low, marginal, elevated, significant)
- Plot temperature and dewpoint sounding profiles
- Load sounding data from CSV files

## Installation

Clone the repository and install:

```bash
pip install -e .
pip install git+https://github.com/deda2367/severe-weather-diagnostics.git
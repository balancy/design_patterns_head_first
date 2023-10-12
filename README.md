# Implementation of design patterns in Python

[![Design patterns](https://github.com/balancy/design_patterns_head_first/actions/workflows/ci.yml/badge.svg)](https://github.com/balancy/design_patterns_head_first/actions/workflows/ci.yml)

![Head First. Design patterns.](./book_cover.jpg)

## Description

1. [x] [Strategy](patterns/chapter_01_strategy/)

**Strategy is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside the original context object.**

Different implementations of the Duck abstract class use different fly and quack behavior. Specific behavior is injected during Duck instance initialization.

2. [x] [Observer](patterns/chapter_02_observer/)

**The observer pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.**

Different sensor displays are subscribed to the weather station. When the weather station changes its measurements, all displays are notified.

## Run

You need to have installed:
- Python3.8+

1. Clone the repo
```sh
git clone https://github.com/balancy/design_patterns_head_first.git
```

2. Run specific pattern example
```sh
python3 -m patterns.chapter_01_strategy.main
```

## Test and Lint

You need to have also installed:
- Poetry as dependencies manager

Run linting
```sh
make lint
```

Run type checking
```sh
make typecheck
```

Run tests
```sh
make test
```

Run all together
```sh
make check
```
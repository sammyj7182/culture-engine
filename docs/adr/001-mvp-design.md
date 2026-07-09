# ADR 0001: Use a modular monolith for the MVP

## Status
Accepted

## Context
Culture Engine is currently a small MVP being built by one developer. The first release only needs film search, watched films, ratings, reviews, and viewed dates.

## Decision
We will build the MVP as a modular monolith rather than splitting it into multiple services.

## Reasoning
This keeps the system simple while still allowing clear internal boundaries between UI, backend, database, and external API logic.

## Consequences
- Easier to build, run, test, and deploy at this stage.
- Less operational complexity.
- If the product grows, parts of the system could be split later.
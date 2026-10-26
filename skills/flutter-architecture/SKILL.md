---
name: flutter-architecture
description: Shape or refactor Flutter application structure, feature boundaries, UI and data separation, dependency flow, and repository contracts. Use when a feature spans layers or the existing architecture is hard to maintain.
---

# Flutter Architecture

Choose architecture to manage real complexity, not to maximize folders, abstractions, or diagrams. Existing project conventions are the default unless they obstruct the required behavior.

## Inspect first

Review the current folder structure, a representative feature, model and repository patterns, dependency injection, routing, state management, test boundaries, and SDK constraints. Identify current pain before proposing a migration.

## Start with clear responsibility boundaries

A pragmatic Flutter feature may contain:

- **Presentation:** widgets and view-level state; translates user intent into actions and renders state.
- **Application or feature logic:** orchestration and business rules complex enough to reuse or test independently.
- **Data access:** repositories exposing domain-oriented operations and services talking to APIs, databases, files, plugins, or platform APIs.

Do not require all layers for every feature. A simple preference may not need a domain use case. Introduce a domain layer when it isolates meaningful business rules, complex orchestration, or reuse across interfaces.

## Dependency direction

- Widgets should not own HTTP details, raw database queries, or long-lived platform integration code.
- Repositories should hide data-source mechanics behind a stable contract when that separation adds value.
- Keep business rules testable without constructing the full widget tree.
- Inject dependencies at a clear composition point using the project's convention.
- Avoid service locators, global mutable state, singleton sprawl, and duplicate sources of truth.
- Treat errors explicitly. Do not swallow exceptions or convert every failure into empty success.

## Organize by feature when it helps

Keep related presentation, state, and data code close enough to understand as a unit. Extract shared code only after identifying a reusable concept. Avoid both a giant shared folder and an abstraction per file.

Names should reveal responsibility. Prefer repository contracts that express user operations over thin interfaces duplicating every method of a third-party client.

## Migration and package choices

Do not change architecture and implement a feature in the same patch unless both are necessary. Do not add a state-management, networking, or DI package solely because it is popular. Verify maintenance, SDK constraints, license, migration cost, and testability before adding one. Extend the existing approach unless a concrete problem justifies changing it. Follow the repository's policy for serialization and code generation.

## Deliverable

Explain the selected boundaries, why each abstraction exists, and how dependencies flow. Test behavior at the layer where it is easiest to prove. The architecture should make the next change simpler, not merely make the current diff look sophisticated.

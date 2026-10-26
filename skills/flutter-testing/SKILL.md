---
name: flutter-testing
description: Design or improve unit, widget, and integration tests for Flutter and Dart code. Use to prove user behavior, isolate regressions, test async state, validate localization, or improve unreliable suites.
---

# Flutter Testing

Tests should give confidence in observable behavior and protect against likely regressions. Optimize for diagnostic value, not line coverage as a vanity metric.

## Choose the right layer

- **Unit tests:** deterministic business rules, transformations, validators, formatters, and state transitions.
- **Widget tests:** rendering and interaction, validation messages, semantics, loading/error/empty states, localization, themes, and navigation behavior.
- **Integration tests:** critical end-to-end paths involving navigation, platform plugins, persistence, or backend wiring that lower layers cannot prove adequately.
- **Golden tests:** selected stable visual contracts such as a design-system component or key screen. Use sparingly and account for fonts, platform differences, text scale, theme, and locale.

Choose the narrowest layer that proves the risk. Do not create slow integration tests for logic a unit test can cover.

## Write useful tests

Follow repository conventions for names, fixtures, and mocks. Assert user-observable outcomes and important invariants, not incidental private method calls. Use deterministic inputs and control time, randomness, and asynchronous completion where they matter.

For async state, test initial, success, failure, retry, and stale-response behavior where relevant. For forms, cover invalid values, submission success/failure, disabled submission, and duplicate taps. For localization, cover supported locales and RTL where layout direction matters. For custom components, test semantics and disabled/selected states as well as callbacks.

Avoid real network calls in ordinary unit/widget tests. Use stable boundaries or explicit integration environments. Prefer lightweight fakes when useful; do not mock every dependency by default.

## Make failures actionable

Use descriptive test names and assertions. Keep setup smaller than the behavior under test. Avoid arbitrary sleeps; use deterministic pumps, completers, or framework synchronization. Do not hide flaky tests by rerunning until they pass without understanding the cause.

## Run and report

Start with targeted tests, then expand to related tests and analysis. Use commands supported by the project and SDK. A successful formatter is not a test result; passing unit tests do not prove device behavior or backend integration.

When a test fails, reproduce it, distinguish product code from setup/environment issues, fix the underlying cause instead of weakening meaningful assertions, then rerun the failed test and relevant regression set.

## Done

Tests pass in the recorded environment, important changed behavior is covered, and unrun checks are listed explicitly. Do not fabricate output or coverage numbers.

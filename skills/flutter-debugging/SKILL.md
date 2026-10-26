---
name: flutter-debugging
description: Investigate and fix Flutter or Dart crashes, exceptions, broken layouts, navigation failures, build errors, and asynchronous regressions using reproducible evidence.
---

# Flutter Debugging

Debug from evidence. Avoid speculative rewrites, random dependency upgrades, and changes that merely hide symptoms.

## 1. Reproduce the problem

Collect the exact error, stack trace, steps to reproduce, affected platform, build mode, locale/theme, and recent relevant changes. Read the error before changing code. Distinguish a reliable reproduction from a one-off symptom.

If the issue cannot be reproduced, form a minimal hypothesis and identify evidence that would confirm or disprove it.

## 2. Trace the failure

Follow the stack trace into the first relevant application frame. Inspect callers, state transitions, data contracts, platform boundaries, and lifecycle. For visual defects, inspect constraints, parent layout, insets, text scaling, directionality, and actual dimensions.

Check common Flutter failure classes: unbounded constraints and overflow; state updates after disposal and stale async results; duplicate listeners and unclosed controllers; navigation stack and deep-link assumptions; nullability, parsing, serialization, and API drift; permissions and plugin differences; and initialization order or SDK incompatibility.

## 3. Narrow the cause

Create a small reproduction or test when useful. Change one plausible cause at a time. Use logs, breakpoints, assertions, DevTools, and existing diagnostics when available. Do not add noisy logs containing tokens, credentials, or personal data.

Avoid catching broad exceptions solely to suppress a crash. Do not replace an error with empty data unless empty data is the real domain meaning.

## 4. Fix the root cause

Choose a fix consistent with the existing architecture. Handle the failure boundary correctly and make recovery predictable. Preserve valid user input and state where appropriate. Do not silence analyzer warnings or weaken tests without a documented reason.

## 5. Verify the fix

Add a regression test that fails before the fix when practical. Run the focused test or reproduction first, then analysis and related tests. If the failure depends on a device, plugin, backend, or release build, record the limitation and test it in the available environment.

## Report

State the root cause with evidence, files changed, regression protection added, and exact verification performed. Separate a confirmed cause from a likely explanation. A device issue is not proven fixed solely because static analysis passed.

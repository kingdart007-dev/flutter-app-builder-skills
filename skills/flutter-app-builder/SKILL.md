---
name: flutter-app-builder
description: Plan and deliver Flutter or Dart features end to end. Use when an agent must inspect an existing repository, turn a goal into an implementation plan, coordinate UI architecture testing and quality work, then verify the actual result.
---

# Flutter App Builder

Deliver a correct, coherent change in the target repository. Do not stop at advice when implementation was requested and tools permit edits.

## Operating principles

- The user's acceptance criteria and documented product standards are authoritative.
- Inspect the real repository before choosing an architecture, package, SDK, or file layout.
- Preserve unrelated work and avoid destructive rewrites.
- Prefer the smallest maintainable solution that meets the requirement.
- Separate facts observed in the project from assumptions needing verification.
- Never claim a test, build, device check, or command passed unless it ran and its result was observed.

## Workflow

### 1. Establish context

Inspect repository status, top-level files, README, project instructions, dependency manifests, SDK constraints, feature structure, routing, state management, localization, themes, tests, and CI. Read relevant implementation before editing. Do not assume a fresh project.

For Flutter, use the repository's declared Flutter/Dart constraints and lockfile as the compatibility boundary. Check the installed toolchain when execution is available. Do not upgrade dependencies merely to use a preferred API.

### 2. Define the outcome

Translate the request into observable acceptance criteria. Identify user-visible behavior and relevant loading, empty, error, retry, success, offline, navigation, persistence, permissions, privacy, localization, and accessibility states. Identify existing patterns to reuse and tests that would prove the behavior.

If details are missing but a safe default exists, state the assumption briefly and proceed. Ask a question only when a missing fact blocks safe or meaningful implementation.

### 3. Choose only the needed playbooks

Use specialized skills for UI/UX, architecture, state management, localization, testing, debugging, performance, security, and review as needed. Do not invoke every discipline for a trivial change. Do not create artificial layers or add packages for ceremony.

### 4. Plan a focused change

Make a short plan tied to acceptance criteria. Identify the smallest relevant file set and likely regression risks. In an unfamiliar app, trace one comparable feature end to end before making structural choices.

### 5. Implement the whole behavior

Build the user journey, not just the happy path. Include correct state transitions, error handling, validation, cancellation or stale-request protection when needed, and input preservation. Keep business and data access logic out of presentation widgets when the project architecture calls for separation.

Avoid placeholder actions, fake success messages, dead buttons, hard-coded secrets, and undocumented assumptions. Do not replace working patterns or rename broad areas unrelated to the request.

### 6. Verify with evidence

Run targeted formatting, analysis, and tests supported by the project and environment. Prefer the narrowest failing test first, then the relevant suite. Inspect the final diff for unrelated changes, broken links, stale imports, missing localization entries, and accidental secrets.

When a tool is unavailable, report the limitation and the best verification completed. Never describe unexecuted checks as passing. Separate static checks from simulator, device, store, and backend verification.

### 7. Report the result

Summarize what changed, key design decisions, exact checks run and outcomes, and remaining limitations. Link directly to changed files or commits when possible. Be explicit about assumptions and unfinished work.

## Definition of done

A change is done when acceptance criteria are met, the diff is focused, relevant states and accessibility are considered, meaningful tests cover the risk, available checks have run, and the result can be explained honestly. A successful code edit alone is not proof that an app builds or works on a device.

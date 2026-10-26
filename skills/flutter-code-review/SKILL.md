---
name: flutter-code-review
description: Review Flutter and Dart changes for correctness, regressions, security, accessibility, maintainability, async safety, and test gaps. Use before merging a patch or evaluating agent-written code.
---

# Flutter Code Review

Review the diff as a skeptical maintainer. Find actionable defects, not stylistic preferences. A review is not complete just because the code compiles.

## Establish context

Read the change description and acceptance criteria. Inspect the full diff, surrounding code, architectural conventions, dependency and SDK constraints, and tests. Trace modified behavior through callers and consumers instead of reviewing changed lines in isolation.

## Look for concrete risks

- Incorrect business logic, invalid assumptions, broken edge cases, and changed contracts.
- Missing or inconsistent loading, empty, failure, retry, and success transitions.
- Duplicate submissions, stale asynchronous responses, lifecycle leaks, and race conditions.
- Navigation and persistence regressions, input loss, offline behavior, and partial failures.
- Unlocalized text, broken RTL assumptions, clipping at large text scales, and inaccessible controls.
- Expensive repeated work, unbounded caches, eager construction of large lists, and resource leaks.
- Secrets, sensitive logging, excess permissions, unsafe deep links, and client-side authorization assumptions.
- Dependencies or abstractions that add risk without clear need.
- Missing tests for important behavior or tests coupled to implementation details.

## Prioritize findings

- **Critical:** credible path to severe compromise, irreversible data loss, or broad outage.
- **High:** serious functional, security, or data-integrity defect on a meaningful path.
- **Medium:** important user-visible defect or likely regression with limited scope or a workaround.
- **Low:** localized edge case or maintainability concern unlikely to block release.

Do not inflate severity. Distinguish a proven defect from a concern needing reproduction.

## Write useful feedback

For each finding, include severity and affected file/line when available, the concrete triggering scenario, why current behavior is incorrect or risky, and a practical direction for fixing it. Lead with the highest-impact findings.

If no actionable issues are found, say so and mention meaningful coverage gaps or checks not run. Do not manufacture findings to fill a quota.

## Verify the review

Run or inspect relevant tests and analyzer output if available. Formatting, a green compile, or an agent's own assertion is not proof of all user-facing behavior. Separate blockers from optional cleanup, and never silently modify code when the requested task was review-only.

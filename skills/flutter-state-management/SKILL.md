---
name: flutter-state-management
description: Select, implement, or debug state management and asynchronous flows in Flutter. Use for shared state, forms, caching, loading and error states, request races, lifecycle bugs, and routing-related state.
---

# Flutter State Management

Use the simplest state owner that matches the lifetime and sharing needs of the data. State ownership should be obvious to the next maintainer.

## Decide who owns the state

- **Ephemeral widget state:** expansion, selection within a local control, animation progress, and values that do not need external sharing can stay in the widget.
- **Feature state:** form drafts, filters, paging, request status, and workflows belong in the feature's established state-management pattern.
- **Shared application state:** session and preferences belong at a deliberate shared boundary only when consumers truly share them.
- **Persisted state:** use durable storage only when product behavior requires it. In-memory state and persistence are different guarantees.

Do not promote every value to global state or duplicate the same fact across widgets, providers, repositories, and models without a clear ownership rule.

## Work with the existing tool

Inspect package versions and existing examples first. Follow current Provider, Bloc, Riverpod, or other conventions. Avoid introducing a second state-management framework for one screen.

For Riverpod projects, use APIs appropriate to the installed major version. In Riverpod 3 code, prefer Notifier or AsyncNotifier patterns where appropriate; do not blindly copy legacy snippets or mechanically migrate stable code. Consult current documentation for version-sensitive APIs.

## Model transitions explicitly

- Represent loading, data, empty, and failure as distinct states when consumers must react differently.
- Keep validation errors separate from infrastructure errors.
- Prevent duplicate submissions while an action is in flight.
- Preserve form input and retry context on recoverable failures.
- Avoid redundant state changes that trigger unnecessary rebuilds or side effects.
- Keep one-time effects separate from durable render state when the architecture supports it.

## Asynchronous safety

Expect requests to complete out of order. Use cancellation, request identity, generation checks, or another suitable strategy so stale results cannot overwrite newer state. Handle disposal and provider/controller lifecycles correctly. Invalidate caches deliberately after writes, avoiding refresh loops and duplicate requests. Define retry, timeout, empty data, connectivity-loss, and partial-failure behavior where relevant. Remember that cancelling a UI request may not cancel server-side work.

## Keep state testable

Test state transitions without animation timing or a full app. Cover initial state, success, failure, retry, duplicate actions, and stale-request behavior where relevant. Mock at stable boundaries, not every internal method.

## Completion questions

Can a reader tell who owns each state, how it changes, when it is cleared, what survives navigation, and what happens when an asynchronous operation fails or finishes late? If not, clarify the model before adding abstractions.

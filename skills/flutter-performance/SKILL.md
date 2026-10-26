---
name: flutter-performance
description: Diagnose and improve Flutter app startup, frame rendering, scrolling, rebuilding, image loading, memory usage, and expensive asynchronous work with measurement-led changes.
---

# Flutter Performance

Optimize what measurements show is slow. Avoid premature caching, broad rewrites, and complexity added without evidence.

## Establish a baseline

Reproduce on a representative device or the closest available environment. Measure the affected interaction in profile mode when possible, using Flutter DevTools performance, CPU, memory, or network views as relevant. Record the scenario and baseline.

If profiling tools or hardware are unavailable, identify a specific likely hotspot and disclose the limitation rather than presenting a guessed gain as measured.

## Diagnose by symptom

- **Janky frames:** inspect expensive build/layout/paint work, synchronous computation, image decode, shader work, and repeated work during scrolling.
- **Excessive rebuilds:** trace changing dependencies and state scope; narrow invalidation only where measurements support it.
- **Slow startup:** identify initialization, synchronous asset or disk work, dependency setup, and network calls blocking the first useful screen.
- **Memory growth:** inspect retained objects, controllers/listeners, caches, subscriptions, and lifecycle cleanup.
- **Slow lists:** inspect eager construction, item complexity, nested scrollables, image size, and unstable item identity.
- **Slow requests:** separate network latency, serialization, scheduling, caching, and rendering costs.

## Choose targeted fixes

Use lazy lists for large collections and avoid repeating expensive work in build methods. Move expensive computation off the UI isolate only when its measured cost warrants it and the operation can be moved safely. Limit image decode sizes to display needs. Reduce unnecessary invalidation without compromising clarity. Avoid blocking the first frame on nonessential work. Dispose subscriptions/controllers and define bounded cache policies.

Do not blindly add const, memoization, isolates, custom painting, or caching as a ritual.

## Validate the change

Repeat the same measurement scenario and compare results. Test correctness, accessibility, loading states, and failure recovery. Consider low-end hardware and large data sets when relevant.

Report before/after numbers only if both were captured under comparable conditions. Otherwise explain the expected effect and what still needs profiling.

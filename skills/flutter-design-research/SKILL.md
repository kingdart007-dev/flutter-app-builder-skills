---
name: flutter-design-research
description: Research UI references, product flows, platform conventions, and current Flutter capabilities before designing or implementing screens. Use when matching a supplied reference, planning a new interface, evaluating visual patterns, or turning research into an actionable Flutter design brief.
---

# Flutter Design Research

Research before prescribing pixels. Translate references and product intent into a compact, evidence-backed design brief that another agent or developer can implement and verify. The goal is to understand the product's interaction model and visual rules—not to copy another app wholesale.

## 1. Establish the task and evidence

- Inspect the current repository first: product requirements, existing screens, theme/tokens, navigation, localization, supported platforms, SDK constraints, and reusable components.
- Capture the actual question: what user task must improve, which platforms/locales/themes are in scope, and what must remain unchanged.
- Use the user's reference links, screenshots, recordings, and explicit specifications as primary inputs. If an asset or route is inaccessible, record that limitation rather than claiming to have inspected it.
- Prefer a complete, representative flow over a single hero screen. For a supplied app/reference, aim to inspect roughly 6–12 relevant screens or states when available; include entry, primary action, validation/loading, success, back/exit, and a meaningful edge case. This is a heuristic, not a quota.
- Use synthetic data. Never capture or publish credentials, personal data, private notifications, or proprietary customer information.

## 2. Use an explicit source hierarchy

1. User-provided product requirements and reference material.
2. Existing repository behavior and established design tokens.
3. Current official platform/framework guidance, especially Flutter, Android, Apple, and an explicitly chosen design system.
4. Current documentation for packages already present in the project.
5. Credible secondary examples and community discussion, clearly marked as inspiration rather than requirements.
6. Personal aesthetic judgment, labeled as a design hypothesis when it has not been validated.

When APIs, component behavior, accessibility guidance, platform conventions, or package maintenance may have changed, consult current primary documentation rather than relying on memory. Useful starting points:

- [Flutter UI and widget guidance](https://docs.flutter.dev/ui)
- [Flutter adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive)
- [Flutter animation introduction](https://docs.flutter.dev/ui/animations)
- [Flutter internationalization](https://docs.flutter.dev/ui/internationalization)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple motion guidance](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Material Design 3](https://m3.material.io/)

Do not invent a dependency on a proprietary MCP, research service, browser extension, or paid tool. Use tools available in the current environment; report blockers and continue with the evidence that is available.

## 3. Inspect references systematically

For each relevant screen or state, record:

- Purpose and user intent.
- Information hierarchy: primary content, supporting details, actions, and status.
- Layout: safe areas, content width, alignment, density, scroll behavior, and responsive changes.
- Visual language: typography roles, color roles, surfaces, borders, radius, icon style, imagery, spacing rhythm, and emphasis.
- Interaction: tap/swipe/drag behavior, focus, keyboard, validation, loading, error recovery, navigation, and dismiss/undo behavior.
- Motion: trigger, direction, duration if observable, easing/continuity, interruptibility, and reduced-motion fallback.
- Platform, locale/direction, theme, device size, and any uncertainty.

Separate observation from interpretation. For example, “the primary action remains visible above the keyboard” is an observation; “a sticky action is the best solution for our product” is a hypothesis to assess against the current app.

When video is available, inspect the whole interaction, not only its initial and final screenshots. Pause or extract representative frames at transition start, midpoint, completion, interruption, and reverse/back navigation. Do not claim frame-by-frame inspection unless frames were actually reviewed.

## 4. Extract reusable patterns, not copies

- Identify repeated rules across screens before defining tokens or components.
- Separate foundational tokens (color, type, spacing, shape, motion) from component rules and screen-specific composition.
- Record deviations and their likely purpose; a one-off visual treatment is not automatically a system-wide rule.
- Avoid pixel-copying a third-party product's distinctive branding, artwork, text, or proprietary assets. Translate the useful interaction and hierarchy into an original implementation appropriate to the requested product.
- Prefer the existing project's system unless the research demonstrates a concrete gap. Do not redesign unrelated screens or replace architecture merely because a reference uses a different stack.

## 5. Account for Flutter and device realities

Research these when applicable:

- Responsive/adaptive behavior for available widths, orientation, window resizing, foldables, and input methods.
- Keyboard and system insets, safe areas, navigation bars, status bars, and gesture regions.
- Real localized strings, Arabic/RTL and LTR directionality, plural/date/number formatting, and long translations.
- Light/dark/system themes, dynamic content, empty/loading/error/success/disabled states.
- Semantics, focus order, touch-target size, text scaling, contrast, and reduced-motion behavior.
- Flutter widgets and packages already in the app, versus any new dependency's maintenance, compatibility, and platform support.

Do not assume a design screenshot proves implementation feasibility or accessibility. Identify what needs a running-device check or an assistive-technology check.

## 6. Deliver an implementable research brief

Use [the design research brief template](../../examples/design-research-brief-template.md). Keep it concise and include:

- Task and scope, with references and their inspection limits.
- Observed patterns and evidence, separated from assumptions.
- Proposed original design direction and the rationale for key decisions.
- Screen/route inventory and interaction states.
- Tokens/components to reuse or introduce, avoiding premature over-generalization.
- Responsive, theme, localization/RTL, accessibility, and motion risks.
- Open questions only where the answer materially changes implementation.
- Acceptance criteria and the exact next verification steps.

## Definition of done

A developer can explain why the proposed design fits the task, identify which decisions came from evidence versus assumptions, implement the intended flow without inventing missing behavior, and test the highest-risk states. If the reference material or device tooling was unavailable, its impact is explicit.

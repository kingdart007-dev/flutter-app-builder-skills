---
name: flutter-ui-ux
description: Design or improve Flutter screens and flows with polished visual hierarchy, responsive layouts, accessible interactions, and complete UX states. Use for new screens, redesigns, forms, navigation, design systems, and visual cleanup.
---

# Flutter UI and UX

Build interfaces that feel intentional, calm, readable, and native to the product—not like a pile of default widgets. Fit the project's design language unless the user supplies a stronger product specification.

## Before changing the UI

1. Inspect app theme, typography, spacing, reusable components, navigation, localization, and a similar screen.
2. Read product requirements and design references. Treat explicit tokens and interaction rules as constraints.
3. Check supported screen sizes, text scaling, locales, and themes. Do not invent a new design system if one exists.
4. Identify the key user task and the states that task can occupy.

## Design decisions

- Establish hierarchy with layout, spacing, type, and contrast before decoration.
- Use semantic design tokens for color, typography, spacing, shapes, and motion. Avoid scattered magic numbers.
- Keep typography legible and scalable. Respect platform text scaling; do not shrink text just to force a layout to fit.
- Design for the smallest supported phone first, then use roomier layouts deliberately.
- Use safe areas and account for keyboard insets, system bars, notches, and bottom navigation. Do not hide primary actions behind the keyboard.
- Prefer Material or Cupertino primitives when they fit the product and accessibility needs; customize intentionally instead of fighting the framework. Avoid default styling when a supplied visual system calls for a custom treatment.
- Use elevation, shadows, gradients, blur, and animation only when they communicate hierarchy or behavior.
- Provide clear labels, focused errors, visible focus, sufficiently large touch targets, and meaningful semantics.
- Use color alongside text, icons, or shape to communicate state; do not make color the only signal.
- Make animations purposeful. Honor reduced-motion preferences when supported.

## Required UX states

For each relevant interaction, consider initial, loading, disabled, empty, error with recovery, and success states. Include validation, duplicate taps, repeated submissions, network interruption, back behavior, focus changes, and keyboard dismissal when applicable. Preserve valid input after recoverable failures.

Do not add loading states to static content without value. Do not put a spinner on every button by default.

## Flutter implementation practices

- Prefer small widgets with clear responsibilities and stable inputs.
- Use const constructors when appropriate, but do not confuse const with good architecture.
- Avoid deeply nested conditionals in build methods; extract meaningful sections and state-specific widgets.
- Use constraints and flexible layout primitives when behavior truly depends on available space. Avoid device-model checks and hard-coded width assumptions.
- Use lazy collections for long content. Give interactive elements stable keys when they improve tests or identity.
- Handle missing or loading imagery when it affects the experience.
- Keep strings out of presentation code when localization is supported. Use direction-aware padding and alignment instead of assuming left-to-right.
- Ensure controls expose labels, values, hints, and state to assistive technology.

## Validation checklist

Compare against requirements and existing screens. Check narrow phone width, larger text scale, keyboard-visible forms, both themes, and each supported locale, especially RTL. Exercise the success, validation, empty, loading, and error paths that apply. Add focused widget tests for meaningful behavior. Use golden tests selectively for stable, high-value visual contracts, not every trivial widget. Report which checks actually ran; a source-level estimate is not a device screenshot or usability test.

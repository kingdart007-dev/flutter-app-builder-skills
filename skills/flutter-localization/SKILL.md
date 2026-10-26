---
name: flutter-localization
description: Implement or review Flutter localization, locale-aware formatting, Arabic and other RTL layouts, accessibility semantics, text scaling, and inclusive interaction behavior.
---

# Localization, RTL, and Accessibility

Localization is part of application architecture and layout, not a final translation pass. Use the project's supported locales and accessibility requirements as the source of truth.

## Inspect the current setup

Check supported locales, localization generation, ARB files or translation tooling, app-level delegates, locale resolution, typography assets, routing, and test conventions. Do not invent supported languages or switch architecture without need.

## Text and formatting

- Move user-facing strings into established localization resources. Avoid hard-coded strings in widgets, validation, notifications, and dialogs.
- Keep keys descriptive and stable. Add translations for every supported locale and review placeholders, pluralization, contextual meaning, and grammatical order.
- Use locale-aware date, time, number, currency, and list formatting instead of manually composing strings.
- Do not concatenate translated fragments into sentences when word order may differ.
- Map known server error codes to localized helpful messages rather than showing raw internal identifiers.
- Use fonts with appropriate glyph coverage, weights, and licensing. Verify Arabic punctuation, numerals, diacritics, and mixed-script text instead of assuming fallback is correct.

## Layout direction

- Let Flutter Directionality and locale-aware framework behavior control directional layout.
- Prefer start/end alignment, directional padding, directional icons, and localized navigation affordances over fixed left/right assumptions.
- Check icons that imply direction, progress sequences, carousels, charts, and gestures. Not every icon should be mirrored.
- Preserve intentional physical positioning where platform conventions require it.
- Test real translated strings; avoid fixed heights that clip longer text.

## Accessibility

Give interactive controls meaningful labels and expose values, hints, selection, and enabled state. Ensure reading order follows the user's task. Use scalable type and layouts that survive larger text scales. Do not rely on color alone, create focus traps, or build custom controls without necessary semantics and keyboard behavior. Respect reduced-motion settings where supported. Keep errors associated with the control they explain and make dynamic updates discoverable.

## Verification

Run localization generation when resources change. Detect missing keys using existing tooling if available. Add widget tests for representative LTR and RTL layouts and important semantics. Inspect narrow layouts, longer translations, large text, mixed Arabic/Latin content, dialogs, and bottom sheets. Report font or screen-reader checks that could not be performed; code inspection alone is not an accessibility audit.

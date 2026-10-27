# Example prompts and expected evidence

Use these prompts to exercise the skills on a real Flutter repository. Replace the feature names and constraints with your product's actual requirements. The example reports below describe what a good report should contain; they are not claims that these tasks have been run in a particular app.

## 1. Build and verify a localized settings screen

**Prompt**

> Inspect this repository before editing. Add a settings screen consistent with the existing design system. Support the locales and themes the app already claims to support. Preserve the current navigation and state-management approach. Include accessible controls, loading/error states only where relevant, and tests. Run formatting, analysis, and the relevant tests. If an emulator is available, exercise the screen and capture real screenshots. Report exactly which checks ran.

**Expected evidence**

- Existing architecture, localization, and theme approach identified before edits.
- A focused implementation with no unrelated dependency or architecture rewrite.
- Widget tests for control behavior, semantics, and relevant theme/locale combinations.
- Exact formatter, analyzer, and test commands with observed results.
- Device screenshots only if the app was run on a real emulator/simulator; otherwise device QA explicitly marked NOT RUN.

## 2. Review Arabic RTL and keyboard behavior

**Prompt**

> Review the checkout form in this existing Flutter app for Arabic RTL, long translations, large text, keyboard-visible layout, validation errors, and bottom-action accessibility. Do not change product behavior without a reason. Fix the issues you can reproduce, add regression tests, and provide screenshot evidence from a running emulator if available. Distinguish checks you performed from checks that need a physical device or screen reader.

**Expected evidence**

- Real Arabic strings used; the review does not rely solely on Directionality toggling with English text.
- Direction-aware alignment and padding, reviewed directional icons, and no fixed-height text clipping.
- Validation errors associated with the relevant fields and no action obscured by the keyboard.
- RTL/widget results and emulator screenshots reported separately.
- Screen-reader and physical-device checks marked NOT RUN unless actually performed.

## 3. Debug a stale-result race

**Prompt**

> Investigate why quickly changing the search query sometimes displays results from an older query. Trace the existing state and repository flow, reproduce the race with a deterministic test, fix the root cause using the project's existing patterns, then run the focused test and related checks. Do not claim the UI/device flow passed unless you exercised it.

**Expected evidence**

- Root cause tied to request ordering or state transitions, not guessed from symptoms.
- A deterministic regression test that proves an older response cannot overwrite the newer result.
- The exact test command and result, plus broader checks that were actually run.
- Any device-specific verification clearly separated from unit/widget verification.

## 4. Check installation of a single skill

From a disposable project directory with the documented Node.js version installed:

```bash
npx skills add kingdart007-dev/flutter-app-builder-skills --skill flutter-visual-qa --agent codex --yes
npx skills list
```

Confirm the CLI reports the requested skill for the selected agent and inspect the generated skill path. Available flags and discovery paths can change; check the current CLI help and agent documentation when the command differs.

## Example of an honest verification summary

This is a format example, not an executed test report:

| Check | Status | Evidence |
| --- | --- | --- |
| `flutter analyze` | NOT RUN | No Flutter SDK available in the current environment. |
| Focused widget tests | PASS / FAIL / NOT RUN | Record the actual command and output. |
| Android emulator flow | PASS / FAIL / NOT RUN | Include device ID, OS/API, route, locale/theme, and screenshot path. |
| iOS Simulator flow | PASS / FAIL / NOT RUN | Include simulator details or explain why it was unavailable. |
| Arabic RTL and large text | PASS / FAIL / NOT RUN | Name the exact configurations actually inspected. |
| Screen-reader audit | PASS / FAIL / NOT RUN | Only mark PASS if an appropriate assistive-technology check occurred. |

Replace every placeholder status with an observed result before sharing the report. Do not copy this table into a real result without executing the checks.


## 5. Research a supplied UI reference before implementation

**Prompt**

> Inspect this Flutter repository and the supplied product/reference material before changing the UI. Review the important screens and states available, record observations separately from design hypotheses, consult current official platform/Flutter guidance for relevant concerns, and produce a concise design brief with screen inventory, tokens/components, localization/RTL, accessibility, responsive behavior, and acceptance criteria. Do not copy distinctive branding or claim references were inspected when they were inaccessible.

**Expected evidence**

- Reference links and actual inspected screens/states are named, with limitations.
- Findings are separated from hypotheses, and relevant platform/API claims cite current authoritative documentation.
- The brief preserves existing product constraints and translates patterns into an original implementation.
- Device, animation, and assistive-technology checks are marked NOT RUN unless performed.

## 6. Verify a motion-heavy flow

**Prompt**

> Run the relevant Flutter app on an available emulator/simulator, exercise the animated flow, record a short real-device clip if supported, then scrub the transition and inspect representative frames. Check interrupted gestures, reverse/back navigation, repeated input, loading completion, and reduced-motion behavior where supported. Report capture and inspection separately from source/test checks.

**Expected evidence**

- Exact device/platform and flow, with a recording/artifact path only if actually created.
- Motion findings grounded in playback or inspected extracted frames, not assumptions based on source code alone.
- Static, widget, screenshot, and motion checks are reported as distinct forms of evidence.
- Unavailable recording, video inspection, reduced-motion, and physical-device checks are explicitly marked NOT RUN.

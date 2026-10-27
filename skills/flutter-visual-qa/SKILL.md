---
name: flutter-visual-qa
description: Verify Flutter UI changes on real emulators or simulators using screenshots, interaction flows, and explicit evidence. Use for visual polish, screen redesigns, responsive layout, themes, keyboard behavior, accessibility, localization, and RTL checks.
---

# Flutter Visual QA and Emulator Verification

Prove how the app actually renders and behaves. Source code review, a passing analyzer, or a generated mockup is not proof that the running Flutter UI is correct.

## Rules of evidence

- Inspect the existing app, acceptance criteria, route, design system, tests, platform targets, SDK constraints, and local run instructions first.
- Prefer the project's existing device/integration-test tooling. Do not add a screenshot, golden-test, automation, or device-control dependency without a reason.
- Never invent a device ID, screenshot, test result, or accessibility result. A check that cannot run is **NOT RUN**, not PASS.
- Do not change the expected screenshot/golden merely to make a failing comparison green. Inspect the difference and confirm the intended visual change first.
- Use synthetic accounts and non-sensitive data. Do not capture tokens, private notifications, personal data, or production customer information in evidence.
- Keep screenshots in an agreed artifact path or temporary directory. Do not commit large or sensitive screenshots unless the repository intentionally versions visual baselines.

## Workflow

### 1. Turn the request into visual acceptance criteria

Identify the primary user task, screen/route, important controls, expected result, and relevant failure cases. Note explicit design references and measurable constraints, such as typography, spacing tokens, minimum touch targets, supported widths, and theme behavior.

Choose a small set of high-value scenarios instead of screenshotting everything indiscriminately. Include only states relevant to the feature:
- Initial, loading, empty, error/retry, and success.
- Invalid input, disabled controls, and double submission for forms.
- Back navigation, dialogs/bottom sheets, and keyboard-visible states.
- Long or missing content, scrolling boundaries, and narrow widths.

### 2. Inspect the environment before executing commands

Read project docs and scripts, then inspect the available tooling. Examples include:

```bash
flutter --version
flutter doctor -v
flutter devices
flutter emulators
```

Use only commands supported by the installed SDK and repository. If no device is available, determine whether one can be launched in the current environment. Do not attempt iOS Simulator commands on non-macOS hosts.

### 3. Run the cheapest meaningful checks first

Run the project's existing targeted widget or integration tests, then analysis and the relevant test suite where appropriate. Preserve failures for diagnosis rather than skipping or weakening them.

Typical checks, when supported by the project:

```bash
flutter analyze
flutter test
```

For device-backed integration tests, inspect the project's test setup and use its supported command (often `flutter test integration_test/<file> -d <device-id>` or the project's configured `flutter drive` workflow). Do not add a new integration-test framework automatically.

### 4. Launch and exercise the real app

Use the project's run configuration and an actual emulator/simulator identifier discovered from the tool output. Exercise the requested flow end to end, including meaningful non-happy paths. Verify that taps navigate correctly, primary actions work, back behavior is coherent, fields preserve input on recoverable errors, and async states do not get stuck.

Prefer the smallest supported phone dimension that exposes layout pressure, then check a representative normal device. Add tablets, foldables, or landscape only when they are in scope.

### 5. Capture real evidence

Capture screenshots from the running application—not from a design mockup or recreated HTML. Examples:

Android (when Android SDK tools and an attached emulator/device are available):

```bash
adb devices
adb exec-out screencap -p > /tmp/flutter-visual-qa.png
```

iOS Simulator (on macOS, after booting the intended simulator):

```bash
xcrun simctl list devices booted
xcrun simctl io booted screenshot /tmp/flutter-visual-qa.png
```

Keep evidence labeled by feature/scenario, device or simulator, locale, theme, and text scale. Inspect the image at readable scale. Look for clipping, overflow, wrong hierarchy, inconsistent spacing, misaligned icons, low contrast, unbalanced empty space, wrong system/keyboard insets, and controls that are too small or obscured.

If the available tools cannot display or inspect the screenshot, say so explicitly. A file existing on disk alone does not prove a visual review was performed.

### 6. Check responsive, theme, locale, and accessibility risks

Use the project's supported configurations. Where they are in scope, verify:
- Light and dark themes, including surfaces, separators, disabled states, and system bars.
- Arabic/RTL and LTR, with real localized strings, direction-aware spacing, directional icons, dialogs, forms, and navigation.
- Large system text scale and longer-than-usual translations.
- Keyboard visible, keyboard dismissed, safe areas, and bottom actions.
- Semantics labels/state and focus order; keyboard navigation where applicable; reduced-motion behavior when the product supports motion settings.
- Loading/error/empty/success feedback and recovery actions.

Do not treat a screenshot as a full accessibility audit. Screen-reader behavior, contrast measurement, and touch-target verification need their own suitable checks.

### 8. Diagnose differences; do not beautify blindly

Compare against the explicit spec, accepted reference, or existing baseline. For golden tests, inspect pixel diffs and the semantic reason for the change before updating expectations. Avoid chasing pixel equality across different fonts/platforms when the test contract should instead check layout and behavior.

Fix root causes rather than hiding overflow with clipping or shrinking text. Do not hard-code a single emulator width when flexible constraints solve the actual problem.

### 9. Report the result with evidence

Use [the visual QA report template](../../examples/visual-qa-report-template.md). For each important check report:
- PASS, FAIL, or NOT RUN.
- Device/platform details and locale/theme/text-scale configuration.
- Exact command or manual interaction performed.
- Screenshot or test artifact path, when created.
- Findings and the regression or test added.
- Environment limitations and remaining manual checks.

Do not report an emulator check as passed when only widget tests ran, or a visual review as passed when only source code was inspected.

## Definition of done

The requested flow works in the tested configuration, meaningful visual defects have been fixed, the highest-risk relevant theme/locale/layout states have been checked, available tests pass, and the report links to evidence. Unsupported platform, screen-reader, physical-device, or release-build checks remain explicitly unverified.

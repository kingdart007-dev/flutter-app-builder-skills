# Flutter Motion QA Checklist

Use this checklist only when the change includes meaningful motion or the user reported an animation/transition defect. It is a reporting aid, not proof that checks have run.

## Recording context
- **Flow / route:**
- **Device, OS/API, screen size, refresh configuration if known:**
- **Locale / direction, theme, text scale:**
- **Build or commit under test:**
- **Recording path (if captured):**
- **Recording viewed / scrubbed:** PASS / FAIL / NOT RUN
- **Frames extracted and visually inspected:** PASS / FAIL / NOT RUN / NOT NEEDED
- **Tooling unavailable or limits:**

## Interaction coverage
- [ ] Start state and trigger are visible.
- [ ] Transition start, midpoint, and settled end were inspected.
- [ ] Repeated taps/actions do not stack or duplicate animations.
- [ ] Gestures can be interrupted or cancelled where expected.
- [ ] Reverse/back/dismiss transitions are coherent.
- [ ] Loading/progress animation stops on success, error, or cancellation.
- [ ] Focus, keyboard, hit targets, and text remain usable during motion.
- [ ] Large text and layout changes do not cause clipping or jumps.
- [ ] Reduced-motion / animation-disabled behavior checked when supported.
- [ ] Important state is communicated without motion alone.

## Findings
| Check | Status | Evidence / observed defect | Follow-up |
| --- | --- | --- | --- |
| Timing and continuity | PASS / FAIL / NOT RUN | | |
| Jank, flicker, or layout jumps | PASS / FAIL / NOT RUN | | |
| Readability and interaction | PASS / FAIL / NOT RUN | | |
| Interrupt, reverse, and dismissal | PASS / FAIL / NOT RUN | | |
| Accessibility / reduced motion | PASS / FAIL / NOT RUN | | |

## Summary
- **Verified behavior:**
- **Defects and reproducing steps:**
- **Tests run and observed result:**
- **Checks not run and why:**

Do not mark PASS when the clip was not watched or the frames were not inspected. A successful screenshot capture is not evidence of correct temporal behavior.

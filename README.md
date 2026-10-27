# Flutter App Builder Skills

[![Validate skills](https://github.com/kingdart007-dev/flutter-app-builder-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/kingdart007-dev/flutter-app-builder-skills/actions/workflows/validate-skills.yml)
[![Browse on skills.sh](https://skills.sh/b/kingdart007-dev/flutter-app-builder-skills)](https://skills.sh/kingdart007-dev/flutter-app-builder-skills)

**Practical, portable agent skills for building better Flutter and Dart applications.**

A focused toolkit for AI coding agents that need to plan, implement, debug, test, review, and ship real Flutter apps—not just generate plausible-looking code.

These skills are framework-aware but not package-dogmatic. They help an agent inspect the project first, work with the architecture and conventions that already exist, verify assumptions against reliable sources, and prove changes with targeted checks.

## What this project is

- **Flutter and Dart first.** Android and iOS are primary targets; web and desktop are considered when the project needs them.
- **Execution-oriented.** Skills define repeatable workflows, decision criteria, edge cases, and a definition of done.
- **Repo-aware.** Existing code, user changes, constraints, and project conventions take precedence over generic templates.
- **Quality over ceremony.** Prefer the smallest design or architecture that fits real requirements.
- **Agent-portable.** Skills use the open `SKILL.md` format and work with compatible coding agents.
- **Evidence-led.** Never claim a command, test, build, or device check passed unless it actually ran and its result was observed.

## Skills

| Skill | Use it when |
| --- | --- |
| [flutter-app-builder](skills/flutter-app-builder/SKILL.md) | Planning and delivering a feature or app end to end. |
| [flutter-design-research](skills/flutter-design-research/SKILL.md) | Researching visual references, platform guidance, interaction flows, and design patterns before implementation. |\n| [flutter-ui-ux](skills/flutter-ui-ux/SKILL.md) | Designing polished, responsive, accessible Flutter screens and flows. |
| [flutter-visual-qa](skills/flutter-visual-qa/SKILL.md) | Verifying real Flutter UI on emulators/simulators, screenshots, accessibility, themes, and RTL. |
| [flutter-architecture](skills/flutter-architecture/SKILL.md) | Choosing boundaries, organizing features, and separating UI, state, and data access. |
| [flutter-state-management](skills/flutter-state-management/SKILL.md) | Selecting or improving local/shared state, async flows, and navigation state. |
| [flutter-localization](skills/flutter-localization/SKILL.md) | Implementing localization, Arabic/RTL, text scaling, semantics, and accessibility. |
| [flutter-testing](skills/flutter-testing/SKILL.md) | Building a meaningful unit, widget, and integration test strategy. |
| [flutter-debugging](skills/flutter-debugging/SKILL.md) | Investigating crashes, rendering issues, async bugs, and regressions from evidence. |
| [flutter-performance](skills/flutter-performance/SKILL.md) | Diagnosing jank, excess rebuilds, slow startup, memory issues, and expensive work. |
| [flutter-security](skills/flutter-security/SKILL.md) | Reviewing secrets, data handling, permissions, dependencies, and release readiness. |
| [flutter-code-review](skills/flutter-code-review/SKILL.md) | Reviewing changes for correctness, regressions, maintainability, and missing tests. |

## Install

The Skills CLI currently documents Node.js 22.20 or later as a prerequisite. Check its [current installation and command documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) if your environment differs.

From your app repository, install from this collection:

```bash
npx skills add kingdart007-dev/flutter-app-builder-skills
```

Install only the visual QA skill for Codex:

```bash
npx skills add kingdart007-dev/flutter-app-builder-skills --skill flutter-visual-qa -a codex
```

Install all skills to the agents supported by the CLI:

```bash
npx skills add kingdart007-dev/flutter-app-builder-skills --all
```

Run `npx skills add --help` to see current flags. The CLI lets you select supported agents and skills; use your agent's current documentation for its precise discovery paths. Installing a skill adds instructions, not Flutter SDKs, dependencies, devices, or app code.

### Manual installation

Copy the individual skill directory into the skill discovery directory supported by your agent. For example, a project-scoped setup may use:

```text
your-project/
└── .agents/
    └── skills/
        └── flutter-visual-qa/
            └── SKILL.md
```

## Get the best results

1. **Start with the repository.** Inspect the app, SDK constraints, architecture, tests, and local conventions before proposing edits.
2. **State the outcome.** Describe user-visible behavior and acceptance criteria instead of prescribing a package without a reason.
3. **Let evidence choose the approach.** Consult current official documentation when APIs, SDK compatibility, security guidance, or package maintenance may have changed.
4. **Verify the actual change.** Request exact formatting, analysis, test, and device-check commands and results. Simulator/device checks must be reported separately from static checks.
5. **Keep the diff intentional.** Avoid unrelated refactors, generated-file churn, unnecessary dependencies, and rewrites of user-owned code.

## Examples and quality checks

- [Realistic prompts and expected evidence](examples/README.md)
- [Visual QA report template](examples/visual-qa-report-template.md)
- [Contributing and local validation](CONTRIBUTING.md)
- [Unreleased changes](CHANGELOG.md)

Run the repository validator and its regression tests locally:

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

CI runs these checks on pushes to `main`, pull requests, and manual dispatch.

## Repository structure

```text
skills/<skill-name>/SKILL.md
examples/
tests/fixtures/{valid,invalid}/
scripts/validate_skills.py
.github/workflows/validate-skills.yml
```

## Status and scope

This is an evolving community toolkit, not a replacement for Flutter's official documentation or a guarantee of production readiness. Package versions, APIs, and platform policies change. Agents should verify time-sensitive details against authoritative documentation and the target project's actual SDK constraints.

## License

MIT. See [LICENSE](LICENSE).

# Flutter App Builder Skills

**Practical, portable agent skills for building better Flutter and Dart applications.**

A focused toolkit for AI coding agents that need to plan, implement, debug, test, review, and ship real Flutter apps—not just generate plausible-looking code.

These skills are framework-aware but not package-dogmatic. They help an agent inspect the project first, work with the architecture and conventions that already exist, verify assumptions against reliable sources, and prove changes with targeted checks.

## What this project is

- **Flutter and Dart first.** Android and iOS are the primary targets; web and desktop are considered when the project requires them.
- **Execution-oriented.** Skills define a repeatable workflow, decision criteria, edge cases, and a definition of done.
- **Repo-aware.** Existing code, user changes, constraints, and project conventions take precedence over generic templates.
- **Quality over ceremony.** Prefer the smallest design or architecture that fits the real requirements.
- **Agent-portable.** Skills use the open `SKILL.md` format and can be installed into compatible coding agents.
- **Evidence-led.** Do not claim a command, test, build, or device check passed unless it actually ran and its result was observed.

## Skills

| Skill | Use it when |
| --- | --- |
| [flutter-app-builder](skills/flutter-app-builder/SKILL.md) | Planning and delivering a feature or app end to end, coordinating the other skills. |
| [flutter-ui-ux](skills/flutter-ui-ux/SKILL.md) | Designing and implementing polished, responsive, accessible Flutter screens and flows. |
| [flutter-architecture](skills/flutter-architecture/SKILL.md) | Choosing boundaries, organizing features, and separating UI, state, and data access. |
| [flutter-state-management](skills/flutter-state-management/SKILL.md) | Selecting or improving local and shared state, async flows, and navigation state. |
| [flutter-localization](skills/flutter-localization/SKILL.md) | Implementing localization, Arabic/RTL, text scaling, semantics, and accessibility. |
| [flutter-testing](skills/flutter-testing/SKILL.md) | Building a meaningful unit, widget, and integration test strategy and fixing failures. |
| [flutter-debugging](skills/flutter-debugging/SKILL.md) | Investigating crashes, rendering issues, async bugs, and regressions from evidence. |
| [flutter-performance](skills/flutter-performance/SKILL.md) | Diagnosing jank, excess rebuilds, slow startup, memory issues, and expensive work. |
| [flutter-security](skills/flutter-security/SKILL.md) | Reviewing secrets, data handling, permissions, dependencies, and release readiness. |
| [flutter-code-review](skills/flutter-code-review/SKILL.md) | Reviewing a patch for correctness, regressions, maintainability, and missing tests. |

## Install

Install all skills in this repository with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add kingdart007-dev/flutter-app-builder-skills
```

Install only one skill:

```bash
npx skills@latest add kingdart007-dev/flutter-app-builder-skills --skill flutter-ui-ux
```

The CLI's available agent targets and flags may change; use `npx skills@latest add --help` for the current options.

### Manual installation

Copy the individual skill directory into the skills directory supported by your agent. For example, a project-scoped Codex setup can use:

```text
your-project/
└── .agents/
    └── skills/
        └── flutter-ui-ux/
            └── SKILL.md
```

Follow your agent's current documentation for the exact discovery path. Skills are plain Markdown instructions; they do not install Flutter, Dart, plugins, or packages into your app.

## How to get the best results

1. **Start with the repository.** Ask the agent to inspect the app, its SDK constraints, current architecture, tests, and local conventions before proposing edits.
2. **State the outcome.** Describe the user-facing behavior and acceptance criteria instead of prescribing a package without a reason.
3. **Let evidence choose the approach.** Ask for current official docs when APIs, SDK compatibility, security guidance, or package maintenance may have changed.
4. **Verify the actual change.** Request relevant formatting, analysis, and tests; ask for exact commands and results. Simulator/device checks should be reported separately from static checks.
5. **Keep the diff intentional.** Avoid broad unrelated refactors, generated-file churn, unnecessary dependencies, and rewrites of user-owned code.

## Repository structure

```text
skills/
  <skill-name>/
    SKILL.md
.github/
  workflows/
    validate-skills.yml
scripts/
  validate_skills.py
```

Each skill has a short metadata description for discovery and a task workflow in its `SKILL.md`. Supporting references should be added only when they improve accuracy or keep a skill's main instructions focused.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Before submitting a skill, ensure it has valid metadata, clear activation criteria, ordered steps, project-aware decision rules, failure/edge-case guidance, and an honest definition of done.

## Status and scope

This is an evolving community toolkit, not a replacement for Flutter's official documentation or a guarantee of production readiness. Package versions, APIs, and platform policies change. Agents should verify time-sensitive details against authoritative sources and the target project's actual SDK constraints.

## License

MIT. See [LICENSE](LICENSE).

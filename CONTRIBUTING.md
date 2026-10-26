# Contributing

Thanks for helping make Flutter and Dart agent skills more useful in real projects.

## What belongs here

A skill should help an agent complete a recognizable class of work with better decisions and fewer missed edge cases. Favor practical workflows, decision criteria, and verification steps over broad advice that could apply to any language.

## Before adding or changing a skill

1. Read the existing skills and avoid duplicating an existing responsibility.
2. Check the [Agent Skills specification](https://agentskills.io/specification) and keep required frontmatter compatible.
3. Define activation criteria, context to inspect, a repeatable workflow, failure modes, and a definition of done.
4. Qualify version-sensitive package and API details. Link authoritative documentation rather than hard-coding claims that age quickly.
5. Respect user requirements, project conventions, privacy, and security.
6. Update the README catalog and examples when a skill is added, renamed, or removed.

## Style guide

- Use a short directory name with lowercase letters, numbers, and hyphens.
- Keep the metadata name identical to the directory name.
- Write a concise description that tells an agent what the skill does and when to use it.
- Use imperative, practical instructions. Explain why a step matters when the choice is not obvious.
- Make decisions conditional on project context. Do not prescribe a package or architecture without a reason.
- Prefer standard Flutter and Dart practices while respecting SDK constraints and existing project patterns.
- Distinguish actions performed from actions merely recommended.
- Keep privacy, accessibility, localization, async safety, and error recovery in scope whenever relevant.
- Avoid fake benchmark figures, unsupported security claims, generic filler, and guaranteed-success language.

## Local validation

Python 3.10 or newer is sufficient for the repository validator and tests; they use only the standard library.

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

GitHub Actions runs the same validation and unit tests on pushes to `main`, pull requests, and manual dispatch. The validator checks required metadata, directory/name consistency, non-empty instructions, README catalog links, and relative Markdown links. It is intentionally dependency-free and is not a full YAML parser or a substitute for reviewing skill quality.

The valid and invalid fixture repositories under `tests/fixtures/` exercise normal and failure paths. When changing validator behavior, add a regression test for it.

## Pull request checklist

- [ ] The skill solves a distinct, real-world Flutter/Dart task.
- [ ] Frontmatter name matches the directory and description gives useful activation cues.
- [ ] Instructions are actionable, ordered, and grounded in project context.
- [ ] Version-sensitive details are qualified or linked to authoritative documentation.
- [ ] Failure modes and verification are included.
- [ ] README catalog and relevant docs are updated.
- [ ] Validator and unit tests pass; claims about testing are accurate.

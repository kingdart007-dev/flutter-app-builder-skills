"""Regression tests for the repository's dependency-free skill validator."""

from pathlib import Path
import unittest

from scripts.validate_skills import validate

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


class ValidateSkillsTests(unittest.TestCase):
    def test_valid_fixture_passes(self) -> None:
        errors, warnings, skill_count = validate(FIXTURES / "valid")
        self.assertEqual([], errors)
        self.assertEqual([], warnings)
        self.assertEqual(1, skill_count)

    def test_invalid_fixture_reports_metadata_catalog_and_link_errors(self) -> None:
        errors, _warnings, skill_count = validate(FIXTURES / "invalid")
        joined = "\n".join(errors)
        self.assertGreaterEqual(skill_count, 1)
        self.assertIn("required metadata field 'description' is empty or missing", joined)
        self.assertIn("must match directory", joined)
        self.assertIn("has no matching skill directory", joined)
        self.assertIn("broken relative Markdown link", joined)

    def test_real_repository_is_consistent(self) -> None:
        errors, warnings, skill_count = validate(ROOT)
        self.assertEqual([], errors, "\n".join(errors))
        self.assertEqual([], warnings, "\n".join(warnings))
        self.assertEqual(12, skill_count)


if __name__ == "__main__":
    unittest.main()

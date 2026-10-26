---
name: flutter-security
description: Review or implement security and privacy protections in Flutter and Dart apps, including credentials, network data, local storage, permissions, deep links, logging, dependencies, and release configuration.
---

# Flutter Security and Privacy

Protect user data and reduce unnecessary authority. Decisions must follow the real threat model, backend contracts, and platform requirements; do not bolt on infrastructure the product does not need.

## Inspect the real boundaries

Review dependency manifests and lockfiles, app initialization, API clients, authentication if present, local persistence, logs, permissions, deep links, web views, build configuration, and release workflow. Identify sensitive data, where it travels, and which component is trusted to make decisions.

## Non-negotiable safeguards

- Never commit API secrets, signing keys, private certificates, passwords, access tokens, or production credentials.
- Treat values embedded in a mobile binary, assets, compile-time defines, and app configuration as extractable. A client-side key is not a secret.
- Keep authorization and ownership enforcement on a trusted backend. Hiding a button or checking a role in the client is not access control.
- Use platform-appropriate secure storage when sensitive values must persist locally. Do not store credentials in ordinary preferences or logs.
- Use TLS with normal platform certificate validation. Never disable certificate checks as a production workaround.
- Minimize collection and retention of personal data; redact sensitive values from logs, crash reports, analytics, and debug output.
- Request only necessary runtime permissions and explain their use in context.
- Validate untrusted input and deep-link destinations. Use strict allowlists for arbitrary URL, file, intent, or WebView navigation where appropriate.
- Review dependency maintenance, provenance, license, transitive risk, and compatibility before adding packages.

## Platform and release checks

Inspect Android permissions, exported components, intent filters, cleartext traffic policy, and signing configuration as relevant. Inspect iOS usage descriptions, URL schemes, entitlements, ATS policy, and signing as relevant. Ensure debug-only shortcuts and verbose diagnostics cannot silently enter a production build.

Do not invent authentication, analytics, push notifications, backend, or secret-management services for a starter or feature that does not require them. Avoid custom cryptography; use established platform or audited libraries when cryptography is genuinely required.

## Respond to a finding

Classify severity based on exploitability, impact, exposure, and required privileges. Explain attack path, affected data, and smallest effective fix. If a real secret was exposed, remove it from code and also rotate/revoke it and review history; deleting the latest line alone is insufficient.

## Verify honestly

Run relevant static checks and tests, inspect the final diff for secrets, and review platform configuration. Do not claim a security audit or penetration test occurred unless it actually did.

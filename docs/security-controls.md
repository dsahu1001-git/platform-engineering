# Security Controls

Initial guardrails:

- Run containers as non-root.
- Require resource requests and limits.
- Avoid `latest` image tags.
- Use service-specific Kubernetes service accounts.
- Store PostgreSQL credentials outside application repos.
- Prefer IRSA for AWS access.
- Keep app teams away from direct cluster credentials.

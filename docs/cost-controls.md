# Cost Controls

Cost-sensitive defaults:

- Start with dev only.
- Use small node groups.
- Use the smallest practical PostgreSQL instance.
- Keep prod disabled for the sample app until needed.
- Tag every AWS resource by platform, environment, and owner.
- Provide a cleanup workflow before creating resources.

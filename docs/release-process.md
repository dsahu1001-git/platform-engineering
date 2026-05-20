# Release Process

Development deployments can be automatic.

Stage and production promotions are governed:

1. A service image is built and pushed.
2. Harness creates a release intent change.
3. Required approvals are collected.
4. The release intent change is merged.
5. Argo CD syncs the environment.
6. Monitoring confirms health.

Rollback is performed by reverting release intent and allowing Argo CD to reconcile.

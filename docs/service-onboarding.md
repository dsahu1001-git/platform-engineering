# Service Onboarding

A future service should be onboarded by submitting service metadata, not by copying deployment folders.

Minimum input:

```yaml
name: payment-api
owner: payments-team
type: backend
runtime: python
repo: github.com/dsahu1001-git/payment-api
port: 8080
healthPath: /health
metricsPath: /metrics
postgres:
  required: true
```

Automation should generate or update release intent, Argo registration, Harness input sets, dashboards, alerts, and policy checks.

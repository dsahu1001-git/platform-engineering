# Observability

The platform owns observability.

Version 1:

- Prometheus metrics.
- Loki logs.
- Grafana dashboards.
- Kubernetes ServiceMonitor templates.
- Application health surfaced through Release Control.

The backend exposes `/metrics` and structured logs. The platform decides how metrics are scraped, logs are shipped, alerts are routed, and dashboards are generated.

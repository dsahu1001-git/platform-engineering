# Operating Model

The platform team owns templates, policies, infrastructure, release mechanics, and observability defaults.

Application teams own application code and service metadata changes through governed pull requests or an IDP workflow.

The platform should scale by automation:

- service catalog entries define application contracts
- release intent files define deployed versions
- templates define approved deployment patterns
- generators produce Argo, Kubernetes, Harness, dashboard, and alert assets
- policies prevent unsafe runtime patterns

# Harness AWS OIDC Bootstrap

This folder records the AWS trust policy used by the Harness AWS OIDC connector.

The connector avoids long-lived AWS access keys. Harness can assume the role only through the OIDC provider for account `c0ar0uHnRFa9kKNjOOf3rg`, org `default`, and project `enterprise_delivery_platform`.

Role:

```text
arn:aws:iam::808849570426:role/harness-oidc-enterprise-delivery-platform
```

Attached permissions:

- `AmazonEC2ContainerRegistryPowerUser`
- inline `HarnessConnectorValidationReadOnly` for `ec2:DescribeRegions` and `sts:GetCallerIdentity`

This role is intentionally limited for connector validation and ECR image operations. Terraform provisioning should use a separate explicitly approved role before infrastructure apply.

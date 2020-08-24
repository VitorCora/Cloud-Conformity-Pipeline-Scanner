import os
import sys
from pathlib import Path
import pytest

CWD = os.path.dirname(os.path.realpath(__file__))
PATH = Path(CWD)
PARENT_DIR = PATH.parent
APP_DIR = f"{PARENT_DIR}/src"
TEMPLATE_DIR = f"{PARENT_DIR}/demo"
sys.path.insert(0, APP_DIR)


def pytest_configure(config):
    config.addinivalue_line("markers", "external: tests which make external API calls")


@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    valid_template_file_path = f"{TEMPLATE_DIR}/secure-s3-bucket.json"
    monkeypatch.setenv("CFN_TEMPLATE_FILE_LOCATION", valid_template_file_path)
    monkeypatch.setenv("CC_RISK_LEVEL", "MEDIUM")


@pytest.fixture
def template_dir():
    return TEMPLATE_DIR


@pytest.fixture(
    params=[
        f"{PARENT_DIR}/demo/insecure-s3-bucket-disable-failure.json",
        f"{PARENT_DIR}/demo/insecure-s3-bucket-disable-failure.yaml",
    ]
)
def disabled_failed_pipeline_templates(request):
    return request.param


@pytest.fixture
def conformity_report():
    return {
        "data": [
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow public " "'READ' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public 'READ' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-001:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-001", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow public " "'READ_ACP' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public 'READ_ACP' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-002:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-002", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow public " "'WRITE' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public 'WRITE' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-003:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-003", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow public " "'WRITE ACP' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public 'WRITE_ACP' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-004:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-004", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow public " "'FULL_CONTROL' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public 'FULL_CONTROL' " "Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-005:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-005", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow " "authenticated users 'READ' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Authenticated Users 'READ' " "Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-006:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-006", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow " "authenticated users 'READ_ACP' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Authenticated Users " "'READ_ACP' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-007:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-007", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow " "authenticated users 'WRITE' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Authenticated Users 'WRITE' " "Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-008:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-008", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow " "authenticated users 'WRITE_ACP' access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Authenticated Users " "'WRITE_ACP' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-009:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-009", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow " "authenticated users 'FULL_CONTROL' " "access",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Authenticated Users " "'FULL_CONTROL' Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-010:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-010", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket has access logging "
                    "enabled delivering logs to "
                    "demo-log-bucket/demo",
                    "not-scored": False,
                    "pretty-risk-level": "Medium",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "MEDIUM",
                    "rule-title": "S3 Bucket Logging Enabled",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-011:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-011", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["reliability"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket has versioning enabled",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "S3 Bucket Versioning Enabled",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-012:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-012", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket configuration is " "MFA-Delete disabled",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "S3 Bucket MFA Delete Enabled",
                    "status": "FAILURE",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-013:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-013", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket doesn't allow public " "access via bucket policies",
                    "not-scored": False,
                    "pretty-risk-level": "Very High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "VERY_HIGH",
                    "rule-title": "S3 Bucket Public Access Via Policy",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-014:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-014", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not allow unknown " "cross account access",
                    "not-scored": False,
                    "pretty-risk-level": "High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "HIGH",
                    "rule-title": "S3 Cross Account Access",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-015:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-015", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket enforces Server-Side " "Encryption",
                    "not-scored": False,
                    "pretty-risk-level": "High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "HIGH",
                    "rule-title": "Server Side Encryption",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-016:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-016", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket enforces SSL to secure " "data in transit",
                    "not-scored": False,
                    "pretty-risk-level": "Medium",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "MEDIUM",
                    "rule-title": "Secure Transport",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-017:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-017", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["performance-efficiency"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket is using a " "DNS-compliant name",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "DNS Compliant S3 Bucket Names",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-018:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-018", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security", "cost-optimisation"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket does not utilize " "lifecycle configurations",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "S3 Buckets Lifecycle Configuration",
                    "status": "FAILURE",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-020:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-020", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Bucket MyS3Bucket has encryption enabled",
                    "not-scored": False,
                    "pretty-risk-level": "High",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "HIGH",
                    "rule-title": "S3 Bucket Default Encryption",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-021:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-021", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["security"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Object Lock is not enabled for " "MyS3Bucket",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "S3 Object Lock",
                    "status": "FAILURE",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-023:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-023", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": ["performance-efficiency"],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "ignored": False,
                    "last-updated-date": None,
                    "message": "Transfer Acceleration is enabled for " "MyS3Bucket",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "S3 Transfer Acceleration",
                    "status": "SUCCESS",
                    "tags": ["Name::MyS3Bucket"],
                    "waste": 0,
                },
                "id": "ccc:AccountId:S3-024:S3:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "S3-024", "type": "rules"}},
                },
                "type": "checks",
            },
            {
                "attributes": {
                    "categories": [
                        "security",
                        "reliability",
                        "performance-efficiency",
                        "cost-optimisation",
                        "operational-excellence",
                    ],
                    "cost": 0,
                    "descriptorType": "s3-bucket",
                    "extradata": [
                        {
                            "internal": True,
                            "label": "Resource tags status for " "s3-bucket MyS3Bucket",
                            "name": "DETAILED_STATUS",
                            "type": "META",
                            "value": '{"service":"S3","descriptorType":"s3-bucket","resourceName":"MyS3Bucket","tags":[{"key":"Environment","hasValue":false},{"key":"Role","hasValue":false},{"key":"Owner","hasValue":false},{"key":"Name","hasValue":true}]}',
                        }
                    ],
                    "ignored": False,
                    "message": "s3-bucket MyS3Bucket has [Environment, " "Role, Owner] tags missing",
                    "not-scored": False,
                    "pretty-risk-level": "Low",
                    "provider": "aws",
                    "region": "us-east-1",
                    "resource": "MyS3Bucket",
                    "risk-level": "LOW",
                    "rule-title": "Tags",
                    "status": "FAILURE",
                    "waste": 0,
                },
                "id": "ccc:AccountId:RG-001:ResourceGroup:us-east-1:MyS3Bucket",
                "relationships": {
                    "account": {"data": {"id": "AccountId", "type": "accounts"}},
                    "rule": {"data": {"id": "RG-001", "type": "rules"}},
                },
                "type": "checks",
            },
        ],
        "meta": {"missingParameters": []},
    }

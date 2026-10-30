# Subscription Dunning & Card Network Updater Re-Tokenization Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Visa Account Updater (VAU) and Mastercard Automatic Billing Updater (ABU) re-tokenization router, decline code categorization, and involuntary churn recovery. Built for GenPark (https://www.genpark.ai).

## Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## MCP Tools Exposed
- `process_card_network_account_updater`: Handle Visa/Mastercard Account Updater response to silently refresh expired card tokens without customer outreach.
- `calculate_dunning_campaign_recovery_yield`: Calculate recovered ARR and reduction in involuntary churn across automated dunning retry cascades.

## Installation & Usage
```bash
python -m genpark_agentic_commerce_automated_dunning_card_updater_vault_skill.server --test
```

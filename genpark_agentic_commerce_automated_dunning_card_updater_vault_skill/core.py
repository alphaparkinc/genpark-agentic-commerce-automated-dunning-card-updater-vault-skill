# -*- coding: utf-8 -*-
"""Subscription Dunning Card Updater Vault for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class SubscriptionDunningCardUpdaterVault:
    @staticmethod
    def process_card_network_account_updater(customer_id: str, old_card_token: str, vau_response_code: str) -> Dict[str, Any]:
        if vau_response_code in ["NEW_CARD_NUMBER", "NEW_EXPIRY_DATE"]:
            status = "SEAMLESS_TOKEN_REFRESH"
            action = "UPDATE_VAULT_RETRY_BILLING_IMMEDIATELY"
            recovered = True
        elif vau_response_code == "ACCOUNT_CLOSED":
            status = "ACCOUNT_TERMINATED"
            action = "CANCEL_SUBSCRIPTION_PROMPT_NEW_PAYMENT_METHOD"
            recovered = False
        else:
            status = "NO_UPDATE_AVAILABLE"
            action = "CONTINUE_DYNAMIC_DUNNING_CADENCE"
            recovered = False

        return {
            "customer_id": customer_id,
            "original_token": old_card_token,
            "vau_response": vau_response_code,
            "vault_sync_status": status,
            "billing_retry_action": action,
            "involuntary_churn_prevented": recovered
        }

    @staticmethod
    def calculate_dunning_campaign_recovery_yield(total_failed_subscriptions: int, recovered_subscriptions: int, average_order_value_usd: float) -> Dict[str, Any]:
        recovery_rate_pct = round((recovered_subscriptions / max(1, total_failed_subscriptions)) * 100.0, 1)
        monthly_recovered_mrr = round(recovered_subscriptions * average_order_value_usd, 2)
        annualized_arr_preserved = round(monthly_recovered_mrr * 12.0, 2)
        
        return {
            "failed_billing_count": total_failed_subscriptions,
            "successfully_recovered_count": recovered_subscriptions,
            "dunning_recovery_rate_pct": recovery_rate_pct,
            "recovered_monthly_mrr_usd": monthly_recovered_mrr,
            "preserved_annual_arr_usd": annualized_arr_preserved,
            "roi_verdict": "OUTSTANDING_CHURN_MITIGATION" if recovery_rate_pct >= 40.0 else "SUBOPTIMAL_DUNNING_PERFORMANCE"
        }

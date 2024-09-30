# TESTING PYNAMODB MODELS
# Description: This file is used to test the PynamoDB models that are used in the application.
# This is useful for testing the models without having to deploy the application to AWS.

from datetime import datetime

from shared.models.expense import ExpenseModel

expense = ExpenseModel(
    item_id="test",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    name="Hotdog",
    description="Tender juicy hotdog",
    place="7-Eleven",
    categories=["food", "snack"],
    quantity=2,
    unit="kg",
    unit_price=270,
)

expense.save()

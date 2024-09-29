# TESTING PYNAMODB MODELS
# Description: This file is used to test the PynamoDB models that are used in the application.
# This is useful for testing the models without having to deploy the application to AWS.

from financier.shared.models.expense import ExpenseModel

from datetime import datetime

expense = ExpenseModel(
    itemId="test",
    createdAt=datetime.now(),
    updatedAt=datetime.now(),
    name="Hotdog",
    description="Tender juicy hotdog",
    place="7-Eleven",
    categories=["food", "snack"],
    quantity=2,
    unit="kg",
    unitPrice=270
)

expense.save()

from django.core.exceptions import ValidationError

from rest_framework import serializers

from .validators import validate_possible_number

from . import models


class MpesaCheckoutSerializer(serializers.ModelSerializer):
    """MpesaCheckout Serializer Class"""
    class Meta:
        """Class Meta"""
        model = models.Transaction
        fields = (
            "phone_number",
            "amount",
            "reference",
            "description",
        )

    def validate_phone_number(self, phone_number):
        """A very Basic validation to remove the preceding + or replace the 0 with 254"""
        if phone_number[0] == "+":
            phone_number = phone_number[1:]
        if phone_number[0] == "0":
            phone_number = "254" + phone_number[1:]
        try:
            validate_possible_number(phone_number, "KE")
        except ValidationError as e:
            raise serializers.ValidationError({"error": f"Phone number is not valid {e}"})

        return phone_number

    def validate_amount(self, amount):
        """this methods validates the amount"""
        if not amount or float(amount) <= 0:
            raise serializers.ValidationError(
                {"error": "Amount must be greater than Zero"}
            )
        return amount

    def validate_reference(self, reference):
        """Write your validation logic here"""
        if reference:
            return reference
        return "Test"

    def validate_description(self, description):
        """Write your validation logic here"""
        if description:
            return description
        return "Test"


class TransactionSerializer(serializers.ModelSerializer):
    """Transaction serializer"""
    class Meta:
        """Class Meta"""
        model = models.Transaction
        fields = "__all__"

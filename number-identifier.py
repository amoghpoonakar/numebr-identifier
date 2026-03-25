import phonenumbers
from phonenumbers import (
    NumberParseException,
    geocoder,
    carrier,
    number_type,
    PhoneNumberType,
    region_code_for_number,
)


def get_number_type(num):
    t = number_type(num)
    return {
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE: "Landline",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Landline/Mobile",
        PhoneNumberType.TOLL_FREE: "Toll-Free",
        PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        PhoneNumberType.VOIP: "VoIP / Internet",
        PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        PhoneNumberType.UAN: "Corporate",
    }.get(t, "Unknown")


def analyze_number(raw_number: str) -> dict:
    try:
        if raw_number.startswith("+"):
            parsed = phonenumbers.parse(raw_number, None)
        else:
            parsed = phonenumbers.parse(raw_number, "IN")

        if not phonenumbers.is_possible_number(parsed):
            return {"error": "Impossible number format"}

        if not phonenumbers.is_valid_number(parsed):
            return {"error": "Number range not assigned"}

        return {
            "Valid": True,
            "Country": region_code_for_number(parsed),
            "Region": geocoder.description_for_number(parsed, "en"),
            "Allocated Carrier": carrier.name_for_number(parsed, "en") or "Unknown",
            "Number Type": get_number_type(parsed),
        }

    except NumberParseException:
        return {"error": "Invalid input"}


def main():
    print("Phone Number Analyzer")
    print("Type 'exit' to quit\n")

    while True:
        number = input("Enter phone number: ").strip()

        if number.lower() in ("exit", "quit", "q"):
            print("Goodbye 👋")
            break

        result = analyze_number(number)

        print("\nResult:")
        print("-------")

        if "error" in result:
            print(result["error"])
        else:
            for key, value in result.items():
                print(f"{key}: {value}")

        print()


if __name__ == "__main__":
    main()

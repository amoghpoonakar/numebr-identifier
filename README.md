# Phone Number Analyzer

A simple and efficient command-line tool to analyze phone numbers using the `phonenumbers` library. It validates numbers and provides detailed metadata such as country, region, carrier, and number type.

---

## Features

* Validate phone numbers (possible and assigned)
* Detect country and region
* Identify carrier information
* Classify number type (Mobile, Landline, VoIP, etc.)
* Supports international numbers
* Defaults to India ("IN") when no country code is provided

---

## Usage

Run the script:

```bash
python main.py
```

You will be prompted to enter a phone number:

```
Phone Number Analyzer
Type 'exit' to quit

Enter phone number: +14155552671
```

---

## Example Output

```
Result:
-------
Valid: True
Country: US
Region: California
Allocated Carrier: AT&T
Number Type: Mobile
```

---

## Error Handling

The tool handles common issues gracefully:

* Invalid input: Non-parsable numbers
* Impossible number format: Structurally incorrect numbers
* Number range not assigned: Valid format but not in use


---

## Dependencies

* `phonenumbers` — Python library for parsing, formatting, and validating international phone numbers

---

## How It Works

* Parses input using region-aware logic
* Validates number structure and assignment
* Extracts metadata:

  * Country code
  * Geographic region
  * Carrier information
  * Number type classification

---

## Notes

* If no country code is provided, the default region is set to India ("IN")
* Carrier detection may return "Unknown" for unsupported or new ranges
* Some numbers may be valid but lack detailed metadata depending on the database

---

## Author

Amogh Poonakar

---

## Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

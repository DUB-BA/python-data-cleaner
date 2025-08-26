# Python Data Cleaning Script

A powerful and efficient Python script designed to clean and standardize messy contact data from a CSV file. This project demonstrates core data manipulation skills using the Pandas library.

---

### The Problem

This script takes a "dirty" input file (`messy_contacts.csv`) with common data entry errors, such as:

-   Inconsistent capitalization (e.g., "JOHN", "Jane", "pEtEr").
-   Leading/trailing whitespace in column headers and data cells.
-   Multiple, inconsistent phone number formats (e.g., `555-123-4567`, `(555) 234-5678`).

### The Solution

The script performs the following cleaning operations:

1.  **Loads the Data:** Reads the messy CSV into a Pandas DataFrame.
2.  **Cleans Headers:** Strips all whitespace from the column names.
3.  **Standardizes Names:** Trims whitespace and applies proper capitalization (e.g., "John", "Doe") to the name columns.
4.  **Sanitizes Emails:** Trims whitespace and converts all email addresses to lowercase for consistency.
5.  **Formats Phone Numbers:** Uses regular expressions to strip all non-numeric characters, resulting in a clean, uniform phone number format (e.g., `5551234567`).
6.  **Exports Clean Data:** Saves the transformed, clean data to a new file, `clean_contacts.csv`, leaving the original file untouched.

### How to Use

1.  Place your messy CSV file in the same directory and name it `messy_contacts.csv`.
2.  Ensure you have the required Python library installed: `pip install pandas`
3.  Run the script from your terminal: `python cleaner.py`
4.  The clean output file, `clean_contacts.csv`, will be created in the same directory.

### Technologies Used

-   Python
-   Pandas
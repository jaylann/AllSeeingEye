from datetime import datetime


def convert_to_date(date):
    # Define a list of possible date formats
    date_formats = [
        # Day-Month-Year formats
        "%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y", "%d %B %Y", "%d %b %Y",
        "%A, %d %B %Y", "%a, %d %b %Y", "%d-%m-%y", "%d/%m/%y",

        # Year-Month-Day formats (universal)
        "%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d", "%Y %B %d", "%Y %b %d",
        # Add more formats as needed
    ]

    # Try to parse the date string using the defined formats
    for fmt in date_formats:
        try:
            return datetime.strptime(date, fmt)
        except ValueError:
            pass

    # If none of the formats match, raise an error
    raise ValueError("Invalid date format")
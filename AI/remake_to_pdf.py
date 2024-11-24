import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO  # Import BytesIO to handle in-memory file objects

# Function to map ANSI escape codes to RGB colors
def ansi_to_color(ansi_code):
    ansi_color_map = {
        "\u001b[91m": (255, 0, 0),  # Bright Red
        "\u001b[92m": (0, 255, 0),  # Bright Green
        "\u001b[93m": (255, 255, 0),  # Bright Yellow
        "\u001b[94m": (0, 0, 255),  # Bright Blue
        "\u001b[95m": (255, 0, 255),  # Bright Magenta
        "\u001b[96m": (0, 255, 255),  # Bright Cyan
        "\u001b[97m": (255, 255, 255),  # Bright White
        "\u001b[0m": None,  # Reset
    }
    return ansi_color_map.get(ansi_code, None)

def string_to_pdf_with_colors(text):
    # Create an in-memory BytesIO buffer to hold the PDF content
    buffer = BytesIO()

    # Create a PDF canvas and write the PDF data into the buffer
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Initial position for the text
    x, y = 50, 750

    # Split the text into lines
    lines = text.split('\n')

    for line in lines:
        if "\033[91m" in line:  # Check for red-highlighted lines
            pdf.setFillColorRGB(1, 0, 0)  # Set red color
            line = line.replace("\033[91m", "").replace("\033[0m", "")  # Clean ANSI codes
        else:
            pdf.setFillColorRGB(0, 0, 0)  # Default to black color
        
        pdf.drawString(x, y, line)
        y -= 15

        # If y is too low, create a new page
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    # Save the PDF into the buffer
    pdf.save()

    # Move buffer's cursor to the beginning of the file (important for reading later)
    buffer.seek(0)

    # Return the buffer which contains the PDF data (as a BLOB)
    return buffer
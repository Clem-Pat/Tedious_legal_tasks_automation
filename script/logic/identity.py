import pytesseract
import re
from PIL import Image

class IdentityExtractor(dict):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.text = self.extract_text()
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.place_of_birth = None
        self.extract_identity_info()

    def extract_text(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(self.image)
        return text

    def extract_identity_info(self):
        text = self.text

        # Regex patterns for extracting information
        name_pattern = re.compile(r"NOM\s*/\s*Sumame\s*(\w+)\s*(\w+)\s*", re.IGNORECASE)
        given_names_pattern = re.compile(r"Prenoms\s*/\s*Given names\s*([\w\s,]+)\s*", re.IGNORECASE)
        dob_pattern = re.compile(r"DATE DE NAISS\.\s*/\s*Date of birth\s*(\w+)\s*(\w+)\s*", re.IGNORECASE)
        pob_pattern = re.compile(r"LIEU DE NAISSANCE\s*/\s*Place of birth\s*(.+)\s*", re.IGNORECASE)

        # Extracting last name and first name
        name_match = name_pattern.search(text)
        if name_match:
            self.last_name = name_match.group(1)
            self.first_name = name_match.group(2)

        # Extracting given names
        given_names_match = given_names_pattern.search(text)
        if given_names_match:
            self.first_name = given_names_match.group(1).replace(',', ' ').strip()

        # Extracting date of birth
        dob_match = dob_pattern.search(text)
        if dob_match:
            raw_dob = dob_match.group(1)
            # Convert "01121995" to "01/12/1995"
            formatted_dob = re.sub(r"(\d{2})(\d{2})(\d{4})", r"\1/\2/\3", raw_dob)
            self.date_of_birth = formatted_dob

        # Extracting place of birth
        pob_match = pob_pattern.search(text)
        if pob_match:
            self.place_of_birth = pob_match.group(1).strip()
        

    def get_identity_info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "place_of_birth": self.place_of_birth
        }


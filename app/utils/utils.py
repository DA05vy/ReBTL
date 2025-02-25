import json
from typing import List, Dict


def load_data(file_path: str) -> List[Dict]:
    """
    Đọc dữ liệu từ file JSON và trả về nội dung.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

# if __name__ == "__main__":
#     # Replace with the correct path to your JSON file
#     data = load_data(r"C:\Users\manhh\OneDrive\Desktop\Python\app\utils\dummy_data.json")

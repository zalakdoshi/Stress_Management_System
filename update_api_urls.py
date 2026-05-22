import os

directory = r"d:\SAP\stress_ management_sys\frontend\src\pages"
target_text = "const API_URL = 'http://localhost:5000/api';"
replacement_text = "const API_URL = process.env.REACT_APP_API_URL || (window.location.hostname === 'localhost' ? 'http://localhost:5000/api' : '/api');"

print("Updating API URLs in frontend files...")

for filename in os.listdir(directory):
    if filename.endswith(".js"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if target_text in content:
            new_content = content.replace(target_text, replacement_text)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")

print("All frontend files updated successfully!")

import os
import logging

# Log formatını təyin edin
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Şablondan və iştirakçı siyahısından istifadə edərək fərdi dəvətnamələr yaradır.

    Args:
        template (str): Yer tutuculara malik dəvətnamə şablonu.
        attendees (list): İştirakçı məlumatlarını ehtiva edən lüğətlər siyahısı.
    """
    # 1. Giriş Növlərinin Yoxlanılması
    if not isinstance(template, str) or not isinstance(attendees, list):
        logging.error("Invalid input types: template must be a string and attendees must be a list of dictionaries.")
        return

    if attendees and not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input types: attendees list must contain only dictionaries.")
        return

    # 2. Boş Girişlərin Yoxlanılması
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Şablonda əvəz ediləcək yer tutucular
    placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
    
    # 3. Hər Bir İştirakçının Emalı
    for index, attendee in enumerate(attendees):
        # Fayl adını təyin edin (1-dən başlayaraq)
        output_filename = f"output_{index + 1}.txt"
        
        processed_invitation = template
        
        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = f"{{{key}}}"
            
            # 4. Çatışmayan Məlumatların İdarə Edilməsi
            # Attendee lüğətində açar yoxdursa və ya dəyər None-dırsa, "N/A" ilə əvəz edin
            value = attendee.get(key)
            if value is None:
                replacement = "N/A"
            else:
                replacement = str(value)
            
            # String replace metodu ilə yer tutucunu əvəz edin
            processed_invitation = processed_invitation.replace(placeholder, replacement)
        
        # 5. Çıxış Fayllarının Yaradılması
        try:
            with open(output_filename, 'w') as f:
                f.write(processed_invitation)
            logging.info(f"Successfully generated {output_filename}")
        except IOError as e:
            logging.error(f"Could not write to file {output_filename}: {e}")

# --- Test Proqramı ---

if __name__ == "__main__":
    # Test Data
    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"} # event_date = None (N/A olmalıdır)
    ]
    
    # Template-in fayldan oxunması
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        logging.error("template.txt not found. Please create it with the provided content.")
        template_content = "" # Boş şablon testini təmin etmək üçün
    
    print("--- Test 1: Normal İşləmə ---")
    generate_invitations(template_content, attendees_data)
    
    print("\n--- Test 2: Boş Şablon ---")
    generate_invitations("", attendees_data)
    
    print("\n--- Test 3: Boş İştirakçı Siyahısı ---")
    generate_invitations(template_content, [])
    
    print("\n--- Test 4: Yanlış Şablon Tipi ---")
    generate_invitations(123, attendees_data)
    
    print("\n--- Test 5: Yanlış İştirakçı Tipi ---")
    generate_invitations(template_content, "not a list")
    
    print("\n--- Test 6: Siyahıda Lüğət Olmayan Elementlər ---")
    attendees_bad_item = attendees_data + ["a string"]
    generate_invitations(template_content, attendees_bad_item)

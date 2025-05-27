import csv
import os
from django.conf import settings

# Construct the path to the CSV file relative to the app's directory
# Assuming the advisor app is at BASE_DIR / 'advisor'
CSV_FILE_PATH = os.path.join(settings.BASE_DIR, 'advisor', 'data', 'careers_data.csv')

def load_careers_from_csv():
    """
    Loads career data from the careers_data.csv file.
    Converts 'is_climate_action' to a boolean.
    Returns a list of career dictionaries.
    """
    careers = []
    try:
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert 'is_climate_action' from string 'TRUE'/'FALSE' to boolean
                is_climate_str = row.get('is_climate_action', 'FALSE').upper()
                row['is_climate_action'] = is_climate_str == 'TRUE'
                
                # Convert 'id' to integer if it exists
                if 'id' in row:
                    try:
                        row['id'] = int(row['id'])
                    except ValueError:
                        # Handle cases where id might be empty or not a valid int
                        # For now, we can assign a default or raise an error
                        # Let's assign 0 or some indicator, or simply leave as is if non-critical
                        pass # Or handle more gracefully

                # Split comma-separated strings into lists for skills and keywords
                if 'required_skills' in row and row['required_skills']:
                    row['required_skills'] = [skill.strip() for skill in row['required_skills'].split(',')]
                else:
                    row['required_skills'] = []

                if 'keywords' in row and row['keywords']:
                    row['keywords'] = [keyword.strip() for keyword in row['keywords'].split(',')]
                else:
                    row['keywords'] = []

                if 'education' in row and row['education']: # New section for education
                    row['education'] = [edu.strip() for edu in row['education'].split(',')]
                else:
                    row['education'] = []
                    
                careers.append(dict(row))
    except FileNotFoundError:
        # Handle the case where the CSV file might not exist
        # You could log this error or raise a specific exception
        print(f"ERROR: The CSV file was not found at {CSV_FILE_PATH}")
        # For a hackathon, returning an empty list might be acceptable to prevent crashes
        # For production, stricter error handling would be needed.
        return [] 
    except Exception as e:
        print(f"An error occurred while loading careers_data.csv: {e}")
        return [] # Return empty list or re-raise

    return careers

# Example of how to access the data (optional, for testing)
# if __name__ == '__main__':
#     # This part requires Django settings to be configured if CSV_FILE_PATH uses settings.BASE_DIR
#     # For standalone testing, you might need to adjust the path or configure settings.
#     # For now, this __main__ block is more for illustration.
#     # To run this standalone, ensure Django settings are minimally configured
#     # or replace CSV_FILE_PATH with a direct path for testing.
#     # Example: settings.configure(BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     
#     # For simplicity, this __main__ block will likely not run correctly without Django context.
#     # The function is intended to be called from within the Django app.
#     # careers_data = load_careers_from_csv()
#     # if careers_data:
#     #     print(f"Loaded {len(careers_data)} careers.")
#     #     for career in careers_data:
#     #         if career['is_climate_action']:
#     #             print(f"- {career['title']} (Climate Action!)")

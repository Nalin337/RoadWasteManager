import json
import os
import datetime

DATA_DIR = 'data'
DATA_FILE = os.path.join(DATA_DIR, 'reports.json')

def ensure_data_file_exists():
    """Checks if the data directory and file exist, creating them if not."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created directory: {DATA_DIR}")
    
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        print(f"Created data file: {DATA_FILE}")

def load_reports():
    """Loads all reports from the JSON file."""
    ensure_data_file_exists()
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_reports(reports):
    """Saves the list of reports to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(reports, f, indent=2)

def get_next_id(reports):
    """Calculates the next available ID."""
    if not reports:
        return 1
    return max(report['id'] for report in reports) + 1

def add_report():
    """Adds a new waste report."""
    print("\n--- Add New Waste Report ---")
    location = input("Enter Location (e.g., 'Main St & 2nd Ave'): ")
    waste_type = input("Enter Waste Type (e.g., 'Overflowing Bin', 'Illegal Dumping'): ")
    description = input("Enter Description: ")

    reports = load_reports()
    
    new_report = {
        "id": get_next_id(reports),
        "location": location,
        "type": waste_type,
        "description": description,
        "status": "Pending",
        "reported_at": datetime.datetime.now().isoformat()
    }
    
    reports.append(new_report)
    save_reports(reports)
    print(f"\n✅ Report #{new_report['id']} added successfully!")

def view_reports():
    """Displays all current waste reports."""
    reports = load_reports()
    
    if not reports:
        print("\nNo waste reports found.")
        return

    print("\n--- Current Waste Reports ---")
    for report in reports:
        print(f"\nID: {report['id']}")
        print(f"  Status:      {report['status']}")
        print(f"  Location:    {report['location']}")
        print(f"  Type:        {report['type']}")
        print(f"  Description: {report['description']}")
        print(f"  Reported At: {report['reported_at']}")
    print("-----------------------------")

def update_status():
    """Updates the status of an existing report."""
    view_reports()
    reports = load_reports()
    
    if not reports:
        return

    try:
        report_id = int(input("\nEnter the ID of the report to update: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    report_found = False
    for report in reports:
        if report['id'] == report_id:
            print(f"Current status for report #{report_id} is: {report['status']}")
            new_status = input("Enter new status (e.g., 'In Progress', 'Completed'): ")
            report['status'] = new_status
            report_found = True
            break
    
    if report_found:
        save_reports(reports)
        print(f"\n✅ Status for report #{report_id} updated to '{new_status}'.")
    else:
        print(f"\n❌ Report with ID #{report_id} not found.")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n--- ♻️ Road Waste Management System ---")
        print("1. Add New Waste Report")
        print("2. View All Reports")
        print("3. Update Report Status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_report()
        elif choice == '2':
            view_reports()
        elif choice == '3':
            update_status()
        elif choice == '4':
            print("\nExiting system. Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main_menu()

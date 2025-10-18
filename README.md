# Road Waste Management System

A simple command-line interface (CLI) application built with Python to log, track, and manage road waste reports.

This project allows users to simulate a waste management system by reporting incidents, viewing all current reports, and updating the status of a clean-up job. All data is saved in a `reports.json` file.

## Features

* **Add New Report**: Log a new waste incident with a location, type (e.g., "Overflowing Bin", "Illegal Dumping"), and description.
* **View All Reports**: Display a formatted list of all waste reports, including their ID, status, location, and details.
* **Update Report Status**: Change the status of a specific report using its ID (e.g., from "Pending" to "In Progress" or "Completed").
* **Persistent Storage**: All reports are saved to `data/reports.json` so no data is lost when the program closes.

## How to Run

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/YourUsername/RoadWasteManager.git](https://github.com/YourUsername/RoadWasteManager.git)
    cd RoadWasteManager
    ```

2.  **Run the application:**
    (This project uses only built-in Python libraries, so no installation is required.)
    ```bash
    python manager.py
    ```

3.  **Follow the on-screen prompts** to manage waste reports.

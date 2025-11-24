from datetime import datetime, timedelta

def calculate_harvest_schedule(planting_data):
    """
    Calculates the estimated harvest date for a list of crops based on
    their planting date and days to maturity (DTM).

    Args:
        planting_data (list): A list of dictionaries, where each dict
                              contains 'crop', 'plant_date', and 'dtm'.

    Returns:
        list: A list of dictionaries including the calculated 'harvest_date'.
    """
    schedule = []
    
    # Define the date format used for input and output
    DATE_FORMAT = "%Y-%m-%d" 
    
    print("\n--- Harvest Planning Schedule ---")

    for item in planting_data:
        try:
            # 1. Parse the planting date string into a datetime object
            plant_date_obj = datetime.strptime(item['plant_date'], DATE_FORMAT)
            
            # 2. Get the Days to Maturity (DTM)
            days_to_maturity = item['dtm']
            
            # 3. Calculate the harvest date
            # Add the timedelta (number of days) to the plant date
            harvest_date_obj = plant_date_obj + timedelta(days=days_to_maturity)
            
            # 4. Format the harvest date back into a string
            harvest_date_str = harvest_date_obj.strftime(DATE_FORMAT)

            # Store the final result
            schedule.append({
                'Crop': item['crop'],
                'Plant Date': item['plant_date'],
                'DTM (Days)': days_to_maturity,
                'Estimated Harvest': harvest_date_str
            })

        except ValueError as e:
            print(f"Error processing data for {item['crop']}: {e}")
            print("Please ensure the date format is YYYY-MM-DD.")
            continue
            
    return schedule

# --- 📅 User Input & Data ---

# Example Data: List of dictionaries for various crops
# 'dtm' = Days To Maturity
crop_planting_schedule = [
    # Succession planting example (same crop, different plant dates)
    {'crop': 'Lettuce (Batch 1)', 'plant_date': '2025-05-01', 'dtm': 45},
    {'crop': 'Lettuce (Batch 2)', 'plant_date': '2025-05-15', 'dtm': 45},
    
    # Long-term crops
    {'crop': 'Tomatoes', 'plant_date': '2025-04-15', 'dtm': 75}, 
    {'crop': 'Carrots', 'plant_date': '2025-05-05', 'dtm': 60}, 
    
    # Quick-harvest crops
    {'crop': 'Radishes', 'plant_date': '2025-05-10', 'dtm': 30},
    
    # Fall crop planning (for later in the season)
    {'crop': 'Winter Squash', 'plant_date': '2025-06-01', 'dtm': 90},
]

# --- 🚀 Execution ---

final_schedule = calculate_harvest_schedule(crop_planting_schedule)

# --- 📊 Output Formatting ---

if final_schedule:
    # Find the maximum width for each column for clean printing
    col_widths = {
        'Crop': max(len(d.get('Crop', '')) for d in final_schedule),
        'Plant Date': max(len(d.get('Plant Date', '')) for d in final_schedule),
        'DTM (Days)': max(len(str(d.get('DTM (Days)', ''))) for d in final_schedule),
        'Estimated Harvest': max(len(d.get('Estimated Harvest', '')) for d in final_schedule)
    }
    
    # Adjust widths for header titles if they are longer
    for key in col_widths:
        col_widths[key] = max(col_widths[key], len(key))

    # Print Header
    header = (
        f"{'Crop':<{col_widths['Crop']}} | "
        f"{'Plant Date':<{col_widths['Plant Date']}} | "
        f"{'DTM (Days)':>{col_widths['DTM (Days)']}} | " # Right-align numbers
        f"{'Estimated Harvest':<{col_widths['Estimated Harvest']}}"
    )
    print(header)
    print("-" * len(header))

    # Print Data Rows
    for row in final_schedule:
        print(
            f"{row['Crop']:<{col_widths['Crop']}} | "
            f"{row['Plant Date']:<{col_widths['Plant Date']}} | "
            f"{row['DTM (Days)']:>{col_widths['DTM (Days)']}} | "
            f"{row['Estimated Harvest']:<{col_widths['Estimated Harvest']}}"
        )
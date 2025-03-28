import os
import shutil

# List of files to archive (relative to your root folder)
files_to_archive = [
    "Stats/All_Player_Numbers.csv",
    "Stats/Cleaned_Trade_Evaluation_Data.csv",
    "Stats/Merged_Trade_Evaluation_Data.csv",
    "Stats/INPUT_Playstyle_Clustering_Value.csv",
    "Stats/Player_Salary.csv",
    "Stats/processed_player_data.csv",
    "Stats/Time_Per_Game_New.csv",
    "Stats/Player_Indecies.csv",
    "Stats/Cell output 22 [DW].csv",
    "Stats/Team_Payroll.xlsx",
]

# Create archive directory if it doesn't exist
archive_dir = "archive"
os.makedirs(archive_dir, exist_ok=True)

# Move each file if it exists
for filepath in files_to_archive:
    if os.path.exists(filepath):
        dest_path = os.path.join(archive_dir, os.path.basename(filepath))
        shutil.move(filepath, dest_path)
        print(f"✅ Moved: {filepath} → {dest_path}")
    else:
        print(f"⚠️ File not found, skipping: {filepath}")

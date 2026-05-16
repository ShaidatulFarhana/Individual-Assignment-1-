import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Point Python to the [subfolder].[filename]
from data.data_loader import load_data
from preprocessing.preprocessing import get_data_summary
from visualization.visualization import plot_analysis
from utility_function.utility_function import handle_error

def main():
    file_path = 'data/sleep_mobile_stress_dataset_15000.csv'
    try:
        df = load_data(file_path)
        get_data_summary(df)
        plot_analysis(df)
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}.")
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()
from data.data import load_data
from src.preprocessing import get_data_summary
from src.visualization import plot_analysis
from src.utils import handle_error

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

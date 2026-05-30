import os
import pandas as pd


def run_analyzer():
    print("--- Welcome to the Mini CSV Analyzer ---")

    # 1. Ask the user for the input file name
    input_file = input(
        "Enter the name of the CSV file to read (e.g., mock_data.csv): "
    )

    # Check if the file actually exists so the program doesn't crash
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found!")
        return

    # Load the dataset
    dataset = pd.read_csv(input_file)
    print("\nDataset loaded successfully!")
    print("Available columns:", list(dataset.columns))

    # 2. Ask the user what column they want to filter, and what value to look for
    filter_column = input(
        "\nWhich column do you want to filter by? (e.g., Age): "
    )

    if filter_column not in dataset.columns:
        print(f"Error: Column '{filter_column}' does not exist.")
        return

    filter_value = input(f"Enter the value to filter for in '{filter_column}': ")

    # Quick trick: If the column is numeric (like Age), convert the user input to a number
    if dataset[filter_column].dtype == "int64":
        filter_value = int(filter_value)
    elif dataset[filter_column].dtype == "float64":
        filter_value = float(filter_value)

    # 3. Filter the data
    filtered_data = dataset[dataset[filter_column] == filter_value]

    # Check if we actually found anything
    if filtered_data.empty:
        print("No rows found matching that criteria.")
        return

    print(f"\nFound {len(filtered_data)} matching rows!")

    # 4. Ask which column to compute statistics on (e.g., Salary)
    target_column = input(
        "Which numeric column do you want statistics for? (e.g., Salary): "
    )

    if target_column not in filtered_data.columns:
        print(f"Error: Column '{target_column}' does not exist.")
        return

    # 5. Compute Stats
    count_rows = filtered_data[target_column].count()
    max_val = filtered_data[target_column].max()
    mean_val = filtered_data[target_column].mean()

    print(f"\n--- Statistics for {target_column} ---")
    print(f"Count: {count_rows}")
    print(f"Max: {max_val}")
    print(f"Mean: {mean_val:.2f}")

    # 6. Save results to a new file
    output_file = input(
        "\nEnter the name of the file to save results to (e.g., results.csv): "
    )

    summary_df = pd.DataFrame(
        {
            "Metric": [
                f"Filtered Column: {filter_column}",
                f"Filtered Value: {filter_value}",
                "Total Count",
                "Max Value",
                "Mean Value",
            ],
            "Value": [None, None, count_rows, max_val, mean_val],
        }
    )

    summary_df.to_csv(output_file, index=False)
    print(f"🎉 Success! Results saved to '{output_file}'.")


# This line tells Python to run our function when the script starts
if __name__ == "__main__":
    run_analyzer()
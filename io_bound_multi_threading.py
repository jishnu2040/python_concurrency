from threading import Thread
from time import perf_counter
from pathlib import Path

def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    
    try:
        # Get the contents of the file
        with open(filename, 'r') as f:
            content = f.read()

        # Replace the substr by new_substr
        content = content.replace(substr, new_substr)

        # Write data into the file
        with open(filename, 'w') as f:
            f.write(content)

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    # Set the base path to the 'text' folder
    base_path = Path(r'C:\Users\rajeesh pk\Desktop\Python_concurrency\text')

    # List of text file paths inside the 'text' folder
    filenames = [base_path / f'task{i}.txt' for i in range(1, 10)]
    
    # Debugging: Print the list of filenames being processed
    print("Filenames to process:", filenames)

    # Create threads
    threads = [Thread(target=replace, args=(filename, 'ids', 'id')) for filename in filenames]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time - start_time:0.2f} second(s) to complete.')

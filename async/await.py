import asyncio
import time

async def fetch_data(api_id):
    await asyncio.sleep(5)  # Non-blocking sleep, simulates API response
    return f"Data from API {api_id}"

async def main():
    start_time = time.time()  # Start timer

    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    result1 = await task1
    result2 = await task2

    end_time = time.time()  # End timer

    # Print the results
    print(result1, result2)
    
    # Calculate and print the total execution time
    total_time = end_time - start_time
    print(f"Total execution time: {total_time:.2f} seconds")

asyncio.run(main())

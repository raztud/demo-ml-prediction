import sys
import os
import requests
import multiprocessing


def save_to_s3(data, s3_key):
    pass


def save_csv(url, s3_key):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            csv_content = response.content
            save_to_s3(csv_content, s3_key)

        else:
            print(f"Failed to download CSV file: {url}")
    except Exception as e:
        print(f"Error downloading CSV file {url} - {str(e)}")


def main():
    # this script will receive as parameter a text file with the urls, one per line
    if len(sys.argv) != 3:
        print("Usage: python downloader.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' not found.")
        sys.exit(1)

    try:
        with open(input_file_path, "r") as input_file:
            urls = input_file.readlines()
    except Exception as e:
        print(f"Error reading input file: {str(e)}")
        sys.exit(1)

    processes = []
    for idx, url in enumerate(urls):
        url = url.strip()
        s3_file = (
            f"csv_file_{idx}.csv"  # generate a smarter unique and identifiable name
        )
        process = multiprocessing.Process(target=save_csv, args=(url, s3_file))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()

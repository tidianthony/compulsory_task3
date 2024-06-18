# main.py
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Program started")

    try:
        # Example operation
        result = calculate_sum(10, 20)
        logging.info(f"Calculation result: {result}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    logging.info("Program finished")

if __name__ == "__main__":
    main()

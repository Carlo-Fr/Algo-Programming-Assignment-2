import sys

# Cache eviction policies

def fifo(k, requests):
    misses = 0
    # Add logic
    return misses

def lru(k, requests):
    misses = 0
    # Add logic
    return misses

def optff(k, requests):
    misses = 0
    # Add logic
    return misses

# Main and parsing

def main():
    # Make sure a file was passed in
    if len(sys.argv) < 2:
        print("Format: python cache_sim.py <input_file>")
        return

    filename = sys.argv[1]

    try:
        # Read text from file and split into list of numbers/words
        with open(filename, 'r') as file:
            data = file.read().split()
        # If there is no data    
        if not data:
            print("Error: Empty file")
            return
        # Read in capacity k and number of requests m
        k = int(data[0])
        m = int(data[1])
        
        # Parse the rest of the file into a list of integer requests
        # Parse the rest as a list of the integer IDs
        requests = []
        for i in range(2, len(data)):
            requests.append(int(data[i]))

        # Run simulations with different policies
        fifo_misses = fifo(k, requests)
        lru_misses = lru(k, requests)
        optff_misses = optff(k, requests)

        # Print output
        print(f"FIFO  : {fifo_misses}")
        print(f"LRU   : {lru_misses}")
        print(f"OPTFF : {optff_misses}")

    # Errors if file can't be found or if file contains non-integers
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
    except ValueError:
        print("Error: Input file must contain integers")

if __name__ == "__main__":
    main()
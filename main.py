from src.parser.MainClassParser import MainClassParser

def main():
    parser = MainClassParser()
    parser.parse_file("input/BlockchainAPIs")

if __name__ == "__main__":
    main()

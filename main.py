from src.parser.MainClassParser import MainClassParser

def main():
    parser = MainClassParser()
    main_file = parser.parse_file("input/BlockchainAPIs")
    print(main_file)

if __name__ == "__main__":
    main()

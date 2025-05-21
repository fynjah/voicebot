import asyncio
from logger import setup_logger
from logic import main_logic

def main():
    setup_logger()
    asyncio.run(main_logic())

if __name__ == "__main__":
    main()
import os
import time
import random
import asyncio
import datetime
from dotenv import load_dotenv
from src.hotbot import HotGameBot

async def main():
    load_dotenv()
    ACCOUNT_ID = os.getenv('ACCOUNT_ID')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    RPC = os.getenv('RPC')
    
    try:
        async with HotGameBot(ACCOUNT_ID, PRIVATE_KEY, rpc=RPC) as client:
            for i in range(5000):
                txn = await client.claim()
                print(txn.transaction_outcome.__dict__, flush=True)  # Flush output
                delay = 60 * 60 * 4 + random.randint(10, 60)
                print(f'\nWait for {str(datetime.timedelta(seconds=delay))}\n', flush=True)  # Flush output
                time.sleep(delay)
                print(f'Finished claiming at {datetime.datetime.now()}', flush=True)  # Flush output
    except Exception as e:
        print(f"An exception occurred: {e}")

asyncio.run(main())

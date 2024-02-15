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
    
    async with HotGameBot(ACCOUNT_ID, PRIVATE_KEY, rpc=RPC) as client:
        for i in range(5000):
            txn = await client.claim()
            print(txn.transaction_outcome.__dict__)
            delay = 60 * 60 * 2 + random.randint(10, 60)
            print(f'\nWait for{str(datetime.timedelta(seconds=delay))}\n')
            time.sleep(delay)
            #client.print_transaction(txn)

asyncio.run(main())
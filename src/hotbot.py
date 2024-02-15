from py_near.account import Account

class HotGameBot:
    def __init__(self, account_id, private_key, rpc=None):
        self._account_id = account_id
        self._private_key = private_key
        self._rpc = rpc if rpc is not None else 'https://rpc.mainnet.near.org'
        self.account = Account(
            self._account_id,
            self._private_key,
            rpc_addr=self._rpc
        )

    async def __aenter__(self):
        await self.account.startup()
        return self

    async def __aexit__(self, *args):
        return
    
    async def claim(self):
        return await self.account.function_call(
            'game.hot.tg',
            'claim',
            {},
            gas=30000000000000
        )
        
    @staticmethod
    def print_transaction(transaction_result):
        receipt_outcome = [receipt.__dict__ for receipt in transaction_result.receipt_outcome]
        receipts = transaction_result.receipts
        transaction_outcome = transaction_result.transaction_outcome.__dict__
        status = transaction_result.status
        transaction_data = transaction_result.transaction.__dict__
        logs = transaction_result.logs
        
        print(f'{receipt_outcome=}\n{receipts=}\n{transaction_outcome=}\n{status=}\n{transaction_data=}\n{logs=}\n')

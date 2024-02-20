import json
import pydantic
from typing import Optional

class Settings(pydantic.BaseModel):
    claim_every: int
    rpc: str

class Account(pydantic.BaseModel):
    account_id: str
    private_key: str
    balance: int

    def update_balance(self, balance):
        self.balance = balance

class Config(pydantic.BaseModel):
    settings: Optional[Settings]
    accounts: Optional[list[Account]]

    @staticmethod
    def from_json(file_path):
        with open(file_path, 'r') as file_handler:
            return Config(**json.load(file_handler))

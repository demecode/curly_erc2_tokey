# 1. In order to to deploty a contract you always need an account .....


from os import access
from scripts.helpers import get_account
from brownie import TheToken
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_tokey():
    account = get_account()
    print(account)
    the_token = TheToken.deploy(initial_supply, {"from": account})
    print(the_token.name())
    


def main():
    deploy_tokey()
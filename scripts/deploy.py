# 1. In order to to deploty a contract you always need an account .....


from os import access
from scripts.helpers import get_account


def deploy_tokey():
    account = get_account()
    print(account)
    


def main():
    deploy_tokey()
class AccountsController:
    def __init__(self):
        self.accounts = []
    
    def create_account(self, account):
        self.accounts.append(account)
        dbmanager.create_entry(account)
    
    def get_accounts(self):
        return self.accounts
    
    def update_account(self, account_id, account):
        for i, a in enumerate(self.accounts):
            if a['id'] == account_id:
                self.accounts[i] = account
                return True
        return False
    
    def delete_account(self, account_id):
        for i, a in enumerate(self.accounts):
            if a['id'] == account_id:
                del self.accounts[i]
                return True
        return False
    
    def get_account(self, account_id):
        for a in self.accounts:
            if a['id'] == account_id:
                return a
        return None

#db config ->Postgres
#dbmanager ->sql, Nosql

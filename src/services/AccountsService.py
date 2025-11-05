from controllers.AccountsController import AccountsController
from accounts_pb2_grpc import AccountsServiceServicer


class AccountsService(AccountsServiceServicer):
    def __init__(self):
        self.accounts_controller = AccountsController()
    
    def CreateAccount(self, request, context):
        return self.accounts_controller.create_account(request)
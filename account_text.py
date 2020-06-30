import unittest # Importing the unittest module
from account import Account # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Abdul","Ali","abc234","zizumoha2015@gmail.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Abdul")
        self.assertEqual(self.new_account.user_name,"Ali")
        self.assertEqual(self.new_account.password,"abc234")
        self.assertEqual(self.new_account.email,"zizumoha2015@gmail.com")


    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","46578907890","test@user.com") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678","test@user.com") # account
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_account_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0704631430","test@user.com") # new account
        test_account.save_account()

        found_account = Account.find_by_name("Test")

        self.assertEqual(found_account.email,test_account.email)    
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0704631430","test@user.com") # new account
        test_account.save_account()

        account_exists = Account.account_exist("0704631430")

        self.assertTrue(account_exists)
    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        displayed = Account.display_accounts()
        self.assertEqual(displayed,Account.account_list)    


if __name__ == '__main__':
    unittest.main()
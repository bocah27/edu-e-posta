from pages.accountDetails import AccountDetail
from pages.costa import Costa


email = input("isi email asli : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
costa = Costa(info, email)
costa.start_process()

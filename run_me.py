from pages.accountDetails import AccountDetail
from pages.costa import Costa

print("Hoşgeldiniz, iyi günler geçirmenizi dileriz.")
print("Bu betikle otomatik .edu e-postaları oluşturabilirsiniz.")
print("Amerikada olduğunuzu gösteren bir VPN kullanın")
print("---")
print("Anwar MEQOR tarafından yazıldı - github.com/AnwarMEQOR")
print("XORCAN tarafından türkçeleştirildi - github.com/xorcan")

email = input("E-posta adresinizi girin (sahte girmeyin, çalışmaz.) : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
costa = Costa(info, email)
costa.start_process()

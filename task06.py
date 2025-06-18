phone_num = (input("Telefon raqamingizni kiriting:+"))

if "99890" and "99891" in phone_num:
    print("Beeline")
if "99893" and "99894" in phone_num:
    print("Ucell")
if "99895" and '99897' in phone_num:
    print("MobiUz")
if '99888' and '99899' in phone_num:
    print("Uzmobile")
else:
    print("Noma'lum operator")            
from calc.fixedDeposite import FixedDeposite
from calc.sip import Sip
fd_total=FixedDeposite(100.00,5,2)
total_fd=fd_total.calculate()
print(f"fd_total:{total_fd:.2f}")

sip_total=Sip(100,5,2)
total_sip=sip_total.calculate()
print(f"SIP:{total_sip:.2f}")

teksts = input ("Ievadi tekstu: ")
def reverseText(teksts):
  if len(teksts)>1:
    sar1 = []
    for burts in teksts:
      sar1.append(burts)
    sar1.reverse()
    teksts = ""
    for elements in sar1:
      teksts += elements
    teksts = teksts.upper()
    print(teksts)
  else:
    teksts = "Pārāk iss teksts"
    print(teksts)
  return teksts
reverseText(teksts)
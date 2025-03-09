from file import File
from datetime import date

fs=File(r"C:\Users\Vampatapu Koushik\handson/1st Day")

print(fs.getMaxsizeFiles(2))
print(fs.getLatestFiles(date(2018,2,1)))
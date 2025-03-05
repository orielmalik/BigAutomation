#THIS SCRIPT IS EXAMPLE HOW TO USE MY PANDAS HELPER LIBARY
from Utils.PandasUtils import  *


target = PandasHelper(file_path = r"C:\Users\User\PycharmProjects\SeleVSPLA\Downloads\euro_coaches.csv")
print(target.read_file().sqlSelect("select * from  t1 where year>=1960 LIMIT 12"))



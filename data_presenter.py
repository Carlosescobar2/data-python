
open_file = open("CupcakeInvoices.csv")
total_amount = 0 
# for row in open_file:
#     print(row)
    
for line in open_file: 
        line = line.rstrip("/n").split(',')

        total_amount += float(line[3]) * float(line[4])


print(total_amount)


open_file.close()



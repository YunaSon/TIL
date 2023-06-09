
data = { 'header' : ['Supplier', 'Invoice Number', 'Part Number', 'Cost','Purchase Data'],
         'd1' : ['SupplierX', '001-1001', '2341', '$500.00', '1/20/2014'],
         'd2' : ['SupplierX', '001-1001', '2341', '$500.00', '1/20/2014'],
         'd3' : ['SupplierX', '001-1001', '5467', '$750.00', '1/20/2014'],
         'd4' : ['SupplierX', '001-1001', '5467', '$750.00', '1/20/2014'],
         'd5' : ['SupplierY', '50-9501', '7009', '$250.00', '1/30/2014'],
         'd6' : ['SupplierY', '50-9501', '7009', '$250.00', '1/30/2014'],
         'd7' : ['SupplierY', '50-9505', '6650', '$124.00', '2/3/2014'],
         'd8' : ['SupplierY', '50-9505', '6650', '$124.00', '2/3/2014'],
         'd9' : ['SupplierZ', '920-4803', '3321', '$615.00', '2/3/2014'],
         'd10' : ['SupplierZ', '920-4804', '3321', '$615.00', '2/10/2014'],
         'd11' : ['SupplierZ', '920-4805', '3321', '$615.00', '2/17/2014'],
         'd12' : ['SupplierZ', '920-4806', '3321', '$615.00', '2/24/2014'],
         'd13' : ['SupplierZ', '920-4807', '3322', '$1,000,615.00', '2/25/2014'],}
         
with open('supplier_data1.csv', 'w') as f:
    for i in data.values():
        j = ",".join(i) + '\n'
        f.write(j)

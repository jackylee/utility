import xlrd
import xlwt
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    data = xlrd.open_workbook(filename)
    table_input = data.sheets()[0]
    nrows = table_input.nrows
    ncols = table_input.ncols
    file = xlwt.Workbook()
    table_output = file.add_sheet("sheet1")
    line = 0
    col = 0
    table_output.write(line, 0, 'IP')
    table_output.write(line, 1, '设备名称')
    table_output.write(line, 2, '业务类型')
    table_output.write(line, 3, '节点')
    table_output.write(line, 4, '设备类型')
    table_output.write(line, 5, '厂商')
    line = line + 1
    for row in range(1, nrows):
        ip = ""
        ip_first = ""
        ip_second = ""
        name = ""
        bussiness = ""
        node_name = ""
        device_type = ""
        manufacture = ""
        for col in range(0, ncols):
           if col == 0:
               ip = table_input.cell_value(row, col)
           elif col == 1:
               name = table_input.cell_value(row, col)
           elif col == 2:
               bussiness = table_input.cell_value(row, col)
           elif col == 3:
               node_name = table_input.cell_value(row, col)
           elif col == 4:
               device_type = table_input.cell_value(row, col)
           elif col == 5:
                manufacture = table_input.cell_value(row, col)
        if '/' in ip:
            ips = ip.split('/')
            ip_dots = ips[0].split('.')
            ip_first = ips[0]
            ip_second = ip_dots[0] + '.' + ip_dots[1] + '.' + ip_dots[2] + '.' + ips[1]
            table_output.write(line, 0, ip_first)
            table_output.write(line, 1, name)
            table_output.write(line, 2, bussiness)
            table_output.write(line, 3, node_name)
            table_output.write(line, 4, device_type)
            table_output.write(line, 5, manufacture)
            line = line + 1
            table_output.write(line, 0, ip_second)
            table_output.write(line, 1, name)
            table_output.write(line, 2, bussiness)
            table_output.write(line, 3, node_name)
            table_output.write(line, 4, device_type)
            table_output.write(line, 5, manufacture)
            line = line + 1
        else:
            table_output.write(line, 0, ip)
            table_output.write(line, 1, name)
            table_output.write(line, 2, bussiness)
            table_output.write(line, 3, node_name)
            table_output.write(line, 4, device_type)
            table_output.write(line, 5, manufacture)
            line = line + 1
    file.save('output.xls')
        

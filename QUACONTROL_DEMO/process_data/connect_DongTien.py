import pymssql
import pandas as pd
from process_data.connect import Connect_SQLServer

class Data_DONGTIEN(Connect_SQLServer):

    def GET_DONGTIEN(self, params):
        # print(params)
        # params = self.convert_params(params)
        # if params[3] != "NULL":
        #     params[3] = f"N{params[3]}"
        # if params[7] in ("'ten_kh'"):
        #     params[8] = f"N{params[8]}"
        # print(params)
        proc_name = 'EXEC dsa_run_DongTien {0}, {1}, {2}, {3}, {4}, {5}'.format(*params)
        cursor = self.Call_Procedure(proc_name)
        if params[0][1:3] == "ov":
            cols = ['Tien']
        elif params[0] == "'dt_LoaiTien'":
            cols = ['ma_kho','ten_vt','tien']
        elif params[0] == "'table_tenvt'":
            cols = ['ten_vt','SoLuong']
        elif params[0] == "'detail'":
            cols = ['ma_kh', 'ten_kh','nh_kh','tien']
        else: cols = ['ma_kho','GiaTri','Text']
        return self.Convert_DataFrame(cursor, cols)
    
    def GET_TIME(self):
        con = pymssql.connect(Data_DONGTIEN)

        qr1 = "Select Top 1. Year(min(ngay_ct)) as min_y, Month(min(ngay_ct)) as min_m, Day(min(ngay_ct)) as min_d from dsa_tiencong"
        df_min = pd.read_sql_query(qr1, con)

        qr2 = "Select Top 1. Year(max(ngay_ct)) as max_y, Month(max(ngay_ct)) as max_m, Day(max(ngay_ct)) as max_d from dsa_tiencong"
        df_max = pd.read_sql_query(qr2, con)


    
        

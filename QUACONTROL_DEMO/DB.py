from process_data.connect_DongTien import Data_DONGTIEN
import pymssql

host = '192.168.1.123:2021'
db_name = 'QUACONTRO_FBOHRMSP2255_App'
uid = 'sa'
pwd = 'Dsa@613NTT!)'

DB_DONGTIEN = Data_DONGTIEN(host, db_name, uid, pwd)


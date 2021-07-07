import dash
import dash_core_components as dcc
import dash_html_components as html
from DB import DB_DONGTIEN
from app import app_DONG_TIEN
from dash.dependencies import Input, Output, State
from utils import GParams
from static.system_dashboard.css import css_define as css
import pandas as pd
from layouts.DongTien.GEN_OVERVIEW import create_card

def gen_layout():
    
    title = 'TỔNG TIỀN THU'
    color = '#548B54'
    icon = 'revenue.svg'

    layout = create_card(title,'ov_THU',color,icon)
           
    return layout


@app_DONG_TIEN.callback(
    Output("ov_THU", "children"),
    [Input('warehouse_date','date'),
     Input('grh_LOAITIEN','selectedData'),
     Input('grh_THUCHI','selectedData'),
     Input('grh_TIENVAY','clickData'),
     Input('detail_VAYNGANHANG','active_cell')],
    [State('detail_VAYNGANHANG','data')]
)
def UPDATE_OV_GT(date_wh,LOAITIEN,THUCHI,TIENVAY,DT_VNH,data_VNH):
    ctx = dash.callback_context
    datatable = {'detail_VAYNGANHANG':data_VNH}
    label, value = GParams.Get_Value(ctx,datatable)
    df = DB_DONGTIEN.GET_DONGTIEN(('ov_THU',date_wh,label,value))
    return df['Thu'].values[0]
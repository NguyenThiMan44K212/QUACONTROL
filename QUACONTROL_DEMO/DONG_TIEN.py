# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from datetime import date
from app import app_DONG_TIEN
from DB import DB_DONGTIEN
from index_string import index_str
from dash.dependencies import Input, Output, State
from layouts.DongTien import OV_TONGTIENMAT, OV_TONGTIENNGANHANG, OV_TONGTHU, OV_TONGCHI, DETAIL_TIENVAY, GRAPH_THU_CHI, GRAPH_TM_TNH, GRAPH_TIENVAY
                        


app_DONG_TIEN.index_string = index_str


def render_layout():

    # now = datetime.datetime.today().strftime('%Y-%m-%d')

    # df = DB_DONGTIEN.get_data()

    layout = html.Div([
        html.Div([
            html.Div([
                OV_TONGTIENMAT.gen_layout(),
                OV_TONGTIENNGANHANG.gen_layout(),
                OV_TONGTHU.gen_layout(),
                OV_TONGCHI.gen_layout()
            ],style={'height':'15vh'},className='ele_row m-b-10'),

            # html.Div([
            #     dcc.DatePickerSingle(
            #     id='warehouse_date',
            #     placeholder='Ngày',
            #     day_size = 42,
            #     clearable=True,
            #     number_of_months_shown=3,
            #     display_format = 'DD/MM/YYYY',
            #     date = now),
            # ],className='col',style ={'marginBottom':'10px'}),
            
            html.Div([
                dcc.DatePickerRange(
                id = 'date',
                min_date_allowed = date(DB_DONGTIEN.GET_TIME(df_min).min_y, 
                                        DB_DONGTIEN.GET_TIME(df_min).min_m, 
                                        DB_DONGTIEN.GET_TIME(df_min).min_d),
                max_date_allowed = date(DB_DONGTIEN.GET_TIME(df_max).max_y, 
                                        DB_DONGTIEN.GET_TIME(df_max).max_m, 
                                        DB_DONGTIEN.GET_TIME(df_max).max_d),
                calendar_orientation = 'vertical',)
                ],className='col',style ={'marginBottom':'10px'}),  

            # html.Div([
            #     dcc.DatePickerRange(
            #     id='warehouse_date',
            #     day_size = 42,
            #     display_format = 'DD/MM/YYYY',
            #     clearable=True,
            #     start_date_placeholder_text='Ngày bắt đầu',
            #     end_date_placeholder_text='Ngày kết thúc',
            #     number_of_months_shown=3,
            #     minimum_nights=0,
            #     start_date_id='start_date',
            #     end_date_id='end_date',
            #     start_date = min(df['ngay_ct']).strftime('%Y-%m-%d'),
            #     end_date = max(df['ngay_ct']).strftime('%Y-%m-%d'),)
            #     ],className='col',style ={'marginBottom':'10px'}),

            html.Div([
                GRAPH_THU_CHI.gen_layout(),
                GRAPH_TM_TNH.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15'),

            html.Div([
                GRAPH_TIENVAY.gen_layout(),
                DETAIL_TIENVAY.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15')

            # html.Div([
            #     dcc.DatePickerRange(
            #             id='date_DG',
            #             day_size = 42,
            #             display_format = 'DD/MM/YYYY',
            #             clearable=True,
            #             start_date_placeholder_text='Ngày bắt đầu',
            #             end_date_placeholder_text='Ngày kết thúc',
            #             number_of_months_shown=3,
            #             minimum_nights=0,
            #             start_date_id='start_date',
            #             end_date_id='end_date',
            #             start_date = min(df['ngay_giao']).strftime('%Y-%m-%d'),
            #             end_date = max(df['ngay_giao']).strftime('%Y-%m-%d'),)
            # ],className='col',style ={'marginBottom':'10px'}),

            # DDL_XE_DG.gen_layout(),

            # html.Div([
            #     SL_XE_DG.gen_layout(),
            #     DETAIL_XE_DG.gen_layout()
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

            # html.Div([
            #     SL_XE_DG_TG.gen_layout(),
            #     DETAIL_MAU_XE_DG.gen_layout(),
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

        ], className="container-fluid")
    ], className="section__content--p30", style={'backgroundColor': '#e5e5e5'})

    return layout

app_DONG_TIEN.layout = render_layout

if __name__ == '__main__':
    app_DONG_TIEN.run_server(port=2222, debug=True,host='127.0.0.1')
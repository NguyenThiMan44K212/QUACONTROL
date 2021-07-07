import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import urllib.parse
import pandas as pd
from dash_table.Format import Format, Scheme
from dash.dependencies import Input, Output, State
from static.system_dashboard.css import css_define as css
from utils import GParams, Graph
from app import app_DONG_TIEN
from DB import DB_DONGTIEN



def gen_layout():
    layout =html.Div([
                        html.Div([
                            html.Div([
                                html.Div("CHI TIẾT TÌNH HÌNH THANH TOÁN VAY NGÂN HÀNG", style={'width':'100%','background': '#e5ecf6'}),
                                html.A(
                                    children=[
                                        html.I(className="fas fa-file-download")
                                    ],
                                    id='download_detail_VAYNGANHANG',
                                    download="VAY_NGAN_HANG.csv",
                                    target="_blank",
                                    href = '',
                                    className='btn btn-primary',
                                    style={'position':'absolute','top':'0','right':'0','paddingTop':'0','paddingBottom':'0','height': '100%','display': 'inline-grid','alignItems': 'center'}
                                ),
                            ], style={'height': '10%','width':'100%','background': '#e5ecf6','textAlign':'center','display':'inline-grid','alignItems':'center','position':'relative'}),
                            dash_table.DataTable(
                                id='detail_VAYNGANHANG',
                                columns=[
                                    {
                                        'name': 'Mã khế ước', 
                                        'id': 'ma_ku'
                                    },
                                    {
                                        'name': 'Mã khách hàng', 
                                        'id': 'ma_kh'
                                    },
                                    {
                                        'name': 'Tên khách hàng', 
                                        'id': 'ten_kh'
                                    },
                                    {
                                        'name': 'Tài khoản', 
                                        'id': 'tk'
                                    },
                                    {
                                        'name': 'Ngày vay', 
                                        'id': 'ngay_vay'
                                    },
                                    {
                                        'name': 'Ngày đáo hạn', 
                                        'id': 'ngay_dh'
                                    },
                                    {
                                        'name': 'Số ngày còn lại', 
                                        'id': 'ngay_conlai',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Dư đầu kỳ', 
                                        'id': 'du_dk'
                                    },
                                    {
                                        'name': 'Phát sinh nợ', 
                                        'id': 'ps_no'
                                    },
                                    {
                                        'name': 'Phát sinh có', 
                                        'id': 'ps_co'
                                    },
                                    {
                                        'name': 'Dư cuối kỳ', 
                                        'id': 'du_ck'
                                    }
                                ],
                                style_cell_conditional=[
                                    {
                                        'if': {'column_id': 'ma_ku'},
                                        'width': '10%',
                                        'textAlign': 'left',
                                        'padding-left': '15px'
                                    },
                                    {
                                        'if': {'column_id': 'ma_kh'},
                                        'width': '10%'
                                    },
                                    {
                                        'if': {'column_id': 'ten_kh'},
                                        'width': '13%'
                                    },
                                    {
                                        'if': {'column_id': 'tk'},
                                        'width': '5%'
                                    },
                                    {
                                        'if': {'column_id': 'ngay_vay'},
                                        'width': '10%'
                                    },
                                    {
                                        'if': {'column_id': 'ngay_dh'},
                                        'width': '10%'
                                    },
                                    {
                                        'if': {'column_id': 'ngay_conlai'},
                                        'width': '7%'
                                    },
                                    {
                                        'if': {'column_id': 'du_dk'},
                                        'width': '10%'
                                    },
                                    {
                                        'if': {'column_id': 'ps_no'},
                                        'width': '10%'
                                    },
                                    {
                                        'if': {'column_id': 'ps_co'},
                                        'width': '10%'
                                    },{
                                        'if': {'column_id': 'du_ck'},
                                        'width': '10%'
                                    }
                                ],
                                css=[
                                        {
                                            'selector': '.dash-fixed-content',
                                            'rule': 'width: 100%;'
                                        }
                                    ],
                                fixed_rows={'headers': True},
                                style_header=css.style_header,
                                style_cell=css.style_cell,
                                page_action = 'none',
                                style_table={'height': '90%','width':'100%'},
                                sort_action="native",
                                # sort_mode="multi",
                                )
                        ], className="au-card",style={'height':'100%'})
                    ], className="col-6",style={'height':'100%'})

    return layout


@app_DONG_TIEN.callback(
    [Output("detail_VAYNGANHANG", "data"),
     Output("detail_VAYNGANHANG", "style_data_conditional")],
    [Input('warehouse_date','date'),
     Input('grh_LOAITIEN','selectedData'),
     Input('grh_THUCHI','selectedData'),
     Input('grh_TIENVAY','clickData'),
     Input('detail_VAYNGANHANG','active_cell')],
    [State('detail_VAYNGANHANG','data')]
)
def UPDATE_detail_VAYNGANHANG(date_wh,LOAITIEN,THUCHI,TIENVAY,DT_VNH,data_VNH):
    ctx = dash.callback_context
    datatable = {'detail_VAYNGANHANG':data_VNH}
    label, value = GParams.Get_Value(ctx,datatable) 
    df = DB_DONGTIEN.GET_DONGTIEN(('table_TIENVAY',date_wh,label,value))

    sdc =   (
                Graph.data_bars(df, 'ngay_conlai', '#8DB6CD') +
                [{
                    'if': {'row_index': 'even'},
                    'backgroundColor': '#f9f9f9'
                }]
            )
    return [df.to_dict(orient='records'), sdc]


@app_DONG_TIEN.callback(
     Output('download_detail_VAYNGANHANG', 'href'),
    [Input('download_detail_VAYNGANHANG','n_clicks'),
     Input('detail_VAYNGANHANG','data')]
)
def UPDATE_DOWNLOAD(click,data):
    df = pd.DataFrame.from_dict(data)
    csv_string = ""
    if len(df) > 0:
        csv_string = df.to_csv(index=False, encoding='utf-8',header=['Mã khế ước','Mã khách hàng','Tên khách hàng','Tài khoản','Ngày vay','Ngày đáo hạn','Số ngày còn lại','Dư đầu kỳ','Phát sinh nợ','Phát sinh có','Dư cuối kỳ'])
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + urllib.parse.quote(csv_string)
    return csv_string



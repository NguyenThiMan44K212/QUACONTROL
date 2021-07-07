import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output, State
from app import app_DONG_TIEN
from utils import Graph, GParams
from DB import DB_DONGTIEN



def gen_layout():
    layout =html.Div([
                html.Div([
                    dcc.Graph(id="grh_LOAITIEN", style={'width': '100%', 'height': '100%'})
                ],className='au-card' ,style={'width': '100%', 'height': '100%'})
            ], className="col-6" , style={'height':'100%'})

    return layout


@app_DONG_TIEN.callback(
    Output("grh_LOAITIEN", "figure"),
    [Input('warehouse_date','date'),
     Input('grh_LOAITIEN','selectedData'),
     Input('grh_THUCHI','selectedData'),
     Input('grh_TIENVAY','clickData'),
     Input('detail_VAYNGANHANG','active_cell')],
    [State('detail_VAYNGANHANG','data')]
)
def UPDATE_LOAITIEN(date_wh,LOAITIEN,THUCHI,TIENVAY,DT_VNH,data_VNH):
    ctx = dash.callback_context
    datatable = {'detail_VAYNGANHANG':data_VNH}
    label, value = GParams.Get_Value(ctx,datatable)
    df = DB_DONGTIEN.GET_DONGTIEN(('dt_LoaiTien',date_wh,label,value))
    return Graph.grh_BarChart(df['ngay_ct'],df['111', '112'],df['Text'],kind="bar",label_x='Thời gian',label_y='Giá trị',title='CƠ CẤU DÒNG TIỀN', margin = [50, 35, 35, 35])

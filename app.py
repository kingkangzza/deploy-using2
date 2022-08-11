import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
import json
import os
import folium
import plotly.express as px
import plotly.offline as pyo
import pandas as pd

# geojson load
seoul_nm = './tmp_data/seoul_SGG.geojson'
seoul_SGG = json.load(open(seoul_nm, encoding='utf-8'))

gangwon_nm = './tmp_data/gangwon_SGG.geojson'
gangwon_SGG = json.load(open(gangwon_nm, encoding='utf-8'))

# CSV load

##인구밀도
P_DEN_whole = pd.read_csv('./tmp_data/P_DEN_SGG2017.csv')

P_DEN_seoul = P_DEN_whole[P_DEN_whole['SD'] == '서울특별시'] # 서울 특별시만 한정해서 사용/
P_DEN_seoul['SGG_cd'] = P_DEN_seoul['SGG_cd'].astype(int)

P_DEN_gangwon = P_DEN_whole[P_DEN_whole['SD'] == '강원도'] # 강원도만 한정해서 사용/
P_DEN_gangwon['SGG_cd'] = P_DEN_gangwon['SGG_cd'].astype(int)

##조출생률
CBR_whole = pd.read_csv('./tmp_data/CBR_SGG2017.csv')

CBR_seoul = CBR_whole[CBR_whole['SD'] == '서울특별시'] # 서울 특별시만 한정해서 사용/
CBR_seoul['SGG_cd'] = CBR_seoul['SGG_cd'].astype(int)

CBR_gangwon = CBR_whole[CBR_whole['SD'] == '강원도'] # 강원도만 한정해서 사용
CBR_gangwon['SGG_cd'] = CBR_gangwon['SGG_cd'].astype(int)

##재정자립도
FI_whole = pd.read_csv('./tmp_data/FI_SGG2017.csv')

FI_seoul = FI_whole[FI_whole['SD'] == '서울특별시'] # 서울 특별시만 한정해서 사용/
FI_seoul['SGG_cd'] = FI_seoul['SGG_cd'].astype(int)

FI_gangwon = FI_whole[FI_whole['SD'] == '강원도'] # 강원도만 한정해서 사용/
FI_gangwon['SGG_cd'] = FI_gangwon['SGG_cd'].astype(int)

##유소년비율 & 고령화비율
AR_YR_whole = pd.read_csv('./tmp_data/AR_YR_SGG2017.csv')

AR_YR_seoul = AR_YR_whole[AR_YR_whole['SD'] == '서울특별시'] # 서울 특별시만 한정해서 사용/
P_DEN_seoul['SGG_cd'] = P_DEN_seoul['SGG_cd'].astype(int)

AR_YR_gangwon = AR_YR_whole[AR_YR_whole['SD'] == '강원도'] # 강원도만 한정해서 사용/
AR_YR_gangwon['SGG_cd'] = AR_YR_gangwon['SGG_cd'].astype(int)

# 오프라인 모드로 변경...
pyo.init_notebook_mode()

template='plotly_white'

fig_seoul = px.choropleth(P_DEN_seoul, geojson=seoul_SGG, locations='SGG_cd', color='P_DEN',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_seoul.update_geos(fitbounds="locations", visible=False)
fig_seoul.update_layout(title_text='인구밀도 예시 데이터로 추후 수정 예정입니다.', title_font_size=20)

fig_gangwon = px.choropleth(P_DEN_seoul, geojson=seoul_SGG, locations='SGG_cd', color='P_DEN',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_gangwon.update_geos(fitbounds="locations", visible=False)
fig_gangwon.update_layout(title_text='인구밀도 예시 데이터로 추후 수정 예정입니다.', title_font_size=20)


# 시설 수 관련 지표 그래프에 들어갈 예시 데이터
area=['전국', '인구감소지역(평균)', '관심지역(평균)','서울특별시']
y=[20, 14, 23,28]

#그래프 생성

#어린이집·유치원 수(2021)
fig = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig.update_layout(autosize=True, showlegend=False, template=template)
fig.update_layout(title={'text': "(단위:영유아 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig.update_layout(title_font_size=18)
fig.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#초·중·고교 수(2021)
fig1 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig1.update_layout(autosize=True, showlegend=False, template=template)
fig1.update_layout(title={'text': "(단위:학생 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig1.update_layout(title_font_size=18)
fig1.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#아동복지시설 수(2021)
fig2 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig2.update_layout(autosize=True, showlegend=False, template=template)
fig2.update_layout(title={'text': "(단위:아동 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig2.update_layout(title_font_size=18)
fig2.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#노인복지시설 수(2021)
fig3 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig3.update_layout(autosize=True, showlegend=False, template=template)
fig3.update_layout(title={'text': "(단위:노인 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig3.update_layout(title_font_size=18)
fig3.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')


# 총 활동인구 및 청년 활동인구
y_0 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_1 = [11,12,16,18,12,15,12,12,14,12,12,12]

x = ['01월','02월','03월','04월','05월','06월','07월','08월','09월','10월','11월','12월']

# 월별·업종별 카드 매출액
y_01 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_02 = [11,12,16,18,12,15,12,12,14,12,12,12]
y_03 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_04 = [11,12,16,18,12,15,12,12,14,12,12,12]
y_05 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_06 = [11,12,16,18,12,15,12,12,14,12,12,12]

x_01 = ['01월','02월','03월','04월','05월','06월','07월','08월','09월','10월','11월','12월']

# 거주지(광역시도)별 카드 매출액
city=['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','제주특별자치도','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']
use =[3.7,77.1,0.9,0.8,0.3,0.4,1.6,0.1,3.7,0.3,0.5,0.4,0.3,0.5,1.3,7.7,0.5]
marker_color=('mediumspringgreen','teal','lime','steelblue','lightsteelblue','dodgerblue','aqua','midnightblue','orange','crimson'
             ,'violet','plum','mistyrose','thistle','slateblue','blanchedalmond','goldenrod','lightpink')

#그래프 생성

# 접근성 관련 지표는 지도 그래프로 추후에 같은 크기에 지도가 들어갈 예정
a= go.Figure([go.Bar()])
a.update_layout(autosize=True, showlegend=False, template=template)

#의료시설 수(2021)
fig4 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig4.update_layout(autosize=True, showlegend=False, template=template)
fig4.update_layout(title={'text': "(단위:인구 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig4.update_layout(title_font_size=18)
fig4.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#문화·체육시설 수(2021)
fig5 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig5.update_layout(autosize=True, showlegend=False, template=template)
fig5.update_layout(title={'text': "(단위:인구 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig5.update_layout(title_font_size=18)
fig5.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#총 활동인구 및 청년 활동인구
fig6 = go.Figure()
fig6.add_trace(go.Bar(x=x,y=y_0,name='청년연령(만19시-34세)',marker=dict(color='rgb(102, 178, 255)'),text=y_0, textposition='auto'))
fig6.add_trace(go.Bar(x=x,y=y_1,name='그외연령',marker=dict(color='rgb(204, 229, 255)'),text=y_1, textposition='auto'))

fig6.update_layout(barmode='stack')
fig6.update_layout(yaxis_title='인구이동량 (단위:천 명)')
fig6.update_layout(xaxis_title='2021년')
fig6.update_layout(legend_title_text='울산광역시 울진군 연령대구분')
fig6.update_layout(autosize=True, template=template)
fig6.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#시간대별 청년 활동인구
fig7= go.Figure(data=go.Scatterpolar(r=[1, 5, 2, 2, 3,8,12,15,16,24,26,25,21,20,30,21,22,21,31,21,21,21,21,21,],
                                     theta=['18','19','20','21','22','23','0/24','1','2','3','4','5','6','7','8','9','10',
                                            '11','12','13','14','15','16','17'],
                                     fill='toself'))
fig7.update_layout(title={'text': "울산광역시 울진군 시간대별 청년 활동인구%",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
fig7.update_layout(polar=dict(radialaxis=dict(visible=True)),showlegend=False)
fig7.update_layout(autosize=True,template=template)

fig7.update_polars(angularaxis_gridwidth=0.1)
#fig7.update_polars(angularaxis_griddash='dash')
fig7.update_polars(angularaxis_gridcolor='gray')

fig7.update_polars(radialaxis_color='gray')
#fig7.update_polars(radialaxis_griddash='dash')
fig7.update_polars(radialaxis_showgrid=True)
fig7.update_polars(radialaxis_gridwidth=0.9)


#월별·업종별 카드 매출액
fig8 = go.Figure()
fig8.add_trace(go.Bar(x=x_01,y=y_01,name='생활서비스',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_02,name='소매/유통',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_03, name='여가/오락',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_04,name='음식',marker=dict( )))
fig8.add_trace(go.Bar(x=x_01,y=y_05,name='의료/건강',marker=dict( )))
fig8.add_trace(go.Bar(x=x_01,y=y_06,name='기타',marker=dict(color='rgb(204, 229, 255)')))

fig8.update_layout(barmode='stack')
fig8.update_layout(yaxis_title='매출액 (백만원 당)')
fig8.update_layout(xaxis_title='2021년')
fig8.update_layout(legend_title_text='울산광역시 울진군 6대 업종분류')
fig8.update_layout(autosize=True, template=template)

#거주지(광역시도)별 카드 매출액
fig9 = go.Figure()
fig9.add_trace(go.Bar(y=city,x=use,orientation="h",marker_color=marker_color,text=use, textposition='auto'))

fig9.update_layout(barmode='stack')
fig9.update_layout(yaxis_title='거주광역시도')
fig9.update_layout(xaxis_title='부산광역시 중구-2021년 매출액 시도별 분포%')
fig9.update_layout(autosize=True, template=template)
fig9.update_layout(modebar_orientation='h')

fig9.update_xaxes(showline=True, linewidth=3, linecolor='white', gridcolor='white')
fig9.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#종합병원 수(2021)
fig10 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig10.update_layout(autosize=True, showlegend=False, template=template)
fig10.update_layout(title={'text': "(단위:인구 천명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig10.update_layout(title_font_size=18)
fig10.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#지도 

# 오프라인 모드로 변경...
#pyo.init_notebook_mode()

template='plotly_white'

##인구밀도
fig_PDEN2017seoul = px.choropleth(P_DEN_seoul, geojson=seoul_SGG, locations='SGG_cd', color='P_DEN',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_PDEN2017seoul.update_geos(fitbounds="locations", visible=False)
fig_PDEN2017seoul.update_layout(title_text='2017년 서울 조출생률', title_font_size=20)

fig_PDEN2017gangwon = px.choropleth(P_DEN_gangwon, geojson=gangwon_SGG, locations='SGG_cd', color='P_DEN',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_PDEN2017gangwon.update_geos(fitbounds="locations", visible=False)
fig_PDEN2017gangwon.update_layout(title_text='2017년 강원도 인구밀도', title_font_size=20)

##조출생률
fig_CBR2017seoul = px.choropleth(CBR_seoul, geojson=seoul_SGG, locations='SGG_cd', color='CBR',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_CBR2017seoul.update_geos(fitbounds="locations", visible=False)
fig_CBR2017seoul.update_layout(title_text='2017년 서울 조출생률', title_font_size=20)

fig_CBR2017gangwon = px.choropleth(CBR_gangwon, geojson=gangwon_SGG, locations='SGG_cd', color='CBR',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_CBR2017gangwon.update_geos(fitbounds="locations", visible=False)
fig_CBR2017gangwon.update_layout(title_text='2017년 강원도 조출생률', title_font_size=20)

##재정자립도
fig_FI2017seoul = px.choropleth(FI_seoul, geojson=seoul_SGG, locations='SGG_cd', color='FI',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_FI2017seoul.update_geos(fitbounds="locations", visible=False)
fig_FI2017seoul.update_layout(title_text='2017년 서울 재정자립도', title_font_size=20)

fig_FI2017gangwon = px.choropleth(FI_gangwon, geojson=gangwon_SGG, locations='SGG_cd', color='FI',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_FI2017gangwon.update_geos(fitbounds="locations", visible=False)
fig_FI2017gangwon.update_layout(title_text='2017년 강원도 재정자립도', title_font_size=20)

##고령화비율
fig_AR2017seoul = px.choropleth(AR_YR_seoul, geojson=seoul_SGG, locations='SGG_cd', color='A_R',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_AR2017seoul.update_geos(fitbounds="locations", visible=False)
fig_AR2017seoul.update_layout(title_text='2017년 서울 고령화 비율', title_font_size=20)

fig_AR2017gangwon = px.choropleth(AR_YR_gangwon, geojson=gangwon_SGG, locations='SGG_cd', color='A_R',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_AR2017gangwon.update_geos(fitbounds="locations", visible=False)
fig_AR2017gangwon.update_layout(title_text='2017년 강원도 고령화 비율', title_font_size=20)

##유소년비율
fig_YR2017seoul = px.choropleth(AR_YR_seoul, geojson=seoul_SGG, locations='SGG_cd', color='Y_R',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_YR2017seoul.update_geos(fitbounds="locations", visible=False)
fig_YR2017seoul.update_layout(title_text='2017년 서울 유소년 비율', title_font_size=20)

fig_YR2017gangwon = px.choropleth(AR_YR_gangwon, geojson=gangwon_SGG, locations='SGG_cd', color='Y_R',
                                color_continuous_scale='Viridis',
                                featureidkey='properties.SGG_cd')
fig_YR2017gangwon.update_geos(fitbounds="locations", visible=False)
fig_YR2017gangwon.update_layout(title_text='2017년 강원도 유소년 비율', title_font_size=20)

## dash code

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "인구감소지역 지원방안"
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
#CONTENT_STYLE = {
#"margin-left": "2rem",
#"margin-right": "2rem",
#"padding": "1rem 1rem",
#}

sidebar = html.Div(
    [
        html.H2("지역선택", className="display-4"),
        html.Hr(),
        html.P(
            "지역 선택에 따른 페이지 변경", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("서울특별시", href="/", active="exact"),
                dbc.NavLink("강원도", href="/page-1", active="exact"),
                #dbc.NavLink("Page 2", href="/page-2", active="exact"),
                #dbc.NavLink("Page 3", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", className='page_content')

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            className='whole_div', children=[html.Div(className='head_div', children=[html.H1(children='인구감소지역 주요 현황')]),
                                            html.Div(className='left_div', children=[html.Div(className='p_up_down', children=[html.P(className='p_up_down_word', children='연평균 인구 증감율'),
                                                                                    html.Nav(className='p_up_down_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='p_up_down_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                    
                                                                                    html.Div(className='yp_move', children=[html.P(className='yp_move_word', children='청년순이동률'),
                                                                                    html.Nav(className='yp_move_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='yp_move_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='aging_ratio', children=[html.P(className='aging_ratio_word', children='고령화비율'),
                                                                                    html.Nav(className='aging_ratio_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='aging_ratio_map', children=dcc.Graph(figure=fig_AR2017seoul))]),
                                                                                     
                                                                                    html.Div(className='early_ratio', children=[html.P(className='early_ratio_word', children='조출생률'),
                                                                                    html.Nav(className='early_ratio_graph', children = dcc.Graph(figure=fig4)),
                                                                                    html.Nav(className='early_ratio_map', children=dcc.Graph(figure=fig_CBR2017seoul))]),
                                                                                     
                                                                                    html.Div(className='p_den', children=[html.P(className='p_den_word', children='인구밀도'),
                                                                                    html.Nav(className='p_den_graph', children = dcc.Graph(figure=fig5)),
                                                                                    html.Nav(className='p_den_map', children=dcc.Graph(figure=fig_PDEN2017seoul))]),
                                                                                     
                                                                                    html.Div(className='p_week', children=[html.P(className='p_week_word', children='주간인구'),
                                                                                    html.Nav(className='p_week_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='p_week_map', children=dcc.Graph(figure=fig_seoul))]), 
                                                                                     
                                                                                    html.Div(className='youth', children=[html.P(className='youth_word', children='유소년비율'),
                                                                                    html.Nav(className='youth_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='youth_map', children=dcc.Graph(figure=fig_YR2017seoul))]),
                                                                                     
                                                                                    html.Div(className='finance', children=[html.P(className='finance_word', children='재정자립도'),
                                                                                    html.Nav(className='finance_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='finance_map', children=dcc.Graph(figure=fig_FI2017seoul))]) 
                                                                                    
                                                                                    ]),
                                            
                                             html.Div(className='right_div', children=[html.Div(className='kinder', children=[html.P(className='kinder_word', children='어린이집·유치원'),
                                                                                    html.Nav(className='kinder_graph', children = dcc.Graph(figure=fig)),
                                                                                    html.Nav(className='kinder_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                    
                                                                                    html.Div(className='schools', children=[html.P(className='schools_word', children='초·중·고교'),
                                                                                    html.Nav(className='schools_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='schools_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='child_fa', children=[html.P(className='child_fa_word', children='아동복지시설'),
                                                                                    html.Nav(className='child_fa_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='child_fa_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='old_fa', children=[html.P(className='old_fa_word', children='노인복지시설'),
                                                                                    html.Nav(className='old_fa_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='old_fa_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='hospital_fa', children=[html.P(className='hospital_fa_word', children='의료시설'),
                                                                                    html.Nav(className='hospital_fa_graph', children = dcc.Graph(figure=fig4)),
                                                                                    html.Nav(className='hospital_fa_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='cul_phy', children=[html.P(className='cul_phy_word', children='문화·체육시설'),
                                                                                    html.Nav(className='cul_phy_graph', children = dcc.Graph(figure=fig5)),
                                                                                    html.Nav(className='cul_phy_map', children=dcc.Graph(figure=fig_seoul))]), 
                                                                                     
                                                                                    html.Div(className='general_hospital', children=[html.P(className='general_hospital_word', children='종합병원'),
                                                                                    html.Nav(className='general_hospital_graph', children = dcc.Graph(figure=fig10)),
                                                                                    html.Nav(className='general_hospital_map', children=dcc.Graph(figure=fig_seoul))]),
                                                                                     
                                                                                    html.Div(className='active_p', children=[html.P(className='active_p_word', children='지역 내 활동 인구 현황'),
                                                                                    html.Nav(className='active_p_graph1', children = dcc.Graph(figure=fig6)),
                                                                                    html.Nav(className='active_p_graph2', children=dcc.Graph(figure=fig7))]),
                                                                                        
                                                                                    html.Div(className='card_sales', children=[html.P(className='card_sales_word', children='지역 내 카드 매출액 현황'),
                                                                                    html.Nav(className='card_sales_graph1', children = dcc.Graph(figure=fig8)),
                                                                                    html.Nav(className='card_sales_graph2', children=dcc.Graph(figure=fig9))])    
                                                                                    
                                                                                    ])
                                            
                                            ]
        )
    elif pathname == "/page-1":
        return html.Div(className='whole_div', children=[html.Div(className='head_div', children=[html.H1(children='인구감소지역 주요 현황')]),
                                            html.Div(className='left_div', children=[html.Div(className='p_up_down', children=[html.P(className='p_up_down_word', children='연평균 인구 증감율'),
                                                                                    html.Nav(className='p_up_down_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='p_up_down_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                    
                                                                                    html.Div(className='yp_move', children=[html.P(className='yp_move_word', children='청년순이동률'),
                                                                                    html.Nav(className='yp_move_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='yp_move_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='aging_ratio', children=[html.P(className='aging_ratio_word', children='고령화비율'),
                                                                                    html.Nav(className='aging_ratio_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='aging_ratio_map', children=dcc.Graph(figure=fig_AR2017gangwon))]),
                                                                                     
                                                                                    html.Div(className='early_ratio', children=[html.P(className='early_ratio_word', children='조출생률'),
                                                                                    html.Nav(className='early_ratio_graph', children = dcc.Graph(figure=fig4)),
                                                                                    html.Nav(className='early_ratio_map', children=dcc.Graph(figure=fig_CBR2017gangwon))]),
                                                                                     
                                                                                    html.Div(className='p_den', children=[html.P(className='p_den_word', children='인구밀도'),
                                                                                    html.Nav(className='p_den_graph', children = dcc.Graph(figure=fig5)),
                                                                                    html.Nav(className='p_den_map', children=dcc.Graph(figure=fig_PDEN2017gangwon))]),
                                                                                     
                                                                                    html.Div(className='p_week', children=[html.P(className='p_week_word', children='주간인구'),
                                                                                    html.Nav(className='p_week_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='p_week_map', children=dcc.Graph(figure=fig_gangwon))]), 
                                                                                     
                                                                                    html.Div(className='youth', children=[html.P(className='youth_word', children='유소년비율'),
                                                                                    html.Nav(className='youth_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='youth_map', children=dcc.Graph(figure=fig_YR2017gangwon))]),
                                                                                     
                                                                                    html.Div(className='finance', children=[html.P(className='finance_word', children='재정자립도'),
                                                                                    html.Nav(className='finance_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='finance_map', children=dcc.Graph(figure=fig_FI2017gangwon))]) 
                                                                                    
                                                                                    ]),
                                            
                                             html.Div(className='right_div', children=[html.Div(className='kinder', children=[html.P(className='kinder_word', children='어린이집·유치원'),
                                                                                    html.Nav(className='kinder_graph', children = dcc.Graph(figure=fig)),
                                                                                    html.Nav(className='kinder_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                    
                                                                                    html.Div(className='schools', children=[html.P(className='schools_word', children='초·중·고교'),
                                                                                    html.Nav(className='schools_graph', children = dcc.Graph(figure=fig1)),
                                                                                    html.Nav(className='schools_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='child_fa', children=[html.P(className='child_fa_word', children='아동복지시설'),
                                                                                    html.Nav(className='child_fa_graph', children = dcc.Graph(figure=fig2)),
                                                                                    html.Nav(className='child_fa_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='old_fa', children=[html.P(className='old_fa_word', children='노인복지시설'),
                                                                                    html.Nav(className='old_fa_graph', children = dcc.Graph(figure=fig3)),
                                                                                    html.Nav(className='old_fa_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='hospital_fa', children=[html.P(className='hospital_fa_word', children='의료시설'),
                                                                                    html.Nav(className='hospital_fa_graph', children = dcc.Graph(figure=fig4)),
                                                                                    html.Nav(className='hospital_fa_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='cul_phy', children=[html.P(className='cul_phy_word', children='문화·체육시설'),
                                                                                    html.Nav(className='cul_phy_graph', children = dcc.Graph(figure=fig5)),
                                                                                    html.Nav(className='cul_phy_map', children=dcc.Graph(figure=fig_gangwon))]), 
                                                                                     
                                                                                    html.Div(className='general_hospital', children=[html.P(className='general_hospital_word', children='종합병원'),
                                                                                    html.Nav(className='general_hospital_graph', children = dcc.Graph(figure=fig10)),
                                                                                    html.Nav(className='general_hospital_map', children=dcc.Graph(figure=fig_gangwon))]),
                                                                                     
                                                                                    html.Div(className='active_p', children=[html.P(className='active_p_word', children='지역 내 활동 인구 현황'),
                                                                                    html.Nav(className='active_p_graph1', children = dcc.Graph(figure=fig6)),
                                                                                    html.Nav(className='active_p_graph2', children=dcc.Graph(figure=fig7))]),
                                                                                        
                                                                                    html.Div(className='card_sales', children=[html.P(className='card_sales_word', children='지역 내 카드 매출액 현황'),
                                                                                    html.Nav(className='card_sales_graph1', children = dcc.Graph(figure=fig8)),
                                                                                    html.Nav(className='card_sales_graph2', children=dcc.Graph(figure=fig9))])    
                                                                                    
                                                                                    ])
                                            
                                            ]
        )
#    elif pathname == "/page-2":
#        return html.P("Oh cool, this is page 2!")
#    elif pathname == "/page-3":
#        return html.P("Oh cool, this is page 3! and another function is possible?")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server()

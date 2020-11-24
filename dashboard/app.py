# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request
# plotly dan plotly.graph_objs : membuat plot
import plotly
import plotly.graph_objs as go
# pandas : untuk membaca csv dan men-generate dataframe
import pandas as pd
import json
## Joblib untuk Load Model
import joblib

# untuk membuat route
app = Flask(__name__)

###################
## CATEGORY PLOT ##
###################

## IMPORT DATA USING pd.read_csv
df = pd.read_csv('csv_building_structure_clean.csv')

# category plot function
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'district_id', cat_y = 'height_ft_pre_eq',
    estimator = 'count', hue = 'damage_grade_bin'):

    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in df[hue].unique():
            hist = go.Histogram(
                x=df[df[hue]==val][cat_x],
                y=df[df[hue]==val][cat_y],
                histfunc=estimator,
                name=val
            )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Histogram'

    elif cat_plot == 'boxplot':
        data = []

        for val in df[hue].unique():
            box = go.Box(
                x=df[df[hue] == val][cat_x], #series
                y=df[df[hue] == val][cat_y],
                name = val
            )
            data.append(box)
        title='Box'

    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    #json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():

    plot = category_plot()
    # dropdown menu
    # kita lihat pada halaman dashboard terdapat menu dropdown
    # terdapat lima menu dropdown, sehingga kita mengirimkan kelima variable di bawah ini
    # kita mengirimnya dalam bentuk list agar mudah mengolahnya di halaman html menggunakan looping
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('foundation_type', 'Foundation Type'), ('age_building', 'Age'), ('damage_grade_bin', 'Damage Grade'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('height_ft_pre_eq', 'Height'), ('plinth_area_sq_ft', 'Plinth Area'), ('height_ft_post_eq', 'Height Post'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('vdcmun_id', 'Municipality id'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]
    list_y = [('foundation_type', 'Foundation Type'), ('age_building', 'Age'), ('damage_grade_bin', 'Damage Grade'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('height_ft_pre_eq', 'Height'), ('plinth_area_sq_ft', 'Plinth Area'), ('height_ft_post_eq', 'Height Post'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('vdcmun_id', 'Municipality id'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('damage_grade_bin', 'Damage Grade'), ('foundation_type', 'Foundation Type'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]

    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot='histplot',
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x='foundation_type',

        # untuk sumbu Y tidak ada, nantinya menu dropdown Y akan di disable
        # karena pada histogram, sumbu Y akan menunjukkan kuantitas data

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator='count',
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue='damage_grade_bin',
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue)


@app.route('/cat_fn/<nav>')
def cat_fn(nav):

    # saat klik menu navigasi
    if nav == 'True':
        cat_plot = 'histplot'
        cat_x = 'district_id'
        cat_y = 'height_ft_pre_eq'
        estimator = 'count'
        hue = 'damage_grade_bin'
    
    # saat memilih value dari form
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    if estimator == None:
        estimator = 'count'
    
    # Saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'height_ft_pre_eq'

    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('foundation_type', 'Foundation Type'), ('age_building', 'Age'), ('damage_grade_bin', 'Damage Grade'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('height_ft_pre_eq', 'Height'), ('plinth_area_sq_ft', 'Plinth Area'), ('height_ft_post_eq', 'Height Post'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('vdcmun_id', 'Municipality id'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]
    list_y = [('foundation_type', 'Foundation Type'), ('age_building', 'Age'), ('damage_grade_bin', 'Damage Grade'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('height_ft_pre_eq', 'Height'), ('plinth_area_sq_ft', 'Plinth Area'), ('height_ft_post_eq', 'Height Post'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('vdcmun_id', 'Municipality id'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('damage_grade_bin', 'Damage Grade'), ('foundation_type', 'Foundation Type'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
    )


def pie_plot(hue = 'damage_grade_bin'):
    


    vcounts = df[hue].value_counts()

    labels = []
    values = []

    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])
    
    data = [
        go.Pie(
            labels=labels,
            values=values
        )
    ]

    layout = go.Layout(title='Pie', title_x= 0.48)

    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')

    if hue == None:
        hue = 'damage_grade_bin'

    list_hue = [('damage_grade_bin', 'Damage Grade'), ('foundation_type', 'Foundation Type'), ('roof_type', 'Roof Type'), ('land_surface_condition', 'Land Surface'), ('count_floors_pre_eq', 'Count Floors'), ('count_floors_post_eq', 'Count Floors Post'), ('district_id', 'District id'), ('position', 'Position'), ('other_floor_type', 'Other Floor Type'), ('plan_configuration', 'Plan Configuration'), ('age_bin', 'Age bins'), ('height_bin', 'Height bins'), ('plinth_area_bin', 'Plinth Area bins'), ('condition_post_eq', 'Condition Post Eq'), ('technical_solution_proposed', 'Technical Solution'), ('has_superstructure_adobe_mud', 'Adobe Mud as Superstructure'), ('has_superstructure_mud_mortar_stone', 'Mud Mortar Stone as Superstructure'), ('has_superstructure_stone_flag', 'Stone as Superstructure'), ('has_superstructure_cement_mortar_stone', 'Cement Mortar Stone as Superstructure'), ('has_superstructure_mud_mortar_brick', 'Mud Mortar Brick as Superstructure'), ('has_superstructure_cement_mortar_brick', 'Cement Mortar Brick as Superstructure'), ('has_superstructure_timber', 'Timber as Superstructure'), ('has_superstructure_bamboo', 'Bamboo as Superstructure'), ('has_superstructure_rc_non_engineered', 'RC non engineered as Superstructure'), ('has_superstructure_rc_engineered', 'RC engineered as Superstructure')]

    plot = pie_plot(hue)
    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue= list_hue)


@app.route('/data_fn')
def data_fn():
    data = pd.read_csv('csv_building_structure_clean.csv')
    df = data.head(21).to_html(classes = 'data')
    return render_template('data.html',  tables=[df])


@app.route('/pred_lr')
## Menampilkan Dataset
def pred_lr():
    return render_template('predict.html')

@app.route("/pred_result", methods = ["POST","GET"])
def pred_result():
    if request.method == "POST":
        input = request.form

        age = int(input['age'])

        height = float(input['height'])

        plinth = float(input['plinth'])

        foundation = input['foundation']
        if foundation == 'Mud mortar-Stone/Brick':
            strFoundation = 'Mud mortar-Stone/Brick'
            dataFoundation = 'Mud mortar-Stone/Brick'
        elif foundation == 'Bamboo/Timber':
            strFoundation = 'Bamboo/Timber'
            dataFoundation = 'Bamboo/Timber'
        elif foundation == 'Cement-Stone/Brick':
            strFoundation = 'Cement-Stone/Brick'
            dataFoundation = 'Cement-Stone/Brick'
        elif foundation == 'RC':
            strFoundation = 'RC'
            dataFoundation = 'RC'
        elif foundation == 'Other':
            strFoundation = 'Other'
            dataFoundation = 'Other'
        
        roof = input['roof']
        if roof == 'Bamboo/Timber-Light roof':
            strRoof = 'Bamboo/Timber-Light roof'
            dataRoof = 'Bamboo/Timber-Light roof'
        elif roof == 'Bamboo/Timber-Heavy roof':
            strRoof = 'Bamboo/Timber-Heavy roof'
            dataRoof = 'Bamboo/Timber-Heavy roof'
        elif roof == 'RCC/RB/RBC':
            strRoof = 'RCC/RB/RBC'
            dataRoof = 'RCC/RB/RBC'
        
        ground = input['ground']
        if ground == 'Mud':
            strGround = 'Mud'
            dataGround = 'Mud'
        elif ground == 'RC':
            strGround = 'RC'
            dataGround = 'RC'
        elif ground == 'Brick/Stone':
            strGround = 'Brick/Stone'
            dataGround = 'Brick/Stone'
        elif ground == 'Timber':
            strGround = 'Timber'
            dataGround = 'Timber'
        elif ground == 'Other':
            strGround = 'Other'
            dataGround = 'Other'
        


        feature = pd.DataFrame({
            'foundation_type' : [dataFoundation],
            'roof_type' : [dataRoof],
            'ground_floor_type' : [dataGround],
            'age_building' : [age],
            'height_ft_pre_eq' : [height],
            'plinth_area_sq_ft' : [plinth],
        })

        pred = model.predict(feature)[0]
        print(pred)

        if pred == 0:
            rslt = 'Low Risk Potential'
        else:
            rslt = 'High Risk Potential'
        
        return render_template('result.html', age = age, height = height, plinth = plinth, foundation = strFoundation, roof = strRoof, 
            ground = strGround, result = rslt)
    


if __name__ == '__main__':
    ## Load Model
    model = joblib.load('model_lr.sav')
    app.run(debug=True)
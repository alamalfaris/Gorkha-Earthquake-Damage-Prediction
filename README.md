# Nepal Earthquake Damage Prediction

## Background: 
> - Negara nepal memiliki kerentanan terhadap gempa karena terletak di selatan perbatasan pertemuan lempeng India yang berada dibawahnya lempeng Eurasia. Setiap tahunnya lempeng India bergerak sebanyak 43 mm per tahun. Sehingga menyebabkan Nepal sering mengalami gempa bumi.

> - 25 April 2015 Nepal mengalami gempa yang terparah sejak 1934, dengan korban meninggal sebanyak 8964 jiwa, korban luka sebanyak 21952 orang, dan 3.5 juta orang menjadi homeless akibat dari banyaknya bangunan yang rusak. Gempa ini memiliki magnitudo sebesar 7.8 Mw (Moment Magnitudo Scale) dengan pusat gempa di Barpak, Distrik Gorkha, dan kedalaman hipocenter sekitar 8.2 km

## Problem:
> - Jika terjadi gempa yang sama, bagaimana dapat mengetahui level kerusakan bangunan dengan kombinasi spesifikasi bangunan

> - Sampai saat ini kemunculan gempa bumi belum bisa diprediksi secara akurat, karena gempa merupakan bencana yang kompleks, melibatkan banyak variabel. Lalu bagaimana pemerintah Nepal dapat mengurangi resiko akibat gempa bumi terkhusus resiko di sektor infrastruktur

## Limitation:
> Model yang akan saya bukanlah model yang serba bisa menebak apapun. Batas dari model ini hanya dapat menebak level kerusakan yang diakibatkan oleh gempa yang sama seperti gempa Gorkha (Magnitudo: 7.8 Mw; Epicenter: Barpak, Gorkha District; Hypocenter: 8.2 km) dari grade 1-5 berdasarkan fitur-fitur yang berkaitan dengan spesifikasi bangunan tempat tinggal(jenis pondasi, jenis atap, struktur, dll).

## Goal: 
> Memprediksi level kerusakan sebuah bangunan akibat gempa bumi, kemudian nantinya pemerintah dapat menghitung nilai kerusakan lalu membuat perencanaan untuk pendanaan kebencanaan

## About data:
> Data yang digunakan saya peroleh dari https://eq2015.npc.gov.np/#/ yang dikumpulkan antara Januari - May 2016

### Feature Description:
- 'building_id': A unique ID that identifies a unique building from the survey
- 'district_id': District where the building is located
- 'vdcmun_id': Municipality where the building is located
- 'ward_id': Ward Number in which the building is located
- 'count_floors_pre_eq': Number of floors that the building had before the earthquake 
- 'count_floors_post_eq': Number of floors that the building had after the earthquake
- 'age_building': Age of the building (in years)
- 'plinth_area_sq_ft': Plinth area of the building (in square feet)
- 'height_ft_pre_eq': Height of the building before the earthquake (in feet)
- 'height_ft_post_eq': Height of the building after the earthquake (in feet)
- 'land_surface_condition': Surface condition of the land in which the building is built
- 'foundation_type': Type of foundation used in the building
- 'roof_type': Type of roof used in the building
- 'ground_floor_type': Ground floor type 
- 'other_floor_type': Type of construction used in other floors (except ground floor and roof)
- 'position': Position of the building
- 'plan_configuration': Building plan configuration
- 'has_superstructure_adobe_mud': Flag variable that indicates if the superstructure of the building is made of Adobe/Mud (0: No, 1: Yes)
- 'has_superstructure_mud_mortar_stone': Flag variable that indicates if the superstructure of the building is made of Mud Mortar - Stone
- 'has_superstructure_stone_flag': Flag variable that indicates if the superstructure of the building is made of Stone
- 'has_superstructure_cement_mortar_stone': Flag variable that indicates if the superstructure of the building is made of Stone
- 'has_superstructure_mud_mortar_brick': Flag variable that indicates if the superstructure of the building is made of Cement Mortar - Stone
- 'has_superstructure_cement_mortar_brick': Flag variable that indicates if the superstructure of the building is made of Mud Mortar - Brick 
- 'has_superstructure_timber': Flag variable that indicates if the superstructure of the building is made of Timber
- 'has_superstructure_bamboo': Flag variable that indicates if the superstructure of the building is made of Bamboo
- 'has_superstructure_rc_non_engineered': Flag variable that indicates if the superstructure of the building is made of RC (Non Engineered)
- 'has_superstructure_rc_engineered': Flag variable that indicates if the superstructure of the building is made of RC (Engineered)
- 'has_superstructure_other': Flag variable that indicates if the superstructure of the building is made of any other material
- 'condition_post_eq': Actual contition of the building after the earthquake
- 'damage_grade': Damage grade assigned to the building by the surveyor after assessment
- 'technical_solution_proposed': Technical solution proposed by the surveyor after assessment

## Kesimpulan
> Setelah melakukan analisis yang cukup panjang di atas, saya sampai pada kesimpulan:

> 1. Bangunan dengan level kerusakan high-risk memiliki beberapa ciri:

>   - Memiliki usia di atas 10 tahun
>   - Menggunakan pondasi berjenis Mud Mortar-Stone/Brick
>   - Menggunakan superstruktur berjenis adobe_mud, mud mortar-stone, stone_flag, mud_mortar_brick, dan timber
>   - Menggunakan ground floor berjenis mud dan brick/stone
>   - Menggunakan atap berjenis Bamboo/Timber-Heavy roof dan Bamboo/Timber-Light roof
>   - Memiliki posisi Not attached dan Attached 1-side

> 2. Bangunan dengan level kerusakan low-risk memiliki beberapa ciri:

>   - Memiliki usia dibawah 10 tahun
>   - Menggunakan pondasi berjenis Bamboo/Timber, Cement-Stone/Brick, dan RC
>   - Menggunakan superstruktur berjenis cement_mortar_stone, cement_mortar_brick, bamboo, dan RC
>   - Menggunakan ground floor berjenis RC (reinforced concrete) dan Timber
>   - Menggunakan atap berjenis RCC/RB/RBC
>   - Memiliki posisi Attached 2-side dan Attached 3-side

> 3. Untuk meningkatkan ketahanan bangunan terhadap gempa cara yang bisa dilakukan yaitu memperkuat SDM dibidang konstruksi, men-train para tukang bangunan untuk membuat bangunan yang lebih kokoh meski dari material sederhana. Kemudian memperkuat bangunan dengan menggunakan material yang terbaik.

> 4. Setelah mengetahui level kerusakan tiap bangunan, pemerintah bisa meneruskan dengan menghitung nilai bangunan yang nantinya akan dimasukkan dalam program disaster risk-financing, perencanaan keuangan yang lebih baik untuk menghadapi bencana sewaktu-waktu.

# Nepal Earthquake Damage Prediction

## Background: 
> - Negara nepal terletak di selatan perbatasan pertemuan lempeng India yang berada dibawahnya lempeng Eurasia. Setiap tahunnya lempeng India bergerak sebanyak 43 mm per tahun. Sehingga menyebabkan Nepal sering mengalami gempa bumi.

> - 25 April 2015 Nepal mengalami gempa yang terparah sejak 1934, dengan korban meninggal sebanyak 8964 jiwa, korban luka sebanyak 21952 orang, dan 3.5 juta orang menjadi homeless. Kerugian ekonomi diperkirakan 35% dari PDB Nepal. Gempa ini memiliki magnitudo sebesar 7.8 Mw (Moment Magnitudo Scale) dengan pusat gempa di Barpak, Distrik Gorkha, dan kedalaman hipocenter sekitar 8.2 km

## Problem:
> - Jika terjadi gempa yang sama, bagaimana dapat mengetahui level kerusakan bangunan dengan kombinasi spesifikasi struktur tertentu

> - Sampai saat ini kemunculan gempa bumi belum bisa diprediksi secara akurat, karena gempa merupakan bencana yang kompleks, melibatkan banyak variabel. Lalu bagaimana pemerintah Nepal dapat mengurangi resiko akibat gempa bumi terkhusus resiko di sektor infrastruktur

## Limitation:
> Model yang akan saya bukanlah model yang serba bisa menebak apapun. Batas dari model ini hanya dapat menebak level kerusakan yang diakibatkan oleh gempa yang sama seperti gempa Gorkha (Magnitudo: 7.8 Mw; Epicenter: Barpak, Gorkha District; Hypocenter: 8.2 km) dari grade 1-5 berdasarkan fitur-fitur yang berkaitan dengan spesifikasi bangunan tempat tinggal(jenis pondasi, jenis atap, struktur, dll).

## Goal: 
> Memprediksi level kerusakan sebuah bangunan akibat gempa bumi yang terbagi menjadi 5 level, kemudian nantinya pemerintah dapat menghitung nilai kerusakan lalu membuat perencanaan untuk pendanaan kebencanaan

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

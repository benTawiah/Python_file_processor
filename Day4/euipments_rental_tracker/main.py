from equipment_fuction import get_equipments, collect_equipments,show_equipment
from storage_function import save_content, load_content


coll_equip = collect_equipments()
content_load = load_content()
content_load.extend(coll_equip)

save_content(coll_equip)


for equipment in coll_equip:
    print("--------Equipment----------")
    show_equipment(equipment)          
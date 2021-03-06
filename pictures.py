import pandas as pd
import numpy as np
from PIL import Image



tn_im=f"images/tn.png"
al_im=f"images/al.png"
asu_im=f"images/asu.png"
ark_state_im=f"images/ark_state.png"
ak_im=f"images/ak.png"
aub_im=f"images/aub.png"
byu_im=f"images/byu.png"
cal_im=f"images/cal.png"
col_state_im=f"images/col_state.png"
ucf_im=f"images/ucf.png"
clem_im=f"images/clem.png"
duke_im=f"images/duke.png"
fl_im=f"images/fl.png"
fsu_im=f"images/fsu.png"
fres_im=f"images/fres.png"
uga_im=f"images/uga.png"
gt_im=f"images/gt.png"
hawaii_im=f"images/hawaii.png"
indiana_im=f"images/indiana.png"
iowa_im=f"images/iowa.png"
hous_im=f"images/hous.png"
ks_im=f"images/ks.png"
uk_im=f"images/uk.png"
latech_im=f"images/latech.png"
lou_im=f"images/lou.png"
lsu_im=f"images/lsu.png"
mem_im=f"images/mem.png"
mia_im=f"images/mia.png"
mich_im=f"images/mich.png"
miss_im=f"images/miss.png"
middle_tn_im=f"images/middle_tn.png"
minnesota_im=f"images/minnesota.png"
ms_im=f"images/ms.png"
missouri_im=f"images/missouri.png"
nc_state_im=f"images/nc_state.png"
north_carolina_im=f"images/north_carolina.png"
nw_im=f"images/northwestern.png"
nd_im=f"images/notre_dame.png"
ok_im=f"images/oklahoma.png"
oregon_im=f"images/oregon.png"
osu_im=f"images/osu.png"
penn_state_im=f"images/penn_state.png"
perdue_im=f"images/perdue.png"
rutgers_im=f"images/rutgers.png"
smu_im=f"images/smu.png"
south_alabama_im=f"images/south_alabama.png"
south_carolina_im=f"images/south_carolina.png"
southern_miss_im=f"images/southern_miss.png"
syracuse_im=f"images/syracuse.png"
tcu_im=f"images/tcu.png"
texas_im=f"images/texas.png"
texas_tech_im=f"images/texas_tech.png"
texas_am_im=f"images/texas_am.png"
toledo_im=f"images/toledo.png"
troy_im=f"images/troy.png"
tulane_im=f"images/tulane.png"
ucf_im=f"images/ucf.png"
ucla_im=f"images/ucla.png"
vanderbilt_im=f"images/vanderbilt.png"
virginia_tech_im=f"images/virginia_tech.png"
virginia_im=f"images/virginia.png"
wake_forest_im=f"images/wake_forest.png"
west_virginia_im=f"images/west_virginia.png"
wisconsin_im=f"images/wisconsin.png"
wku_im=f"images/wku.png"
uconn_im=f"images/ucon.png"
umass_im=f"images/umass.png"
washington_im=f"images/washington.png"
wyoming_im=f"images/wyoming.png"



TV = pd.read_csv('TV_Ratings_onesheet.csv')
TV_cols=TV['Home Team']
TV_cols=TV_cols.unique()
TV_ims=pd.DataFrame({'team': ['Alabama'],'path':al_im})
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Arizona State'],'path':asu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Arizona State'],'path':asu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Arkansas'],'path':ak_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Arkansas State'],'path':ark_state_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Auburn'],'path':aub_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['BYU'],'path':byu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Brigham Young'],'path':byu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['California'],'path':cal_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Central Florida'],'path':ucf_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Central Florida (UCF)'],'path':ucf_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Colorado State'],'path':col_state_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Connecticut'],'path':uconn_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Clemson'],'path':clem_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Duke'],'path':duke_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Florida'],'path':fl_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Florida State'],'path':fsu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Fresno'],'path':fres_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Georgia'],'path':uga_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Georgia Tech'],'path':gt_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Hawaii'],'path':hawaii_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Iowa'],'path':iowa_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Indiana'],'path':indiana_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Houston'],'path':hous_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Kansas State'],'path':ks_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Kentucky'],'path':uk_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Louisiana Tech'],'path':latech_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Louisville'],'path':lou_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['LSU'],'path':lsu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Memphis'],'path':mem_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Massachusetts'],'path':umass_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Miami (FL)'],'path':mia_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Michigan'],'path':mich_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Mississippi (Ole Miss)'],'path':miss_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Mississippi State'],'path':ms_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Middle Tennessee'],'path':middle_tn_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Minnesota'],'path':minnesota_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Missouri'],'path':missouri_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['NC State'],'path':nc_state_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['North Carolina'],'path':north_carolina_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Notre Dame'],'path':nd_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Northwestern'],'path':nw_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Oklahoma State'],'path':osu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Oregon'],'path':oregon_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Oklahoma'],'path':ok_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Penn State'],'path':penn_state_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Purdue'],'path':perdue_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Rutgers'],'path':rutgers_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['South Carolina'],'path':south_carolina_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Southern Methodist'],'path':smu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Southern  Methodist'],'path':smu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Syracuse'],'path':syracuse_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['TCU'],'path':tcu_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Tennessee'],'path':tn_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Texas A&M'],'path':texas_am_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Texas'],'path':texas_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Troy'],'path':troy_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Texas Tech'],'path':texas_tech_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Toledo'],'path':toledo_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Tulane'],'path':tulane_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['UCLA'],'path':ucla_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Massachusetts'],'path':umass_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['South Alabama'],'path':south_alabama_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Southern Miss'],'path':southern_miss_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Syracuse'],'path':syracuse_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Vanderbilt'],'path':vanderbilt_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Virginia'],'path':virginia_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Virginia Tech'],'path':virginia_tech_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Wake Forest'],'path':wake_forest_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Washington'],'path':washington_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['West Virginia'],'path':west_virginia_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Western Kentucky'],'path':wku_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Wisconsin'],'path':wisconsin_im}))
TV_ims=TV_ims.append(pd.DataFrame({'team': ['Wyoming'],'path':wyoming_im}))






import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import csv
import pandas as pd

################

current_directory = Path(__file__).parent

################

IL_report= []
IL_r_high = []
IL_r_medium = []
IL_r_low = []
IL_r_ecg = []

IR_report= []
IR_r_high = []
IR_r_medium = []
IR_r_low = []
IR_r_ecg = []

ER_report= []
ER_r_high = []
ER_r_medium = []
ER_r_low = []
ER_r_ecg = []

EL_report= []
EL_r_high = []
EL_r_medium = []
EL_r_low = []
EL_r_ecg = []

################

file_path = current_directory / 'files_orig' / 'IL.csv'

with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter = ',')
    for ROWS in plotting:
        array = ROWS[0].split(',')
        IL_report.append(float(array[0]))
        IL_r_high.append(float(array[1]))
        IL_r_medium.append(float(array[2]))
        IL_r_low.append(float(array[3]))
        IL_r_ecg.append(float(array[4]))
        array.clear()

IL_rep_points = np.array(IL_report)

IL_data_high = np.array(IL_r_high)
IL_data_medium = np.array(IL_r_medium)
IL_data_low = np.array(IL_r_low)
IL_data_ecg = np.array(IL_r_ecg)

################

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_high)
#plt.plot(IL_rep_points, IL_data_ecg)
ax.set_xlim(750, 2275)
ax.set_ylim(-60, 100)
plt.title('PRCG Insp Left High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 750, 2275
y_min, y_max = -60, 100

new_reports = IL_rep_points[x_min : x_max]
new_data = IL_data_high[y_min : y_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ILH_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)
"""
fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_medium)
ax.set_xlim(750, 2200)
ax.set_ylim(-120, 120)
plt.title('PRCG Insp Left Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_low)
#ax.set_xlim(75, 1335)
plt.title('PRCG Insp Left Low')
plt.xlabel('ReportS')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_ecg)
#ax.set_xlim(250, 1600)
plt.title('ECG Insp Left')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

################

file_path = current_directory / 'files_csv' / 'InsRightPHMLEcg.csv'
with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')
    for ROWS in plotting:
        array = ROWS[0].split(',')
        IR_report.append(float(array[0]))
        IR_r_high.append(float(array[1]))
        IR_r_medium.append(float(array[2]))
        IR_r_low.append(float(array[3]))
        IR_r_ecg.append(float(array[4]))
        array.clear()

IR_rep_points = np.array(IR_report)

IR_data_high = np.array(IR_r_high)
IR_data_medium = np.array(IR_r_medium)
IR_data_low = np.array(IR_r_low)
IR_data_ecg = np.array(IR_r_ecg)

################

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_high)
ax.set_xlim(337, 1572)
ax.set_ylim(-60, 50)
plt.title('PRCG Insp Right High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_medium)
ax.set_xlim(270, 1600)
ax.set_ylim(-60, 50)
plt.title('PRCG Insp Right Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_low)
ax.set_xlim(322, 1600)
ax.set_ylim(-60, 50)
plt.title('PRCG Insp Right Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_ecg)
ax.set_xlim(190, 1400)
plt.title('ECG Insp Right')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

################

file_path = current_directory / 'files_csv' / 'ExpRightPHMLEcg.csv'
with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')

    for ROWS in plotting:
        array = ROWS[0].split(',')
        ER_report.append(float(array[0]))
        ER_r_high.append(float(array[1]))
        ER_r_medium.append(float(array[2]))
        ER_r_low.append(float(array[3]))
        ER_r_ecg.append(float(array[4]))
        array.clear()

ER_rep_points = np.array(ER_report)

ER_data_high = np.array(ER_r_high)
ER_data_medium = np.array(ER_r_medium)
ER_data_low = np.array(ER_r_low)
ER_data_ecg = np.array(ER_r_ecg)

################

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_high)
ax.set_xlim(115, 1200)
ax.set_ylim(-40, 50)
plt.title('PRCG Exp Right High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_medium)
ax.set_xlim(139, 1302)
ax.set_ylim(-15, 15)
plt.title('PRCG Exp Right Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_low)
ax.set_xlim(156, 1312)
ax.set_ylim(-30, 30)
plt.title('PRCG Exp Right Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_ecg)
ax.set_xlim(300, 1500)
plt.title('ECG Exp Right')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

###############


file_path = current_directory / 'files_csv' / 'ExpLeftPHMLEcg.csv'
with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')

    for ROWS in plotting:
        array = ROWS[0].split(',')
        EL_report.append(float(array[0]))
        EL_r_high.append(float(array[1]))
        EL_r_medium.append(float(array[2]))
        EL_r_low.append(float(array[3]))
        EL_r_ecg.append(float(array[4]))
        array.clear()

EL_rep_points = np.array(EL_report)

EL_data_high = np.array(EL_r_high)
EL_data_medium = np.array(EL_r_medium)
EL_data_low = np.array(EL_r_low)
EL_data_ecg = np.array(EL_r_ecg)

################

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_high)
ax.set_xlim(276, 1445)
ax.set_ylim(-60, 60)
plt.title('PRCG Exp Left High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_medium)
ax.set_xlim(396, 1621)
ax.set_ylim(-30, 25)
plt.title('PRCG Exp Left Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_low)
ax.set_xlim(278, 1326)
ax.set_ylim(-35, 35)
plt.title('PRCG Exp Left Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_ecg)
ax.set_xlim(300, 1450)
plt.title('ECG Exp Low')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()
"""
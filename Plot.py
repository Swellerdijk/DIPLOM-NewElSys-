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

################ Inspiration Left

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

################ Построение ILH

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_high)
#plt.plot(IL_rep_points, IL_data_ecg)
ax.set_xlim(3300, 4730)
ax.set_ylim(-60, 100)
plt.title('PRCG Insp Left High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3300, 4730
y_min, y_max = -60, 100

new_reports = IL_rep_points[x_min : x_max]
new_data = IL_data_high[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ILH_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ILM

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_medium)
ax.set_xlim(3300, 4760)
ax.set_ylim(-60, 120)
plt.title('PRCG Insp Left Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3300, 4760

new_reports = IL_rep_points[x_min : x_max]
new_data = IL_data_medium[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ILM_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ILL

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_low)
ax.set_xlim(3370, 4820)
ax.set_ylim(-50, 60)
plt.title('PRCG Insp Left Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3370, 4820

new_reports = IL_rep_points[x_min : x_max]
new_data = IL_data_low[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ILL_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение IL ECG

fig, ax = plt.subplots()
plt.plot(IL_rep_points, IL_data_ecg)
ax.set_xlim(3050, 4520)
plt.title('ECG Insp Left')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

x_min, x_max = 3050, 4520

new_reports = IL_rep_points[x_min : x_max]
new_data = IL_data_ecg[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ILECG_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Inspiration Right

file_path = current_directory / 'files_orig' / 'IR.csv'

with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter = ',')
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

################ Построение IRH

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_high)
ax.set_xlim(3300, 4760)
ax.set_ylim(-20, 60)
plt.title('PRCG Insp Right High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3300, 4760

new_reports = IR_rep_points[x_min : x_max]
new_data = IR_data_high[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'IRH_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение IRM

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_medium)
ax.set_xlim(4310, 5800)
ax.set_ylim(-100, 150)
plt.title('PRCG Insp Right Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 4310, 5800

new_reports = IR_rep_points[x_min : x_max]
new_data = IR_data_medium[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'IRM_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение IRL

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_low)
ax.set_xlim(3860, 5120)
ax.set_ylim(-40, 60)
plt.title('PRCG Insp Right Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3860, 5130

new_reports = IR_rep_points[x_min : x_max]
new_data = IR_data_low[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'IRL_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение IR ECG

fig, ax = plt.subplots()
plt.plot(IR_rep_points, IR_data_ecg)
ax.set_xlim(2700, 4060)
plt.title('ECG Insp Right')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

x_min, x_max = 2700, 4060

new_reports = IR_rep_points[x_min : x_max]
new_data = IR_data_ecg[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'IRECG_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Expiration Right

file_path = current_directory / 'files_orig' / 'ER.csv'

with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter = ',')
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

################ Построение ERH

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_high)
ax.set_xlim(3820, 5110)
ax.set_ylim(-40, 40)
plt.title('PRCG Exp Right High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3820, 5110

new_reports = ER_rep_points[x_min : x_max]
new_data = ER_data_high[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ERH_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ERM

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_medium)
ax.set_xlim(3000, 4230)
ax.set_ylim(-60, 80)
plt.title('PRCG Exp Right Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3000, 4230

new_reports = ER_rep_points[x_min : x_max]
new_data = ER_data_medium[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ERM_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ERL

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_low)
ax.set_xlim(3160, 4380)
ax.set_ylim(-60, 80)
plt.title('PRCG Exp Right Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3160, 4380

new_reports = ER_rep_points[x_min : x_max]
new_data = ER_data_low[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ERL_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ER ECG

fig, ax = plt.subplots()
plt.plot(ER_rep_points, ER_data_ecg)
ax.set_xlim(2450, 3650)
ax.set_ylim(-400, 1000)
plt.title('ECG Exp Right')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

x_min, x_max = 2450, 3650

new_reports = ER_rep_points[x_min : x_max]
new_data = ER_data_ecg[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ERECG_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Expiration Left

file_path = current_directory / 'files_orig' / 'EL.csv'

with open(file_path, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter = ',')
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

################ Построение ELH

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_high)
ax.set_xlim(3950, 5120)
ax.set_ylim(-100, 120)
plt.title('PRCG Exp Left High')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3950, 5120

new_reports = EL_rep_points[x_min : x_max]
new_data = EL_data_high[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ELH_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ELM

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_medium)
ax.set_xlim(3520, 4710)
ax.set_ylim(-60, 180)
plt.title('PRCG Exp Left Middle')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3520, 4710

new_reports = EL_rep_points[x_min : x_max]
new_data = EL_data_medium[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ELM_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение ELL

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_low)
ax.set_xlim(3400, 4540)
ax.set_ylim(-50, 50)
plt.title('PRCG Exp Left Low')
plt.xlabel('Reports')
plt.ylabel('Z, mOhm')
plt.show()

x_min, x_max = 3400, 4540

new_reports = EL_rep_points[x_min : x_max]
new_data = EL_data_low[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ERL_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

################ Построение EL ECG

fig, ax = plt.subplots()
plt.plot(EL_rep_points, EL_data_ecg)
ax.set_xlim(3430, 4610)
plt.title('ECG Exp Left')
plt.xlabel('Reports')
plt.ylabel('Ampl, mcV')
plt.show()

x_min, x_max = 3430, 4610

new_reports = EL_rep_points[x_min : x_max]
new_data = EL_data_ecg[x_min : x_max]

data_to_save_csv = {
    'отчет' : new_reports,
    'значение' : new_data
}
file_path = current_directory / 'orig_cut' / 'ELECG_Cut.csv'

df = pd.DataFrame(data_to_save_csv)
df.to_csv(file_path, index = False)
df = pd.read_csv(file_path, skiprows = 1)
df.to_csv(file_path, index = False)

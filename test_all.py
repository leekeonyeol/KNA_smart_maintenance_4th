raw_logs = [ " S01 , motor_temp , 78.456 ", "s02, PUMP_PRESSURE ,95", " S01 , Motor_Temp , 81.2 ", "S03 , vibration , 0.5 ", "s02 , pump_pressure , 88",]
for i in raw_logs :
    report = i.strip().split(",")
    report_1 = report[0].strip().upper()
    report_2 = report[1].strip().lower()
    report_3 = float(report[2])
print(report) 

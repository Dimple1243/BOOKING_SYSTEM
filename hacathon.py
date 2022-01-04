# print("office time = 09:00 - 17:30 ")
# appointment_date = []
# appointment_time = []
# duration = []
# def  meeting(time):
#     if time <"17:29:00":
#         date = input("enter a date YYYY-MM-DD :")
#         if date >= "2021-12-04 ":
#             time = input("enter a time :")
#             if time >="09:00:00" and time <="17:30:00":
#                     Date_of_appointment = input("enter a date :")
#                     Time_of_appointment = int(input("enter a time :"))
#                     Hours_of_meeting = int(input("enter time in hours:"))
#                     time_of_meeting = str(Time_of_appointment+Hours_of_meeting)+":00"
#                     Time_of_appointment = str(Time_of_appointment)+":00"
#                     if Date_of_appointment >= "2021-12-04":
#                         if Date_of_appointment not in appointment_date:
#                             appointment_date.append(Date_of_appointment)
#                             if Time_of_appointment >="09:00" and time_of_meeting<"17:30":
#                                 if Time_of_appointment not in appointment_time:
#                                     appointment_time.append(Time_of_appointment ) 
#                                     if time_of_meeting not in duration:
#                                         duration.append(time_of_meeting)
#                                         meeting(time)
#     print(appointment_time , appointment_date , duration)
# meeting("09:00")

print("09:00 17:30")
submission_time = {}
i = 0
while i< 5:
    meeting_date = {}
    j = 0
    while j<1:
        request_submission_time=input("YYYY-MM-DD HH:MM-SS EMPLOYEE ID :")
        if request_submission_time[11:19]< "17:30:00" and request_submission_time[5:10]<="12-31":
            if request_submission_time >="2020-06-01 09:00:00 EMPOO1":
                meeting_start_time=input("YYYY-MM-DD HH:MM HOUR :")
                if meeting_start_time>="2020-06-01 09:00 1" :
                    date = meeting_start_time[:10]
                    time = str(int(meeting_start_time[11:13])+ int(meeting_start_time[-1]))+":00" 
                    T = meeting_start_time[11:17] +time + request_submission_time[19:]
                    if time < "17:30":
                        meeting_date[date] = T
        j+=1
    submission_time[request_submission_time[:19]] = meeting_date
    i+=1
print(submission_time)
Date=0
for k in submission_time:
    for n in submission_time[k]:
        if n!=Date:
            print(n)
            print(submission_time[k][n])
        if n==date:
            print(submission_time[k][n])
            Date=n

    




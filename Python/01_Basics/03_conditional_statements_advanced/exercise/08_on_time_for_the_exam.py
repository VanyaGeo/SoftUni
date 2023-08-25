exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam_minutes = exam_hour * 60 + exam_minute
total_arrival_minutes = arrival_hour * 60 + arrival_minute

hours = 0
minutes = 0

if 0 <= total_exam_minutes - total_arrival_minutes <= 30:
    print("On time")
elif total_exam_minutes - total_arrival_minutes > 30:
    print("Early")
elif total_arrival_minutes > total_exam_minutes:
    print("Late")

if total_exam_minutes - total_arrival_minutes != 0:
    if 0 < total_exam_minutes - total_arrival_minutes < 60:
        print(f"{total_exam_minutes - total_arrival_minutes} minutes before the start")
    elif total_exam_minutes - total_arrival_minutes >= 60:
        hours = (total_exam_minutes - total_arrival_minutes) // 60
        minutes = (total_exam_minutes - total_arrival_minutes) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    elif 0 < total_arrival_minutes - total_exam_minutes < 60:
        print(f"{total_arrival_minutes - total_exam_minutes} minutes after the start")
    elif total_arrival_minutes - total_exam_minutes >= 60:
        hours = (total_arrival_minutes - total_exam_minutes) // 60
        minutes = (total_arrival_minutes - total_exam_minutes) % 60
        print(f"{hours}:{minutes:02d} hours after the start")

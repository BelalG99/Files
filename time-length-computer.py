print("This program computes the length of an event.")

start_hour = int(input("Enter start hour of the event: "))
start_minute = int(input("Enter start minute of the event: "))
start_second = int(input("Enter start second of the event: "))
end_hour = int(input("Enter end hour of the event: "))
end_minute = int(input("Enter end minute of the event: "))
end_second = int(input("Enter end second of the event: "))

start_seconds = start_second + start_minute*60 + start_hour*60*60
end_seconds = end_second + end_minute*60 + end_hour*60*60

seconds = end_seconds - start_seconds

length_hour = seconds // (60*60)

remaining_seconds = seconds - length_hour*60*60

length_minute = remaining_seconds // 60

length_second = remaining_seconds - length_minute*60

print("The length of the event is: "+str(length_hour)+":"+str(length_minute)+":"+str(length_second)+".")
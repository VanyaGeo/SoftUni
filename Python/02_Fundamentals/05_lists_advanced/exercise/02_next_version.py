software_version = [int(number) for number in input().split(".")]


software_version[2] += 1
if software_version[2] == 10:
    software_version[1] += 1
    software_version[2] = 0
if software_version[1] == 10:
    software_version[0] += 1
    software_version[1] = 0

software_version_old = [str(number) for number in software_version]
new_version = ".".join(software_version_old)
print(new_version)
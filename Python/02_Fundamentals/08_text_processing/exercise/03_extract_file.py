# path_name = input().split("\\")
# file_name, extension = (path_name[-1]).split(".")
# print(f"File name: {file_name}")
# print(f"File extension: {extension}")


# II

path_name = input().split("\\")
file_and_extension = (path_name[-1]).split(".")
file_name = file_and_extension[0]
extension = file_and_extension[1::]

print(f"File name: {file_name}")
print(f"File extension: {'.'.join(extension)}")


# C:\Internal\training-internal\Template.pptx
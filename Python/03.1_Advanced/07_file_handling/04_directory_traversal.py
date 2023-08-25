import os


def get_files(directory_path):
    for file_name in os.listdir(directory_path):
        current_file = os.path.join(directory_path, file_name)

        if os.path.isfile(current_file):
            extension = "." + current_file.split(".")[-1]
            result[extension] = result.get(extension, []) + [file_name]

        elif os.path.isdir(current_file):
            get_files(current_file)


directory = input()
result = {}
get_files(directory)

# вариант I създава папка, в която принтира резултата

with open("report.txt", "w") as report_file:
    for extensions, files in sorted(result.items()):
        report_file.write(f"{extensions}\n")

        for file in sorted(files):
            report_file.write(f"--- {file}\n")

# вариант II принтира резултата в конзолата

# final_result = []
#
# for extensions, files in sorted(result.items()):
#     final_result.append(f"{extensions}")
#
#     for file in sorted(files):
#         final_result.append(f"--- {file}")
#
# print("\n".join(final_result))
# #
# #
# # import os
# #
# #
# # def save_extensions(dir_name, first_level=False):
# #
# #     for filename in os.listdir(dir_name):
# #         file_path = os.path.join(dir_name, filename)
# #
# #         if os.path.isfile(file_path):
# #             extension = filename.split(".")[-1]
# #
# #             if extension not in extensions:
# #                 extensions[extension] = []
# #
# #             extensions[extension].append(filename)
# #
# #         elif os.path.isdir(file_path) and not first_level:
# #             save_extensions(file_path, first_level=True)
# #
# #
# # directory = input("Enter name of directory to search: ")
# #
# # extensions = {}
# #
# # try:
# #     save_extensions(directory)
# # except FileNotFoundError:
# #     print(f"Not a valid directory: {directory}")
# #     exit()
# #
# # extensions = sorted(extensions.items(), key=lambda x: x[0])
# #
# # result = []
# #
# # for extension, files in extensions:
# #     result.append(f".{extension}")
# #     result.extend([f"- - - {file}" for file in sorted(files)])
# #
# # with open(os.path.join(directory, "report.txt"), "w") as report_file:
# #     report_file.write("\n".join(result))
#
# import os
#
# directory = input()
# extensions = {}
#
# for filename in os.listdir(directory):
#     file = os.path.join(directory, filename)
#
#     if os.path.isfile(file):
#         extension = filename.split(".")[-1]
#
#         if extension not in extensions:
#             extensions[extension] = []
#
#         extensions[extension].append(f"- - - {filename}")
#
# extensions = dict(sorted(extensions.items(), key=lambda x: x[0]))
#
# for extension, files in extensions.items():
#     files = sorted(files)
#
#     with open("report.txt", 'a') as file_dict:
#         file_dict.write("." + extension + "\n")
#         [file_dict.write(file + "\n") for file in files]
#
# print("Open the 'report.txt' file. After seeing the result, you can delete it.")



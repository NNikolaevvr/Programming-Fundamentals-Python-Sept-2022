path = input().split("\\")

file = path[-1]

file = file.split(".")
file_name = file[0]
extension = file[1]

print(f'File name: {file_name}' )
print(f'File extension: {extension}')
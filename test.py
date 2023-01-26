import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

html_folder = ''



def create_index_file(dir_path, style_path, intent, c_path):
	print(intent +dir_path)
	html_folder_list = ''
	title = dir_path.split('/')[-2]

	subfolders = [d for d in os.listdir(dir_path) ]
	# subfolders = [d for d in os.listdir(dir_path) if os.path.isdir(dir_path + d)]

	for name in subfolders:
		if name == '.git' or name == 'index.html':
			continue
		if os.path.isdir(dir_path + name):
			create_index_file(f'{dir_path}/{name}/', style_path+'../', intent+'--', f'{c_path}/{name}')
			pass

		html_folder_list += f'<li><a href="{name}">{name}</a></li>'
		# html_folder_list += f'<li>{name}</li>'
		# print(html_folder_list)
		# break

		# print(f'--<li><a href="{name}">{name}</a></li>')
	# return
	
	html = f'''

		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>{title} | English Speaking Course</title>

			<link rel="stylesheet" href="{style_path}style.css">
		</head>
		<body>

			<div align="center">
				<h3>{title}</h3>
				<hr>
			</div>
		<div class="container">
			<a href="../" class="btn btn-info btn-sm mb-3">Back</a>
			<p>
				<strong>Path: </strong>
				<span>{c_path}</span>
			</p>

			<ul class="dir-list sort-list">

				{html_folder_list}
				
			</ul>
		</div>
		<script src="{style_path}javascript.js">
		<script>
			window.onload = sortList;
		</script>
		</body>
		</html>	'''

	with open(f'{dir_path}index.html', 'w') as file:
		file.write(html)
		file.close()




create_index_file(f'{BASE_DIR}/', './', '--', '')



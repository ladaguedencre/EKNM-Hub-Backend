# Read the input Markdown file
input_file_path = './../data/input.md'
output_file_path = './../data/output.md'

with open(input_file_path, 'r') as input_file:
    # Read the content of the input file
    markdown_content = input_file.read()

# Replace characters
markdown_content = markdown_content.replace('\n', '\\n')
markdown_content = markdown_content.replace('\'', '\\\'')
markdown_content = markdown_content.replace('\"', '\\\"')

# Write the modified content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(markdown_content)

print(f"Converted {input_file_path} to a one-line Markdown file: {output_file_path}")

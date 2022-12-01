def to_indexed(source_file, output_file):

    with open(source_file, 'r') as file_in:
        with open(output_file, 'w') as file_out:

            for i, line in enumerate(file_in):
                file_out.write(f"{i}: {line}")

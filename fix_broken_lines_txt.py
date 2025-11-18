# fix txt files with broken lines
# example: if line is "asdf9asjd0ja" but somehow broken like "asdf9\nasjd0ja" (with \n being a breakline)

def fix_file(input, output):
    corrected_lines = []
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith(";"):  
                if corrected_lines:
                    corrected_lines[-1] += line
            else:
                corrected_lines.append(line)

    with open(output, "w", encoding="utf-8") as f:
        for line in corrected_lines:
            f.write(line + "\n")

fix_file("input.txt", "output.txt")

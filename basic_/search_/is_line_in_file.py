def is_line_in_file(line, file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return line + '\n' in lines


if __name__ == '__main__':
    line = '''六三，未济，征凶。利涉大川。'''
    file = "未济卦.txt"
    print(is_line_in_file(line, file))
def print_progress_bar(current, total):
    current_percent = int((current/(total-1)) * 100)

    black_spaces = 100 - current_percent
    white_spaces = 100 - black_spaces

    white_spaces = ' ' * white_spaces
    black_spaces = ' ' * black_spaces

    end = '\n' if current_percent == 100 else ''

    print(f'\r| \033[;7m{white_spaces}\033[;0m{black_spaces} | {current_percent}%', end=end)
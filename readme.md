<h1>print_progress_bar</h1>
<p>
    A tiny python function to print a progress bar. 
    The progress bar looks very similar to pip, I'd bet the code below also looks similar to how they are doing it.
</p>
<h2>Usage</h2>
<p>The entire print_progress_bar function is below. Just copy and paste it into your own code.</p>

```python
def print_progress_bar(current, total):
    current_percent = int((current/(total-1)) * 100)

    black_spaces = 100 - current_percent
    white_spaces = 100 - black_spaces

    white_spaces = ' ' * white_spaces
    black_spaces = ' ' * black_spaces

    end = '\n' if current_percent == 100 else ''

    print(f'\r| \033[;7m{white_spaces}\033[;0m{black_spaces} | {current_percent}%', end=end)
```

<h2>Example</h2>

```python
import time
max = 420

print('I am going to load something now.')
for x in range(max):
    print_progress_bar(x, max)
    time.sleep(.01)
print('I have finished loading.')
```
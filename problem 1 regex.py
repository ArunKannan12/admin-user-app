import re

data = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"messages":"[php warning #2] count(): parameter must be an array or an object that implement countable (153)"}]}'

pattern = re.compile(r'"id":(\d+)')
matches = pattern.findall(data)

numbers = [int(match) for match in matches]
print(numbers)

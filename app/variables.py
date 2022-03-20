import random
import string

# генерация рандомной строчки
letters = string.ascii_lowercase
(''.join(random.choice(letters) for i in range(10)))



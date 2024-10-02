from flask import Flask
import os

app = Flask(__name__)

counter_file = '/data/counter.txt'

# Função para ler o valor do contador
def read_counter():
    if os.path.exists(counter_file):
        with open(counter_file, 'r') as f:
            return int(f.read())
    return 0

# Função para incrementar e salvar o contador
def increment_counter():
    counter = read_counter() + 1
    with open(counter_file, 'w') as f:
        f.write(str(counter))
    return counter

@app.route('/')
def index():
    count = increment_counter()
    return f'Contador: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

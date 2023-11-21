import copy

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

input_index = 0

matrix1 = [[1, 2, 1, 3], [1, 7, 2, 9], [4, 3, 2, 1]]
matrix2 = [[1, 8, 1], [2, 1, 4], [3, 2, 4], [6, 3, 5]]
old_matrix2 = copy.deepcopy(matrix2)


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        result.append(row)

    return result


def add_delays(matrix):
    for index, row in enumerate(matrix):
        # Prepend None as delays
        for i in range(len(matrix) - index - 1):
            row.insert(0, 0)
        # Append None as delays
        for i in range(index):
            row.append(0)
    return matrix


matrix1 = add_delays(matrix1)
matrix2 = transpose(add_delays(transpose(matrix2)))

cols = len(matrix2[0])
rows = len(matrix1)

cells = [
    [{'c': 0, 'm1_in': 0, 'm1_out': 0, 'm2_in': 0, 'm2_out': 0} for _ in range(cols)]
    for _ in range(rows)
]


@app.route('/')
def index():
    global matrix1, matrix2, old_matrix2, cells
    print(f"{cells=}")

    return render_template('index.html', cells=cells, matrix1=matrix1, matrix2=matrix2, old_matrix2=old_matrix2)


@app.route('/next_step')
def next_step():
    global input_index, matrix1, matrix2, old_matrix2, cells

    print(f"{matrix1=}")
    print(f"{matrix2=}")
    
    # First propagate the input
    for i in range(rows):
        for j in range(cols):
            cells[i][j]['m1_in'] = cells[i][j + 1]['m1_out'] if j < cols - 1 else matrix1[i][input_index] if input_index < len(
                matrix1[i]) else 0
            cells[i][j]['m2_in'] = cells[i + 1][j]['m2_out'] if i < rows - 1 else matrix2[input_index][j] if input_index < len(
                matrix2) else 0

    # Execute the algorithm and update the register and the out
    for i in range(rows):
        for j in range(cols):
            cells[i][j]['c'] += cells[i][j]['m1_in'] * cells[i][j]['m2_in']
            cells[i][j]['m1_out'] = cells[i][j]['m1_in']
            cells[i][j]['m2_out'] = cells[i][j]['m2_in']

    input_index += 1
    print(f"{cells=}")

    return render_template('index.html', cells=cells, matrix1=matrix1, matrix2=matrix2, old_matrix2=old_matrix2)


@app.route('/clear')
def clear():
    global cells

    cells = [
        [{'c': 0, 'm1_in': 0, 'm1_out': 0, 'm2_in': 0, 'm2_out': 0} for _ in range(cols)]
        for _ in range(rows)
    ]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

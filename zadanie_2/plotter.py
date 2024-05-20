import os
import matplotlib.pyplot as plt


def get_data(file_name, matrix_size):

    file_path = os.path.join("results", file_name)
    time_results = []
    instruction_results = []
    cycles_results = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(1, len(lines), 3):
            time_data = float(lines[i].strip())
            instructions = float(lines[i + 1].strip())
            cycles = float(lines[i + 2].strip()) 

            time_results.append(time_data)
            instruction_results.append(instructions / matrix_size[i // 3])
            cycles_results.append(cycles)


    return time_results, instruction_results, cycles_results


if __name__ == "__main__":
    x = [100, 200, 300, 400, 500, 800, 1000, 1300, 1600, 2000]
    
    plt.figure(figsize=(25, 15))
    for file_name in os.listdir("results"):
        t, i, c = get_data(file_name, x)
        label = file_name[7:13]
        print(label)
        plt.plot(x, c, label=label)

    plt.grid(True)
    plt.legend(loc='best') 
    plt.xlabel("Matrix size (nxn)")
    plt.ylabel("Cycle Count")
    plt.show()

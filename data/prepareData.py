import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import os


def open_file(filename):
    groupBySensor = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            try:
                if row[-1] in groupBySensor:
                    groupBySensor[row[-1]].append(float(row[-6]))
                else:
                    groupBySensor[row[-1]] = [float(row[-6])]
            except:
                continue

    return groupBySensor


if __name__ == '__main__':
    filename = "/Users/yhx/Downloads/7days.csv"
    res = open_file(filename)
    # print(res)
    print(len(res.keys()))
    x_axis = []
    y_axis = []

    dest_file = "7dayRes.csv"

    with open(dest_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["edge", "machineType", "sensorId", "min10", "max90", "median", "avg", "std"])
        for sensorId in res.keys():
            edge = sensorId[:3]
            machineType = sensorId[6:].upper()
            min10 = np.percentile(res[sensorId], 10)
            max90 = np.percentile(res[sensorId], 90)
            avg = np.average(res[sensorId])
            std = np.std(res[sensorId])
            median = np.median(res[sensorId])
            writer.writerow(
                [edge, machineType, sensorId, round(min10, 4), round(max90, 4), round(median, 4), round(avg, 4),
                 round(std, 4)])
            print([edge, machineType, sensorId, round(min10, 4), round(max90, 4), median, round(avg, 4), round(std, 4)])
    for id in res.keys():
        print(id, len(res[id]))

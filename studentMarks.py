import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df=pd.read_csv("studentMarks.csv")
data = df["score"].tolist()

# fig = ff.create_distplot([data],["Math score"],show_hist=False)
# fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Mean of population :-",mean)
print("standard deviation of population :-",std_dev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        rand_index = random.randint(0,len(data)-1)
        value = data[rand_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


mean_list=[]
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of sampling distribution: ",mean)
print("Standard deviation of sampling distribution", std_dev)

std_1_dev_start, std_1_dev_end = mean-std_dev, mean+std_dev
std_2_dev_start, std_2_dev_end = mean-(2*std_dev), mean+(2*std_dev)
std_3_dev_start, std_3_dev_end = mean-(3*std_dev), mean+(3*std_dev)

print("std 1: ",std_1_dev_start,std_1_dev_end)
print("std 2: ",std_2_dev_start,std_2_dev_end)
print("std 3: ",std_3_dev_start,std_3_dev_end)

fig = ff.create_distplot([mean_list],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.18], mode='lines', name="Mean"))

fig.add_trace(go.Scatter(x=[std_1_dev_start,std_1_dev_start], y=[0,0.18], mode='lines', name="1 std_dev start"))
fig.add_trace(go.Scatter(x=[std_1_dev_end,std_1_dev_end], y=[0,0.18], mode='lines', name="1 std_dev end"))

fig.add_trace(go.Scatter(x=[std_2_dev_start,std_2_dev_start], y=[0,0.18], mode='lines', name="2 std_dev start"))
fig.add_trace(go.Scatter(x=[std_2_dev_end,std_2_dev_end], y=[0,0.18], mode='lines', name="2 std_dev end"))

fig.add_trace(go.Scatter(x=[std_3_dev_start,std_3_dev_start], y=[0,0.18], mode='lines', name="3 std_dev start"))
fig.add_trace(go.Scatter(x=[std_3_dev_end,std_3_dev_end], y=[0,0.18], mode='lines', name="3 std_dev end"))

fig.show()

#finding mean of data 1 csv and plotting on graph

df = pd.read_csv('data1.csv')
data = df['score'].tolist()

mean_of_sample1 = statistics.mean(data)
print("mean of sample1: ", mean_of_sample1)
fig = ff.create_distplot([mean_list],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.18], mode='lines', name="Mean"))

fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0,0.18], mode='lines', name="Mean of sample who got ipad"))
fig.add_trace(go.Scatter(x=[std_1_dev_end,std_1_dev_end], y=[0,0.18], mode='lines', name="1 std_dev end"))
fig.show()

z_score = (mean_of_sample1-mean)/std_dev
print("z-score: ",z_score)
#finding mean of data 2 csv and plotting on graph

df = pd.read_csv('data2.csv')
data = df['score'].tolist()

mean_of_sample2 = statistics.mean(data)
print("mean of sample2: ", mean_of_sample2)
fig = ff.create_distplot([mean_list],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.18], mode='lines', name="Mean"))

fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0,0.18], mode='lines', name="Mean of sample who got extra classes"))
fig.add_trace(go.Scatter(x=[std_1_dev_end,std_1_dev_end], y=[0,0.18], mode='lines', name="1 std_dev end"))
fig.add_trace(go.Scatter(x=[std_2_dev_end,std_2_dev_end], y=[0,0.18], mode='lines', name="2 std_dev end"))
fig.show()
z_score2 = (mean_of_sample2-mean)/std_dev
print("z-score 2: ",z_score2)
#finding mean of data 3 csv and plotting on graph

df = pd.read_csv('data3.csv')
data = df['score'].tolist()

mean_of_sample3 = statistics.mean(data)
print("mean of sample3: ", mean_of_sample3)
fig = ff.create_distplot([mean_list],["Student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.18], mode='lines', name="Mean"))

fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0,0.18], mode='lines', name="Mean of sample who got funsheets"))
fig.add_trace(go.Scatter(x=[std_3_dev_end,std_3_dev_end], y=[0,0.18], mode='lines', name="3 std_dev end"))
fig.add_trace(go.Scatter(x=[std_2_dev_end,std_2_dev_end], y=[0,0.18], mode='lines', name="2 std_dev end"))
fig.show()
z_score3 = (mean_of_sample3-mean)/std_dev
print("z-score 3: ",z_score3)
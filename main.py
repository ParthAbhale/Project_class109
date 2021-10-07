from pandas import read_csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

df = read_csv("data.csv")
data = df["reading score"].to_list()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
std = statistics.stdev(data)


st_m_start1,st_m_end1 = mean - std,mean + std
st_m_start2,st_m_end2 = mean - (2*std),mean + (2* std)
st_m_start3,st_m_end3 = mean - (3* std),mean + (3*std)

fig = ff.create_distplot([data],['reading data'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[st_m_start1,st_m_start1],y=[0,0.17],mode='lines',name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[st_m_end1,st_m_end1],y=[0,0.17],mode='lines',name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[st_m_start2,st_m_start2],y=[0,0.17],mode='lines',name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[st_m_end2,st_m_end2],y=[0,0.17],mode='lines',name="STANDARD DEVIATION 2"))
fig.show()

list_1 = [result for result in data if result > st_m_start1 and result < st_m_end1]
list_2 = [result for result in data if result > st_m_start2 and result < st_m_end2]
list_3 = [result for result in data if result > st_m_start3 and result < st_m_end3]

print("{}% in standard deviation first".format(len(list_1)*100/len(data)))
print("{}% in standard deviation second".format(len(list_2)*100/len(data)))
print("{}% in standard deviation third".format(len(list_3)*100/len(data)))




# Process prep
from vedo import show
from vedo import load
from vedo import Video
from vedo import vector
from vedo import buildLUT
from vedo import Sphere
from vedo import settings
from vedo import colorMap
from vedo import pyplot

# CSV export prep
import pandas as pd
import numpy as np

# User prompt prep
import PySimpleGUI as sg
sg.theme("DarkTeal2")

### LUT Creator
colors = []
for i in np.linspace(-80, 80):
    c = colorMap(i, name='CMRmap', vmin=-80, vmax=80)
    if abs(i) < 5:
        c = 'white'
    colors.append([i, c])

lut = buildLUT(
    colors,
    vmin=-80,
    vmax=80,
    interpolate=True)

## Building Window 1
layout = [[sg.T("")], [sg.Text("Choose a Ref: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]
window = sg.Window('Ref Model Browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        a=values["-IN-"]
        print(a)
        window.close()
        break

## Building Window 2
layout2 = [[sg.T("")], [sg.Text("Choose a Exp: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]
window = sg.Window('Exp Model Browser', layout2, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        b=values["-IN-"]
        print(b)
        window.close()
        break
    

### Process
s1 = load(a).extractLargestRegion()
s2 = load(b).extractLargestRegion()

s1.distanceToMesh(s2, signed=True)
s1.cmap(input_array="Distance", cname=lut)
s1.addScalarBar(title='Signed\nDistance(\mum)')

#### show results

print(s1.pointdata["Distance"])
show(s1).close()

pyplot.histogram(s1.pointdata['Distance']).show().close()

### save results
DF = pd.DataFrame(s1.pointdata["Distance"])
DF.to_csv("C:/Users/Matt/Desktop/signed distance/data1.csv")
s1.write("C:/Users/Matt/Desktop/signed distance/test.vtk")

### Make 360 video
cam = dict(pos=(671.1, -895.8, -603.0),
           focalPoint=(224.7, 165.8, 125.2),
           viewup=(-0.4209, 0.2192, 0.8802),
           distance=1247,
           clippingRange=(651.1, 2000))

p = s1.centerOfMass()
v = vector(0, 0, 1)

video = Video("C:/Users/Matt/Desktop/signed distance/test.mp4", duration=12, backend='ffmpeg')

for j in range(30):
    show(s1.rotate(j, axis=v, point=p), interactive=False,
         resetcam=False, camera=cam)  # render the scene
    video.addFrame()  # add individual frame

video.close()


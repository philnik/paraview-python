from paraview.simple import *
# Save a screenshot from a specific view.
#myview = GetActiveView()
animationScene1 = GetAnimationScene()
tk = GetTimeKeeper()
timesteps = tk.TimestepValues
def export_animation(i):
    animationScene1.AnimationTime = timesteps[i]
    layout = GetLayout()
    root="/home/me/python/paraview/images/aview_/"
    fname="aview_"+'{:04d}'.format(i)+".png"
    fname1=root+fname
    SaveScreenshot(fname1, layout,
                   ImageResolution=[1920, 1080])

for i in range(0,len(timesteps)): export_animation(i)

from paraview.simple import *
from pathlib import Path
import json
import uuid
rv = GetActiveViewOrCreate("RenderView")
anim = GetAnimationScene()
ocam = GetCameraTrack(view=rv)
anim_files = list(Path(Path.home()/".config/Paraview/Animation_Cues/").rglob("paraview_animation_*"))
for a in anim_files:
  cue = CameraAnimationCue()
  cue.Mode = ocam.Mode
  # leaving this out means we can't view from the camera on this cue
  cue.AnimatedProxy = rv
  print("opening file",a)
  with open(a,"r") as phile:
      kfs = json.loads(phile.read())
      for kfd in kfs:
          kf = CameraKeyFrame()
          print(kfd)
          kf.KeyTime = kfd[0]
          kf.Position = kfd[1]
          kf.FocalPoint = kfd[2]
          kf.ViewUp = kfd[3]
          cue.KeyFrames.append(kf)
  anim.Cues.append(cue)

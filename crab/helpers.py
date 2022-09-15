def GetSampleList(file):
  samplelist = file.readlines()
  samplelist = [x.strip() for x in samplelist] 
  samplelist = [x for x in samplelist if x] # Choose lines that are not empty
  samplelist = [x for x in samplelist if not(x.startswith("#"))] # Choose lines that do not start with #
  return samplelist

def TrimPrimaryNameForMC(dataset):
  name = dataset.split('/')[1]
  name = name.replace("_13TeV","")
  name = name.replace("_13p6TeV","")
  name = name.replace("_TuneCP5","")
  name = name.replace("pythia","py")
  name = name.replace("herwig","hw")
  name = name.replace("madgraph","mg")
  name = name.replace("powheg","phg")
  name = name.replace("amcatnlo","mcNLO")
  name = name.replace("powhegMiNNLO","pwhg")
  name = name.replace("-photos","")
  name = name.replace("FXFX","")
  name = name.replace("_MatchEWPDG20","")
  return name

def TrimSecondaryNameForMC(dataset):
  name = dataset.split('/')[2]

  name = name.replace("Run3Winter22MiniAOD-","MC22_122")#RENAME CAMPAIGN. CHECK ITS UPDATED
  name = name.replace("122X_mcRun3_2021_realistic_v9","") #REMOVE GT. CHECK ITS UPDATED

  name = name.replace("-v1","")# 
  name = name.replace("-v2","")# 
  name = name.replace("-v3","")#
  name = name.replace("-v4","")# Remove any version indication.There should only be one valid version for MC samples
  return name

def TrimSecondaryNameForData(dataset):
  name = dataset.split('/')[2]
  #
  # Note: For PromptReco, we do need the version as different versions 
  # means different run number ranges.
  #
  # name = name.replace("-v1","")# 
  # name = name.replace("-v2","")# 
  # name = name.replace("-v3","")#
  # name = name.replace("-v4","")# Remove any version indication.
  return name

def IsSampleData(dataset):
  name = dataset.split('/')[2]
  isData = False
  if   "Run2022" in name:isData = True
  return isData


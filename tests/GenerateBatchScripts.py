import os
import glob
import re
import collections
import copy

# XROOTD="root://cms-xrd-global.cern.ch/"
XROOTD="root://xrootd-cms.infn.it/"

NEVENTS="100"
# NEVENTS="250"
# NEVENTS="500"
# NEVENTS="1000"
# NEVENTS="10000"
# NEVENTS="-1"

nanoVersion  = "NanoAODv10"

EOSUSER=""
EOSUSER="root://eosuser.cern.ch/"
# EOSUSER+="/eos/user/n/nbinnorj/JMENano/Run3/v2/"
EOSUSER+="/eos/user/n/nbinnorj/JMENano/Run3/v2p1/"

CUSTOM_PRE = "process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\\n"
CUSTOM_PRE = CUSTOM_PRE+"process.MessageLogger.cerr.FwkReport.reportEvery = 10\\n"

CUSTOM_DATA = CUSTOM_PRE+"from PhysicsTools.NanoAOD.custom_jme_cff import PrepJMECustomNanoAOD_Data; PrepJMECustomNanoAOD_Data(process)\\n"
CUSTOM_MC = CUSTOM_PRE+"from PhysicsTools.NanoAOD.custom_jme_cff import PrepJMECustomNanoAOD_MC; PrepJMECustomNanoAOD_MC(process)\\n"

def main(): 
  #
  #
  #
  GTDict, ERADict = GetGTandEraDicts()
  #
  #
  #
  sampleDict = MyDict()
  sampleDict["Data22B_DoubleMuon"] = {
    "GT"          : GTDict["Data22B"][nanoVersion],
    "ERA"         : ERADict["Data22B"][nanoVersion],
    "DAS"         : "/DoubleMuon/Run2022B-PromptReco-v1/MINIAOD",
    "MINIAOD"     : [
      XROOTD+"/store/data/Run2022B/DoubleMuon/MINIAOD/PromptReco-v1/000/355/558/00000/18bfe77b-5a39-4a98-8e73-82059b6b44a1.root"
    ],
    "NANOAOD"     : "JMENano_Data22B_DoubleMuon.root",
    "CFGFILE"     : "JMENano_Data22B_DoubleMuon_cfg.py",
    "CUSTOM"      : CUSTOM_DATA,
  }

  sampleDict["Data22C_Muon"] = copy.deepcopy(sampleDict["Data22B_DoubleMuon"])
  sampleDict["Data22C_Muon"]["GT"]  = GTDict["Data22C"][nanoVersion]
  sampleDict["Data22C_Muon"]["ERA"] = ERADict["Data22C"][nanoVersion]
  sampleDict["Data22C_Muon"]["DAS"] = "/Muon/Run2022C-PromptReco-v1/MINIAOD"
  sampleDict["Data22C_Muon"]["MINIAOD"] = [
    XROOTD+"/store/data/Run2022C/Muon/MINIAOD/PromptReco-v1/000/356/968/00000/11ff108b-7ddd-43a7-b449-2c98b0663369.root"
  ]
  sampleDict["Data22C_Muon"]["NANOAOD"] = "JMENano_Data22C_Muon.root"
  sampleDict["Data22C_Muon"]["CFGFILE"] = "JMENano_Data22C_Muon_cfg.py"

  sampleDict["Data22D_Muon"] = copy.deepcopy(sampleDict["Data22B_DoubleMuon"])
  sampleDict["Data22D_Muon"]["GT"]  = GTDict["Data22D"][nanoVersion]
  sampleDict["Data22D_Muon"]["ERA"] = ERADict["Data22D"][nanoVersion]
  sampleDict["Data22D_Muon"]["DAS"] = "/Muon/Run2022D-PromptReco-v1/MINIAOD"
  sampleDict["Data22D_Muon"]["MINIAOD"] = [
    XROOTD+"/store/data/Run2022D/Muon/MINIAOD/PromptReco-v1/000/357/706/00000/0c0f10ea-13a5-40ab-a045-258b631ec1f2.root"
  ]
  sampleDict["Data22D_Muon"]["NANOAOD"] = "JMENano_Data22D_Muon.root"
  sampleDict["Data22D_Muon"]["CFGFILE"] = "JMENano_Data22D_Muon_cfg.py"

  sampleDict["Data22D_JetMET"] = copy.deepcopy(sampleDict["Data22B_DoubleMuon"])
  sampleDict["Data22D_JetMET"]["GT"]  = GTDict["Data22D"][nanoVersion]
  sampleDict["Data22D_JetMET"]["ERA"] = ERADict["Data22D"][nanoVersion]
  sampleDict["Data22D_JetMET"]["DAS"] = "/JetMET/Run2022D-PromptReco-v1/MINIAOD"
  sampleDict["Data22D_JetMET"]["MINIAOD"] = [
    XROOTD+"/store/data/Run2022D/JetMET/MINIAOD/PromptReco-v1/000/357/613/00000/bec4b892-91ed-481d-a341-ed10b01d17a7.root"
  ]
  sampleDict["Data22D_JetMET"]["NANOAOD"] = "JMENano_Data22D_JetMET.root"
  sampleDict["Data22D_JetMET"]["CFGFILE"] = "JMENano_Data22D_JetMET_cfg.py"
  ######################################################
  #
  # MC TTTo2L2Nu
  #
  ######################################################
  sampleDict["MC22_122_TTTo2L2Nu"] = {
    "GT"          : GTDict["MC22_122"][nanoVersion],
    "ERA"         : ERADict["MC22_122"][nanoVersion],
    "DAS"         : "/TTTo2L2Nu_CP5_13p6TeV_powheg-pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM",
    "MINIAOD"     : [ # 
      XROOTD+"/store/mc/Run3Winter22MiniAOD/TTTo2L2Nu_CP5_13p6TeV_powheg-pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9-v2/2550000/d05b5bca-8177-4371-8172-2527a58c73ab.root",
    ],
    "NANOAOD"     : "JMENano_MC22_122_TTTo2L2Nu.root",
    "CFGFILE"     : "JMENano_MC22_122_TTTo2L2Nu_cfg.py",
    "CUSTOM"      : CUSTOM_MC,
  }

  ######################################################
  #
  # MC DYJetsToLL
  #
  ######################################################
  sampleDict["MC22_122_DYJetsToLL"] = copy.deepcopy(sampleDict["MC22_122_TTTo2L2Nu"])
  sampleDict["MC22_122_DYJetsToLL"]["DAS"] = "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9_ext2-v2/MINIAODSIM"
  sampleDict["MC22_122_DYJetsToLL"]["MINIAOD"] = [
    XROOTD+"/store/mc/Run3Winter22MiniAOD/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9_ext2-v2/40001/5e306acf-9696-4364-89e3-b56c6a64fa55.root"
  ]
  sampleDict["MC22_122_DYJetsToLL"]["NANOAOD"] = "JMENano_MC22_122_DYJetsToLL.root"
  sampleDict["MC22_122_DYJetsToLL"]["CFGFILE"] = "JMENano_MC22_122_DYJetsToLL_cfg.py"

  ######################################################
  #
  # MC QCD_Pt-15to7000_Flat
  #
  ######################################################
  sampleDict["MC22_122_QCD_Pt-15to7000_Flat"] = copy.deepcopy(sampleDict["MC22_122_TTTo2L2Nu"])
  sampleDict["MC22_122_QCD_Pt-15to7000_Flat"]["DAS"] = "/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM"
  sampleDict["MC22_122_QCD_Pt-15to7000_Flat"]["MINIAOD"] = [
    XROOTD+"/store/mc/Run3Winter22MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat_13p6TeV_pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9-v2/40000/d1e21ec5-4f08-48a6-a471-26b94bcb1a25.root"
  ]
  sampleDict["MC22_122_QCD_Pt-15to7000_Flat"]["NANOAOD"] = "JMENano_MC22_122_QCD_Pt-15to7000_Flat.root"
  sampleDict["MC22_122_QCD_Pt-15to7000_Flat"]["CFGFILE"] = "JMENano_MC22_122_QCD_Pt-15to7000_Flat_cfg.py"

  for key in sampleDict:
    #
    # Ignore Data22B at the moment. Nano doesn't run. probably it due its 123X GT. maybe wait for 12_4 rereco
    #
    if "Data22B_DoubleMuon" in key: continue
    # if not("JetMET" in key or "QCD_Pt" in key): continue #TEMP;
    print(key)
    CreateBashScript(sampleDict,key)

def GetGTandEraDicts():
  #
  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRun3Analysis
  #
  GT = MyDict()
  # GT["Data22B"]["NanoAODv10"]  = "123X_dataRun3_Prompt_v12"
  GT["Data22C"]["NanoAODv10"]  = "124X_dataRun3_Prompt_v4"
  GT["Data22D"]["NanoAODv10"]  = "124X_dataRun3_Prompt_v4"
  GT["MC22_122"]["NanoAODv10"] = "124X_mcRun3_2022_realistic_v11"

  ERA = MyDict()
  ERA["Data22B"]["NanoAODv10"]  = "Run3"
  ERA["Data22C"]["NanoAODv10"]  = "Run3"
  ERA["Data22D"]["NanoAODv10"]  = "Run3"
  ERA["MC22_122"]["NanoAODv10"] = "Run3,run3_nanoAOD_122"

  return GT, ERA

def CreateBashScript(sampleDict, sampleName):

  OUTDIR="./OUTPUT/"

  fName = "RunJMENano_%s.sh" %(sampleName)  

  isMC = True if "MC" in sampleName else False

  f = open(fName, 'w')
  f.write('#                                      \n')
  f.write('#Created by GenerateBashScript.py      \n')
  f.write('#                                      \n')
  f.write('\n')
  f.write('#!/bin/bash\n\n\n')
  
  f.write('mkdir -p %s \n\n' %OUTDIR)

  inFileStr = ",".join(sampleDict[sampleName]["MINIAOD"])

  #
  # Write the command
  #
  command  = "cmsDriver.py step1 \\\n"
  command += "--filein %s \\\n"  %(inFileStr)
  command += "--fileout %s \\\n" %(EOSUSER+sampleDict[sampleName]["NANOAOD"])
  command += "--python_filename %s \\\n" %(OUTDIR+sampleDict[sampleName]["CFGFILE"])
  command += "--step NANO \\\n"
  command += "--conditions %s \\\n" %(sampleDict[sampleName]["GT"])
  command += "--era %s \\\n"        %(sampleDict[sampleName]["ERA"])
  if isMC:
    command += "--mc \\\n"
    command += "--eventcontent NANOAODSIM \\\n"
    command += "--datatier NANOAODSIM \\\n"
  else:
    command += "--data \\\n"
    command += "--eventcontent NANOAOD \\\n"
    command += "--datatier NANOAOD \\\n"
  command += "-n %s \\\n" %(NEVENTS)
  command += "--no_exec \\\n"
  command += "--customise Configuration/DataProcessing/Utils.addMonitoring \\\n"
  command += "--customise_commands=\"%s\""  %(sampleDict[sampleName]["CUSTOM"])
  f.write(command)
  f.write('\n\n\n')

  #
  # Write the second command
  #
  f.write("echo -e \"\\n\\n\\n\\n\" \n")
  f.write("echo \"cmsRun $NANOAOD_CFG\" \n")
  f.write("echo \"Started at `date`\"   \n")
  f.write("cmsRun %s 2>&1 | tee %s      \n" %(OUTDIR+sampleDict[sampleName]["CFGFILE"], OUTDIR+sampleDict[sampleName]["NANOAOD"].replace("root","log")))
  f.write("echo \"Finished at `date`\"  \n")
  f.write('\n\n\n')
  f.close()

  #
  # Change batch script permission
  #

  preliminary_command = 'chmod +x %s' % fName
  os.system(preliminary_command)
  return fName

class MyDict(collections.OrderedDict):
  def __missing__(self, key):
    val = self[key] = MyDict()
    return val

if __name__ == "__main__":
  main()


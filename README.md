# JMENanoAOD-Production

```bash
cmsrel CMSSW_12_4_8
cd CMSSW_12_4_8/src/
cmsenv
git cms-init
git cms-merge-topic nurfikri89:from1248_NanoV10_JMENanoRun3_forPrivate_v2
scram b -j4
```



```bash
git clone git@github.com:nurfikri89/JMENanoAOD-Production JMENanoAOD/Production
scram b -j4
```

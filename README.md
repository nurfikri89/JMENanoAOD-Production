# JMENanoAOD-Production

```bash
cmsrel CMSSW_12_4_6
cd CMSSW_12_4_6/src/
cmsenv
git cms-init
git cms-merge-topic nurfikri89:portFrom125XTo124X_JMENanoRun3_forPrivateProduction
scram b -j4
```



```bash
git clone git@github.com:nurfikri89/JMENanoAOD-Production JMENanoAOD/Production
scram b -j4
```

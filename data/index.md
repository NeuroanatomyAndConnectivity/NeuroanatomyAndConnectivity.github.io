---
layout: page
order: 04
title: DATA
permalink: /data/index.html
---

# Data

We have released several MRI datasets for open use. Below are descriptions, as well as links to further information, code, and the data itself.   

We have also been involved in the [International Neuroimaging Data-sharing Initiative][INDI]{:target="\_blank"} and the [Primate Neuroimaging data-exchange (PRIME-DE)][PRIME_DE]{:target="\_blank"}, as well as [preprocessing initiatives][ADHD_prepro]{:target="\_blank"} to facilitate interdisciplinary collaboration.
<hr class="style5">

## MPI--Leipzig: Mind, Brain, Body dataset  
The Max Planck Institute--Leipzig: Mind, Brain, Body (MPILMBB) dataset consists of MRI data as well as several behavioral measures.  
### Data paper  
A preprint describing the acquisition protocol, dataset, and processing code:  
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 10px 10px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @article[key=Mendes164764] %}</div>  
### Data  
[**→ <i class="fa fa-database"></i> MRI data (BIDS format)**][mpilmbb_data_bids]{:target="\_blank"}  
[**→ <i class="fa fa-database"></i> MRI data (Preprocessed)**][mpilmbb_data_preproc]{:target="\_blank"}  
[**→ <i class="fa fa-database"></i> Behavioral data**][mpilmbb_behav]{:target="\_blank"}  
### Code  
[**→ <i class="fa fa-github-alt"></i> MRI data preprocessing scripts**][preproc_lsd]{:target="\_blank"}  
[**→ <i class="fa fa-github-alt"></i> Adaptive visual and auditory oddball task**][oddball]{:target="\_blank"}  
[**→ <i class="fa fa-github-alt"></i> Conjunctive continuous performance task (CCPT)**][CCPT]{:target="\_blank"}   
### Questions?  
We encourage users to subscribe to the [**mailing list <i class="fa fa-users"></i>**][mpilmbb_email]{:target="\_blank"} for updates and discussions regarding the preprocessing pipelines.  
<hr class="style5">  

## 7T resting-state MRI data  
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 10px 10px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @article[key=gorgolewski2015a] %}</div>  
[**→ <i class="fa fa-database"></i> MRI data**][7T_data]{:target="\_blank"}  
Additional related 7T MRI data made available by [Pierre-Louis Bazin][PLB]:  
[**→ <i class="fa fa-database"></i> MRI data**][7T_Bazin]{:target="\_blank"}  
<hr class="style5">

## Berlin resting-state MRI data  
Publications describing the data:  
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 10px 10px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @article[key=biswal2010a|| key=rohr2013a] %}</div>
[**→ <i class="fa fa-database"></i> MRI data**][Berlin_INDI]{:target="\_blank"}  
[**→ <i class="fa fa-database"></i> MRI & Phenotypic data**][Berlin_Data]{:target="\_blank"}  
<hr class="style5">  

## Group-synchrony dance data  
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 10px 10px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @article[key=ellamil2016b] %}</div>  
[**→ <i class="fa fa-database"></i> Data**][dance_data]{:target="\_blank"}  


[INDI]: http://fcon_1000.projects.nitrc.org
[PRIME_DE]: http://fcon_1000.projects.nitrc.org/indi/indiPRIME.html
[Broca_labels]: http://wwwuser.gwdg.de/~cbsarchi/archiv/public/hcp/
[ADHD_prepro]: http://neurobureau.projects.nitrc.org/ADHD200/Introduction.html
[mpilmbb_datapaper]: https://www.biorxiv.org/content/early/2017/07/18/164764
[mpilmbb_datapaper_pdf]: {{site.baseurl}}/downloads/pubs/Mendes2017.pdf
[CCPT]: https://github.com/NeuroanatomyAndConnectivity/ConjunctiveContinuousPerformanceTask
[oddball]: https://github.com/NeuroanatomyAndConnectivity/opendata/blob/master/scripts/oddball_task.py
[preproc_lsd]: https://github.com/NeuroanatomyAndConnectivity/pipelines/tree/v2.0/src/lsd_lemon
[mpilmbb_data_preproc]: https://hdl.handle.net/21.11101/0000-0004-2CD6-A
[mpilmbb_data_bids]: https://www.openfmri.org/dataset/ds000221/
[mpilmbb_behav]: http://nitrc.org/projects/mpilmbb/
[mpilmbb_email]: http://groups.google.com/group/resting_state_preprocessing
[CFG]: http://blog.chrisgorgolewski.org/p/about.html
[7T_data]: http://openscience.cbs.mpg.de/7t_trt/
[PLB]: https://nin.nl/about-us/the-organisation/team/pierre-louis-bazin/
[7T_Bazin]: http://openscience.cbs.mpg.de/bazin/7T_Quantitative/
[Berlin_INDI]: http://fcon_1000.projects.nitrc.org/fcpClassic/FcpTable.html
[Berlin_Data]: http://fcon_1000.projects.nitrc.org/indi/pro/Berlin.html
[ME]: https://harmonylabs.org/melissa-ellamil/
[dance_data]: http://openscience.cbs.mpg.de/ellamil/
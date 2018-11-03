---
layout: page
order: 03
title: CODE
permalink: /code/index.html
robots: nofollow
---

# Code
All our code is available at [**<i class="fa fa-github-alt"></i> github.com/NeuroanatomyAndConnectivity**][github]{:target="\_blank"}  

Below you'll find descriptions of some of our tools, as well as additional software resources that were developed by [lab members] over the years.

[github]:https://github.com/NeuroanatomyAndConnectivity
[lab members]:{{site.baseurl}}/people/index.html
<hr class="style5">

## Resting-state processing pipelines

[<i class="fa fa-github-alt"></i> Pipelines][pipelines]{:target="\_blank"} for processing resting-state fMRI data using [Nipype]{:target="\_blank"}.

[pipelines]: https://github.com/NeuroanatomyAndConnectivity/pipelines
[Nipype]:https://nipype.readthedocs.io/en/latest/
<hr class="style5">

## Connectivity visualization
We have developed a few tools for visualization of brain data.

[![]({{site.baseurl}}/thumbnails/image1.jpg){: .right .small}]({{site.baseurl}}/images/image1.png){:target="\_blank"}
### Edge-bundling & connectivity glyphs
[Joachim Böttger][boettger]{:target="\_blank"} developed several software tools to facilitate the interactive visualization of high-dimensional connectivity data in three-dimensions:  
- [<i class="fa fa-external-link"></i> brainGL][brainGL]{:target="\_blank"}
- [<i class="fa fa-github-alt"></i> vidviewer][vidviewer]{:target="\_blank"}
- [<i class="fa fa-github-alt"></i> brainbundler][brainbundler]{:target="\_blank"}

[![]({{site.baseurl}}/thumbnails/zones_01.jpg){: .right .small}]({{site.baseurl}}/images/zones_01.png){:target="\_blank"}  
### Spatial trends along the cortical surface

[Sebastian Eichelbaum]{:target="\_blank"} developed the [<i class="fa fa-github-alt"></i> Directionality Indicator][di]{:target="\_blank"}, which enables the visualization of directional information along the cortical surface.  
Click the image to the right to see [an example]({{site.baseurl}}/images/zones_01.png){:target="\_blank"}.  

[boettger]: https://joachim.visualistics.de
[braingl]: https://code.google.com/p/braingl/
[vidviewer]: https://github.com/NeuroanatomyAndConnectivity/vidview
[brainbundler]: https://github.com/NeuroanatomyAndConnectivity/brainbundler
[Sebastian Eichelbaum]:www.nemtics.com
[di]:https://github.com/NeuroanatomyAndConnectivity/DirectionalityIndicator
<hr class="style5">

## Measuring distance along the cortical surface
[![]({{site.baseurl}}/images/surfdist.png){: .right .medium}]({{site.baseurl}}/images/surfdist.png){:target="\_blank"}   

The [<i class="fa fa-github-alt"></i> surfdist][sd]{:target="\_blank"} Python package can be used to calculate the exact geodesic distance from nodes or regions-of-interest along the cortical surface.

[sd]:https://github.com/NeuroanatomyAndConnectivity/surfdist
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 0px 0px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @inproceedings[key=surfdist] %}</div>
<hr class="style5">

## Mind-wandering questionnaire

[<i class="fa fa-github-alt"></i> The New York Cognition Questionnaire (NYC-Q)][nycq]{:target="\_blank"} is a questionnaire developed by [Jonny Smallwood]{:target="\_blank"} to characterize the content and form of mind-wandering.

[nycq]:https://github.com/NeuroanatomyAndConnectivity/NYC-Q
[Jonny Smallwood]:https://www.york.ac.uk/psychology/staff/academicstaff/jonathan_smallwood/#profile
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 0px 0px;">{% bibliography -T bib_small_no_num --style /bibcsl/acta_small.csl --query @article[key=gorgolewski2014a] %}</div>
<hr class="style5">

## Nighres

[Nighres <i class="fa fa-external-link"></i> ][nighres]{:target="\_blank"} is a Python package for processing of high-resolution neuroimaging data developed by [Julia Huntenburg]{:target="\_blank"}, [Pierre-Louis Bazin]{:target="\_blank"}, and [Chris Steele]{:target="\_blank"}.  

[nighres]:https://nighres.readthedocs.io/
[Julia Huntenburg]:http://neuro.fchampalimaud.org/en/person/510/
[Pierre-Louis Bazin]:https://scholar.google.com/citations?user=g1EY49YAAAAJ&hl=en
[Chris Steele]:https://scholar.google.de/citations?user=oNLt7OUAAAAJ&hl=en
<div style="background-color: #f9f9f9; padding: +1.5%; margin -1.5%; border-radius: 10px 10px 10px 10px;">{% bibliography -f nighres.bib -T bib_small_no_num --style /bibcsl/acta_small.csl %}</div>

---
layout: page
order: 01
title: RESEARCH
permalink: /research/index.html
---

# Research

[**→ Full publication list**][publications]  
[**→ Google Scholar**][googlescholar]  

Our **[research publications][publications]** are primarily in the domain of **cognitive and systems neuroscience**. Our research aims to understand the organization of the cerebral cortex through broadly investigating patterns of connectivity in relation to cortical structure. Below are brief summaries of several lines of our research:  
[→ cortical gradients](#gradients)  
[→ connectivity visualization](#vis)  
[→ manual area parcellation](#brocasarea)  
[→ comparative connectomics](#species)  
[→ self-generated thought](#SGT)  
[→ age-prediction](#age)  
[→ group synchrony](#synchrony)  

[publications]: publications.html
[googlescholar]: https://scholar.google.com/citations?user=al10sgYAAAAJ

# Projects

## Gradients in cortical organization <a name="gradients"></a>
[![]({{site.baseurl}}/images/principal_gradient.png){: .right .half}]({{site.baseurl}}/images/principal_gradient.png){:target="\_blank"}    

**What are the spatial trends underlying the organization of the cerebral cortex, and what are their functional implications?** Our primary research agenda focuses on describing these topographic principles of cortical organization. We recently characterized a principal axis of cortical connectivity,{% cite margulies2016a %} which relates to cortical geometry and captures a functional hierarchy. We have also mapped the relationship between the principal gradient and measures of cortical microstructure,{% cite huntenburg2017a %} as well as the distance between interconnected areas.{%cite oligschlager2017a %}  

**Through ongoing collaborations,** we have further probed the functional implications of the principal gradient,{% cite murphy2018a %} and investigated its phylogenetic precursors in other primate species, including the marmoset monkey.{% cite Buckner415141 %}  

**Our future research** expands on this axis of connectivity to establish a coordinate system with the aim of differentiating cognitive states, investigating inter-individual variance in brain-behaviour relationships, and mapping individual cortical anatomy.

For an overview, see our recent review article{% cite huntenburg2018a %} and the [OHBM keynote presentation].  

Gradient maps in HCP 32k cifti space can be downloaded here: [**→<i class="fa fa-database"> Gradient templates</i> **]({{site.baseurl}}/downloads/data/hcp.gradients.dscalar.nii)  

[OHBM keynote presentation]:https://www.pathlms.com/ohbm/courses/8246/sections/12540/video_presentations/115833  
{% include biblio.html %}

## Visualization of cortical connectivity<a name="vis"></a>

[![]({{site.baseurl}}/thumbnails/image1.jpg){: .right .medium}]({{site.baseurl}}/images/image1.png){:target="\_blank"}
The visualization of large-scale brain connectivity requires specialized tools and consideration of the features of interest.{% cite margulies2013b %}  

[Joachim Böttger][joachim] developed two approaches: edge-bundling{% cite bottger2014a %} and connectivity glyphs{% cite bottger2014b %}, which we applied to the manual parcellation of [Broca's area](#brocasarea).  

To visualize large-scale spatial trends along the cortical surface, we developed the visualization software [Directionality Indicator][dir_ind], which projects arrows onto the cortical surface based on the orientation of streamlines that follow a progression of cortical features.  
[![]({{site.baseurl}}/thumbnails/zones_01.jpg){: .right .medium}]({{site.baseurl}}/images/zones_01.png){:target="\_blank"}

[joachim]: https://joachim.visualistics.de
[dir_ind]: https://github.com/NeuroanatomyAndConnectivity/DirectionalityIndicator
{% include biblio.html %}

## Manual and Automated Parcellation of Broca's area <a name="brocasarea"></a>

[![]({{site.baseurl}}/images/jakobsen_01.png){: .right .half}]({{site.baseurl}}/images/jakobsen_01.png)
Building on our work describing connectivity-based subdivisions with ventrolateral frontal cortex on the group-{% cite kelly2010a %} and individual-level{% cite margulies2013a %}, we aimed to delineate the extent of areas 44 and 45 at high-resolution. Using novel software tools we developed to [visualize](#vis) high-resolution functional connectivity data, [Estrid Jakobsen][estrid] manually delineated these areas in 101 individual datasets from the [Human Connectome Project (HCP)][hcp]{% cite jakobsen2016a %}, and developed an automated pipeline for delineating these areas in further datasets{% cite jakobsen2018a %}.  

Manually delineated labels for areas 44 and 45 in 101 [HCP][hcp] participates are available [here][Broca_labels].  

[hcp]: http://humanconnectome.org/
[estrid]: https://www.zlab.mcgill.ca/wp-content/uploads/2017/10/estridCV_public.pdf
[Broca_labels]: http://wwwuser.gwdg.de/~cbsarchi/archiv/public/hcp/  
{% include biblio.html %}

## Cross-species comparative cortical connectivity<a name="species"></a>

[![]({{site.baseurl}}/thumbnails/macaque_human_pmc.png){: .right .half}]({{site.baseurl}}/images/macaque_human_pmc.tif)
Comparative studies of connectivity organization between different species enable the translation across literatures. The macaque monkey offers a half-century of gold-standard knowledge of primate cortical connectivity based on tract-tracing studies. We have investigated subdivisons with the posteromedial cortex{% cite margulies2009a %}, ventral frontal cortex{% cite margulies2013a %}, as well as parcellation of the macaque monkey lateral frontal cortex{% cite goulas2017a %}.  

In addition, we characterized the [principal gradient](#gradients) in marmoset monkeys based on [tract-tracing data][marmoset_data]{% cite Buckner415141 %}.  

We have also co-organized the openly available non-human primate MRI database: the [Primate Neuroimaging data-exchange (PRIME-DE)][PRIME_DE]{% cite milham2018a %}.  

[marmoset_data]: http://www.marmosetbrain.org
[PRIME_DE]: http://fcon_1000.projects.nitrc.org/indi/indiPRIME.html
{% include biblio.html %}

## Connectomic correlates of self-generated thought<a name="SGT"></a>

[![]({{site.baseurl}}/thumbnails/sgt.png){: .right .half}]({{site.baseurl}}/thumbnails/sgt.png)
How does spontaneous brain activity relate to the dynamics of ongoing thought? In collaboration with [Jonny Smallwood][jonny] we have been pursuing this question through a series of studies that combine cognitive and behavioral paradigms, psychological questionnaires, and neuroimaging data.{% cite baird2013a golchert2017a golchert2017b smallwood2013a smallwood2016a %}  

We have also validated a questionnaire that captures the content and form of mind wandering,{% cite gorgolewski2014a %} which is openly available [here][nycq].  

[jonny]:https://www.york.ac.uk/psychology/staff/academicstaff/jonathan_smallwood/#profile
[nycq]:https://github.com/NeuroanatomyAndConnectivity/NYC-Q
{% include biblio.html %}

## Age prediction <a name="age"></a>

[![]({{site.baseurl}}/thumbnails/age_prediction.png){: .right .medium}]({{site.baseurl}}/thumbnails/age_prediction.png)
[Franz Liem][franz] recently developed a multimodal imaging approach to age prediction.{% cite liem2017a %} For a plug-and-play version based on cortical thickness, cortical surface area, and subcortical information, check out Brain-Age Regression Analysis and Computation Utility Software as the [**<i class="fa fa-github-alt"></i> BARACUS Bids App**][baracus]  

[franz]: https://www.dynage.uzh.ch/en/aboutus/team/postdocs/fliem.html
[baracus]: https://github.com/BIDS-Apps/baracus
{% include biblio.html %}

## Group synchrony <a name="synchrony"></a>

[![]({{site.baseurl}}/thumbnails/dance.png){: .right .full}]({{site.baseurl}}/thumbnails/dance.png)
How do individuals synchronize their behavior when in a group?{% cite ellamil2016a %} [Melissa Ellamil][melissa] investigated this question in a club setting in collaboration with [Guerilla Science][guerillascience].{% cite ellamil2016b %}  

[melissa]: https://harmonylabs.org/melissa-ellamil/
[guerillascience]: http://guerillascience.org
{% include biblio.html %}

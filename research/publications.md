---
layout: page
title: PUBS
order: 15
permalink: /research/publications.html
sitemap: false
robots: noindex,nofollow
---

# Publications

1. [Preprints](#preprints)  
2. [Journal articles](#articles)  
3. [Conference proceedings](#conf)  
4. [Book chapters](#chap)  
<hr class="style5">

## Preprints <a name="preprints"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type=preprint] %}
<hr class="style5">

## Journal articles <a name="articles"></a>
##### 2019 <a name="2019"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2019] %}
##### 2018 <a name="2018"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2018] %}
##### 2017 <a name="2017"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2017] %}
##### 2016 <a name="2016"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2016] %}
##### 2015 <a name="2015"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2015] %}
##### 2014 <a name="2014"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2014] %}
##### 2013 <a name="2013"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2013] %}
##### 2012 <a name="2012"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2012] %}
##### 2011 <a name="2011"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2011] %}
##### 2010 <a name="2010"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2010] %}
##### 2009 <a name="2009"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2009] %}
##### 2008 <a name="2008"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2008] %}
##### 2007 <a name="2007"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2007] %}
##### 2006 <a name="2006"></a>
{% bibliography --style /bibcsl/acta.csl --query @article[type!=preprint && year=2006] %}
<hr class="style5">

## Conference Proceedings <a name="conf"></a>
{% bibliography --style /bibcsl/acta.csl --query @inproceedings %}
<hr class="style5">

## Book chapters <a name="chap"></a>
{% bibliography --style /bibcsl/acta.csl --query @inbook %}

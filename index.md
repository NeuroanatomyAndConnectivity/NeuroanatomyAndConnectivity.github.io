---
layout: page
title: [Neuroanatomy & Connectivity](https://www.cbs.mpg.de/groups/misc/nac))
tagline: at the Max Planck Institute for Human Cognitive & Brain Sciences
---
{% include JB/setup %}



Code

Freely available [data analysis scripts](https://github.com/NeuroanatomyAndConnectivity)

Tutorials

[Making cortical surface figures with pysurfer](http://nbviewer.ipython.org/urls/dl.dropboxusercontent.com/s/cadukne7hcl03ni/pysurfer_blog_post.ipynb?token_hash=AAE6qvOXiIVB1Btbs_yHvZDRNv3sepefKT_J21EVag8soA&dl=1)

Read [Jekyll Quick Start](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)

Complete usage and documentation available at: [Jekyll Bootstrap](http://jekyllbootstrap.com)

## Update Author Attributes

In `_config.yml` remember to specify your own data:
    
    title : My Blog =)
    
    author :
      name : Name Lastname
      email : blah@email.test
      github : username
      twitter : username

The theme should reference these variables whenever needed.
    
## Sample Posts

This blog contains sample posts which help stage pages and blog data.
When you don't need the samples anymore just delete the `_posts/core-samples` folder.

    $ rm -rf _posts/core-samples

Here's a sample "posts list".

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## To-Do

This theme is still unfinished. If you'd like to be added as a contributor, [please fork](http://github.com/plusjade/jekyll-bootstrap)!
We need to clean up the themes, make theme usage guides with theme-specific markup examples.



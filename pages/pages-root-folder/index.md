---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#


#{% assign my_variable = site.data.socialmedia | where: "name", "YouTube" | first %}
#{{ my_variable.url }}

layout: frontpage
header:
# image_fullwidth: header_unsplash_12.jpg
  image_fullwidth: d3logo.gif
widget1:
  title: "Blog"
  url: '/blog/'
  image: widget-1-302x182.jpg
  text: 'Enjoy reading some stories to understand what we understand.'
widget2:
  title: "Events"
  url: '/events/'
  image: widget-2-302x182.jpg
  text: 'What's going on?'
widget3:
  title: "Videos"
  url: 'https://www.youtube.com/playlist?list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn'
  text: 'Watch some videos featuring Delta3Consulting consultants and videos we find ourselves watching and referring often. '
  target: new
#  video: '<a href="https://www.youtube.com/playlist?list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn" target="_new" data-reveal-id="videoModal"><img src="http://phlow.github.io/feeling-responsive/images/start-video-feeling-responsive-302x182.jpg" width="302" height="182" alt=""/></a>'
  video: '<a href="https://www.youtube.com/playlist?list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn" target="_new" ><img src="images/DustinAgile2022NashvilleMBD-YT.png" width="302" height="182" alt=""/></a>'
#widget3:
#  title: "Download Theme"  Consider putting Models here. 20220919
#  url: 'https://github.com/Phlow/feeling-responsive'
#  image: widget-github-303x182.jpg
# text: '<em>Feeling Responsive</em> is free and licensed under a MIT License. Make it your own and start building. The code is well-documented and explains you how it works.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: 
  text: 
  style: 
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/watch?v=Ip6ArDkUm4U&list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn&index=4" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>

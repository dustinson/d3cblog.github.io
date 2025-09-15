---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#


layout: frontpage
header:
 image_fullwidth: header_unsplash_9.jpg
# image_fullwidth: Delta3Logo.png 
widget1:
  title: "Events"
  url: '/events'
  image: header-bus.jpg
  text: "What's going on?"

widget2:
  title: "Blog"
  url: '/blog'
  image: header_typewriter.jpg
  text: 'Enjoy reading some stories to understand what we understand.'

widget3:
  title: "Videos"
  url: '/videos/'
  image: PortoOcean1.jpg
  text: 'Watch some videos featuring Delta3Consulting consultants and videos we find ourselves watching and referring often.'
---

<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/watch?v=Ip6ArDkUm4U&list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn&index=4" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>

---
layout: post
title:  "Monte Carlo"
subheadline: Blog
categories: blog
image:
    thumb: monteCarlo.jpg
    title: monteCarlo.jpg
header:
    image_fullwidth: "monteCarloTable.png"
---
--WIP--
(this blog is currently under development)

Monte Carlo forecasts are a probabilistic approach to determining when something will be done. 
I'd recommend you download the example from <a href='https://www.focusedobjective.com/pages/free-spreadsheets-and-tools' target='new'>https://www.focusedobjective.com/pages/free-spreadsheets-and-tools </a> and work along with this example.
Please follow Troy Magennis on Twitter <a href='https://twitter.com/t_magennis'>https://twitter.com/t_magennis </a> for more info.  

<h3>Simple example</h3>
<img src="{{ site.urlimg }}b/monteCarloSimple.png" >

It's the start of a new year.  
We have 20 stories to get done and always get 3 stories done per 1 week sprint.  
When will we get done?
Feb 19th. I can say that with 100% confidence.  

This is usually where linear Velocity Planning looks good.  
Easy Peasy.

<h3>"Except it may be a few more stories...</h3>
<img src="{{ site.urlimg }}b/monteCarloMoreStories.png" >
No problem.  It could be as many as 25 stories you say?  Very well.
That's probably going to take a bit longer.  
Maybe 1 week more, maybe 2.  
If you need to be absolutely certain, expect 9 weeks.  
We have 80% confidence that it will be done in 8 weeks, by 2/26.

<h3>"And we're still trying to determine scope...</h3>
<img src="{{ site.urlimg }}b/monteCarloScope.png" >

That makes sense.  This is new work and we learn as we go.
Based on that, we expect some learning to allow for a bit of scope creep.  
Looks like we're targeting early April now.  There's just a 25% chance it'll still be done in Febuary, so we may want to adjust scope or adjust expectations.

<h3>"Sometimes we find the stories are too big, so we spit them...</h3>
<img src="{{ site.urlimg }}b/monteCarloSplit.png" >

That's pretty common.  Good choice.  
How often?  Just 10% of the time?  One out of ever 5 stories is split?
Based on that I'd have to say there's only a 50% chance we are going to get this done by the middle of March.

<h3>"And our Velocity hasn't been stable...</h3>
<img src="{{ site.urlimg }}b/monteCarloVelocity.png" >

Based on the Jira reports, it looks like the worst is 1 story in a sprint, but sometimes it was 6!
We'll want to keep an eye on that.  If we are expecting 100% confidence, I'd prepare for end of April. 
End of March seems pretty reasonable though.  90%.

<h3>"We're taking on another project as well with 1/4 of our time...</h3>
<img src="{{ site.urlimg }}b/monteCarloAllocation.png" >

Yeaaaaaah.  This could be quite challenging.  It'll be a coin flip if we can get this done by March.
We might be looking at May if we're only 75% allocated.  
Let's start exploring some contingency plans.  

I mean, it's March 2020.  What else could go wrong?

Notes:
This is a basic walk through of how I've used Monte Carlo forecasts.  Even when there was a LOT of uncertainty, the accuracy was pretty impressive.  
The goal is NOT to commit to a date.  We are not trying to look at this binary: Will we make it or not?
It's meant to address the grey.  How confident do we feel?  What discussions can this trigger?
What options to we have?
What if we reduced load on the team?  
What if we reduced scope? 
What if we made investments to reduce manual steps or reduce production interruptions?

This spreadsheet includes additional options to use actual data from Jira, Rally or whatever tool you are using to capture throughput metrics.
You can also add in Risks with a % likely hood. 
What % is the risk that a developer leaves us?
What if the designers don't get us the images?
What if the production server crashes and we lose data?
What are the chances that another more pressing project demands our attention?
What are the chances that the world goes down in a lockdown and we never get to eat cake for birthdays again?

These are all real life scenarios which are never adequately addressed with a simple time estimate for work.  
It's never worked well and trying harder won't make a difference. 
Try better.  Work in ranges and leverage math.  

Reduce your focus on what needs to be built and what you are working on. 
Reducing wip to decrease cycle time and increase throughput is the goal (Little's Law).
The less variables you introduce, the higher your chances are at successfully achieving your goal.  
It seems complex, but it really isn't.


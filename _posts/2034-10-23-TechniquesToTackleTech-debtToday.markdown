---
layout: post
title:  "Techniques To Tackle Tech-debt Today"
subheadline: Blog
categories: blog
image:
    thumb: TechDebt/T5.png
    title: TechDebt/T5.png
header:
    image_fullwidth: "TechDebt/T5.png"
---
Techniques To Tackle Tech-debt Today.
![T5.png](TechDebt/T5.png)

<h1>Introduction</h1>
Every team is different, but most share one common challenge: Tech Debt.
This blog is a summary of a presentation which has been well received by attendees and teams.  It will cover the high-level concepts, with possible blog entries of more specific recommendations in the future.

If you would like to watch the full presentation, you can 
<a href="https://youtu.be/5A_leEwOBW0 target="new">watch it here</a>).

<h1>Overview</h1>
Tech-debt is a prevalent problem for most teams.
For the purposes of simplicity, we'll define Tech-debt as anything which prevents a team from achieving flow and maximizes their ability to convert Opportunities to Outcomes.  
Maybe it's a complex code base, or a brittle pipeline, or inadequate tooling.
The cost for tech-debt will appear in extended timelines, reduced user experience, interruptions from emergent quality issues, and reduced satisfaction for the technical and business people in the company.  
These costs may not always appear directly on a spreadsheet for an accountant to pinpoint, but all involved parties feel and pay the price.


![CostOfChange.png](TechDebt/CostOfChange.png)
Ultimately, the Cost Of Change is too damn high!
Over time, the cost increases and our ability to meet needs reduces.  

While the problems may be rooted in technology, the solutions are not.  
Both technical and interpersonal improvements are needed to reduce the cost and burden.
For focus, we'll explore how these improvements can be achieved for an individual (Self), their Team and their Stakeholders.


<h2>- Self</h2>
1) Acknowledge the problem and commit to making an improvement (see also the <a href="https://delta3consulting.com/blog/ACEmodel/" target="new">ACE Model</a>).
    Does someone have the Will to make the improvement?
    Are they willing to make the personal investments to increasing their Skill to make improvements?
    It's much easier to Blame the environment or Justify the reasons, but more valuable to increase their ability to respond.
    The clearer the vision of a better technical environment, the better the chances that improvements will materialize. 
    ![MissedShots.png](TechDebt/MissedShots.png)
2) Learn how to identify (by name) and articulate the problems as they appear. (Code Smells)
    Feeling the pain is an early response.  It is personal, though.  
    To make it communal, and objective, learn the language.  
    Learn what the names for common Code Smells are, so you can quickly identify them, and help others do the same. 
    ![CodeSmells.png](TechDebt/CodeSmells.png)
3) Learn how to resolve Code Smells with Refactoring Practices and Design Patterns
    After you recognize a Code Smell, you should be able to identify better alternatives.  
    Sometimes it's just reducing the lines of code for one method by extracting the contents of an IF block and moving it to another class.
    Sometimes it's the pattern recognition to see that a Strategy Pattern could replace a long method with many nested IF blocks.
    Learn more about how to <a href="https://www.industriallogic.com/img/blog/2005/09/smellstorefactorings.pdf" target="new">convert code smells to patterns.</a>
4) Build the muscle.
    Practice converting Code Smells into a variety of structured patterns. 
    More important than the speed at which someone writes code, should be the speed at which they can change it.
    <a href="https://github.com/emilybache" target="new">Code Katas</a> are dedicated practices where developers can build muscle memory to perform the common tasks, and use the features of their tooling, to quickly and confidently make improvements.
    Practicing dribbling and shooting allows a player to execute those actions without thought during a game.  
    While coding, the focus is usually on the business problem being solved, not the mechanics of how it's being solved.  
    Automated tests (at low and high levels), increase the feedback cycle and confidence that the changes didn't have negative effects.
    Most modern tooling allows for risk-free changes.  Extracting a method, moving code to another class or renaming something to be easier to understand should be done early and often.
    Learn the practices to make changes quickly, and confidently. 
5) Start Small
     ![ImproveIncrementally.png](TechDebt/ImproveIncrementally.png)
    Make the changes to leave a reference for others to follow.  
    Create opportunities to make some improvements without being overwhelmed by fixing all the problems.  
    If people make new changes by referring to other code, leave them some better code to reference.

<h3>- Team</h3>
1) Lead by Example
    Exemplify the behaviors you'd like others to exhibit.  Many devs will use the existing code base as a reference for their changes.  Give them something better to reference.
    Ask the tough questions, do the tough work.  Set the bar, set the tone.
2) Katas as a Team
    ![TeamKata.png](TechDebt/TeamKata.png)
    People learn by doing and from others.  Practicing together helps with the mechanics and the tricks.  This transfers immediately to the "real work", when people often find they don't have time to learn as they are focused on the deadline of the problem they are solving.
    Build the team's muscle, and culture.
    Give slower practitioners the opportunity to build their speed.  Maybe they need to type faster, or type less.  
    Everyone has their favorite shortcuts (besides Copy/Paste). When they see someone do something quicker than they could do it, take the time to for them to learn it. 
3) Optimize for the team's flow, not "Resource Utilization"
    ![Mob.png](TechDebt/Mob.png)
    A common assumption in business (which goes back to the beginning of the Industrial Revolution, and beyond) is "Local Optimization" or "Resource Utilization".
    There is an unconscious, core belief, that you get the most of the system by keeping each individual their busiest.  
    This may be true when solving the same problem repeatedly, it doesn't apply with emergent knowledge work.
      Most technologists learn technology: in school, on StackOverflow and via podcasts or youtube.  They may not learn
4) Isolate
    A LOT of the challenges teams face have to do with large systems spread across many teams.  
    If you change the oil in your car and the radio quits working, you may have this problem.  
    It's nicer when you can test the radio independently.  You may still need to turn the car on when you change the stereo system, but you shouldn't need to test every single function.
    Find ways to create interfaces with your components to decouple them from the larger system.  Wrap that system with tests and validate it works in a dedicated CI\CD pipeline. 
    Isolate your methods, classes, modules, components, services and pipelines.
5) Get Organized
    Change how you think about how you organize.
    A default assumption for people is to think about organizing around functional purpose.  
    ![GetOrganized.png](TechDebt/GetOrganized.png)
    It may make sense to organize around a function.  Pliers, screw drivers, power tools, hammers, first aid, etc.  
    When you need to fix a toilet, grab all the tools you need for that. When you need to change the oil or patch a hole in the wall, grab all the tools you need for that task.
    It's logical to organize on function, but it's not as easily applied for a given purpose.

    ![GetOrganizedOnPurpose.png](TechDebt/GetOrganizedOnPurpose.png)
    Instead, think about what tools you need for the bathroom or automobile job.  Put them in 1 spot so you have what you need for that job. 
    Yes, each toolbox will include band-aids, but you won't need to think about that ahead of time.  
    Consider this in your code base as well.  Does your code have folders for Controllers, Services, Validators, DataAccess etc?
    How many different places do you need to go to make a simple change, like adding the MiddleName to your Person object?
    If you had a Person folder, then your system would be more cohesive.  The things that change together stay together.  
    This might not be obvious, or easy, but it will simplify things in the future, and will allow for greater changes later.

    Organizationally,  you may also notice that having different teams for QA, UI, UX, API, DB, Security and DevOps gives you the same problems.
    Organizing teams around the purpose for a customer can allow for greater adaptability.  The teams will likely be more effective and efficient.  

<h3>- Stakeholders</h3>
1) Be Empathetic
   People are doing their best.  Many Managers, Leaders and Stakeholders are pulled into important decisions with a lot of responsibilities, and not always a lot of support.
   Each of them is reporting to someone else and trying to make them happy.  Vague goals are set without a lot of definition on what success looks like or how to achieve the goal. 
   A person could use the Peter Principle to blame them for being ineffective.  The things they did well to succeed at their prior position might not be enough to succeed at their current position.  
   Assume they want to do their best at making their people happy: those they report to and those they are responsible for.
2) Positively Influence
   "Consulting may be defined as the art of influencing someone, at their request." -- Gerry Weinberg
   You may need higher level support to achieve your goals of increasing Flow and minimizing Tech-debt.  
   To get that support, you will need to understand and speak to their needs.  
     - Higher Quality (less complaining customers, service interruptions or missed sprint goals because of fighting fires)
     - Better Predictability (clearer timelines, focused sprints, reliable deployments)
     - Cost management (development costs, hosting costs, roadmap budgeting)
3) Make it Visible
   Find ways to visually show how Tech-debt issues are causing issues in Quality, Predictability and Cost.
   "Every tool is a weapon, if you use it right." -- Ani DiFranco
   Use Jira to show how a prefactoring step before making code changes.  If the code is a mess, you may need to clean it up first to make the easy change.
   Over time, it should take less time to clean up the code base and less time to add or alter functionality.  As the environment improves to make changes quicker, timelines will shrink and the amount of solutions delivered will increase.  
   Stakeholders will also be able to intuitively understand that changes in cleaner environments are faster and more predictable than those in atrophied environments.  
   A Cumulative Flow Diagram can be a very easy way to visualize this.  
   Other areas of Wasted Time can be easily visualized when KanBan is effectively configured to represent the actual workflow instead of simply TODO/Doing/Done.  Show where work stalls for reviews or waiting on dependencies.  
   Calculate how efficient the development flow is.  What percentage of time does a story actually sit in a development stage vs a processing/review stage?  How much time is spent managing the workflow or communicating, coordinating and collaborating with dependencies?
   What if wwe had some of those people on our team so we don't have delays introduced by competing priorities?
4) Small Changes, Frequently
   Large scale refactoring initiatives often don't go well.  Teams may spend weeks or months cleaning up an environment for a large cost (direct and missed opportunity), with no new abilities.
   Reduce risk by frequently making small changes and show how each improvement positively the teams flow.  Have Lead Times or Cycle Times improved?
   Do automations make it quicker and easier to confidently push changes to Production? 
5) Be Succinct
   Focus more on your message being heard, and less on all your thoughts supporting the message.  
   Most leaders are busy and want you to cut to the chase.  
     1- State the Problem (A problem well defined is a problem half solved)
     2- State the Solution (including the other options you considered, and why you think the option you selected is best)
     3- State the Path (How do you propose we get from the Problem to the solution)
     4- Stop talking.  Be ready to support each statement with 2 or 3 levels of details, and supply them when the questions are asked.  
   Read more about being Succinct <a href="https://delta3consulting.com/blog/Succinct/" target="new">here!</a>

<h2>Conclusion</h2>
The Tech-debt problem is so prevalent for teams because there are a lot of forces involved.  

It's easier to solve a problem in the short term than the long term, but eventually that catches up with us.  
It's easy to swipe the credit card to make a purchase today, but eventually that interest payments overtake the ability to spend money on new things.  

Acknowledging there is a problem and committing to do something about it is the first step (<a href="https://delta3consulting.com/blog/ACEmodel/" target="new">ACE Model</a>).

Focus on yourself first.  The abilities to solve these problems will be used wherever your career takes you.  The investment is good for you, your team and your company.

Lead your team.  Lead by example and help others get better at improving Tech-dbt so it's not as challenging.  

Influence your leaders.  Support them to solve their problems by solving your problems.  Keep It Simple, Keep it Safe, and Keep it Obvious.  



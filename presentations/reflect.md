# What functionality does Reflect provide?
Reflect can be used to build either stand alone web apps or dynamic content embedded in existing webpages. 

In both cases users load a generic JavaScript client app that will be driven from a Python process on the server side.

# How does Reflect relates to No/Low Code solutions?
Low/No code solutions generally comes with a powerful UI allowing to extract and publish data and define actions either through a UI interface or short code.
Reflect is a lower level framework in that it does not offer any pre-build functionality such database connectors, .

# What problem are we solving?

Developing a web application is hard work.

1. Setup: Putting the right components/technologies together
2. Develop: Develop functionalities on different ends (server vs client) in two different programming languages
3. Operate: Ensure releases are delivered on a regular basis, provide failover mechanisms, transparent bug reporting, etc...

We are making business apps development an order of magnitude easier. This makes possible 

Except for software companies, software development is a powerful mean to an end. 
It is resource intensive to create and operate subsequently. Software development process can be trivially described as addressing business needs in a form that can be understood by a machine. Development processes have became increasingly more efficient mostly thanks to the Agile movement. The technical landscape has also undergone some radical changes over the last decade. In particular high level programming languages have became much more widespread allowing for massive productivity boost, although the most significant area of improvement is arguably the web technologies. Those have not only dramatically transformed user experience but transformed radically software deployment and operation to give rise to SASS. But as dramatic as those transformations have been, those have not fully had much effect on business apps development yet. This area did improve over the years but only marginally. We believe there is now a potential for significant improvement in this domain. 

# Common business application development solutions

Here is a list of the solutions commonly used to develop software to automate, support, business. 

## MS Office hacking
Advanced users managed to develop a very broad variety of business applications using Excel and VBA. Its very low technical entry level combined with its amazing flexibility made it, de facto, the most ubiquitous application framework in use nowadays. But even though it is a very effective solution for simple needs, its intrinsic nature  makes it very hard to turn into robust and scalable systems. 
    - Pros: Very agile, user friendly, can often be developed by end users themselves, play well with the rest of the MS ecosystem.
    - Cons: Hardly scalable beyond a few users, limited to MS ecosystem

## Traditional web technologies
Web technologies have underwent massive improvements both in terms of flexibility and speed of development. There are now used in a more and more advanced way to provide various functionalities across companies through so called micro services. There are also plenty of powerful frameworks to choose from allowing to implement those functionalities in pretty much any existing programming language. Yet due to their intrinsic design those technologies cannot easily be repurposed to develop interactive applications.
    - Pros: Very easy to setup, allows for very flexible, scalable architectures.
    - Cons: Provide only limited interactivity through classic page navigation.

## Native desktop applications
 These are executable installed and run on users machines. They are commonly developed in strongly typed programming languages (C/C++, Java, C#). Those used to be the only mean to produce highly bespoke user experiences (web technologies are making significant improvements years after years) as well as high performances due the nature of the programming languages used.
 This makes them the solution of choice for highly specialized softwares but a bit heavy handed for less advanced needs. 
    - Pros: Best suited for highly bespoke applications (eg: games, text processor, image/video processor, etc).
    - Cons: Requires fairly technical resources due to the programming languages and intrinsic complexity. Expensive to maintain and operate because of the fact that they not be deployed and run on end users machines. This can be alleviated by using highly standardized virtual machines which run in a cloud.

# The most recent ones allows to leverage web technologies (eg: electron) using more modern programming languages .

# Web UI powered solutions
## Web browser based solutions
Over the last decade many solution have been developed to harness the power of web UIs. One popular approach is to embed a web browser inside an application. The most well known example of this approach is the [Electron](https://www.electronjs.org/) project which has been used to develop recent softwares such as Skype, Slack, VS Code, etc.

- Pros: Combine Web UI with native application power.
- Cons: Mostly suited for JavaScript development although other languages can be used although not straight out of the box [Python + Electron](https://medium.com/@abulka/electron-python-4e8c807bfa5e)). Similarly to native applications, apps run on end users machines.

## Web app servers
Another increasingly popular approach to take advantage of Web UI technology is to create frameworks that can run applications processes on the server side while rendering them in a browser on the client side (spoiler: this Reflect architecture). This has many compelling advantages, starting from the fact they can target any programming language, apps can deployed instantly on server side. They require to expose a Web UI API to the targeted programming language, they also require a powerful server application which can manage app sub processes and their communication with client web browsers. This approach has been followed by Microsoft backed [Blazor](https://stackoverflow.blog/2020/02/26/whats-behind-the-hype-about-blazor/) project. It has also been implemented in R with [Shiny](https://www.dominodatalab.com/data-science-dictionary/shiny-in-r) and Python (eg: Plotly, Streamlit, PyWebIO, etc). 
    - Pros: Allows very fast development cycles of business apps, low maintenance and operation cost thanks to its server based architecture.
    - Cons: Incur a higher initial loading time, which can be noticeable on mobile networks, does not work offline, slightly less customizable than custom build JavaScript clients.

## JavaScript client with custom server 
This is the most general and modern architecture one can think of. This what powers all  advanced web application (social networks, google apps, web mail etc). This architecture involves developing a fairly advanced JavaScript client backed a custom server. This architecture has gain an impressive amount ground over native desktop applications over the last decade. Many JavaScripts have been developed to support this, most notably [React](https://effectussoftware.com/blog/what-is-react-js/) and [Angular](https://www.geeksforgeeks.org/angularjs/). 
    - Pros: Extremely flexible and powerful.
    - Cons: Advanced setup requiring an ad hoc infrastructure.


What do we offer?

A user friendly yet powerful way to build web apps.

- Using Python which is arguably the best suited programming language for developing business apps nowadays.

- Using formulas which allows users to define dynamic behaviours naturally.

- Relying on a battled tested app framework allowing an easy maintenance and deployment.

What are the benefits?

- Anyone who knows Python can build professional web app. Those can range from single user applications to large scale systems.

- Maintenance and deployment are reduced to a minimum thanks to the built-in app server functionalities.

What are the benefits from a business point of view?

A massive productivity boost in software development. 

- Software development is dramatically more efficient (aka agile), allowing to build ad hoc solutions as you go with very few resources.

How does it integrate with existing systems?

- Reflect has been specifically designed to allow for a smooth adoption and integration. You can start building simple applications immediately, and migrate 


overlap with any part of existing systems. In particular it does not come with any database integration, user management, analytics, IDE, etc. This should allow to easily integrate it with your existing systems.  


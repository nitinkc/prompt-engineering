from OpenApiConnect import get_completion

# role = user
prompt = f"""
    Translate the following English text to Hindi: \ 
    ```Hi, The train had left before I arrive at the station```
    """
if __name__ == '__main__':
    response = get_completion(prompt)
    print(response)

    software_requirement_specification = """
    URL shortening services like bit.ly or TinyURL are very popular to generate shorter aliases for long URLs. You need to design this kind of web service where if a user gives a long URL then the service returns a short URL and if the user gives a short URL then it returns the original long URL. For example, shortening the given URL through TinyURL: 
    
    https://www.geeksforgeeks.org/get-your-dream-job-with-amazon-sde-test-series/?ref=leftbar-rightbar
    We get the result given below:
    
    https://tinyurl.com/y7vg2xjl
    A lot of candidates might be thinking that designing this service is not difficult. When a user gives a long URL converts it into a short URL and updates the database and when the user hits the short URL then search the short URL in the database, get that long URL, and redirect the user to the original URL. Is it really simple? Absolutely not if we think about the scalability of this service. 
    When you’re asked this question in your interviews don’t jump into the technical details immediately. Most of the candidates make mistakes here and immediately they start listing out some bunch of tools, databases, and frameworks. In this kind of question, the interviewer wants a high-level design idea where you can give the solution for the scalability and durability of the service. 
    Let’s start by talking about the requirement first… 
    
    1. Requirement
    Before you jump into the solution always clarify all the assumptions you’re making at the beginning of the interview. Ask questions to identify the scope of the system. This will clear the initial doubt, and you will get to know what specific detail the interviewer wants to consider in this service. 
    
    Given a long URL, the service should generate a shorter and unique alias for it.
    When the user hits a short link, the service should redirect to the original link.
    Links will expire after a standard default time span.
    The system should be highly available. This is really important to consider because if the service goes down, all the URL redirection will start failing.
    URL redirection should happen in real time with minimal latency.
    Shortened links should not be predictable.
    Let’s start by making some assumptions about the traffic (for scalability) and the length of the URL. 
    
    2. Traffic
    Let’s assume our service has 30M new URL shortenings per month. Let’s assume we store every URL shortening request (and associated shortened link) for 5 years. For this period the service will generate about 1.8 B records. 
    
    30 million * 5 years * 12 months = 1.8B
    3. URL Length
    Let’s consider we are using 7 characters to generate a short URL. These characters are a combination of 62 characters [A-Z, a-z, 0-9] something like http://ad.com/abXdef2.
    
    4. Data Capacity Modeling
    Discuss the data capacity model to estimate the storage of the system. We need to understand how much data we might have to insert into our system. Think about the different columns or attributes that will be stored in our database and calculate the storage of data for five years. Let’s make the assumption given below for different attributes… 
    
    Consider the average long URL size of 2KB ie for 2048 characters.
    Short URL size: 17 Bytes for 17 characters
    created_at- 7 bytes
    expiration_length_in_minutes -7 bytes
    The above calculation will give a total of 2.031KB per shortened URL entry in the database. If we calculate the total storage then for 30 M active users total size = 30000000 * 2.031 = 60780000 KB = 60.78 GB per month. In a Year of 0.7284 TB and in 5 years 3.642 TB of data. 
    
    We need to think about the reads and writes that will happen on our system for this amount of data. This will decide what kind of database (RDBMS or NoSQL) we need to use.
    
    5. URL Shortening Logic (Encoding)
    To convert a long URL into a unique short URL we can use some hashing techniques like Base62 or MD5. We will discuss both approaches. 
    Base62 Encoding: Base62 encoder allows us to use the combination of characters and numbers which contains A-Z, a-z, 0–9 total( 26 + 26 + 10 = 62). So for 7 characters short URL, we can serve 62^7 ~= 3500 billion URLs which is quite enough in comparison to base10 (base10 only contains numbers 0-9 so you will get only 10M combinations). If we use base62 making the assumption that the service is generating 1000 tiny URLs/sec then it will take 110 years to exhaust this 3500 billion combination. We can generate a random number for the given long URL and convert it to base62 and use the hash as a short URL id. 
        
    """

srs_document_format = """
    1. Front matter
    Title 
    Author(s)
    Team
    Reviewer(s)
    Created on
    Last updated
    Epic, ticket, issue, or task tracker reference link
    2. Introduction
    a. Overview, Problem Description, Summary, or Abstract
    
    Summary of the problem (from the perspective of the user), the context, suggested solution, and the stakeholders. 
    b. Glossary  or Terminology
    
    New terms you come across as you research your design or terms you may suspect your readers/stakeholders not to know.  
    c. Context or Background
    
    Reasons why the problem is worth solving
    Origin of the problem
    How the problem affects users and company goals
    Past efforts made to solve the solution and why they were not effective
    How the product relates to team goals, OKRs
    How the solution fits into the overall product roadmap and strategy
    How the solution fits into the technical strategy
    d. Goals or Product and Technical Requirements
    
    Product requirements in the form of user stories 
    Technical requirements
     e. Non-Goals or Out of Scope
    
    Product and technical requirements that will be disregarded
    f. Future Goals
    
    Product and technical requirements slated for a future time
    g. Assumptions
    
    Conditions and resources that need to be present and accessible for the solution to work as described. 
    3. Solutions
    a. Current or Existing Solution / Design
    
    Current solution description
    Pros and cons of the current solution
    b. Suggested or Proposed Solution / Design 
    
    External components that the solution will interact with and that it will alter
    Dependencies of the current solution
    Pros and cons of the proposed  solution 
    Data Model / Schema Changes
    Schema definitions
    New data models
    Modified data models
    Data validation methods
    Business Logic
    API changes
    Pseudocode
    Flowcharts
    Error states
    Failure scenarios
    Conditions that lead to errors and failures
    Limitations
    Presentation Layer
    User requirements
    UX changes
    UI changes
    Wireframes with descriptions
    Links to UI/UX designer’s work
    Mobile concerns
    Web concerns
    UI states
    Error handling
    Other questions to answer
    How will the solution scale?
    What are the limitations of the solution?
    How will it recover in the event of a failure?
    How will it cope with future requirements?
    c. Test Plan
    
    Explanations of how the tests will make sure user requirements are met
    Unit tests
    Integrations tests
    QA
    d. Monitoring and Alerting Plan 
    
    Logging plan and tools
    Monitoring plan and tools
    Metrics to be used to measure health
    How to ensure observability
    Alerting plan and tools
    e. Release / Roll-out and Deployment Plan
    
    Deployment architecture 
    Deployment environments
    Phased roll-out plan e.g. using feature flags
    Plan outlining how to communicate changes to the users, for example, with release notes
    f. Rollback Plan
    
    Detailed and specific liabilities 
    Plan to reduce liabilities
    Plan describing how to prevent other components, services, and systems from being affected
    g. Alternate Solutions / Designs
    
    Short summary statement for each alternative solution
    Pros and cons for each alternative
    Reasons why each solution couldn’t work 
    Ways in which alternatives were inferior to the proposed solution
    Migration plan to next best alternative in case the proposed solution falls through
    4. Further Considerations
    a. Impact on other teams
    
    How will this increase the work of other people?
    b. Third-party services and platforms considerations
    
    Is it really worth it compared to building the service in-house?
    What are some of the security and privacy concerns associated with the services/platforms?
    How much will it cost?
    How will it scale?
    What possible future issues are anticipated? 
    c. Cost analysis
    
    What is the cost to run the solution per day?
    What does it cost to roll it out? 
    d. Security considerations
    
    What are the potential threats?
    How will they be mitigated?
    How will the solution affect the security of other components, services, and systems?
    e. Privacy considerations
    
    Does the solution follow local laws and legal policies on data privacy?
    How does the solution protect users’ data privacy?
    What are some of the tradeoffs between personalization and privacy in the solution? 
    f. Regional considerations
    
    What is the impact of internationalization and localization on the solution?
    What are the latency issues?
    What are the legal concerns?
    What is the state of service availability?
    How will data transfer across regions be achieved and what are the concerns here? 
    g. Accessibility considerations
    
    How accessible is the solution?
    What tools will you use to evaluate its accessibility? 
    h. Operational considerations
    
    Does this solution cause adverse aftereffects?
    How will data be recovered in case of failure?
    How will the solution recover in case of a failure?
    How will operational costs be kept low while delivering increased value to the users? 
    i. Risks
    
    What risks are being undertaken with this solution?
    Are there risks that once taken can’t be walked back?
    What is the cost-benefit analysis of taking these risks? 
    j. Support considerations
    
    How will the support team get across information to users about common issues they may face while interacting with the changes?
    How will we ensure that the users are satisfied with the solution and can interact with it with minimal support?
    Who is responsible for the maintenance of the solution?
    How will knowledge transfer be accomplished if the project owner is unavailable? 
    5. Success Evaluation
    a. Impact
    
    Security impact
    Performance impact
    Cost impact
    Impact on other components and services
    b. Metrics
    
    List of metrics to capture
    Tools to capture and measure metrics
    6. Work
    a. Work estimates and timelines
    
    List of specific, measurable, and time-bound tasks
    Resources needed to finish each task
    Time estimates for how long each task needs to be completed
    b. Prioritization
    
    Categorization of tasks by urgency and impact
    c. Milestones
    
    Dated checkpoints when significant chunks of work will have been completed
    Metrics to indicate the passing of the milestone
    d. Future work
    
    List of tasks that will be completed in the future
    7. Deliberation
    a. Discussion
    
    Elements of the solution that members of the team do not agree on and need to be debated further to reach a consensus.
    b. Open Questions
    
    Questions about things you do not know the answers to or are unsure that you pose to the team and stakeholders for their input. These may include aspects of the problem you don’t know how to resolve yet. 
    8. End Matter
    a. Related Work
    
    Any work external to the proposed solution that is similar to it in some way and is worked on by different teams. It’s important to know this to enable knowledge sharing between such teams when faced with related problems. 
    b. References
    
    Links to documents and resources that you used when coming up with your design and wish to credit. 
    c. Acknowledgments
    
    Credit people who have contributed to the design that you wish to recognize.
    """

court_case = """ K. M. Nanavati vs State Of Maharashtra on 24 November, 1961
Facts of the Case of KM Nanavati vs State of Maharashtra
In KM Nanavati v State of Maharashtra, M. Nanavati, Indian Naval Officer, who was the second in charge of the Indian navy ship “Mysore.” He was married to Sylvia and had three children together. Nanavati and his family had moved around a lot because of the nature of his work before settling in Bombay, where they met the late Prem Bhagwan Ahuja for the first time through mutual acquaintances in Bombay. When Nanavati was regularly absent from Bombay on official duties for extended periods of time, his wife, Sylvia, fell in love with Prem Ahuja and began illicit relationships with him.
After coming back, even after being affectionate with his wife, the same responses were not reverted back from his wife. Initially, when asked by Nanavati, his wife didn’t confess, but later on 27th April, 1959, Sylvia confessed about her illicit relationship with Prem Ahuja. Firstly, Nanavati drove his children and wife to the movies, promising to pick them up later.
He then drove to his ship and, under false premises, got a handgun and six bullets, from there he went to Ahuja’s office, later he went to his residence as Ahuja was not there in his office. When he arrived at Ahuja’s place, the servant verified his presence, upon which he walked to Ahuja’s bedroom carrying the brown packet containing the gun and inquired about his intentions concerning Sylvia and his children. After receiving a dishonorable answer, he shot Prem Ahuja and later confessed his crime in the nearest police station.

Issues in KM Nanavati vs State of Maharashtra
There were couple of issues that was questioned in this KM Nanavati vs State of Maharashtra-

As contradicting to Nanavati case, whether the Governor’s pardoning power and special leave petition can be combined together?
The major question of the Nanavati case is whether the act was done in the sudden moment accidentally or was it a pre-planned assassination?
Whether the High Court has the authority under Section 307(3) of the CrPC to overturn a jury’s judgment on the basis of misdirection in charge?
Whether the High Court lacked jurisdiction to investigate the circumstances in order to evaluate the competency of the Sessions Judge’s reference under Section 307 of the CrPC?

Petitioner’s Arguments:
The first contention in Nanavati case put forth by Nanvati’s lawyers was after hearing the confession given by Sylvia, Nanavati wanted to kill himself but his wife managed to calm him down. He had an intention to know whether Prem Ahuja wanted to marry her, due to which he left his wife and children off at the movie theater and drove to his
He misinformed the authorities before taking the handgun and six bullets, but his main intention was to shoot himself, both the handgun and ammunition were kept inside a brown package. With that he drove straight to Ahuja’s office, and on not finding him he drove to his residence and walked straight to his
Upon entering the bedroom, Nanavati cursed Ahuja and inquired about his intentions about marrying Sylvia and care for the children. To that Prem Ahuja replied, “Do I have to marry every woman I have sex with” which infuriated Nanavati. In the meantime, Ahuja got hold of the revolver due to which Nanavati commanded to return which thereby, broke into a fight resulting in two shots accidentally discharged, killing Prem
After the shooting, Nanavati went to his car and drove it to the police station, where he surrendered. As a result, the petitioner fired at Ahuja in reaction to a grave and sudden provocation, and even if he did commit an offence, it would be culpable homicide, not In a sudden battle between two parties, if one party dies as a result of the other party’s conduct made out of grave provocation or fury as a result of it, the accused will only be responsible for culpable homicide not equal to murder. None of the parties can blame the other for starting the fight, both the parties will be held equally responsible for initiating the fight.

Respondent’s Arguments:
Ahuja had just come out of the shower while wearing a The first contention given by the respondent was that even after having a fight, it is unlikely to discover the towel without loosening or falling off from the body.
Secondly, according to Sylvia’s confession, Nanavati dropped her off in the movie theater and then proceeded towards his ship to get the handgun that too on false This proves that he had adequate cooling time, that the offense was not grave nor sudden, and that Nanavati planned the murder.
The servant of Ahuja, Anjani was present at the time of the incident and was a direct witness, and testifies that four bullets were fired in fast succession and the entire incident took less than a minute, ruling out a
Nanavati left Ahuja’s house without alerting his sister Mamie, who was in another room, that there had been an accident. According to the Deputy Commissioner of Police, Nanavati acknowledged shooting Ahuja and even rectified a spelling error in the police record, proving Nanavati’s capacity to think
"""
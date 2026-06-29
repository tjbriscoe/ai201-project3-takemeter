# ai201-project3-takemeter


## Community Being Analyzed 
1.  r/rap : In this subreddit, I want to analyze and assess the popularity of the rap group, Griselda, amongst hip-hop fans. I want to know where the members of this group and their discography stands amongst avid hip-hop listener and where they would rank them all time as a rap collective/group. 
2. r/hiphopheads
3. r/griselda
4. r/letstalkmusic


## Taxomonies

**analysis** — A structured argument backed by specific evidence. The post uses sonic observation,
historical comparison, biographical context, or statistical data to support a claim.
The argument could be fact-checked or disputed on its merits. Simply naming an album
is not evidence — the evidence must be load-bearing. If you removed it, the argument
would collapse.

**hot_take** — A bold, confident opinion stated without supporting evidence. The post asserts
rather than argues. Includes rankings, superlatives, and strong claims with no backup.
The claim might be true, but the post makes no case for it.
Decision boundary: if removing the evidence doesn't weaken the claim, it's a hot_take.

**reaction** — An immediate emotional response to a specific event, release, or moment.
Feeling-first, little to no argument. Often triggered by a new drop, a controversy,
or something the poster just heard for the first time. Time-sensitive content that
wouldn't make full sense out of context.

**lore_drop** — Shares factual background, history, or biographical context about Griselda
without making an evaluative argument. Informational, not opinionated. Decision boundary:
does it argue something, or just share something? If it draws a conclusion, it's analysis.

**off_topic** — Griselda or a member is mentioned only in passing. The comment is primarily
about another artist, a general rap debate, or something unrelated. If Griselda is
one name in a long list with no specific discussion, it's off_topic.


## Measurements
emotional_response: What emotions are encapsulated in the collective music and what emotions does that invoke out of the listener. Do they feel motivated? Nostalgic? Gritty? Luxurious?
analytical_data: Based on the collective's performance as individual artists, when looking at success parameters (social impact, quality of work, career tenure and relevance, ticket sales, monthly streaming listeners) where does the group rank in the last decade in regard to these 
historical_evidence : Comparing their performance and impact on the rap game to their predecessors, how do they perform when it comes to quality of music, longevity, and quality of work throughout the years



## Handling Ambigious Posts

Boundary 1: hot_take vs. analysis

"Benny is the best pure rapper of the three — his pen on Burden of Proof is just on another level compared to what Conway and Gunn were doing that year."

Could be hot_take (bold ranking claim) or analysis (cites a specific project, implies comparative listening).
Decision rule: Does the evidence constrain the claim, or just decorate it? Naming an album isn't evidence — it's a pointer. If you removed "Burden of Proof," does the argument collapse or just sound vaguer? Here it sounds vaguer but survives. → hot_take. If the post explained what specifically on that album, it would cross into analysis.

Boundary 2: reaction vs. hot_take

"Conway just tossed that Griselda photo off stage — he clearly hates Westside Gunn at this point."

Could be reaction (responding to a specific event) or hot_take (bold claim with no evidence beyond vibes).
Decision rule: Is the claim about the event, or does the event just trigger a pre-existing opinion? Here the claim ("he hates Gunn") goes well beyond what the event shows. The event is the springboard, not the argument. → hot_take. A pure reaction would be "I can't believe Conway just did that, this is so sad."

TieBreaker Rule:
When a post contains multiple clause types, label the dominant clause. If the hot take is the conclusion of the post, label it hot_take. If the reaction is the majority of the text and the opinion is incidental, label it reaction.

## AI Tool Plan 
I plan on using claude AI to help convert my JSON Data file into a csv file that consists of the reddit comments gathered from my push_pull script and uploading it to the google colab notebook.
I will also use AI to help me plan and evaluate label ambiguity and correctly categorizing comments with the right label.





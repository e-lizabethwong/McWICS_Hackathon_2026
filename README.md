# ANCHOUR

## Inspiration
Community & Friendship are becoming harder to sustain because interest slowly drifts without anyone noticing. Clubs and community organizations often realize something is wrong only after engagement has already collapsed. We wanted to build a tool that catches that drift early and helps communities course-correct before they hit rock bottom.

## What it does
**```anchOUR```** is a community engagement centre for clubs and communities.
It analyzes engagement data, such as attendance, posts and followers, to detect when participation is declining and explain why it’s happening.
The platform visualizes engagement decay over time and provides data-backed insights and recommendations to help leaders re-engage members and stabilize their community before it fades.

## How we built it
* Google AI Studio (Gemini) for website design

* Python for data processing and modelling

* Apify to collect engagement and social data

* Snowflake as our central data warehouse

* Streamlit for building interactive dashboards

* Snowflake Cortex AI + Gemini for insight generation, cluster labelling

* snowflake-arctic-embed-m to create vector embeddings of text data

* scikit-learn MiniBatchKMeans for clustering social media post types

## Challenges we ran into
This was our first time working with Snowflake and Streamlit, which came with a steep learning curve. Understanding how to connect data pipelines, deploy Streamlit apps inside Snowflake, and properly use Cortex AI took significant experimentation and debugging—but it paid off.

## Accomplishments that we're proud of
* Building a full end-to-end analytics pipeline from data collection to insights

* Successfully integrating ML and AI inside Snowflake

* Creating a clear, visually consistent dashboard that matches our neo-brutalist design vision

* Turning abstract “community health” into measurable, explainable signals

## What we learned
* How to effectively use Snowflake as more than just a database

* Applying ML + AI directly within Snowflake, including Cortex AI

* Creating and deploying Streamlit apps, including Streamlit inside Snowflake

* Creating bright and eye-catching website using Google AI Studio (Gemini)

## What's next for anchOUR

Our next step is **full integration with the Meta API** to access real-time Instagram engagement data. We were limited during the hackathon because we didn’t have a business or creator account for testing, but this integration will unlock deeper analytics, stronger predictive signals, and more accurate recommendations for community leaders.

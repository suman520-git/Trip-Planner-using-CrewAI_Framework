from crewai import Task
from textwrap import dedent
from datetime import date
import streamlit as st

class TripTasks():
    def __validate_inputs(self,origin,cities,interests,date_range):
        if not origin or not cities or not interests or not date_range:
            raise ValueError("All input parameters must be provided")
        
        return True
    

    def identify_task(self,agent,origin,cities,interests,range):
        self.__validate_inputs(origin ,cities,interests,range)
        return Task(description=dedent(f"""
            Analyze and select the best city for the trip based
            on specific criteria such as weather patterns, seasonal
            events, and travel costs. This task involves comparing
            multiple cities, considering factors like current weather
            conditions, upcoming cultural or seasonal events, and
            overall travel expenses.

            Your final answer must be a detailed
            report on the chosen city, and everything you found out
            about it, including the actual flight costs, weather
            forecast and attractions.
            {self.__tip_section()}

            Traveling from: {origin}
            City Options: {cities}
            Trip Date: {range}
            Traveler Interests: {interests}
          """

        ),
        expected_output="A detailed report on the chosen city with flight costs, weather forecast, and attractions.",
        agent=agent
        )
    
    def gather_task(self, agent, origin, interests, range):
        return Task(description=dedent(f"""
            As a local expert on this city you must compile an
            in-depth guide for someone traveling there and wanting
            to have THE BEST trip ever!
            Gather information about  key attractions, local customs,
            special events, and daily activity recommendations.
            Find the best spots to go to, the kind of place only a
            local would know.
            This guide should provide a thorough overview of what
            the city has to offer, including hidden gems, cultural
            hotspots, must-visit landmarks, weather forecasts, and
            high level costs.

            The final answer must be a comprehensive city guide,
            rich in cultural insights and practical tips,
            tailored to enhance the travel experience.
            {self.__tip_section()}

            Trip Date: {range}
            Traveling from: {origin}
            Traveler Interests: {interests}
          """),
            expected_output="A comprehensive city guide with cultural insights and practical tips.",
            agent=agent)

    def plan_task(self, agent, origin, interests, range):
        return Task(description=dedent(f"""
            Expand this guide into a full travel
            itinerary for this time {range} with detailed per-day plans, including
            weather forecasts, places to eat, packing suggestions,
            and a budget breakdown.

            You MUST suggest actual places to visit, actual hotels
            to stay and actual restaurants to go to.

            This itinerary should cover all aspects of the trip,
            from arrival to departure, integrating the city guide
            information with practical travel logistics.

            Your final answer MUST be a complete expanded travel plan,
            formatted as markdown, encompassing a daily schedule,
            anticipated weather conditions, recommended clothing and
            items to pack, and a detailed budget, ensuring THE BEST
            TRIP EVER, Be specific and give it a reason why you picked
            # up each place, what make them special! {self.__tip_section()}

            Trip Date: {range}
            Traveling from: {origin}
            Traveler Interests: {interests}
          """),
            expected_output="A complete 7-day travel plan, formatted as markdown, with a daily schedule and budget.",
            agent=agent)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"
